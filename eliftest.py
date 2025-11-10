secret = 7
guess = 9

if guess > secret:
    print("too high")
elif guess < secret:
    print("too low")
else:
    print("just right!")

small = False
green = False


if small == False and green == False:
    print("Pumpkin")
elif small == True and green == False:
    print("Cherry")
elif small == False and green == True:
    print("watermelon")
else:
    print("Pea")

nums = [3, 2, 1, 0]
for int in nums:
    print(int)

guess_me = 7
number = 1

while number <= guess_me:
    if number > guess_me:
        print("oops!")
    elif number < guess_me:
        print("too low")
    else:
        print("found it!")
    number += 1

guess_me = 5

for number in range(10):
    if number > guess_me:
        print("oops")
        exit()
    elif number < guess_me:
        print("too low")
    else:
        print("found it!")
        exit()