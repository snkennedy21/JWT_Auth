# JWT_Auth
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
<br>
This repository is intended to provide individuals with a starting point for building personal projects and to help with learning. 

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#application-features">Application Features</a>
    </li>
    <li>
      <a href="#tech-stack">Tech Stack</a>
    </li>
    <li><a href="#how-to-get-started">How To Get Started</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

# Application Features
- Full Stack Application
- Frontend Web Client
- API Server
- Persistent Database
- Authentication
- JWT Based Access Tokens and Refresh Tokens
- Examples of Protected/Unprotected API Endpoints
- Automated API Calls
- Dockerized Environment
- 3rd Party Database Management Tool
- Database Migration Tool
- SQL ORM

# Tech Stack
- Server: FastAPI 
- Database: PostgreSQL 
- Object Relational Mapper: SQL Alchemy
- Database Migration Tool: Alembic
- Frontend Framework: React
- State Management Library: Redux Toolkit
- CSS Framework: Tailwind
- Containerization Tools: Docker & Docker-Compose

# How To Get Started
### Starting The Application
- Fork this repository
- clone your fork
- cd /path/to/your-fork
- `docker-compose up`

### Accessing The Application
- React Client is at 'http://localhost:5173'
- FastAPI Server is at 'http://localhost:8000'
- PG Admin GUI is at 'http://localhost:5050'

### Using PG Admin

- Navigate to 'http://localhost:5050/'
- email: `admin@admin.com`
- password: `root`
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
