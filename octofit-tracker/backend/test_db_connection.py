from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['octofit_db']

# Test inserting a document
test_collection = db['test_collection']
test_document = {"name": "test", "value": 123}
test_collection.insert_one(test_document)

# Test retrieving the document
retrieved_document = test_collection.find_one({"name": "test"})
print("Retrieved Document:", retrieved_document)

# Clean up
test_collection.delete_one({"name": "test"})