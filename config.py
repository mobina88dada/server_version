import os
db_config={
    'user':os.environ.get('db_user'),
    'password':os.environ.get('password'),
    'host':os.environ.get('db_host'),
    'database':os.environ.get('database_name')
}

API_TOKEN=os.environ.get('BOT_TOKEN')
SUPPORT_CID=int(os.environ.get('SUPPORT_CID'))
