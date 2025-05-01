"""Example of how to use Google IMAP Extensions using Python

GMAIL API: http://code.google.com/apis/gmail/imap/

"""

import imaplib
import re


class GmailIMAP4_SSL(imaplib.IMAP4_SSL):
    def __init__(
        self,
        host="imap.gmail.com",
        port=imaplib.IMAP4_SSL_PORT,
        keyfile=None,
        certfile=None,
    ):
        imaplib.IMAP4_SSL.__init__(self, host, port, keyfile, certfile)

        imaplib.Commands["XLIST"] = ("AUTH", "SELECTED")
        imaplib.Commands["ID"] = "AUTH"

    def id(self, *args):
        """Provide app information to the server,
        and get information in return"""
        arg = '("' + '" "'.join(args) + '")'
        name = "ID"
        typ, dat = self._simple_command(name, arg)
        return self._untagged_response(typ, dat, name)

    def xlist(self, directory='""', pattern="*"):
        """List mailbox names in directory matching pattern.
        (typ, [data]) = <instance>.xlist(directory='""', pattern='*')
        'data' is list of XLIST responses.
        """
        name = "XLIST"
        typ, dat = self._simple_command(name, directory, pattern)
        return self._untagged_response(typ, dat, name)

    def special_folders(self):
        """return a dictionary of localized Gmail special folders"""
        path = {}

        for entry in imap_obj.xlist()[1]:
            for name in ("Inbox", "Starred", "Sent", "Drafts", "Spam", "AllMail"):
                if re.search(" .%s\)" % name, entry):
                    path[name] = re.search('"([^"]+)"$', entry).group(1)

        return path

    def uid2msgid(self, uid):
        """Convert an IMAP UID to a Gmail MSGID"""

        typ, data = self.uid(r"fetch", uid, r"(X-GM-MSGID)")

        msgid_dec = re.search(r"X-GM-MSGID ([0-9]+)", data[0]).group(1)
        msgid_hex = hex(int(msgid_dec))

        return msgid_hex[2:]


if __name__ == "__main__":
    imap_obj = GmailIMAP4_SSL()

    imap_obj.login("user", "password")

    # Provide app info to Google, and get some back in return (RFC2971)
    print(imap_obj.id("name", "Joe Developer", "contact", "joe@example.com"))

    # get localized path names for the special folders
    folders = imap_obj.special_folders()
    for key in folders.keys():
        print(key, folders[key])

    # RFC3501
    # get the message count from e.g. ('OK', ['3'])
    incnt = int(imap_obj.select(folders["Inbox"], readonly=True)[1][0])

    for index in range(1, incnt + 1):
        # get the uid from e.g. ('OK', ['1 (UID 15310)'])
        response = imap_obj.fetch(index, "(UID)")[1][0]
        uid = re.search("([0-9]+)\)", response).group(1)

        msgid = imap_obj.uid2msgid(uid)

        print("https://mail.google.com/mail/u/0/#all/" + msgid)

    imap_obj.logout()
