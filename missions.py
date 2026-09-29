def show_missions(missions):
    print("=== Каталог космических миссий ===")
    for n, mission in enumerate(missions , start=1):
        print(f"{n}. {mission['name']}\n Год запуска: {mission['year']}\n Направление: {mission['direction']}")

def search_missions():
    while True:
        user_direction = input("Введите направление для поиска: ")
        if user_direction == "Луна":
            print(f" Artemis-1,\n Год заупска: 2022,\n Направление: Луна")
            break
        elif user_direction == "Далёкий космос":
            print(f" Voyager,\n Год запуска: 1977,\n Направление: Далёкий космос")
            break
        elif user_direction == "Марс":
            print(f" Curiosity,\n Год запуска: 2011,\n Направление: Марс")
            break
        else:
            print("Данного направления не существует!")