
# 🛂 Visitor Management System (CVMS)

A web-based **Visitor Management System** built using **Django**, designed to manage and monitor visitors in an organization. It includes features for adding, searching, updating, and filtering visitor records between dates.

---

## 📌 Features

- 🔐 User authentication
- 🧾 Add new visitors
- 📋 Manage existing visitor records
- 🔍 Search by name or contact number
- 📅 Filter visitors between two dates
- 📊 Pagination support
- 🎨 Clean and responsive UI using Bootstrap 5
- ✅ Flash messages for successful actions
- 🗂 Sidebar navigation for easy access

---

## ⚙️ Tech Stack

| Layer      | Technology                  |
|------------|------------------------------|
| Backend    | Django (Python)              |
| Frontend   | HTML5, CSS3, Bootstrap 5     |
| Icons      | Bootstrap Icons              |
| Database   | SQLite (can be switched to PostgreSQL/MySQL) |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/visitor-management.git
cd visitor-management
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to open the app.

---

## 📁 Project Structure

```
visitor-management/
│
├── manage.py
├── db.sqlite3
├── visitor_app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── ...html files
├── static/
│   └── css/js/images
├── templates/
│   └── base.html
└── README.md
```

---

## 🔐 Admin Access

Create a superuser to access Django Admin:

```bash
python manage.py createsuperuser
```

---

## ✍️ Screenshots

> 📌 Add some screenshots of your dashboard, add/search forms, etc.

---

## 💡 Future Enhancements

- Email notification to admin on new visitor
- PDF download/export of visitor logs
- Role-based access (e.g., receptionist, security)
- Integration with RFID or QR scan

---

## 🧑‍💻 Author

- **Vedant Thate**
- GitHub: [@yourusername](https://github.com/yourusername)

---

## 📄 License

This project is open source under the [MIT License](LICENSE).
