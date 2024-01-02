# Recipe API
    This is the API and frontend for a recipe management application.

## Backend
    The backend is a Flask application that provides RESTful API endpoints for managing recipes.

# Key files:

    app.py - Defines the Flask application and API routes
    models.py - Defines the Recipe SQLAlchemy model
    database.py - Database configuration and initialization
    The backend handles:

    Storing recipes in a SQLite database
    Exposing endpoints to add, edit, delete recipes
    Serving the frontend static files
    API Endpoints
    GET /recipes - Get a list of all recipes
    POST /add_recipe - Create a new recipe
    PUT /recipes/<id> - Update a recipe by id
    DELETE /recipes/<id> - Delete a recipe by id
    Frontend
    The frontend provides a simple UI for managing recipes.

## Key files:

    index.html - Main recipes list page
    add_recipe.html - Form for adding a new recipe
    The frontend handles:

    Displaying recipes fetched from the API
    Form for adding a new recipe
    Making API requests to CRUD recipes
    Getting Started
    To run the app locally:

    Clone the repo
    Install dependencies with pip install -r requirements.txt
    Run python app.py
    Access the app at http://localhost:9000
    The frontend is served from the Flask backend.

# Status
    This project is currently in development. Additional features and improvements will be made over time.

# License
#### This project is licensed under the MIT License - see the LICENSE file for details.