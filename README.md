# transfer
#save requirements:
  $pip freeze > requirements.txt

#install saved requirements: 
  $pip install -r path/to/requirements.txt
  if psycopg2 fail then try to install :
    $apt-get install libpq-dev
    or
    $apt-get install python-dev 
    or
    $apt-get install python3-dev

#migrate the tables to de database, go to the folder that holds manage.py and in the console
  $python manage.py migrate
#run seeder, run on the console
  python manage.py shell
  on the shell write
  >>> from moneytransfer.populate import *
  >>> poblar()


  