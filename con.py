from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
import os



# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('mongodb://devroot:devroot@localhost:27017/mydb?authSource=admin')

# db=client.admin
# # Issue the serverStatus command and print the results
# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult) 


mydb = client["mydb"]
mycol = mydb["to"]


# Поиск всех записей в коллекции
# myquery = {  }

#mydoc = mycol.find(myquery)

#for x in mydoc:
#  print(x) 

# Добавить записи
# myquery = {"name": "John", "address": "Highway 37"}

# mydoc = mycol.insert_one(myquery)
with open('/var/log/auth.log') as f:
    contents = f.read()
    print(contents.split())

# count = 0
# for line in contents:
#     count += 1
#     print(f'line {count}: {line}') 

# f = open('','r')

# print(read(f))
#172.18.0.2