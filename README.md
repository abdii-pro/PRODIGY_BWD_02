# Flask User Management System

A simple Flask web application that allows users to perform CRUD (Create, Read, Update, Delete) operations on user data. The app uses PostgreSQL for database management and SQLAlchemy for Object-Relational Mapping (ORM). It includes input validation and supports database migrations via Flask-Migrate.

## Features

- **Create**: Add a new user with name, email, and age.
- **Read**: Fetch all users or a specific user by ID.
- **Update**: Modify user details such as name, email, and age.
- **Delete**: Remove a user from the database.
- **Validation**: Ensures correct input for name, email, and age.
  
## Prerequisites

Before running the app, ensure that you have the following installed:
- Python 3.x
- PostgreSQL

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/abdii-pro/PRODIGY_BWD_02.git
   cd PRODIGY_BWD_02
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file to store your database URI:
   ```bash
   touch .env
   ```

   Inside `.env`, add the following:
   ```
   DB_URI=postgresql+psycopg2://username:password@localhost:5432/your_database_name
   ```

   Replace `username`, `password`, and `your_database_name` with your PostgreSQL credentials.

5. Initialize the database and apply migrations:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

## Running the Application

To start the Flask development server:
```bash
flask run
```

The application will be running at `http://127.0.0.1:5000`.

## API Endpoints

- **POST** `/users`: Create a new user
- **GET** `/users`: Retrieve all users
- **GET** `/users/<user_id>`: Retrieve a specific user by ID
- **PUT** `/users/<user_id>`: Update an existing user
- **DELETE** `/users/<user_id>`: Delete a user by ID

## Testing with Postman

You can test the endpoints using Postman or any API testing tool:
- Create user: POST `http://127.0.0.1:5000/users`
- Get all users: GET `http://127.0.0.1:5000/users`
- Get user by ID: GET `http://127.0.0.1:5000/users/<user_id>`
- Update user: PUT `http://127.0.0.1:5000/users/<user_id>`
- Delete user: DELETE `http://127.0.0.1:5000/users/<user_id>`
