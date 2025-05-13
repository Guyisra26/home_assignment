# FastAPI CRUD Application

This project implements a RESTful API using FastAPI for managing Users and Partners with file-based persistence.

## Project Overview

This application provides CRUD (Create, Read, Update, Delete) operations for two entity types:
- **Users**: With status tracking (active/inactive)
- **Partners**: With a flexible, open-ended data structure

The persistence layer uses JSON files for data storage, making it simple to deploy without database dependencies.

## Features

- RESTful API design with proper resource URLs
- Complete CRUD operations for both entity types
- Input validation using Pydantic models
- File-based persistence using JSON files
- Comprehensive test suite

## Requirements

- Python 3.10+
- Dependencies listed in requirements.txt

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Guyisra26/home_assignment.git
   cd home_assignment
   ```

2. **Set up a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To start the application, run:

```bash
uvicorn main:app --reload
```

The API will be available at http://localhost:8000.

You can access the auto-generated API documentation at:
- http://localhost:8000/docs (Swagger UI)

## API Endpoints

### Users

- `GET /users` - List all users
- `GET /users/{id}` - Get a specific user by ID
- `POST /users` - Create a new user
- `PUT /users/{id}` - Update an existing user
- `DELETE /users/{id}` - Delete a user

**User Model:**
```json
{
  "status": "active" // or "inactive"
}
```

### Partners

- `GET /partners` - List all partners
- `GET /partners/{id}` - Get a specific partner by ID
- `POST /partners` - Create a new partner
- `PUT /partners/{id}` - Update an existing partner
- `DELETE /partners/{id}` - Delete a partner

**Partner Model:**
```json
{
  "data": {
    // Any JSON-compatible data
  }
}
```

## Testing

To run the test suite:

```bash
pytest
```

The project includes both unit tests and end-to-end tests:
- Unit tests for the database client
- End-to-end tests for API endpoints
licensed under the MIT License - see the LICENSE file for details.