from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Connect to MongoDB instance
try:
    client = MongoClient("mongodb://admin:admin@mongo:27017/?ssl=false")
    db = client["world"]
    # Test the MongoDB connection
    client.admin.command('ping')
    print("Connected to MongoDB!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

@app.route('/books', methods=['POST'])
def create_book():
    try:
        data = request.get_json()
        db.BOOKSTORE.insert_one(data)
        return jsonify({"message": "Book created!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/books', methods=['GET'])
def get_books():
    try:
        books = list(db.BOOKSTORE.find())
        for book in books:
            book["_id"] = str(book["_id"])
        return jsonify(books), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/books/<id>', methods=['PUT'])
def update_book(id):
    try:
        data = request.get_json()
        db.BOOKSTORE.update_one({"_id": ObjectId(id)}, {"$set": data})
        return jsonify({"message": "Book updated!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    try:
        db.BOOKSTORE.delete_one({"_id": ObjectId(id)})
        return jsonify({"message": "Book deleted!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
