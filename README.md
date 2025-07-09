# 🧠MindVault Pro

**MindVault Pro** is an extended, more powerful version of MindVault — adding notifications, better UX, cleaner UI, and dashboard functionality.

---


## 🚀 MindVault Pro – Additional Features

MindVault Pro builds on MindVault and adds the following new features:



### ✍️ Entry Management
- Add, edit, delete notes
- Notes contain:
  - `Title`
  - `Content`
  - `Problem Type` (e.g., silly, concept, calc, skip, other)
  - `Priority` (high, medium, low)
  - `Resolved Status` (resolved or unresolved)
  - Auto `created_at` and `updated_at` timestamps

### 🔔 Smart Notifications
- Triggered only on your **first note**
- Shows helpful messages to guide new users
- Dismissed after one-time use (tracked per user)
- Notification panel with **seen/unseen** toggle

### 🧭 Dashboard Interface
- Light Bootstrap theme
- Navigation bar with:
  - Home
  - Predict Crop (if extended)
  - Farm Management (if extended)
  - Notes
  - Notifications
  - User Dropdown (Your Account, Logout)

### 🎯 Problem Type Tags
- Automatically highlighted using Bootstrap badges:
  - `bg-warning` for silly
  - `bg-danger` for big
  - `bg-info` for concept
  - `bg-primary` for calc
  - `bg-secondary` for skip
  - `bg-dark` for other

### 📊 Priority & Resolved Status
- Visual priority indicators (color-coded)
- Toggle resolved/unresolved status in UI
- Helpful for tracking what still needs attention

### 🔐 Authentication
- Django user system
- Session-based login/logout
- User-specific data isolation

---

## 🛠️ Tech Stack

| Layer       | Tech                    |
|-------------|--------------------------|
| Frontend    | HTML, CSS (Bootstrap), Vanilla JS |
| Backend     | Python 3.x, Django       |
| Database    | MySQL                    |
| Auth        | Django sessions          |
| Hosting     | (Deploy locally or on Heroku / PythonAnywhere) |

---

## Folder Structure

MindVault-Pro/<br>
├── Notes/<br>
│   ├── VIEWS/<br>
│   │   ├── auth/<br>
│   │   ├── notifications/<br>
│   │   ├── notes/<br>
│   │   ├── __init__.py<br>
│   ├── templates/<br>
│   ├── static/<br>
│   ├── models.py<br>
│   └── urls.py<br>
├── manage.py<br>
├── requirements.txt<br>
├── env/<br>
└── README.md<br>


## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/MindVault-Pro.git
cd MindVault-Pro

python -m venv env
# Linux/Mac
source env/bin/activate
# Windows
env\Scripts\activate

pip install -r requirements.txt
