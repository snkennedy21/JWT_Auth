# JWT_Auth
The purpose of this repository is to provide individuals with a baseline repo from which to build personal projects. The tech stack for this baseline project is going to be the following
- Server: FastAPI
- Database: PostgreSQL 
- Object Relational Mapper: SQLAlchemy
- Migration Tool: Alembic
- Frontend Framework: React
- State Management Library: Redux
- CSS Framework: Tailwind

# Run Application In Detached Moded
docker-compose up -d

# Make A Migration File
docker-compose run api alembic revision --autogenerate -m "Your Message Here"

# Migrate Changes To Postgres Database
docker-compose run api alembic upgrade head