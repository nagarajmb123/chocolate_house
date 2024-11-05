
 Chocolate House Application

This is a simple Python-based application for managing a fictional chocolate house's offerings, ingredient inventory, and customer suggestions using Flask and SQLite. The application provides endpoints for managing seasonal flavors, ingredient inventory, and customer feedback regarding flavor suggestions and allergy concerns.


Table of Contents

- [Project Setup](#project-setup)
- [Database Structure](#database-structure)
- [Endpoints](#endpoints)
  - [Seasonal Flavors](#seasonal-flavors)
  - [Ingredients](#ingredients)
  - [Customer Suggestions](#customer-suggestions)
- [Docker](#docker)
- [Testing Instructions](#testing-instructions)
- [Usage](#usage)

---

Project Setup

Prerequisites
- **Python 3.x**
- **SQLite**
- **Git** (for version control)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/chocolate_house.git
   cd chocolate_house
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up the Database**: Run the following command to create the database and tables:
   ```bash
   python models/db_setup.py
   ```

4. **Start the Flask Application**:
   ```bash
   python app.py
   ```
   The server should now be running on `http://127.0.0.1:5000`.

---

## Database Structure

The SQLite database `chocolate_house.db` contains three tables:

- **SeasonalFlavors**: Stores information on seasonal chocolate flavors.
- **Ingredients**: Manages ingredient inventory.
- **CustomerSuggestions**: Logs customer flavor suggestions and allergy concerns.

Each table has its own CRUD functionality defined in the `models` directory.

---

## Endpoints

The application provides REST API endpoints for each table. Below are the details on how to interact with each resource.

### Seasonal Flavors
- **GET /flavors** - Retrieve all seasonal flavors.
- **POST /flavors** - Add a new seasonal flavor.

   **Example POST Request**:
   ```json
   POST /flavors
   {
       "flavor_name": "Mint Chocolate",
       "description": "Refreshing blend of mint and chocolate."
   }
   ```

### Ingredients
- **GET /ingredients** - Retrieve all ingredients.
- **POST /ingredients** - Add a new ingredient to the inventory.

   **Example POST Request**:
   ```json
   POST /ingredients
   {
       "ingredientName": "Cocoa Powder",
       "Quantity": 200
   }
   ```

### Customer Suggestions
- **GET /suggestions** - Retrieve all customer suggestions.
- **POST /suggestions** - Add a new customer suggestion.

   **Example POST Request**:
   ```json
   POST /suggestions
   {
       "customerName": "John Doe",
       "suggestion": "Try a hazelnut flavor!",
       "allergyConcern": "None"
   }
   ```

---

## Docker

To build and run the application using Docker:

1. **Build the Docker Image**:
   ```bash
   docker build -t chocolate_house_app .
   ```

2. **Run the Docker Container**:
   ```bash
   docker run -p 5000:5000 chocolate_house_app
   ```

The application will now be accessible at `http://127.0.0.1:5000`.

---

## Testing Instructions

1. **Check Database Setup**: Ensure that `chocolate_house.db` has been created in the `db` directory with the correct tables by running `python models/db_setup.py`.

2. **Run the Application**: Start the server with `python app.py` or via Docker as described above.

3. **API Testing**:
   - Use **Postman** or **curl** to test the endpoints.
   - Verify that you can successfully add and retrieve data for each of the three resources: seasonal flavors, ingredients, and customer suggestions.

4. **Example Testing with Postman**:
   - Use the **POST** requests outlined above to add entries.
   - Use **GET** requests to verify that data is correctly stored and retrieved.

---

This README provides setup, usage, and testing instructions to help users understand and operate the Chocolate House application.