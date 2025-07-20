# 🛒 Django Product Catalog

A simple full-stack web application for browsing grocery products. Users can search by name or description and filter by category or tags.

---

## ⚙️ Features

- Product list with name, price, description
- Search by keyword
- Filter by category and tag
- Admin panel to manage products, categories, and tags

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/myproject.git
cd myproject

```


### 2. Create a Virtual Environment

```bash
python -m venv env

```

Windows PowerShell

```bash
.\env\Scripts\Activate.ps1

```

macOS / Linux

```bash
source env/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

If you don’t have a requirements.txt yet, create one with:

```bash
pip freeze > requirements.txt

```

### 4. Set Up the Database

```bash
python manage.py makemigrations
python manage.py migrate

```

### 5. Create Superuser for Admin Access

```bash
python manage.py createsuperuser

```

### 6. Run the Development Server

```bash
python manage.py runserver

```

Visit http://127.0.0.1:8000/products/ to view the product list.

Visit http://127.0.0.1:8000/admin/ to log in to the admin interface.


##  AI Usage & Attribution

Some portions of the frontend template (product_list.html) were initially generated using an AI tool (ChatGPT) to scaffold basic HTML and Django template logic for filtering and rendering.

Manual modifications were made on:

- Add logic for category and tag selection

- Integrate Django template variables

- Ensure readability and correct functionality

All backend logic (models, views, URLs, migrations) was written and understood by the developer.

### Notes: 

- Frontend is using Django templates.