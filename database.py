from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get MongoDB Atlas credentials from environment variables
username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")
cluster_uri = "cluster0.xb0mite.mongodb.net"

def get_database_connection(username, password, cluster_uri):
    # Construct the URI with your credentials
    uri = f"mongodb+srv://{username}:{password}@{cluster_uri}/?retryWrites=true&w=majority"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    
    return client

# Establish a connection to the database
client = get_database_connection(username, password, cluster_uri)

# Now you can use `client` to interact with the database (e.g., insert data, query data, etc.)


db = client["Expense_Tracker"]
collection = db["periods"]

def insert_period(period, incomes, expenses, comment):
    """Inserts a new period record into the MongoDB collection."""
    data = {
        "key": period,
        "incomes": incomes,
        "expenses": expenses,
        "comment": comment
    }
    collection.insert_one(data)

def fetch_all_periods():
    """Returns a list of all periods."""
    return list(collection.find({}, {"_id": 0}))

def get_period(period):
    """Returns the period data if found, otherwise returns None."""
    return collection.find_one({"key": period}, {"_id": 0})
