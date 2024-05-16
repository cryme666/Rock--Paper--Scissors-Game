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
    with open(csv_file, mode='a', newline='') as file:
        fieldnames = ['id', 'username', 'balance']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(user_data)


def get_balance(user_id):
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] == str(user_id):
                return int(row['balance'])
    return None

def update_balance(user_id, new_balance):
    rows = []
    updated = False
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] == str(user_id):
                row['balance'] = str(new_balance)
                updated = True
            rows.append(row)

    if not updated:
        return False  # Якщо користувача не знайдено, повертаємо False

    with open(csv_file, mode='w', newline='') as file:
        fieldnames = ['id', 'username', 'balance']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(rows)

    return True  # Повертаємо True, якщо оновлення балансу вдалося
