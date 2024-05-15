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
    with open(csv_file, mode='a', newline='') as file:
        fieldnames = ['id', 'username']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writerow(user_data)


