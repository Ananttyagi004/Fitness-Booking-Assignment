Here’s a complete `README.md` file for your **Fitness Studio Booking API** with setup instructions and all required cURL examples:

---

### 📄 `README.md`

````markdown
# Fitness Studio Booking API

A simple Django-based REST API for a fictional fitness studio offering classes like Yoga, Zumba, and HIIT. Users can view available classes, book a class, and retrieve bookings using their email.

---

##  Features

- View all upcoming fitness classes
- Book a spot in a class (with slot validation)
- Retrieve all bookings by email
- Timezone-aware (IST)
- In-memory DB (SQLite)
- Clean, modular Django + DRF code

---

##  Setup Instructions

```bash
git clone https://github.com/<your-username>/fitness-booking-api.git
cd fitness-booking-api
python -m venv env
source env/bin/activate   # Windows: env\Scripts\activate
pip install -r requirements.txt

# Run initial setup
python manage.py makemigrations
python manage.py migrate


# Start server
python manage.py runserver
````

---


##  API Endpoints & Sample cURL Requests

###  `GET /api/classes/`

Fetch all upcoming fitness classes

```bash
curl -X GET http://localhost:8000/api/classes/
```

---

###  `POST /api/book/`

Book a class by providing class ID, client name, and email

```bash
curl -X POST http://localhost:8000/api/book/ \
  -H "Content-Type: application/json" \
  -d '{
    "class_id": 1,
    "client_name": "Anant Tyagi",
    "client_email": "anant@example.com"
}'
```

---

###  `POST /api/bookings/`

Retrieve all bookings made by a specific email

```bash
curl -X POST http://localhost:8000/api/bookings/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "anant@example.com"
}'
```

🧾 **Sample Response:**

```json
[
  {
    "id": 1,
    "client_name": "Anant Tyagi",
    "client_email": "anant@example.com",
    "class_name": "Yoga",
    "date_time": "2025-06-10T17:00:00Z",
    "instructor": "Yoga Instructor"
  }
]
```

---

## 🧠 Tech Stack

* Python 3
* Django 4.x
* Django REST Framework
* SQLite (in-memory)

---





