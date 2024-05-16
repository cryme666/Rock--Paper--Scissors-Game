import csv
import time
from utils import BONUS_INTERVAL

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
    user_data['last_bonus_claimed'] = time.time()

    with open(csv_file, mode='a', newline='') as file:
        fieldnames = ['id', 'username', 'balance','wins','loses','last_bonus_claimed']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(user_data)

def update_info(user_id, update_info, info):
    rows = []
    updated = False
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames  
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
                if '.' in row[user_row]:
                    return float(row[user_row])
                else:
                    return int(row[user_row])
    return None

def get_bonus(user_id,user_name):
    current_time = time.time()
    user_data = {"id": str(user_id), "username":user_name}
    check_user(user_data)
    time_since_last_bonus = current_time - get_info(user_id, 'last_bonus_claimed')
    if time_since_last_bonus < BONUS_INTERVAL:
        remaining_time = round((BONUS_INTERVAL - time_since_last_bonus) / 3600, 2)
        # print(f"Ви вже отримували бонус. Знову можна через {remaining_time} годин.")
        return remaining_time

    user_balance = get_info(user_id, 'balance')
    user_balance += 300
    update_info(user_id, 'balance', user_balance)

    # last_bonus_claimed[user_id] = current_time
    update_info(user_id, 'last_bonus_claimed',current_time)
    # print("Вам нараховано бонус у розмірі 300 монет.")
    return 0


