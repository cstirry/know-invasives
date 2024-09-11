# Invasive Plant Search App

Django-based app allows users to search for plants and check if they are invasive. 
Created to explore building user-friendly interface for personal use to search a personal compiled dataset to prevent 
accidentally purchasing and planting invasive plants. 

This repo only contains a basic data sample and html template for example purposes.

## Getting Started

To run the app locally, follow these steps:

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/invasive-plant-search.git
cd invasive-plant-search
```

### 2. Set up virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Set up local database (default SQLite):
```bash
python manage.py migrate
```

### 5. Add your own dataset:
Only a data sample is included. If interested in invasive plant data, consider a source like invasiveplantatlas.org.
Update `\data` and `\commands\load_plants.py`.


### 6. Run the server:
```bash
python manage.py runserver  #http://127.0.0.1:8000/
```


