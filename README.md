# Blog Platform using FastAPI

This is a blog platform built using the FastAPI framework, which provides a simple and efficient way to create web APIs with Python. The platform includes token-based authentication to secure the API endpoints, ensuring that only authorized users can access the resources.

## Features

- **FastAPI Framework**: Built using FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **Token-based Authentication**: Implements token-based authentication to secure the API endpoints, ensuring that only authorized users can access the resources.
- **User Management**: Provides user management functionalities such as user registration, login, and password reset.
- **Blog Creation and Management**: Allows users to create, read, update, and delete blog posts. Users can also add tags to their blog posts for better categorization.
- **Comments and Likes**: Users can comment on blog posts and like them to show their appreciation.
- **Search Functionality**: Includes a search functionality to search for blog posts based on keywords or tags.
- **Pagination**: Implements pagination for better performance and usability when dealing with large amounts of data.
- **Database Support**: Utilizes a database (e.g., PostgreSQL, MySQL, SQLite) to store blog posts, user information, comments, and likes.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/abinashbordoloi/Blog_Platform-using-FastAPI.git
   
## Installation

To run this project locally, follow these steps:

2. Navigate to the project directory:

     ```bash
     cd Blog_Platform-using-FastAPI
   
3. Create and activate a virtual environment (optional but recommended):
  python3 -m venv env
      ```bash
      source env/bin/activate
    
 
4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Configure the database settings in the config.py file.
6. Configure the database settings in the config.py file.
    ```bash
    alembic upgrade head
    ```

7. Start the development server
    ```
    uvicorn main:app --reload
    ```

8. The blog platform should now be accessible at http://localhost:8000.






