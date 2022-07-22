import pymongo
client = pymongo.MongoClient("mongodb+srv://raza:ra96za@cluster0raza.xrd4qcd.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name":"sudhanshu","age":78,"home":"patna"
}

db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)