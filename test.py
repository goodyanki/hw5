import mysql.connector

def connect_to_database():
    try:
        # 替换以下信息为你的数据库详情
        cnx = mysql.connector.connect(
            host='localhost',
            user='root',
            password='12345678',
            database='homework04'
        )
        print("Connected to database successfully!")
        return cnx
    except mysql.connector.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")

cnx = connect_to_database()

def insert_data(cnx):
    cursor = cnx.cursor()
    query = "INSERT INTO expenses (category_ID, expense_date, expense, amount, notes) VALUES (%s, %s, %s, %s, %s)"
    values = (1, '2023-10-01', 'Dinner', 45.50, 'Business dinner')
    try:
        cursor.execute(query, values)
        cnx.commit()  # 确保提交事务以保存更改
        print("Data inserted successfully!")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

# 调用插入函数
insert_data(cnx)

# 最后，不要忘了关闭数据库连接
cnx.close()
