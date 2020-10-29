# transfer
#Install postgres
  https://phoenixnap.com/kb/how-to-install-postgresql-on-ubuntu
  https://www.liquidweb.com/kb/change-a-password-for-postgresql-on-linux-via-command-line/
 
 Note: if you need to change the password perhaps you would need to start the engine
 sudo /etc/init.d/postgresql start
  
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


  
