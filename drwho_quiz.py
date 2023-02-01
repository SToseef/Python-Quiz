import os , time
print("\nWelcome to the Doctor Who Quiz!\n")

playing = input("Would you like to play? [yes/no] : ")

#Player lower makes user input lower case

if playing.lower() != "yes":
    quit()

#Clearing the screen w/ delay

time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')

print("\nAllonsy! Let's start...\n")

time.sleep(3)

print("#####################################################")
print("   ! Guess by typing the numbers to the choices !   ")
print("#####################################################\n")

score = 0

#Questions 
time.sleep(2)
answer = input("[Question] Which Doctor regenerated outside of their Tardis? \n [1] 13 \n [2] 10 \n [3] 12 \n [4] 9 \n[Answer]: ")
if answer == "1" : 
    print("\n##### Correct! ######\n")
    print("Next Question...\n")
    score += 1
else: 
    print("\nIncorrect!\n")
    print("Next Question...\n")

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')
answer = input("[Question] Who said the following 'I don't want to go'? \n [1] 11th \n [2] 8th \n [3] 10th \n [4] 5th \n[Answer]: ")
if answer == "3" : 
    print("\n##### Correct! ######\n")
    print("Next Question...\n")
    score += 1
else: 
    print("\nIncorrect!\n")
    print("Next Question...\n")

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')
answer = input("[Question] Who was the 11th Doctors first companion? \n [1] Clara Oswald \n [2] Rose Tyler \n [3] Amy Pond \n [4] Bill Potts \n[Answer]: ")
if answer == "3": 
    print("\n##### Correct! ######\n")
    print("Next Question...\n")
    score += 1
else: 
    print("\nIncorrect!\n")
    print("Next Question...\n")

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')
answer = input("[Question] Where is the Doctor orignally from? \n [1] Segonax \n [2] Indigo 3 \n [3] Skaro \n [4] Gallifrey \n[Answer]: ")
if answer == "4": 
    print("\n##### Correct! ######\n")
    print("Next Question...\n")
    score += 1
else: 
    print("\nIncorrect!\n")
    print("Finalising Score...\n")

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')

#Final score summed up

print("You got " + str(score) + "/4 questions correct!")
print("You got " + str((score/4)* 100) + "%!")
print("\nThanks For Playing!\n")