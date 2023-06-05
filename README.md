# Blog Platform using FastAPI

This is a blog platform built using FastAPI framework, which provides a simple and efficient way to create web APIs with Python. It includes token-based authentication to secure the API endpoints.

## Features

- User registration and authentication using tokens
- CRUD operations for blog posts
- User authentication required for creating, updating, and deleting blog posts
- Retrieve and list blog posts
- Token-based authentication using JSON Web Tokens (JWT)

## Prerequisites

Make sure you have the following installed on your system:

- Python 3.7+
- Pip (Python package manager)

## Installation

1. Clone the repository:

2. Navigate to the project directory:

3. Install the required dependencies:


## Configuration

Before running the application, you need to configure some settings. Open the `app/config.py` file and update the following variables:

- `SECRET_KEY`: Set a secret key for securing the JWT tokens.
- `DATABASE_URL`: Update the database URL based on your configuration. By default, SQLite is used for local development.

## Usage

1. Start the application:

2. Open your web browser and navigate to `http://localhost:8000/docs`. This will open the Swagger UI, where you can test the API endpoints and view the documentation.

3. Create a new user by sending a `POST` request to `/users/register` endpoint. Provide the required fields such as username and password in the request body.

4. Authenticate the user by sending a `POST` request to `/users/login` endpoint. Provide the username and password in the request body. This will return an access token.

5. Use the access token in the `Authorization` header for accessing the protected endpoints.

## API Endpoints

- `/users/register`: Register a new user.
- `/users/login`: Authenticate the user and obtain an access token.
- `/blog/posts`: Create a new blog post.
- `/blog/posts/{post_id}`: Retrieve, update, or delete a specific blog post.
- `/blog/posts`: List all blog posts.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).


