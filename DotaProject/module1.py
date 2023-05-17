# Load reviews from file
def load_reviews_from_file():
    reviews = []
    try:
        with open('reviews.txt', 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 3:  # Check if the line contains all three values
                    nickname, review, phone = data
                    reviews.append({'nickname': nickname, 'review': review, 'phone': phone})
    except FileNotFoundError:
        pass
    return reviews

# Save review to file
def save_review_to_file(review):
    with open('reviews.txt', 'a', encoding='utf-8') as file:
        file.write(f"{review['nickname']},{review['review']},{review['phone']}\n")


