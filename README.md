# Flask Final Project Starter Template
## Directions
1. Log into GitHub and click the `Use this template` button
2. Name your new repository with a descriptive name
3. In Cloudshell, `git clone` with your repo's link
4. Code your Flask app!
5. Refer to the rest of this `README` file for code snippest on how to incorporate an API or MongoDB

## Extensions
### Including an API
To include an API in your Flask app, you need to include `import requests` in your `app.py` file and potentially in your `model.py` file

### Including MongoDB
To include MongoDB in your Flask app, you need a few pieces of set up first.
#### Set up a .ENV file
1. In your top level folder `touch .env` and then `cloudshell open .env`
2. In your `.env` file include
```bash
MONGO_DBNAME = ''
MONGO_DBUSERNAME = ''
MONGO_DBPASSWORD = ''
MONGO_DBCLUSTER = ''
```
3. In your `app.py` include this code to load your `.env` file.
```python
import os
from dotenv import load_dotenv
load_dotenv()
```

#### Set up PyMongo
1. Import PyMongo and Load the `.env` information.
```python
from flask_pymongo import PyMongo
MONGO_DBNAME = os.getenv("MONGO_DBNAME")
MONGO_DBUSERNAME = os.getenv("MONGO_DBUSERNAME")
MONGO_DBPASSWORD = os.getenv("MONGO_DBPASSWORD")
MONGO_DBCLUSTER = os.getenv("MONGO_DBCLUSTER","cluster0-kxrbn")
```
1. This code stores the MongoDB config information in your flask `app` instance
```python
app.config['MONGO_DBNAME'] = MONGO_DBNAME
app.config['MONGO_URI'] = f'mongodb+srv://{MONGO_DB_USERNAME}:{MONGO_DB_PASSWORD}@{MONGO_DBCLUSTER}.mongodb.net/{MONGO_DBNAME}?retryWrites=true'
```
2. Finally, instantiate the PyMongo class
```python
mongo = PyMongo(app)
```
3. To access the collections in this database use `mongo.db.collection_name`
