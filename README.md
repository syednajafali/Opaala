# Opaala
Assignment for Book Management
-- Book List Management App

This project is a full-stack application using Angular (Frontend) and Django REST Framework (Backend) to manage book lists.

-- Users can:
1) Create new book lists

2) Fetch available books from the backend

3) Add books to a list

4) Remove books from a list

5) Delete a book list

-- Technologies Used :

-   Frontend (Angular 19)
-   Standalone Components
-   Angular Services for API Calls
-   HttpClientModule for HTTP Requests
-   TypeScript
-   CSS for Basic Styling

-- Backend (Django REST Framework) : 

-   Django Models for Book, List, and Booklist
-   REST API Endpoints to Perform CRUD Operations



-- Clone the repository:

-   git clone <https://github.com/syednajafali/Opaala.git>
-   cd backend

-- Create a virtual environment and install dependencies:

-   python -m venv Opaala
-   source Opaala/bin/activate  # For macOS/Linux
-   Opaala\Scripts\activate  # For Windows
-   pip install -r requirements.txt
-   Run database migrations:
-   python manage.py migrate
-   Start the Django development server
-   python manage.py runserver

-- Frontend (Angular) Setup

-   Navigate to the frontend folder:
-   cd frontend
-   Install dependencies:
-   npm install
-   Start the Angular development server
-   ng serve

-- API Endpoints

Method     |     Endpoint     |      Description

GET             /api/books/         Retrieve all books
GET             /api/lists/         Retrieve all book lists
POST            /api/lists/         Create a new book list
GET             /api/booklists/     Retrieve books in lists
POST           /api/booklists/      Add book to a list
DELETE         /api/booklists/{id}/  Remove book from a list
DELETE          /api/lists/{id}/      Delete a book list



Usage Instructions

-   Create a new book list
-   Enter a list title and click Create List.
-   Add a book to a list
-   Select a book from the dropdown and click Add Book.
-   Remove a book from a list
-   Click the X button next to the book.
-   Delete a book list
-   Click X Delete List button.

Folder Structure

📂 Opaala
 ├── 📂 backend  (Django REST API)
 │    ├── manage.py
 │    ├── 📂 Opaalalibrary (Django app)
 │    │    ├── models.py
 │    │    ├── views.py
 │    │    ├── urls.py
 │    │    ├── serializers.py
 │    │    ├── settings.py
 │    
 │
 ├── 📂 frontend  (Angular App)
 │    ├── src/
 │    │    ├── app/
 │    │    │    ├── components/
 │    │    │    │    ├── book-list.component.ts
 │    │    │    │    ├── book-list.component.html
 │    │    │    ├── services/book.service.ts
 │    │    ├── main.ts
 │    │    ├── app.config.ts
 │    ├── package.json



Contributors :  Syed Najaf Ali


