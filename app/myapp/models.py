from database import mydb
from fill_database import new_form

mycol = mydb["mycol"]
result = mycol.insert_many(new_form)