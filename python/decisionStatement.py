age = 18

if age < 18:
    print("still growing")
elif age >= 18 and age < 21:
    print("You're a young adult")
else:
    print("You're an adult")

users = ["Lucky", "Wami", "Taburu", "Z-Sosu"]

for user in users:
    print("User name: {}".format(user))

num = 10
stepper = 0
while stepper <= num:
    if stepper % 2 == 0:
        print(stepper)
    stepper += 1

index = 0
while index < len(users):
    print(users[index])
    index += 1

nums = range(50)
sum = 0
for num in nums:
    sum += num
print(sum)
