This project contains automated tests for the Swag Labs website using Selenium WebDriver and Pytest.

1️⃣ Install Dependencies
Ensure you have Python 3.x installed, then install the required packages:

bash
pip install -r requirements.txt

2️⃣ Set Up WebDriver
Download and place the appropriate WebDriver (e.g., ChromeDriver for Chrome) in your system path.

3️⃣ Run Tests
Execute tests using Pytest:
cd test-script/tests
pytest -v

🔹 Project Structure
bash
Copy
Edit
/tests            # Test cases  
/pages           # Page Object Model (POM) classes  
/config  # Pytest fixtures & setup  
/drivers #required drivers
/requirements.txt # Dependencies  
