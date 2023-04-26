import time

print("Welcome to T-34: The Game!\n")
time.sleep(1)
print("You are a Soviet tank commander leading a group of soldiers to victory against the Nazi army.\n")
time.sleep(1)

# Game starts here
print("You are in command of a T-34 tank and a group of soldiers. You receive orders to attack a German supply convoy.")
time.sleep(1)
print("What do you do?")
time.sleep(1)

# First choice
choice1 = input("A) Attack head-on or B) Flank the convoy: ")

if choice1.lower() == "a":
    print("You order your tank to charge at the convoy head-on.")
    time.sleep(1)
    print("The German soldiers are caught off guard and you successfully destroy the convoy.")
    time.sleep(1)
    print("Well done, comrade! Your bravery will be remembered.")
    
elif choice1.lower() == "b":
    print("You order your tank to flank the convoy and take them by surprise.")
    time.sleep(1)
    print("Your plan works and you successfully destroy the convoy without taking any losses.")
    time.sleep(1)
    print("Well done, comrade! Your tactical prowess will be remembered.")

# Second choice
print("\nYou receive new orders to capture a German fort.")
time.sleep(1)
print("What do you do?")
time.sleep(1)

choice2 = input("A) Attack head-on or B) Lay siege to the fort: ")

if choice2.lower() == "a":
    print("You order your tank to charge at the fort head-on.")
    time.sleep(1)
    print("The Germans have prepared for your attack and your tank is hit by a rocket. You lose the battle.")
    time.sleep(1)
    print("Your bravery will be remembered, comrade.")
    
elif choice2.lower() == "b":
    print("You order your soldiers to lay siege to the fort while your tank provides cover fire.")
    time.sleep(1)
    print("After a long and grueling battle, you successfully capture the fort and take many prisoners.")
    time.sleep(1)
    print("Well done, comrade! Your strategic brilliance will be remembered.")

# Third choice
print("\nYour unit has been assigned to destroy a German artillery battery.")
time.sleep(1)
print("What do you do?")
time.sleep(1)

choice3 = input("A) Attack head-on or B) Sneak in behind enemy lines: ")

if choice3.lower() == "a":
    print("You order your tank to charge at the artillery battery head-on.")
    time.sleep(1)
    print("The Germans are prepared and your tank is hit by heavy artillery fire. You lose the battle.")
    time.sleep(1)
    print("Your bravery will be remembered, comrade.")
    
elif choice3.lower() == "b":
    print("You order your soldiers to sneak in behind enemy lines and sabotage the artillery battery.")
    time.sleep(1)
    print("Your plan works and you successfully destroy the artillery battery without being detected.")
    time.sleep(1)
    print("Well done, comrade! Your cunning tactics will be remembered.")

# Fourth choice
print("\nYour unit has been tasked with defending a key bridge from a German assault.")
time.sleep(1)
print("What do you do?")
time.sleep(1)

choice4 = input("A) Hold the bridge at all costs or B) Retreat and set up a new defense line: ")

if choice4.lower() == "a":
    print("You order your soldiers to hold the bridge at all costs.")
    time.sleep(1)
    print("The Germans launch a fierce assault and you suffer heavy casualties, but you manage to hold the bridge.")
    time.sleep(1)
    print("Well done, comrade! Your determination and sacrifice will be remembered.")
    
elif choice4.lower() == "b":
    print("You order your soldiers to retreat and set up a new defense line.")
    time.sleep(1)
    print("The Germans manage to cross the bridge, but you are able to set up a new defense line and repel their attack.")
    time.sleep(1)
    print("Well done, comrade! Your quick thinking and flexibility will be remembered.")
    
else:
    print("Invalid input. Please choose A or B.")


print("\nYour unit has been ordered to take out a German tank division.")
time.sleep(1)
print("What do you do?")
time.sleep(1)

choice5 = input("A) Engage the tanks directly or B) Set up an ambush: ")

# Fifth choice
print("\nYour unit has been tasked with taking out a division of German tanks.")
time.sleep(1)
print("What do you do?")
time.sleep(1)

while True:
    choice5 = input("A) Engage the German tanks directly or B) Set up an ambush: ")
    if choice5.lower() == "a":
        print("You order your tank to engage the German tanks directly.")
        time.sleep(1)
        print("Your tank is hit by a barrage of shells and is disabled. You lose the battle.")
        time.sleep(1)
        print("Your bravery will be remembered, comrade.")
        break
    elif choice5.lower() == "b":
        print("You order your soldiers to set up an ambush and wait for the German tanks to come by.")
        time.sleep(1)
        print("Your plan works and you are able to take out the German tank division with minimal losses.")
        time.sleep(1)
        print("Well done, comrade! Your strategic brilliance and teamwork will be remembered.")
        break
    else:
        print("Invalid input. Please choose A or B.")


print("\nYour unit is on a reconnaissance mission behind enemy lines.")
time.sleep(1)
print("You stumble upon a German supply convoy.")
time.sleep(1)
print("What do you do?")
time.sleep(1)

choice3 = input("A) Call in an air strike or B) Attack the convoy with your tank: ")

if choice3.lower() == "a":
    print("You call in an air strike on the convoy.")
    time.sleep(1)
    print("The air strike is successful and the convoy is destroyed.")
    time.sleep(1)
    print("Well done, comrade! Your quick thinking and decisiveness will be remembered.")

elif choice5.lower() == "b":
    print("You order your tank to attack the convoy.")
    time.sleep(1)
    print("Your tank destroys several German vehicles, but is eventually hit and disabled by enemy fire.")
    time.sleep(1)
    print("You and your crew are captured and sent to a concentration camp.")
    time.sleep(1)
    print("You spend several months in captivity, enduring harsh conditions and forced labor.")
    time.sleep(1)
    print("But you never lose hope and continue to resist the Nazi oppressors in any way you can.")
    time.sleep(1)
    print("Eventually, you are liberated by the advancing Soviet army and return home a hero.")


print("\nCongratulations! You have completed all the missions and emerged victorious against the Nazi army.")
time.sleep(1)
print("Your name will go down in history as a hero of the Soviet Union.\n")
time.sleep(1)
print("Thanks for playing T-34: The Game!")
