print("Welcome to the Quiz!")

playing = input("Do Want To Start The Quiz? (Type 'yes' to play any other key to stop) : ")

if playing != "yes":
    quit()

print("Okay! Let's Start The Quiz)")
score = 0

answer = input("How much is 2+2 ? : ")
if answer == "4":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("How much is 10*10 ? :  ")
if answer == "100":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("How many times 'E' comes in ELEPHANT ? :  ")
if answer == "2":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")    

answer = input("----- Comes before 100 : ")
if answer == "99":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")    

answer = input("How many prime numbers are there below 25? :  ")
if answer == "9":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")



print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) +"%.")