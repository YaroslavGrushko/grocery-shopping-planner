# Grocery shopping planner - Django (Rest Framework) REST API (CRUD for products and categories)
## Features:  
- Django Rest Framework  
- PostgreSQL  
- Authorization (JWT Token)  
- Swagger documentation (drf-yasg)  
- Docker  
- Unit Tests  
- Ruff (linter and code formatter)  
- GitHub Actions  
- Front-end part on **React** ([Grocery-shopping-planner-frontend](https://github.com/YaroslavGrushko/Grocery-shopping-planner-frontend))  
  
## Get Started  
**To run with Docker:**    
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
10. Now you can visit [http://127.0.0.1:8000/api/swagger/](http://127.0.0.1:8000/api/swagger/) to access REST API  
**_Note:_** All methods (except /accounts/login/ and /accounts/register/) of Grocery REST API needed JWT Token Authorization, so to use this methods you need:  
  10.1 register User with /accounts/register/ endpoint or login as existing User with /accounts/login/ . As response you will get JWT Token.  
  10.2 on Swagger page [http://127.0.0.1:8000/api/swagger/](http://127.0.0.1:8000/api/swagger/) click **Authorize** button and insert your JWT Token in value field like that:

    <p align="center">
        <img src="https://github.com/YaroslavGrushko/grocery-shopping-planner/blob/main/jwt_token.png?raw=true" width="500" height="auto" style="margin: auto">
    </p>

## Bonus: To run with front end (React) part:  
1. Run this Django app locally  
2. Run [Front-end part](https://github.com/YaroslavGrushko/Grocery-shopping-planner-frontend) locally  
3. Visit [http://localhost:5173](http://localhost:5173) and feel free to register/login/create categories and products!  
