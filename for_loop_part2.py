### to do sum of the digits of a number by for loop



total = 0

num = input("Enter a number")

for i in range(0, len(num)):

    total += int(num[i])
print(total)


### sum of the number from 1 to entered number


n = int(input("please enter a number"))
total = 0

for i in range(1, n+1):

    total+=i

print(total)

### print count of letters in a str by for loop

name = input("Please enter a string : ")

temp = ""
for i in range(len(name)):

    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")

        temp += name[i]


## break and continue keywords

for i in range(1, 11):

    if i ==5:

        break
    print(i)

for i in range(1, 11):

    if i == 5:
        continue
    print(i)



winning_number=  43

guess_number = 1

number = int(input("please enter a number b/t a to 100 : "))

game_over = False

while not game_over:

    if number == winning_number:

        print(f"you have won, and you guessed this in {guess_number} times")
        game_over = True

    else:

        if number < winning_number:

            print("too low")
            guess_number +=1
            number = int(input("please enter number again"))

        else:
            print("too high")

            guess_number +=1
            number = int(input("please enter number again"))

winning_number=  43

guess_number = 1

number = int(input("please enter a number b/t a to 100 : "))

game_over = False

while not game_over:

    if number == winning_number:

        print(f"you have won, and you guessed this in {guess_number} times")
        game_over = True

    else:

        if number < winning_number:

            print("too low")

        else:
            print("too high")

        guess_number +=1
        number = int(input("please enter number again"))

number = int(input("please enter a number b/t a to 100 : "))

winning_number=  43

guess_number = 1

game_over = False

while not game_over:

    if number == winning_number:

        print(f"you have won, and you guessed this in {guess_number} times")
        game_over = True

    else:

        if number < winning_number:

            print("too low")

        else:
            print("too high")

        guess_number +=1
    number = int(input("please enter a number b/t a to 100 : "))

##Stap argument

for i in range(1, 11, 2):

    print(i)

for i in range(0, 11, 2):
    print(i)


for i in range(10, 0, -1):

    print(i)



    ##### for loop with string

name = "Anoop"
for i in range(len(name)):

    print(name[i])


name = "Anoop"
for i in name:

    print(i)
name = input("please enter your name : ")

name = str(name)
for i in range(len(name)):

    print(name[i])


num = input("enter a number")
total = 0

for i in num:

    total += int(i)

