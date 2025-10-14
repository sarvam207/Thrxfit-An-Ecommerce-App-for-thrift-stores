# Thrxfit - Ecommerce App for Thrift Stores

**Thrxfit** is a Django-powered ecommerce web application tailored for thrift stores, enabling seamless online storefront management, cart functionalities, user registration, and more.

---

## 🌐 Architecture Diagram

```
+-----------------------+
|      Client (Web)     |
+----------+------------+
           |
           v
+-----------------------+
|      Static Files     |  <- HTML, CSS
+----------+------------+
           |
           v
+-----------------------+
|      Django Views     |  (store_app, cart_app, buy_app, user_app)
+----------+------------+
           |
           v
+-----------------------+
|    Django Models      |  <- ORM interacting with
+----------+------------+
           |
           v
+-----------------------+
|    Database Layer     |  (SQLite by default)
+-----------------------+
```

- **store_app**: Handles product management, listing, and details.
- **cart_app**: Manages shopping cart features.
- **buy_app**: Processes purchase logic and checkout.
- **user_app**: Handles user registration, authentication, and profiles.
- **static/**: Stores HTML templates, CSS, and static resources.

---

## ⚙️ Setup and Deployment Instructions

### Prerequisites

- Python 3.x (recommended: 3.10+)
- Git
- pip (Python package manager)

### 1. Clone the Repository

```bash
git clone https://github.com/sarvam207/Thrxfit-An-Ecommerce-App-for-thrift-stores.git
cd Thrxfit-An-Ecommerce-App-for-thrift-stores
```

### 2. (Optional) Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Linux/Mac
venv\Scripts\activate          # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Run Development Server

```bash
python manage.py runserver
```

### 6. Access the App

Open your browser and navigate to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🚀 Deployment

- By default, the app uses **SQLite** (`db.sqlite3`).
- For production, update your settings to use **PostgreSQL** or similar.
- Static and media files should be served using a web server like **Nginx**.
- For cloud deployment, platforms like **Render**, **Railway**, or **Heroku** are recommended.
- Configure relevant environment variables (SECRET_KEY, DEBUG, DB credentials) before deployment.

---

## 📂 Main Folders Overview

- **store_app/**: Product catalog management
- **cart_app/**: Cart/checkout mechanics
- **buy_app/**: Purchase workflow and order management
- **user_app/**: User profiles, login, registration
- **static/**: Frontend resources
- **thrxfit/**: Django project settings and routing

---

## ✨ Additional Details

- **Requirements** are listed in `requirements.txt`.
- The project follows standard Django application structure.
- Integration-ready for payment gateways (add endpoints in `buy_app`).
- To add new thrift stores/products, modify models in `store_app`.

---

## 💡 Contribution

Feel free to open pull requests for bug fixes, new features, or improvements!

---

## 📃 License

This project is licensed under the MIT License.

---
