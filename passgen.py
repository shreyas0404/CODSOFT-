import secrets
import string
import random

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
special = "!@#$%_"
allChars = lower + upper + digits + special
password = ""

pwLen = int(input("Enter the length of the password"))
minUpper = int(input("Minimum Upper case: "))
minLower = int(input("Minimum Lower case: "))
mindigits = int(input("Minimum Number: "))
minSpec = int(input("Minimum Special Characters"))

for i in range(minUpper):
    password += "".join(random.choice(secrets.choice(upper)))

for i in range(minLower):
    password += "".join(random.choice(secrets.choice(lower)))

for i in range(mindigits):
    password += "".join(random.choice(secrets.choice(digits)))

for i in range(minSpec):
    password += "".join(random.choice(secrets.choice(special)))

remaining = pwLen - minLower - minUpper - mindigits - minSpec

for i in range(remaining):
    password += "".join(random.choice(secrets.choice(allChars)))

password = list(password)
random.shuffle(password)
print("".join(password))
