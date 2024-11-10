import threading
import random
import time
import string
import os
import argparse
from seleniumwire import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# Define your ProxyEmpire rotating proxy URL (Optional)
proxy_host = "rotating.proxyempire.io"
proxy_port = "5000"  # Replace with your ProxyEmpire port
proxy_user = "package-10001-country-us"  # Replace with ProxyEmpire username
proxy_pass = "Z69zPkXzsZf58IkP"  # Replace with ProxyEmpire password

# List of sample first and last names for randomization
first_names = ["John", "Jane", "Alex", "Emily", "Chris", "Michael", "Sarah", "David", "Amanda", "James", 
"Jessica", "Robert", "Ashley", "William", "Mary", "Daniel", "Linda", "Joseph", "Elizabeth", 
"Charles", "Susan", "Matthew", "Karen", "Andrew", "Nancy", "Thomas", "Betty", "Mark", "Helen", 
"Joshua", "Dorothy", "Steven", "Patricia", "Paul", "Deborah", "Kevin", "Ruth", "Brian", "Sharon", 
"Steven", "Cynthia", "Brian", "Margaret", "George", "Betty", "Edward", "Carol", "Jack", "Helen", 
"Ryan", "Denise", "Gary", "Grace", "Adam", "Ann", "Aaron", "Megan", "Samuel", "Irene", "Gregory", 
"Emily", "Philip", "Alice", "Ethan", "Rose", "Jack", "Ruby", "Henry", "Lori", "Frank", "Martha", 
"Samuel", "Barbara", "Leo", "Jean", "Nicholas", "Alice", "Oliver", "Anna", "Steven", "Zoe", 
"Peter", "Lucy", "Jake", "Sarah", "Victor", "Chloe", "Adam", "Sophia", "Liam", "Victoria", 
"Benjamin", "Julia", "Thomas", "Ella", "Lucas", "Grace", "Ryan", "Maria", "Daniel", "Carla", 
"Paul", "Lisa", "Timothy", "Samantha", "Jack", "Sophie", "Brian", "Leah", "Christian", "Lily", 
"Matthew", "Chloe", "Jacob", "Charlotte", "Eli", "Ivy", "Elijah", "Lena", "Marcus", "Rachel"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Martinez", "Hernandez",
"Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee",
"Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Roberts", "Walker",
"Young", "Allen", "King", "Scott", "Green", "Adams", "Baker", "Gonzales", "Nelson", "Carter",
"Mitchell", "Perez", "Robinson", "Hughes", "Green", "Campbell", "Bailey", "Murphy", "Rivera", "Cook",
"Rogers", "Morgan", "Cooper", "Reed", "Bailey", "Bell", "Ward", "Flores", "Harris", "Graham",
"Diaz", "Wright", "Cameron", "James", "Morris", "Graham", "Garrett", "Hughes", "Jennings", "Burns",
"Price", "Hughes", "Collins", "Morris", "Rodriguez", "Foster", "Bryant", "Alexander", "Hudson", "Russell",
"Carson", "Simmons", "Bryant", "Kim", "Ward", "Douglas", "Jenkins", "Reynolds", "Hamilton", "Gibson",
"Webb", "Fox", "Cross", "Simmons", "Freeman", "Chapman", "Stewart", "Chavez", "Woods", "Hawkins",
"Grant", "Russell", "Fox", "Chavez", "Sanders", "Murray", "Ford", "Jenkins", "Stephens", "Mason",
"Howard", "Stevens", "Knight", "Wells", "Mendez", "Richards", "Sullivan", "Butler", "Hunter", "Hicks"]
domain_names = ["coursesman", 
"eliteemailtech", 
"emailexperthub", 
"emailnetworkpro", 
"emailorbit", 
"emailprox", 
"emailsyncpro", 
"emailzeal", 
"foxsoftmail", 
"fprai", 
"itsdollar", 
"itsmefox", 
"mailcrafted", 
"mohamedfekri", 
"mohamedfox", 
"newcareertime", 
"remoteworkmail", 
"secondad", 
"wolfpoints",
"yahoo",
"Hotmail"]
# Function to set up WebDriver with ProxyEmpire rotating proxy
def setup_driver_with_proxy():
    # Set Chrome options for handling SSL/TLS errors
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Optional: run headless if no UI is needed
    chrome_options.add_argument('--ignore-certificate-errors')  # Ignore SSL certificate errors
    chrome_options.add_argument('--disable-web-security')  # Disable web security features (optional)
    chrome_options.add_argument('--disable-gpu')  # Optional: disable GPU for headless mode
    
    # Initialize the WebDriver with the SOCKS5 proxy and options
    driver = webdriver.Chrome(
        options=chrome_options, 
        seleniumwire_options={
            'proxy': {
                # SOCKS5 Proxy Configuration for HTTP and HTTPS
                'http': 'socks5://package-10001-country-us:Z69zPkXzsZf58IkP@rotating.proxyempire.io:5000',
                'https': 'socks5://package-10001-country-us:Z69zPkXzsZf58IkP@rotating.proxyempire.io:5000',
            },
            'request_storage_base_dir': 'your_storage_dir',
            'timeout': 30  # Timeout in seconds
        }
    )
    return driver

# Function to generate a random password
def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Generate random first name, last name, email, and phone number
def generate_random_contact_info():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    email = f"{first_name.lower()}{random.randint(1000, 99999999999999)}@{random.choice(domain_names)}.com"
    phone_number = f"{random.randint(100, 999)}{random.randint(100, 999)}{random.randint(1000, 9999)}"
    password = generate_random_password()  # Generate a random password
    return first_name, last_name, email, phone_number, password

# Function to save data to a text file in a formatted way
def save_to_text_file(data):
    with open('account_info.txt', 'a') as file:
        file.write(
            f"First Name: {data['first_name']}\n"
            f"Last Name: {data['last_name']}\n"
            f"Email: {data['email']}\n"
            f"Phone Number: {data['phone_number']}\n"
            f"Password: {data['password']}\n"
            "----------------------------------------\n"
        )

# Automate account creation with form filling after navigating to the registration page
def create_account():
    driver = setup_driver_with_proxy()
    wait = WebDriverWait(driver, 10)  # Increased wait time

    try:
        # Step 1: Go to the login page
        driver.get("https://my.stubhub.com/secure/login")
        print("Navigated to the login page.")

        # Step 2: Wait for and click on the link to navigate to the register page
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Create account')]")))
        submit_button.click()

        # Step 3: Wait for the registration form elements to load
        first_name_input = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
        last_name_input = wait.until(EC.presence_of_element_located((By.NAME, "lastName")))
        email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        country_code_input = driver.find_element(By.ID, "react-select-2-input")
        country_code_input.send_keys("US")  # Type the country code
        phone_input = wait.until(EC.presence_of_element_located((By.NAME, "phoneNumber.phoneNumber")))
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))

        # Generate randomized contact info
        first_name, last_name, email, phone_number, password = generate_random_contact_info()

        # Fill in the form fields with random data
        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)
        email_input.send_keys(email)
        phone_input.send_keys(phone_number)
        password_input.send_keys(password)
        # The email address you entered is invalid
        # Profile
        # Click the submit button
        time.sleep(5)
        try:
            submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Create account')]")))
            driver.execute_script("arguments[0].click();", submit_button)
            print("Attempted to click the 'Create account' button with JavaScript.")

            # If click fails, simulate pressing Enter
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ENTER)
            print("Sent Enter key to the body.")
        except Exception as e:
            print(f"Failed to click the 'Create account' button: {e}")


        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone_number': phone_number,
            'password': password,
        }
        save_to_text_file(data)
        # Optional: Random delay
        # time.sleep(random.randint(1, 5))
        time.sleep(50)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the browser session
        driver.quit()
        print("Browser closed.")

# Run multiple threads for concurrent account creation
def run_multithreaded_tasks(total_accounts=10, thread_count=5):
    accounts_per_thread = total_accounts // thread_count
    remaining_accounts = total_accounts % thread_count

    threads = []
    for i in range(thread_count):
        accounts_in_thread = accounts_per_thread + (1 if i < remaining_accounts else 0)
        thread = threading.Thread(target=create_account_batch, args=(accounts_in_thread,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Function for each thread to create a batch of accounts
def create_account_batch(num_accounts):
    for i in range(num_accounts):
        print(f"Creating account {i + 1} in this thread.")
        create_account()
        time.sleep(random.uniform(2, 5))  # Random delay to avoid detection

# Main execution
if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Automate account creation using multiple browsers in threads.")
    parser.add_argument('--total_accounts', type=int, required=True, help='Total number of accounts to create')
    parser.add_argument('--thread_count', type=int, required=True, help='Total number of accounts to create')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Run the multi-threaded account creation with browsers
    run_multithreaded_tasks(total_accounts=args.total_accounts,thread_count=args.thread_count)
