# JWT_Auth
Repository to create JWT tokens and Refresh Tokens


# Run Application In Detached Moded
docker-compose up -d

# Make A Migration File
docker-compose run api alembic revision --autogenerate -m "Your Message Here"

# Migrate Changes To Postgres Database
docker-compose run api alembic upgrade head