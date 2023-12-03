from PIL import Image
import os
from filters import RedFilter, BlueFilter, GreenFilter, InversedFilter, DarkFilter, LigthFilter

def main():
    list_filters = {
        1: {
            "name": "Красный фильтр",
            "description": "Делает изображение с уклоном в красный "
                           "(у всех пикселей увеличивается параметр красного).",
            "function": RedFilter()
        },
        2: {
            "name": "Зелёный фильтр",
            "description": "Делает изображение с уклоном в зелёный "
                           "(у всех пикселей увеличивается параметр зелёного).",
            "function": GreenFilter()
        },
        3: {
            "name": "Синий фильтр",
            "description": "Делает изображение с уклоном в синий "
                           "(у всех пикселей увеличивается параметр синего).",
            "function": BlueFilter()
        },
        4: {
            "name": "Инверсия",
            "description": "Меняет цвет писеля на противоположный "
                           "(красный, зелёный и синий именют свой параметр на противоположный).",
            "function": InversedFilter()
        },
        5: {
            "name": "Затемнение",
            "description": "Делает изображение более темным "
                           "(каждый пиксель приближается к чёрному).",
            "function": DarkFilter()
        },
        6: {
            "name": "Высветление",
            "description": "Делает изображение более светлым "
                           "(каждый пиксель приближается к белому).",
            "function": LigthFilter()
        }
    }

    print("Добро пожаловать в консольный фоторедактор.")
    print()
    finished = False
    while not finished:
        path_to_image = input("Введите путь к файлу: ")
        while not os.path.exists(path_to_image):
            print("Неверный путь к файлу...")
            path_to_image = input('Введите путь к файлу: ')
        img = Image.open(path_to_image)
        print()

        for i in range(len(list_filters)):
            print(f'{i + 1} - {list_filters[i + 1]["name"]}')
        print('0 - Выход')

        chose_filter = int(input("Введите фильтра (или 0 для выхода): "))
        while chose_filter not in range(0, 7):
            print("Недопустимое значение...")
            chose_filter = int(input("Введите фильтра (или 0 для выхода): "))
            if chose_filter == 0:
                print("Выход...")
                break

        right_filter = list_filters[int(chose_filter)]["function"]

        print(list_filters[int(chose_filter)]["description"])
        print()

        apply = input('Применить фильтр к картинке? (Да/Нет): ')
        if apply.lower() == 'нет':
            continue
        elif apply.lower() != 'да':
            print('Недопустимое значение')
            break

        img.show()
        img = right_filter.apply_to_image(img)
        path_to_save = input("Куда сохранить: ")
        img.save(path_to_save)

        will_continue = input("Обратотать ещё изображения (Да/Нет): ")
        if will_continue.lower() != 'да':
            if will_continue.lower() == 'нет':
                print("Выход...")
            finished = True


if __name__ == '__main__':
    main()
