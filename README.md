# 🚀 Lostify API (My First REST API)

This is my first REST API built using FastAPI as part of my learning journey alongside Android development.

---

## 📌 About the Project

Lostify API is a simple backend service that allows users to:

* Add lost items
* View all lost items
* Work with JSON-based requests and responses

This project helped me understand how backend systems work and how mobile apps communicate with servers.

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Uvicorn

---

## ⚙️ How to Run the Project

1. Install dependencies:

```bash
pip install fastapi uvicorn
```

2. Run the server:

```bash
uvicorn main:app --reload
```

3. Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoints

### 🔹 GET /

* Check if API is running

### 🔹 POST /add_item

* Add a lost item

**Request Body:**

```json
{
  "name": "wallet",
  "description": "black leather wallet"
}
```

---

### 🔹 GET /items

* Get all lost items

---

## 📚 What I Learned

* How to build REST APIs
* Handling JSON data
* Using FastAPI
* API testing using Swagger docs
* Backend fundamentals

---

## 🚧 Future Improvements

* Add database (SQLite / MongoDB)
* Add unique IDs for items
* Add authentication (JWT)
* Connect with Android app
* Add image upload support

---

## 🙌 Author

Built by me as part of my backend learning journey 💻

---

⭐ Feel free to check it out and give feedback!
