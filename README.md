# Maternal Health Risk Predictor

This is a simple web application to predict maternal health risk based on various health parameters. The application uses Flask for the backend and Tailwind CSS for the frontend.

## Features

- Input health parameters such as age, blood pressure (systolic, diastolic), blood sugar level, body temperature, and heart rate.
- Validate input data to ensure they are within acceptable ranges.
- Display health risk predictions with color-coded risk levels (high, mid, low).

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/irfandwisamudra/maternal-health-risk.git
   cd maternal-health-risk
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Run the Flask application:

   ```bash
   flask --app app run
   ```

2. Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Usage

1. Enter the required health parameters into the form.
2. Submit the form to get the risk prediction.
3. The risk prediction will be displayed with a color-coded background:
   - **High Risk**: Red background
   - **Mid Risk**: Yellow background
   - **Low Risk**: Green background

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them with descriptive messages.
   ```bash
   git commit -m "Description of changes"
   ```
4. Push your changes to your fork.
   ```bash
   git push origin feature-name
   ```
5. Create a pull request to the main repository.

## Acknowledgements

This project uses the following libraries and frameworks:

- [Flask](https://flask.palletsprojects.com/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Flowbite](https://flowbite.com/)

## Contact

For any inquiries or issues, please open an issue on the repository or contact the repository owner.
