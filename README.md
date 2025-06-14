# Superheroes Flask API

This is builted with Flask for tracking superheroes and their powers. It's part of a coding challenge assessment. The API manages heroes, their powers, and the strength of each hero's abilities.

---

## Features

- View all heroes and their super names
- Retrieve a hero and their powers
- View all powers and individual power details
- Update power descriptions
- Assign powers to heroes with strength levels
- Validations to ensure data integrity
- Seeded sample data for testing
- Postman Collection available for easy testing

---

## Project Structure
    
        project-root/
        │
        ├── app.py
        ├── models.py
        ├── config.py
        ├── seed.py
        ├── migrations/
        │
        ├── README.md
        └── requirements.txt
    

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/superheroes-api.git
cd superheroes-api 
```

### 2. Create & Activate a virtual Enviroment
```bash
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. install Dependencies
```bash 
pip install -r requirements.txt
```

### 4. Set up the database
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 5. seed the Database
```bash 
python seed.py
```

### 6. Run the server
```bash 
flask run
```

## Postman Collection 
Test the Api with postman:
- Open Postman 
- Click on import > upload file 
- Select the ```challenge-2-superheroes.postman_collection.json``` file
- Start testing the routes

### API Endpoints Summary

| Method | Route          | Description                        |
| ------ | -------------- | ---------------------------------- |
| GET    | `/heroes`      | List all heroes                    |
| GET    | `/heroes/<id>` | Get a specific hero + their powers |
| GET    | `/powers`      | List all powers                    |
| GET    | `/powers/<id>` | Get a specific power               |
| PATCH  | `/powers/<id>` | Update a power's description       |
| POST   | `/hero_powers` | Assign a power to a hero           |


## Validations
* ```HeroPower.strength``` must be one of 'Stromg', 'Weak', 'Average'
* ```Power.description``` must exist and be at least 20 characters.

## Author
Derick Sheldrick
