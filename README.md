# Server-side REST API using Django & PostgreSQL

This repository contains a **Server-side REST API** built using **Django** and **Django REST Framework (DRF)**, integrated with **PostgreSQL** as the database and managed via **PgAdmin**. The API supports **CRUD operations** and follows RESTful principles.

## 🚀 Features
- Built with **Django** & **Django REST Framework (DRF)**
- Uses **PostgreSQL** as the database
- API documentation with **Swagger**
- Authentication & Permissions
- **CRUD operations** for data management
- Tested using **Postman**

---

## 🛠 Technologies Used
- **Django** - Python Web Framework  
- **Django REST Framework (DRF)** - RESTful API development  
- **PostgreSQL** - Relational database  
- **PgAdmin** - GUI tool for PostgreSQL management  
- **Postman** - API testing tool  

---

## 📌 Installation & Setup

### 1️⃣ Clone the Repository  

git clone https://github.com/vasanthakumar-hub/Server-side-REST-API.git
cd Server-side-REST-API

2️⃣ Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Configure PostgreSQL Database

Install PostgreSQL & PgAdmin (if not installed).
Create a database (e.g., server_db).
Update settings.py with PostgreSQL credentials:
python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'server_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
5️⃣ Apply Migrations

python manage.py makemigrations
python manage.py migrate

6️⃣ Create a Superuser (For Admin Access)

python manage.py createsuperuser

7️⃣ Run the Server

python manage.py runserver

API will be accessible at http://127.0.0.1:8000/

🔥 API Endpoints
Method	Endpoint	Description
GET	/api/items/	Fetch all items
GET	/api/items/{id}/	Fetch a single item
POST	/api/items/	Create a new item
PUT	/api/items/{id}/	Update an item
DELETE	/api/items/{id}/	Delete an item

📄 Project Structure

📂 Server-side-REST-API  
 ├── 📂 server_api  
 │   ├── 📂 models.py         # Database models  
 │   ├── 📂 serializers.py    # DRF serializers  
 │   ├── 📂 views.py          # API views  
 │   ├── 📂 urls.py           # API routing  
 │   ├── 📂 admin.py          # Django Admin settings  
 ├── 📂 server  
 │   ├── settings.py          # Django settings  
 │   ├── urls.py              # Project URL configurations  
 ├── requirements.txt         # Dependencies  
 ├── manage.py                # Django management script  
 ├── README.md                # Documentation  

🛠 Testing the API with Postman

🛠️ Step 1: Install Postman
Download and install Postman from here.

🚀 Step 2: Start Your API Server
Run the server using:
python manage.py runserver
The API will be accessible at http://127.0.0.1:8000/.

🔥 Step 3: Test Endpoints in Postman
1️⃣ GET all items

Method: GET
URL: http://127.0.0.1:8000/api/items/
Click: "Send"
Response: A list of items in JSON format.

2️⃣ GET a single item by ID

Method: GET
URL: http://127.0.0.1:8000/api/items/{id}/
Replace {id} with an actual item ID.

3️⃣ Create a new item

Method: POST
URL: http://127.0.0.1:8000/api/items/
Body (JSON format):

{
    "name": "New Item",
    "description": "This is a test item"
}
Click: "Send"
Response: The created item with an assigned ID.

4️⃣ Update an existing item

Method: PUT
URL: http://127.0.0.1:8000/api/items/{id}/
Body (JSON format):
json
Copy
Edit
{
    "name": "Updated Item",
    "description": "This item has been updated"
}
Click: "Send"
Response: The updated item.

5️⃣ Delete an item

Method: DELETE
URL: http://127.0.0.1:8000/api/items/{id}/
Click: "Send"
Response: A confirmation message.

📌 API Documentation
Open Swagger UI for interactive API documentation: 🔗 http://127.0.0.1:8000/swagger/
Open ReDoc UI for detailed API documentation: 🔗 http://127.0.0.1:8000/redoc/

📝 License
This project is open-source and available under the MIT License.
