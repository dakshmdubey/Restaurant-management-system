# 🍽️ Restaurant Management System

A web-based Restaurant Management System developed using **Python and Django** to simplify restaurant operations, manage orders, maintain menus, and track sales.

## 📌 About the Project

The Restaurant Management System is designed to help restaurant owners manage their daily activities through a simple and user-friendly web interface.

It helps manage food items, customer orders, restaurant tables, and sales reports in one place.

## ✨ Features

- **Dashboard:** Overview of restaurant activities.
- **Menu Management:** Add, update, view, and delete food items.
- **Order Management:** Create and manage customer orders.
- **Order Status:** Track orders (Pending, Preparing, Ready, Delivered).
- **Table Management:** Manage restaurant tables and their availability.
- **Sales Reports:** View restaurant sales and order statistics.
- **PDF Billing:** Generate PDF bills for orders.

## 🛠️ Technologies Used

- Python
- Django
- HTML5
- CSS3
- Bootstrap
- SQLite
- JavaScript

## 📂 Project Structure

```text
restaurant_management/
│
├── restaurant/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── restaurant_management/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── README.md
```

## ⚙️ Installation & Setup

**1. Clone the repository**

```bash
git clone https://github.com/dakshmdubey/Restaurant-management-system.git
```

**2. Navigate to the project directory**

```bash
cd Restaurant-management-system
```

**3. Install dependencies**

```bash
pip install django reportlab
```

Install any other dependencies required by your project.

**4. Apply migrations**

```bash
python manage.py migrate
```

**5. Run the development server**

```bash
python manage.py runserver
```

**6. Open in your browser**

```text
http://127.0.0.1:8000/
```

## 🚀 Future Improvements

- Staff Management
- User Authentication and Role Management
- Improved Analytics and Reporting
- Online Ordering Integration

## 👨‍💻 Author

**Daksh Dubey**

Aspiring Software Engineer

GitHub: https://github.com/dakshmdubey

---

⭐ If you find this project interesting, feel free to explore the repository!