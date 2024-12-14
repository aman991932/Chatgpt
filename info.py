from os import environ

API_ID = int(environ.get('API_ID', '21956488'))
API_HASH = environ.get('API_HASH', '812529f879f06436925c7d62eb49f5d1')
BOT_TOKEN = environ.get('BOT_TOKEN', "7760069843:AAH4QG0WloZkx9zDgbj0OZjndoU7LGDZ5PE")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002110971750"))
ADMINS = int(environ.get("ADMINS", "5977931010"))
DB_URI = environ.get('DB_URI', "mongodb+srv://aman727587:aman@cluster0.bk39x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get('DB_NAME', "cluster0")
START_IMG = environ.get('START_IMG', 'https://envs.sh/Aeg.jpg')
START = environ.get('START', 'https://envs.sh/AwV.jpg')              
AUTH_CHANNEL = int(
    environ.get("AUTH_CHANNEL", "-1002102037760")
)  # add your channel id for force subscribe
FSUB = environ.get("FSUB", True)
