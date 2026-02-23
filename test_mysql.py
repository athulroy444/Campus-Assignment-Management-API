import MySQLdb

passwords = ['', 'root', '1993', 'admin', 'password', 'root123', 'admin123', '12345678', '1234']

for p in passwords:
    try:
        db = MySQLdb.connect(host='127.0.0.1', user='root', passwd=p)
        print(f"SUCCESS: {p}")
        db.close()
        break
    except MySQLdb.Error as e:
        print(f"FAILED: {p} - {e}")
