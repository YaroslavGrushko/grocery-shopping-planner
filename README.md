To run with Docker:  
1. create .env and specify environment variables like this:  
**DB_HOST=127.0.0.1  
  DB_NAME=grocery  
  DB_USER=postgres  
  DB_PASSWORD=1**  
   
3. Install Docker locally
4. From root of project:  
   **docker-compose build**  
   **docker-compose up**  
You see error:  
**FATAL:  database "grocery" does not exist** - it's OK, keep calm.  
6. Open Terminal/Cmd and enter to psql:  
  **psql -h localhost -p 5432 -U postgres**  
  **create database grocery;**
7. Exit psql and make migrations  
**python manage.py makemigrations**  
**python manage.py migrate**  
8. create django superuser:  
**python manage.py createsuperuser**  
9. restart docker-compose:  
to stop on Windows: **ctrl+c**  
to start: **docker-compose up**
10. Now visit [http://127.0.0.1:8000/api/swagger/](http://127.0.0.1:8000/api/swagger/) and feel free to use REST API