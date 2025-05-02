n: float = 1234.5678
print(round(n, 2))  # 1234.57
# string format
print(f"{n:.2f}")  # 1234.567
print(f"{n:.0f}")  # 1234
print(f"{n:,.3f}")  # 1,234.568

a: int = 5
b: int = 10
my_var: str = "Bob says hi"

# 'a + b = ' will be maintained
print(f"{a + b = }")  # a + b = 15
