# Name: HARSHIT THAKUR | UID: 23BAI70435
print("Name: HARSHIT THAKUR | UID: 23BAI70435")


num = int(input("Enter a number: "))

while num >= 10:
    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10

    num = total

print("Single digit result:", num)