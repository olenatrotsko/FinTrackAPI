# FinTrackAPI

A Django REST Framework (DRF) application for tracking financial transactions, including income and expenses, with support for categories and reporting.

## Features

- User authentication and authorization
- CRUD operations for financial transactions
- Categorization of transactions
- Detailed transaction reporting

## Prerequisites

- Python 3.12
- PostgreSQL (or any other supported database)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/trolchiha/FinTrackAPI.git
    cd FinTrackAPI
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser (admin account):

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Configuration

Update the environment variables in the `.env` file or settings in `settings.py` as needed, especially for database settings.

## Usage

- Access the API at `http://localhost:8000`

## Testing

Run the tests using:

```bash
pytest
