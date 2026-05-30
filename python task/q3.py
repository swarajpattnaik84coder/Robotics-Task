num1 = int(input("enter 1st number:"))
num2 = int(input("enter 2nd number:"))



x, y = num1, num2

while y != 0:
    x, y = y, x % y

gcd = x
lcm = (num1 * num2) // gcd

print("GCD =", gcd)
print("LCM =", lcm)