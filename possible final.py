""" import time
import random

def start_game():
    print("Welcome to racer")
    print("You are an underground racer aiming to reach the boss racer and defeat him")
    print("To do so, you must conquer multiple levels and answer questions to gain speed.")
    print("Prepare for your first race")
    print("-------------------------------------")
    time.sleep(2)
    play_level(1)

def play_level(level):
    print("Level", level)
    print("Get ready for the race")

    race_time = race(level)

    if race_time <= 0:
        print("you failed to win the race")
        print("you will not become a legend ")
        return

    print(" nice you finsihed the race in ", race_time, "seconds!")
    print("You have unlocked the next level.")
    print("-------------------------------------")
    time.sleep(2)

    if level < 5:
        play_level(level + 1)
    else:
        fight_boss()

def race(level):
    distance = 0
    start_time = time.time()
    speed_boost = 1

    while distance < 100:
        speed = random.randint(80, 120) + speed_boost
        time.sleep(1)
        distance += speed

        if distance % 30 == 0:
            speed_boost += answer_question(level)

        if distance >= 100:
            break

    end_time = time.time()
    race_time = round(end_time - start_time, 2)

    return race_time

def answer_question(level):
    print("You've reached a checkpoint answer the question correctly to increase your speed.")
    print("Level", level, "question:")

    if level == 1:
        question = "What is the capital city of France? (a) Paris (b) London (c) Berlin"
        correct_answer = "a"
    elif level == 2:
        question = "Which planet is known as the Red Planet? (a) Venus (b) Mars (c) Jupiter"
        correct_answer = "b"
    elif level == 3:
        question = "Who painted the Mona Lisa? (a) Michelangelo (b) Leonardo da Vinci (c) Pablo Picasso"
        correct_answer = "b"
    elif level == 4:
        question = "What is the tallest mountain in the world? (a) Mount Everest (b) Mount Kilimanjaro (c) Mount Fuji"
        correct_answer = "a"
    else:
        question = "Which element has the chemical symbol 'H'? (a) Hydrogen (b) Helium (c) Carbon"
        correct_answer = "a"

    print(question)

    user_answer = input("Enter your answer (a, b, or c): ")

    if user_answer.lower() == correct_answer:
        print("Correct answer! You receive a speed boost!")
        return random.randint(10, 20)
    else:
        print("Wrong answer! No speed boost this time.")
        return 0

def fight_boss():
    print("Final level You're about to face the boss racer.")
    print("Defeat the boss to become a legendary racer")

    boss_speed = random.randint(120, 150)
    player_speed = random.randint(100, 160)

    print("Boss racer speed:", boss_speed, "km/h")
    print("Player speed:", player_speed, "km/h")
    print("-------------------------------------")
    time.sleep(2)

    if player_speed >= boss_speed:
        print(" wow you actually defeated him, your a legendary racer now ")
    else:
        print("The boss racer was too fast for you. You couldn't defeat him.")
        print("Your underground racing career ends here.")

    print("Thank you for playing ")

start_game()
 """
import time

class FordMustang:
    def __str__(self):
        return "Ford Mustang Boss 429"

class DodgeCharger:
    def __str__(self):
        return "Dodge Charger 1978"

class LamborghiniA:
    def __str__(self):
        return "Lamborghini Aventador"

def select_Car():
    print("1. Ford Mustang Boss 429")
    print("2. Dodge Charger 1978")
    print("3. Lamborghini Aventador")
    
    choice1 = int(input("Choose wisely by entering the number of your choice: "))

    if choice1 == 1:
        user_car = FordMustang()
        print("You chose Ford Mustang, a classic car and a great choice. Here are some basic stats:")
        time.sleep(2)
        print("429 cubic-inch V8 engine, 375 horsepower, four-speed manual transmission, top speed of 150 mph.")
        time.sleep(1)

    elif choice1 == 2:
        user_car = DodgeCharger()
        print("You chose Dodge Charger, iconic and classic. Let me give you the rundown of this beast:")
        time.sleep(2)
        print("318 cubic-inch 400 V8 engine, 230 horsepower, four-speed manual transmission, top speed of 125 mph.")
        time.sleep(1)

    elif choice1 == 3:
        user_car = LamborghiniA()
        print("You chose Lamborghini, a flashy choice sure to make some heads turn. Here are some stats:")
        time.sleep(2)
        print("396.5 cubic-inches 6.5-liter V12 engine, 759 horsepower, seven-speed ISR transmission, top speed of 217 mph.")
        time.sleep(1)

    else:
        print("Error: Please choose 1, 2, or 3.")
        return select_Car()
    
    print("Great choice choosing the", user_car)
    print("Let's get you racing!")

select_Car()
