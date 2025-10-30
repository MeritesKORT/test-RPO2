import random

def guess_number_game_v2():
    secret_number = random.randint(1, 100)
    guess = None
    attempts = 0

    print("Я загадал число от 1 до 100. Попробуй угадать!")


    while guess != secret_number:
        try:
            guess = int(input("Введи число: "))
            attempts += 1

            if guess < secret_number:
                print("Загаданное число БОЛЬШЕ")
            elif guess > secret_number:
                print("Загаданное число МЕНЬШЕ")
            else:
                print(" Ура! Число {secret_number} угадано за {attempts} попыток!")

        except ValueError:
            print(" Ошибка! Вводи только целые числа!")
