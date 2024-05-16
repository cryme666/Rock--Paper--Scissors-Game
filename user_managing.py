import csv

csv_file = "users.csv"

def check_user(user_data):
    existing_users = set()  

    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            existing_users.add(row['id'])

    if user_data['id'] in existing_users:
        return True

    add_new_user(user_data)
    return False

def add_new_user(user_data):
    user_data['balance'] = 300
    user_data['wins'] = 0
    user_data['loses'] = 0
    with open(csv_file, mode='a', newline='') as file:
        fieldnames = ['id', 'username', 'balance','wins','loses']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(user_data)


# def get_balance(user_id):
#     with open(csv_file, mode='r') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             if row['id'] == str(user_id):
#                 return int(row['balance'])
#     return None

def update_info(user_id, update_info, info):
    rows = []
    updated = False
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames  # Отримуємо список полів з файлу CSV
        for row in reader:
            if row['id'] == str(user_id):
                row[update_info] = str(info)
                updated = True
            rows.append(row)

    if not updated:
        return False  # Якщо користувача не знайдено, повертаємо False

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return True  # Повертаємо True, якщо оновлення вдалося


def get_info(user_id,user_row):
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] == str(user_id):
                return int(row[user_row])
    return None

# print(get_info(655826401, 'balance'))