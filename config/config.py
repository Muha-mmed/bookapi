from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB Connection
MONGO_URI = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URI)
db = client['blogApi']  # Replace 'my_database' with your database name

# Example Collection
blogCollection = db['blog']  # Replace 'my_collection' with your collection name

try:
    client.server_info()
    print(client)
except:
    print("Failed to connect to DB")