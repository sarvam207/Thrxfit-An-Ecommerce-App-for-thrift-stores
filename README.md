# Thrxfit - Ecommerce App for Thrift Stores

**Thrxfit** is a Django-powered ecommerce web application tailored for thrift stores, enabling seamless online storefront management, cart functionalities, user registration, and more.

---
## **Demo Login Credentials:**

Username: Demo

Password: Thrxfit@1

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

## ⚙️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** Django Templates, HTML, CSS, JavaScript (static)
- **Database:** SQLite (default, PostgreSQL-ready)
- **Authentication:** Django built-in (user registration/login)
- **Other:** See `requirements.txt` for all dependencies


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

## 📂 Project Structure

Thrxfit-An-Ecommerce-App-for-thrift-stores/

├── buy_app/ # Handles purchase and order logic

├── cart_app/ # Shopping cart and checkout

├── store_app/ # Product management and catalog

├── user_app/ # User accounts, profiles, auth

├── static/ # Static assets (CSS, JS, Images)

├── thrxfit/ # Project config/settings/urls

├── templates/ # Global templates (if used)

├── requirements.txt # Python dependencies

├── manage.py # Django project launcher

├── db.sqlite3 # Default local database

└── README.md # Project documentation



---

## 🔑 Key Features (Currently Implemented)


- **User Registration & Login**: Secure authentication for shoppers

- **Product Browsing**: By category, with listings and details

- **Cart Management**: Add to cart, update quantities, remove items

- **Order Checkout**: Place orders, order tracking

- **Admin Product Management**: Add/Edit/Delete products (via admin dashboard)

- **Template-based UI**: HTML/CSS/JS for storefront, dashboard, and checkout

---


## 📷 Screenshots

### Home Page

<img width="1899" height="969" alt="image" src="https://github.com/user-attachments/assets/e2a9f2ac-354d-4fba-ba37-32abb139dd7f" />

---
<img width="1903" height="969" alt="image" src="https://github.com/user-attachments/assets/90a6b332-78c2-4954-bdda-502a85ce7794" />

---
### Product Detail Page

<img width="1902" height="968" alt="image" src="https://github.com/user-attachments/assets/c43623ca-34dc-4dd8-a1fc-0a0f111f941a" />

---
<img width="1899" height="971" alt="image" src="https://github.com/user-attachments/assets/1f19456f-56a9-4040-bf8d-73349a30209e" />

---
### Category Filter view
<img width="1901" height="971" alt="image" src="https://github.com/user-attachments/assets/80fa81af-31cf-4701-b6ed-6b385b5cce8d" />

---
### User Authentication
<img width="1897" height="973" alt="image" src="https://github.com/user-attachments/assets/82b7a078-9847-4396-8d06-ba7a6af6e5e3" />

---
<img width="1903" height="970" alt="image" src="https://github.com/user-attachments/assets/39f100fb-2ce3-46eb-9ff7-b9fa0163f3c3" />

---
### User Dashboard (Order history, Manage shipping address, logout functionality)
<img width="1918" height="968" alt="image" src="https://github.com/user-attachments/assets/ae4b21b7-ed96-42bb-8c51-73674d7b1d2f" />

---
<img width="1895" height="960" alt="image" src="https://github.com/user-attachments/assets/bdac6cc0-0c7b-4308-aa0e-1a44dc7ac3de" />

---


### Cart & Checkout (PayPal integration)

This project supports **PayPal payments** as part of the checkout flow. On the cart and checkout page (`buy_app/checkout.html`), users can review their order and pay securely via PayPal.

**How it works:**
- At checkout, the user sees a PayPal button to initiate payment.
- Clicking the button redirects to PayPal’s payment gateway.
- After successful payment, order confirmation is recorded.

**Where to find:**  
- The Buy/Checkout functionality and PayPal button are implemented in `buy_app/checkout.html`.

#### Screenshot Example

<img width="1902" height="973" alt="image" src="https://github.com/user-attachments/assets/763b9184-a40f-476c-883a-013eee79fba9" />

---
<img width="1919" height="1026" alt="image" src="https://github.com/user-attachments/assets/1d804dde-09ff-4de6-b28c-6479b1ec1b95" />


---
### Admin Dashboard
<img width="1894" height="976" alt="image" src="https://github.com/user-attachments/assets/b4fab617-8a57-465c-932b-2f5202a9dd39" />

---
<img width="1916" height="967" alt="image" src="https://github.com/user-attachments/assets/0e89b770-c390-4d88-bdf2-c2a4082db0a0" />

---
<img width="1919" height="907" alt="image" src="https://github.com/user-attachments/assets/a4967dd2-026c-4f93-b2a5-1815a841e484" />

---
<img width="1073" height="584" alt="image" src="https://github.com/user-attachments/assets/fa4566ff-71ff-443a-861a-70310e927cd1" />

---
## 🚧 Future Improvements / TODOs

- Implement product image upload with media handling.
- Email notifications for order confirmation.
- Analytics dashboard for admins.
- Add multiple mock payment gateway integration along with paypal (e.g., Stripe).



---
## 👤 About the Developer

**Sarvam Saroha**

[LinkedIn](https://linkedin.com/in/sarvamsaroha) |
[GitHub](https://github.com/sarvam207) 


_Eager to learn and contribute to professional engineering teams, with a track record of clear communication, efficient coding, and project ownership. Thank you team Thinknyx for considering my submission in the technical screening round._

---
