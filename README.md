# minifyURL

## Overview

The **Django URL Shortener App** is a simple web application that allows users to shorten long URLs into shorter, more manageable links. Additionally, it provides analytics to track the traffic on these shortened URLs.

## Features

1. **URL Shortening**: Users can input a long URL, and the app will generate a short, unique link for them.

2. **Analytics Dashboard**: Registered users can view detailed analytics for their shortened URLs.

## Installation

1. Clone this repository:
   ```
   https://github.com/rajat-jkg/minifyURL
   ```

2. Navigate to the project directory:
   ```
   cd minifyURL
   ```

3. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install djando:
   ```
   pip install -r django
   ```

6. Apply migrations:
   ```
   python manage.py migrate
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

8. Access the app at `http://localhost:8000/`.

## Usage

1. Register an account or log in.

2. Shorten a URL by providing the long URL and clicking "Shorten."

3. View your shortened URLs and their analytics in the dashboard.

## Contributing

Contributions are welcome! If you find any issues or have suggestions, feel free to create a pull request.
