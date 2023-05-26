# выгрузка из файла
def load_file(): #метод загрузки из файла
    reviews = []
    try:
        with open('activeuser.txt', 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 4:  # проверка, что там есть отзывы
                    nickname, review, phone, timestamp = data
                    reviews.append({'nickname': nickname, 'review': review, 'phone': phone, 'timestamp': timestamp})
    except FileNotFoundError:
        pass
    return reviews

# сохранение в файл
def save_file(review): #сохранение в файл
    with open('activeuser.txt', 'a', encoding='utf-8') as file:
        file.write(f"{review['nickname']},{review['review']},{review['phone']},{review['timestamp']}\n")

# Загрузка подготовленных вариантов
def load_file_AI(): #метод загрузки из файла
    reviews1 = []
    try:
        with open('activeuser_AI.txt', 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 4:  # проверка, что там есть отзывы
                    nickname, review, phone, timestamp = data
                    reviews1.append({'nickname': nickname, 'review': review, 'phone': phone, 'timestamp': timestamp})
    except FileNotFoundError:
        pass
    return reviews1