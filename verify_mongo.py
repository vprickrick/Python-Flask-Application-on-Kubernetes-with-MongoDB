from pymongo import MongoClient

try:
    # Connect to MongoDB instance
    client = MongoClient("mongodb://admin:admin@mongo:27017/?ssl=false")
    db = client.admin
    # Verify connection
    db.command('ping')
    print("Connected to MongoDB!")

    # List users
    users = db.command("usersInfo")
    for user in users['users']:
        print(user)
except Exception as e:
    print(f"Error: {e}")
