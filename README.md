# django-rest-nosql-mongodb  ✅
![django-rest-nosql-mongodb image](https://raw.githubusercontent.com/excommunicades/django-rest-nosql-mongodb/main/django-rest-nosql-mongodb.png)

## DESCRIPTION: 

This project provides a simple RESTful API for managing products in an online store. The API allows users to perform basic CRUD (Create, Read, Update, Delete) operations on product data. The backend is built using Django, Django REST Framework, and Djongo (a connector for MongoDB), making it suitable for projects that require NoSQL databases.

## Key Features 💡

- **Product Management:** Allows users to create, read, update, and delete product entries through a RESTful API.
- **MongoDB Integration:** Uses Djongo to interact with MongoDB, providing a NoSQL solution for storing and retrieving product data.
- **Data Serialization:** Implements Django REST Framework serializers to format and validate product data for API interactions.

### Prerequisites 💻

Ensure you have Docker and Docker Compose installed on your machine. You can download them from:

- Python 3.x installed on your machine.
- [MongoDB running locally or through a cloud service (e.g., MongoDB Atlas).](https://www.mongodb.com/)

### Environment Variables
Create a `.env` file in the root of your project directory with the following content:
```
    NAME=your_db_name (Example: DjangoNoSQL)
    HOST=your_mongo_host (your mongodb connection)
    USERNAME=your_mongo_username (Example: user)
    PASSWORD=your_mongo_password (Example: 12345)
    AUTHSOURCE=your_authsource (Example: admin)
    AUTHMECHANISM=your_authmechanism (Example: SCRAM-SHA-1)
```

# Installation Guide 📕:

1. **Clone the repository:** ```git clone https://github.com/excommunicades/django-rest-nosql-mongodb.git``` -> ```cd DjangoNoSQL```
2. **Install dependencies:** ```pip install -r requirements.txt```
4. **Create database migrations:** ```python3 manage.py makemigrations```
4. **Apply database migrations:** ```python3 manage.py migrate```
5. **Run the development server:** ```python3 manage.py runserver```

### API Endpoints

- **POST** /api/products/: Create a new product entry.🟡
- **GET** /api/products/: Retrieve all products. 🟢
- **GET** /api/products/{id}/: Retrieve a specific product by its primary key (ID). 🟢
- **PUT** /api/products/{id}/: Update an existing product by its primary key (ID). 🟡
- **PATCH** /api/products/{id}/: Partially update an existing product by its primary key (ID).🟡
- **DELETE** /api/products/{id}/: Delete a specific product by its primary key (ID). 🔴

# Stopping the Services 🚪

1. **To stop the server:** ```python3 manage.py stop OR Ctrl+C```

# Conclusion 🎉

This project provides a simple but powerful API to manage products with MongoDB as the database backend. It is designed to be easy to extend, allowing you to add more features or adapt it to fit different use cases.

You can use it as a starting point for more complex systems, or simply as an example of integrating Django with MongoDB using Djongo.

## Authors 😎

- **Stepanenko Daniil** - "DjangoNoSQL"