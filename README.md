# Server-side REST API

This repository contains a **Server-side REST API** implementation using **Python** and **FastAPI**. The project follows RESTful principles to handle CRUD operations efficiently.

## 🚀 Features
- REST API with FastAPI  
- CRUD (Create, Read, Update, Delete) functionality  
- Integrated with a database (MongoDB/MySQL/PostgreSQL)  
- Follows best practices for API development  
- Fast and asynchronous request handling  

## 🛠 Technologies Used
- **FastAPI** - High-performance web framework  
- **Uvicorn** - ASGI server for running FastAPI  
- **Database** - (Mention the database used: MongoDB/MySQL/PostgreSQL)  
- **Pydantic** - Data validation and serialization  

## 📌 Installation & Setup

### 1️⃣ Clone the Repository  

git clone https://github.com/vasanthakumar-hub/Server-side-REST-API.git
cd Server-side-REST-API

2️⃣ Create a Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run the API Server

uvicorn main:app --reload
🔥 API Endpoints
Method	Endpoint	Description
GET	/items	Fetch all items
GET	/items/{id}	Fetch an item by ID
POST	/items	Create a new item
PUT	/items/{id}	Update an existing item
DELETE	/items/{id}	Delete an item
📄 Project Structure
graphql
Copy
Edit
📂 Server-side-REST-API  
 ├── 📂 app  
 │   ├── main.py         # Main FastAPI application  
 │   ├── models.py       # Database models  
 │   ├── routes.py       # API routes  
 │   ├── database.py     # Database connection setup  
 ├── requirements.txt    # Dependencies  
 ├── README.md           # Documentation  
 ├── .gitignore          # Git ignore file  

📌 Testing the API
After running the server, open Swagger UI for interactive API documentation:
🔗 http://127.0.0.1:8000/docs

Alternatively, use Postman or curl for API testing.

📝 License
This project is open-source and available under the MIT License.
