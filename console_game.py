import random
list = ["камінь", "папір", "ножниці"]
keep_playing = True
computer_score = 0
human_score = 0
number_of_ties = 0

while keep_playing:
    while True:
        human_choice = input("\nВведіть ваш вибір(камінь, ножниці або папір): ")
        if human_choice in list:
            break
    сomputer_choice = random.choice(list)
    
    print(f"Вибір опонента -> {сomputer_choice}")
    
    if human_choice == сomputer_choice:
        print("Перемогла дружба!")
        number_of_ties += 1
    elif human_choice == "ножниці" and сomputer_choice == "папір":
        print("Переміг гравець!")
        human_score += 1
    elif human_choice == "папір" and сomputer_choice == "камінь":
        print("Переміг гравець!")
        human_score += 1
    elif human_choice == "камінь" and сomputer_choice == "ножниці":
        print("Переміг гравець!")
        human_score += 1
    else:
        print("Переміг опонент!")
        computer_score += 1
    print("-"*20)
    print(f"Гравець -> {human_score}\nОпонент -> {computer_score}\nНічія -> {number_of_ties}")
    print("-"*20)
    while True:
            keep_playing = input("Хочете зіграти ще раз?\nВведіть так/ні")
            if keep_playing == "так":
                keep_playing = True
                break
            elif keep_playing == "ні":
                keep_playing = False
                print("Приходь ще пограти!")
                break