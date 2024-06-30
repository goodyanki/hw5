import mysql.connector
from datetime import datetime, timedelta
import random


def generate_random_date(year, month):
    date = datetime(year, month, 1)
    max_day = (date.replace(month=month % 12 + 1) - timedelta(days=1)).day
    random_day = random.randint(1, max_day)
    return date.replace(day=random_day).strftime('%Y-%m-%d')


def insert_data(cnx, year, month, num_records):
    cursor = cnx.cursor()
    categories = ['Dinner', 'Groceries', 'Utilities', 'Entertainment', 'Travel', 'Fuel', 'Education', 'Healthcare',
                  'Clothing', 'Electronics']
    notes_prefix = ['Business', 'Personal', 'Family', 'Emergency', 'Routine', 'Leisure', 'Vacation', 'Health',
                    'Fashion', 'Tech']

    for _ in range(num_records):
        category_id = random.randint(1, 10)  # Assuming you have categories 1 to 10
        date = generate_random_date(year, month)
        expense = random.choice(categories)
        amount = round(random.uniform(10, 1000), 2)  # Amounts between $10 and $1000
        notes = f'{random.choice(notes_prefix)} {expense.lower()}'
        query = "INSERT INTO expenses (category_ID, expense_date, expense, amount, notes) VALUES (%s, %s, %s, %s, %s)"
        values = (category_id, date, expense, amount, notes)
        cursor.execute(query, values)

    cnx.commit()  # Commit the transaction
    cursor.close()
    print(f"Inserted {num_records} records for {month}/{year}")


def connect_to_database():
    try:
        cnx = mysql.connector.connect(
            host='localhost',
            user='root',
            password='12345678',
            database='homework04'
        )
        return cnx
    except mysql.connector.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return None


def main():
    cnx = connect_to_database()
    if cnx:
        for year in range(2000, 2021):  # 从2000年到2020年
            for month in range(1, 13):  # 每年的12个月
                insert_data(cnx, year, month, 10)  # 每个月插入10条数据
        cnx.close()


if __name__ == '__main__':
    main()
