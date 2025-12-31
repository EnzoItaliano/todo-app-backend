# 🚀 Universal Task Management API (Dual-Stack)

A production-ready RESTful API implementation showcasing backend architectural consistency across two of the most popular industry stacks: **Node.js (Express)** and **Python (FastAPI)**.

This repository serves as a technical demonstration of advanced backend concepts including **JWT Authentication**, **Role-Based Access Control (RBAC)**, and **Modern Cryptography**.

---

## 🛠️ The Tech Stacks

### 1. Python Implementation (FastAPI)
* **Framework:** FastAPI (Asynchronous, High Performance)
* **Database ORM:** SQLAlchemy
* **Security:** Argon2id (No 72-byte truncation limit)
* **Auth:** JWT-based stateless authentication
* **Testing:** Comprehensive suite with `pytest`
* **Environment:** Dependency locking via `pip-tools`

### 2. Node.js Implementation (Express)
* **Framework:** Express.js
* **Database ORM:** Sequelize
* **Database:** MySQL
* **Architecture:** MVC (Model-View-Controller) structure

---

## 🔐 Advanced Security Features (Python Version)

While the Node.js version provides a standard CRUD implementation, the Python version is upgraded with enterprise-grade security:
* **Argon2id Hashing:** Uses the modern winner of the Password Hashing Competition to resist GPU-based attacks.
* **RBAC (Role-Based Access Control):** Implements a custom dependency system to restrict sensitive operations (like deleting tasks) to users with the `admin` role.
* **Automated Documentation:** Self-documenting OpenAPI (Swagger) interface available out-of-the-box.

---

## 📦 Installation & Setup

### Python (FastAPI)
1. **Navigate to the directory:**
   ```bash
   cd python-fastapi-implementation
2. **Install & Sync Dependencies:**
    ```bash
    pip install pip-tools
    pip-sync requirements.txt
3. **Run the Server:**

    ```bash
    uvicorn app.main:app --reload
4. **Run Tests:**
    ```bash
    python -m pytest
**Node.js (Express)**
1. **Navigate to the directory:**
    ```bash
    cd node-express-implementation
2. **Install Dependencies:**
    ```bash
    npm install
3. **Run the Server:**

    ```bash
    node server.js
## 🏗️ Project Structure

    /
    ├── node-express-implementation/   # Node.js + Express + Sequelize
    │   ├── app/
    │   │   ├── controllers/           # Request logic
    │   │   ├── models/                # DB Schemas
    │   │   └── routes/                # API Endpoints
    │   └── server.js                  # Entry point
    ├── python-fastapi-implementation/ # Python + FastAPI + SQLAlchemy
    │   ├── app/
    │   │   ├── auth.py                # Security & JWT logic
    │   │   ├── main.py                # API Routes & Logic
    │   │   └── tests/                 # Automated Pytest suite
    │   └── requirements.txt           # Locked dependencies
    └── database/
        └── database.sql               # Shared SQL schema
---
👨‍💻 Developed By
Enzo Italiano Backend Developer Specializing in Python & Node.js