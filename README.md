# ElecNetSupervisor

ElecNetSupervisor is a Django and project designed for station control rooms to input and manage hourly readings such as MW, KV, etc. The application automates the calculation process and uploads the readings to a specified Google Sheet.

## Features

- Input hourly readings for station control rooms.
- Automated calculation of readings.
- Seamless integration with Google Sheets for data upload.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x
- Django
- Django Rest Framework
- Google Sheets API credentials (Follow [Google Sheets API documentation](https://developers.google.com/sheets/api/guides/authorizing) to set up)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ElecNetSupervisor.git

2. Navigate to the project directory:

    ```bash
   cd elecnetsupervisor
   
3. Install dependencies:

    ```bash
    pip install -r requirements.txt

4. Apply migrations:
        
    ```bash
   python manage.py migrate

5. Create a superuser for the Django admin:
    
    ```bash
   python manage.py createsuperuser

6. Set up Google Sheets API credentials (Follow the instructions in the Google Sheets API documentation).


7. Configure API credentials in settings.py:

    ```bash
   # settings.py

    GOOGLE_SHEET_API_CREDENTIALS = 'path/to/your/credentials.json'
    GOOGLE_SHEET_ID = 'your_google_sheet_id'

## Usage

1. Run the development server:
    
   ```bash
   python manage.py runserver

2. Access the Django admin at http://localhost:8000/admin/ and log in with the superuser credentials.


3. Use the admin interface to manage hourly readings.


4. The application will automatically calculate and upload the readings to the specified Google Sheet.


## Contributing


## License

This project is licensed under the MIT License - see the LICENSE file for details.


Feel free to customize this template based on your specific project details and requirements. Additionally, you may want to include sections like Testing, Deployment, and Troubleshooting based on your project's complexity and needs.










