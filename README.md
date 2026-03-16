# 🎮 Flask Game Explorer

A simple Flask-based web application that allows users to browse video games using the RAWG Video Games Database API and manage a personalized favorites list.

This project was built primarily to practice **backend fundamentals**, including API integration, authentication, database relationships, and asynchronous frontend communication using JavaScript.

---

# 📌 Features

* Browse video games from the **RAWG Video Games Database API**
* User **registration and login system**
* **Session-based authentication**
* Add games to a **personal favorites list**
* Remove games from favorites using **asynchronous DELETE requests**
* Favorites are stored **per user** in the database
* Dynamic UI updates using **JavaScript Fetch API**

---

# 🏗 Project Architecture

This project follows a simple **Flask MPA (Multi Page Application)** architecture.

Core components:

1. **Flask**

   * Handles routing
   * Renders HTML templates
   * Manages authentication and sessions

2. **External API**

   * RAWG Video Games Database API provides game data.

3. **SQLite + SQLAlchemy**

   * Stores user accounts
   * Stores user favorites

4. **JavaScript (Fetch API)**

   * Handles asynchronous requests for adding/removing favorites.

---

# 📂 Project Structure

```
app3/
│
├── app.py                # Main Flask application
├── models.py             # SQLAlchemy database models
├── extensions.py         # Database initialization
├── services.py           # External API service logic
│
├── templates/            # HTML templates
│   ├── games.html
│   ├── favorites.html
│   └── login / register pages
│
├── static/
│   └── js/
│       └── game.js       # Frontend API calls
│
├── instance/
│   └── app.db            # SQLite database
│
└── .env                  # Environment variables
```

---

# 🗄 Database Schema

## Users Table

| Column        | Type    | Description     |
| ------------- | ------- | --------------- |
| id            | Integer | Primary key     |
| username      | String  | Unique username |
| password_hash | String  | Hashed password |

Passwords are stored using **Werkzeug password hashing**.

---

## Favorites Table

| Column     | Type     | Description                   |
| ---------- | -------- | ----------------------------- |
| id         | Integer  | Primary key                   |
| user_id    | Integer  | Foreign key referencing users |
| game_id    | Integer  | Game ID from RAWG API         |
| game_name  | String   | Game title                    |
| created_at | DateTime | Timestamp                     |

Relationship:

```
User 1 ---- * Favorites
```

Each user can have multiple favorite games.

---

# 🔐 Authentication

Authentication is implemented using **Flask sessions**.

Workflow:

1. User registers with username and password
2. Password is hashed using:

```
werkzeug.security.generate_password_hash()
```

3. After login, the user's `id` is stored in the session:

```
session["user_id"]
```

4. Protected routes check the session before allowing access.

---

# ⭐ Favorites System

The favorites system supports full CRUD operations.

### Add Favorite

Frontend sends a POST request:

```
POST /favorites/<game_id>
```

Payload:

```
{
  "game_name": "Game Title"
}
```

Backend logic:

* Check user session
* Create a new `Favorites` record
* Save it to the database

---

### Delete Favorite

Frontend sends a DELETE request:

```
DELETE /favorites/<game_id>
```

Backend logic:

1. Validate user session
2. Find the favorite record for that user
3. Delete the record from the database

After deletion, the UI updates dynamically using JavaScript.

---

# 🌐 RAWG API Integration

Game data is retrieved from:

RAWG Video Games Database API

Example request flow:

```
Flask → RAWG API → JSON Response → Template Rendering
```

The application does **not store game data locally**; it only stores user favorites.

---

# ⚙️ Environment Variables

Sensitive values are stored in a `.env` file.

Example:

```
SECRET_KEY=your-secret-key
RAWG_API_KEY=your-api-key
```

Loaded using:

```
python-dotenv
```

---

# 🚀 Running the Project

## 1️⃣ Install dependencies

```
pip install flask
pip install flask-sqlalchemy
pip install python-dotenv
pip install requests
```

---

## 2️⃣ Set environment variables

Create a `.env` file:

```
SECRET_KEY=your_secret_key
RAWG_API_KEY=your_rawg_api_key
```

---

## 3️⃣ Run the application

```
flask run
```

Then open:

```
http://127.0.0.1:5000
```

---

# 🧠 Learning Goals

This project focuses on understanding:

* Flask application structure
* REST-style route design
* Database relationships using SQLAlchemy
* Session-based authentication
* Frontend-backend interaction using Fetch API
* External API consumption

---

# 📚 Future Improvements

Possible improvements include:

* Prevent duplicate favorites
* Pagination for game results
* AJAX-based favorite loading
* PostgreSQL migration
* User profile page
* Favorite game thumbnails

---

# 👨‍💻 Author

Developed as a backend learning project focused on Flask and API integration.
