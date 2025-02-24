### **Book List API**  
*A simple REST API for managing books, built with Django REST Framework.*

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Django](https://img.shields.io/badge/Django-4.2-green.svg)
![DRF](https://img.shields.io/badge/DRF-3.14-red.svg)

---

## 📚 **Overview**
The **Book List API** provides a simple interface for managing a collection of books. Users can **create, retrieve, update, and delete** books using RESTful endpoints.  

This project is built using **Django REST Framework (DRF)** and follows best practices for API development.

---

## 🏰 **Project Structure**
```
book_list/
│── book_list_manager/
│   ├── migrations/           # Database migrations
│   ├── templates/            # HTML templates (API Documentation)
│   ├── tests.py              # Unit tests for API endpoints
│   ├── models.py             # Database models
│   ├── serializers.py        # DRF serializers for request/response validation
│   ├── views.py              # API logic (CRUD operations)
│   ├── urls.py               # API routes
│   ├── admin.py              # Django admin configuration
│── manage.py                 # Django project manager
│── README.md                 # Project documentation (this file)
│── requirements.txt          # List of dependencies
│── db.sqlite3                # SQLite database (for local development)
```

---

## 🎯 **Design Decisions**
1. **Django REST Framework (DRF)** → Used for building scalable and robust APIs.  
2. **Class-Based Views (CBVs)** → Improve readability and maintainability.  
3. **Bootstrap HTML Template** → Serves API documentation when `/` is accessed.  
4. **Validation Rules**  
   - **ISBN Validation**: Must be exactly **10 or 13 digits** (Regex enforced).  
   - **Publication Date**: Cannot be set in the future.  
5. **Unit Tests** → Ensures API endpoints work as expected.  

---

## ⚙ **Installation**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/AustinMusuya/book_list.git
cd book-list-api
```

### **2️⃣ Create a Virtual Environment & Activate**
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Run Migrations**
```sh
python manage.py migrate
```

### **5️⃣ Start the Server**
```sh
python manage.py runserver
```
Now, open **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** to see the API documentation.

---

## 🔥 **API Endpoints**
| Method | Endpoint       | Description                |
|--------|--------------|---------------------------|
| `GET`  | `/books/`    | Retrieve all books        |
| `POST` | `/books/`    | Add a new book            |
| `GET`  | `/books/<id>/` | Retrieve a specific book |
| `PUT`  | `/books/<id>/` | Update a book            |
| `DELETE` | `/books/<id>/` | Delete a book          |

---

## 📌 **Example Requests**
### **1️⃣ Retrieve All Books**
```sh
curl -X GET http://127.0.0.1:8000/books/
```

### **2️⃣ Create a New Book**
```sh
curl -X POST http://127.0.0.1:8000/books/ \
     -H "Content-Type: application/json" \
     -d '{
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "publication_date": "2008-08-01",
        "isbn": "9780132350884"
     }'
```

### **3️⃣ Update an Existing Book**
```sh
curl -X PUT http://127.0.0.1:8000/books/1/ \
     -H "Content-Type: application/json" \
     -d '{
        "title": "Clean Code (Updated)",
        "author": "Robert C. Martin",
        "publication_date": "2008-08-01",
        "isbn": "9780132350884"
     }'
```

### **4️⃣ Delete a Book**
```sh
curl -X DELETE http://127.0.0.1:8000/books/1/
```

---

## 🧙️ **Running Tests**
To run unit tests, use:
```sh
python manage.py test
```

---

## 📚 **Contributing**
1. Fork the repository  
2. Create a feature branch:  
   ```sh
   git checkout -b feature-new
   ```
3. Commit your changes:  
   ```sh
   git commit -m "Add new feature"
   ```
4. Push and create a pull request  

---

## 📝 **License**
This project is licensed under the MIT License.

---

## **Author**
**Austin Musuya**  
[GitHub](https://github.com/austinmusuya) | [LinkedIn](https://www.linkedin.com/in/austinmusuya)

---

