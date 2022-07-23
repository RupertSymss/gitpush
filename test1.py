import pymongo
client = pymongo.MongoClient("mongodb+srv://rupert:VodG97PQ65H82Hee@cluster0.0llqc.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "sudhanshu",
    "email" : "skumar@ineuron.ai",
    "surname" : "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

#