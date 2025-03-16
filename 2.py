import os

def get_cats_info(path):
    cats_info = []

    # Проверяем, существует ли файл
    if not os.path.isfile(path):
        print(f"Файл за шляхом {path} не знайдений.")
        return cats_info

    # Открываем файл и обрабатываем его строки
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()  # Убираем лишние пробелы и символы новой строки
                if ',' in line:  # Если в строке есть разделитель
                    cat_id, name, age = line.split(',')  # Разделяем строку на части
                    cat_info = {"id": cat_id, "name": name, "age": age}  # Создаем словарь для кота
                    cats_info.append(cat_info)  # Добавляем его в список
    except Exception as e:
        print(f"Сталася помилка при обробці файлу: {e}")

    return cats_info

# Путь к файлу (замените на ваш путь, если файл находится в другой папке)
cats_info = get_cats_info("text2.txt")
print(cats_info)

