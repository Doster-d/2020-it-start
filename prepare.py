from simplite import Pylite
DB = Pylite("userDB.db")

#DB.add_table("Users", id="BIGINT", account_status="INTEGER")
DB.add_table("Tasks", id="INTEGER PRIMARY KEY", theme="BIGINT", question="BLOB", answer="BLOB", decision = "BLOB")

# a = "a"

# for i in range(1, 101):
#     b = a*i
#     DB.insert("Tasks", i, b, "answer of {}".format(b), "explanation of {}".format(b))

# print(DB.get_items("Tasks"))

DB.close_connection()