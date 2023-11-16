# JWT_Auth
The purpose of this repository is to provide individuals with a baseline repository they can use to build personal projects. Here is the tech stack used in the repository
- Server: FastAPI
- Database: PostgreSQL 
- Object Relational Mapper: SQL Alchemy
- Migration Tool: Alembic
- Frontend Framework: React
- State Management Library: Redux Toolkit
- CSS Framework: Tailwind

## How To Start The Application
Fork this repository
```
git clone thissite
```
```
cd /path/to/JWT_Auth
```
```
docker-compose up -d
```

## Navigating The Application
- React Client is at 'http://localhost:5173'
- FastAPI Server is at 'http://localhost:8000'
- PG Admin GUI is at 'http://localhost:5050'

## PG Admin
### Accessing GUI
- Navigate to `http://localhost:5050/`
- email: `admin@admin.com`
- password: `root`

### Registering Database 
- Once signed on, right click on server, and select register server
- In the `General` tab, give the server any name you want
- In the `Connection` tab, enter the following:
- Host name/address: db
- Port: 5432
- Maintenance Database: Postgres
- Username: root
- Password: root
- Optional: check save password so you don't have to log into the database again whenever you log onto PG Admin

## Database Management
This project uses SQL Alchemy and Alembic to manage changes to the database and migrations. If you want to make changes to your local database you can do the following:

#### 1. Make a Change to JWT_Auth/app/models.py
These changes will be picked up and recognized by SQL Alchemy

#### 2. Make A Migration File
`docker-compose run api alembic revision --autogenerate -m "Your Message Here"`

#### 3. Migrate Changes To Postgres Database
`docker-compose run api alembic upgrade head`
