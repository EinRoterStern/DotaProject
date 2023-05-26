# �������� �� �����
def load_file(): #����� �������� �� �����
    reviews = []
    try:
        with open('activeuser.txt', 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 4:  # ��������, ��� ��� ���� ������
                    nickname, review, phone, timestamp = data
                    reviews.append({'nickname': nickname, 'review': review, 'phone': phone, 'timestamp': timestamp})
    except FileNotFoundError:
        pass
    return reviews

# ���������� � ����
def save_file(review): #���������� � ����
    with open('activeuser.txt', 'a', encoding='utf-8') as file:
        file.write(f"{review['nickname']},{review['review']},{review['phone']},{review['timestamp']}\n")

# �������� �������������� ���������
def load_file_AI(): #����� �������� �� �����
    reviews1 = []
    try:
        with open('activeuser_AI.txt', 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 4:  # ��������, ��� ��� ���� ������
                    nickname, review, phone, timestamp = data
                    reviews1.append({'nickname': nickname, 'review': review, 'phone': phone, 'timestamp': timestamp})
    except FileNotFoundError:
        pass
    return reviews1