# Load reviews from file
def load_reviews_from_file(): #метод загрузки из файла
    reviews = []
    try:
        with open('reviews.txt', 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 4:  # проверка, что там есть отзывы
                    nickname, review, phone, timestamp = data
                    reviews.append({'nickname': nickname, 'review': review, 'phone': phone, 'timestamp': timestamp})
    except FileNotFoundError:
        pass
    return reviews

# Save review to file
def save_review_to_file(review): #сохранение в файл
    with open('reviews.txt', 'a', encoding='utf-8') as file:
        file.write(f"{review['nickname']},{review['review']},{review['phone']},{review['timestamp']}\n")


