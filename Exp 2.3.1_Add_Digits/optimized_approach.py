# Name: HARSHIT THAKUR | UID: 23BAI70435
print("Name: HARSHIT THAKUR | UID: 23BAI70435")


num = int(input("Enter a number: "))

if num == 0:
    answer = 0
else:
    answer = 1 + (num - 1) % 9

print("Single digit result:", answer)