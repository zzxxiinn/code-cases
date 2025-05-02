# 可以用 _ 来分割大数字，让他更易读一些

n: int = 10_0000_0000
print(n)

# using a thousand eparator
n: int = 1000000000
print(f"{n:_}")  # 1_000_000_000
print(f"{n:,}")  # 1,000,000,000

# add charators to alignment
var: str = "var"
print(f"{var: >20}:")  #                  var:
print(f"{var: <20}:")  # var                 :
print(f"{var: ^20}:")  #         var         :
print(f"{var:_^20}:")  # ________var_________:

# formatting time string
from datetime import datetime

now: datetime = datetime.now()
print(f"{now:%d.%m.%y}")  # 02.05.25
# local version of the date and time
print(f"{now:%c}")  # Fri May  2 21:50:40 2025
print(f"{now:%I%p}")  # 09PM -> 12h format followed by PM and AM
