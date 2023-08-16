import uuid
from pymongo import MongoClient
from paste import Paste

HOST='localhost'
PORT=27017
DATABASE_NAME="content"
PASTE_COLLECTION_NAME="pastes"

def get_database(host, port):
    """ Returns the mongodb database """
    client = MongoClient(host, port)
    return client[DATABASE_NAME]

def get_paste_collection():
    """ Returns the pastes collection of the database """
    client = get_database(HOST, PORT)
    return client[PASTE_COLLECTION_NAME]

def generate_uuid():
    """ Generates a new UUID """
    return str(uuid.uuid4())

def create_paste(content, s3_key=None, 
                expires=None, is_exploading=False, 
                is_encrypted=False):
    """ Creates a paste object """
    paste_id = generate_uuid()
    return Paste(id=paste_id, content=content, s3_key=s3_key, expires=expires, 
                      is_exploading=is_exploading, is_encrypted=is_encrypted)

def insert_paste(paste_collection, paste: Paste):
    """ Inserts paste into database """
    try:
        insert_result = paste_collection.insert_one(paste.mongo_obj)
        return True, insert_result.inserted_id
    except Exception as e:
        return False, e
    
def get_paste(paste_collection, paste_id):
    """ Returns the paste given a paste_id. If not found, return None """
    return paste_collection.find_one({'_id': paste_id})

def delete_paste(paste_collection, paste_id):
    """ Deletes paste from database. 
        Returns (True, delete_count) if object was successfully deleted
        Returns (False, Exception) if object failed to be deleted
    """
    try:
        delete_result = paste_collection.delete_one({'_id': paste_id})
        if delete_result.deleted_count == 0:
            return False, Exception("No object found with paste_id " + paste_id)
        return True, delete_result.deleted_count

    except Exception as e:
        return False, e

if __name__ == "__main__":   
  
    # Get the database
    #dbname = get_database('localhost', 27017)
    #collection_name = dbname["pastes"]
    #paste_2_test = Paste(id="123457", content="This is a test paste 2")
    #collection_name.insert_many([paste_2_test.mongo_obj])

    paste_collection = get_paste_collection()
    paste = create_paste(content="This is a test paste")
    #paste_bad = Paste(id="1a3b4daa-f7b3-4e78-946b-13266a8d935c", content="asdf")
    #print(insert_paste(paste_collection, paste))
    print(delete_paste(paste_collection, '86355668-b932-47f5-aa08-24d989d69206'))
