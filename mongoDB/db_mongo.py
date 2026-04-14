from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["escola"]
estudantes = db["estudantes"]

estudantes.insert_one({"nome": "Pedro", "idade": 21})

for estudante in estudantes.find():
    print(estudante)

