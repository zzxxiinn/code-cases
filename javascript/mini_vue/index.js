var user = {
  name: "郭源潮",
  birthday: "1990-01-01",
};

observe(user);

function showFirstName() {
  document.querySelector("#firstName").textContent = "姓：" + user.name[0];
}

function showLastName() {
  document.querySelector("#lastName").textContent = "名：" + user.name.slice(1);
}

function showAge() {
  var birthday = new Date(user.birthday);
  var today = new Date();
  today.setHours(0, 0, 0, 0);
  var thisYearBirthday = new Date(
    today.getFullYear(),
    birthday.getMonth(),
    birthday.getDate()
  );
  document.querySelector("#age").textContent =
    "年龄：" + (thisYearBirthday.getFullYear() - birthday.getFullYear());
}

autorun(showFirstName);
autorun(showLastName);
autorun(showAge);
