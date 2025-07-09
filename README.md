# 🧠MindVault Pro

**MindVault Pro** is an extended, more powerful version of MindVault — adding notifications, better UX, cleaner UI, and dashboard functionality.

---


## 🚀 MindVault Pro – Additional Features

MindVault Pro builds on MindVault and adds the following new features:

- 🔔 **Notification System**
  - Custom user notifications (`Notifications` model)
  - Notifications are shown only once after first activity
  - Seen/unseen filter and notification page

- 📬 **Dashboard & Dropdown UI**
  - Search bar, dropdowns, and navbar
  - Account menu with options:
    - Your Account
    - Notifications
    - Your Notes

- 📅 **Smart Notification Trigger**
  - Notification appears *only once* after user's first note is saved
  - Avoids repeated alerts on every page load

- 🎨 **Enhanced UI**
  - Color-coded badges for different note types
  - Light-colored, professional Bootstrap UI

- 🧠 **Future-Proofed Structure**
  - Modular `VIEWS/` folder with `auth/`, `notes/`, `notifications/` subfolders
  - Better maintainability and scalability

---

## ⚙️ Tech Stack

- **Frontend**: HTML, CSS (Bootstrap), minimal JavaScript
- **Backend**: Django (Python 3.x)
- **Database**: MySQL
- **Auth**: Django Sessions
- **Notifications**: Custom model + logic
- **Virtual Environment**: Python venv

---

## Folder Structure

MindVault-Pro/
├── Notes/
│   ├── VIEWS/
│   │   ├── auth/
│   │   ├── notifications/
│   │   ├── notes/
│   │   ├── __init__.py
│   ├── templates/
│   ├── static/
│   ├── models.py
│   └── urls.py
├── manage.py
├── requirements.txt
├── env/
└── README.md


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
