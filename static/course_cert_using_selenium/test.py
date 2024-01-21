from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import logging

options = webdriver.ChromeOptions()

# Download the latest NopeCHA crx extension file.
with open('ext.crx', 'wb') as f:
    f.write(requests.get('https://nopecha.com/f/ext.crx').content)
options.add_extension("/home/amirjon/Desktop/course_cert_using_selenium/NopeCHA-CAPTCHA-Solver.crx")
driver = webdriver.Chrome(options=options)

driver.maximize_window()
def sign_in(driver, fullname, email, password):
    driver.get("https://www.coursera.org/projects/youtube-small-business-marketing?action=enroll&authMode=signup")

    # Use WebDriverWait to wait for the name input field to be present
    login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "name"))
    )
    login.send_keys(fullname)

    # Find and fill the email input field
    email_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'email'))
    )
    email_name.send_keys(email)

    # Find and fill the password input field
    password_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'password'))
    )
    password_name.send_keys(password)

    # Find and click the login button
    login_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div/div/section/section/div[1]/form/button'))
    )
    login_btn.click()

    # Wait for the page to load after clicking the login button
    WebDriverWait(driver, 60).until(
        EC.url_to_be('https://www.coursera.org/projects/youtube-small-business-marketing?action=enroll')
    )

    print("Please wait for 10 seconds for Turing")
def enroll(driver,name,email,password):
    logging.info('<------------------Dastur ishga Tushdi------------------>')
    sign_in(driver, name, email,password)

    # Replace with your actual email and password
    driver.get('https://www.coursera.org/projects/youtube-small-business-marketing')
    time.sleep(5)

    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "c-modal-overlay"))
    )

    enroll_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "cds-button-primary"))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", enroll_button)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", enroll_button)
    time.sleep(5)

    # Check if the "primary.cozy.continue-button" is present and clickable
    try:
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "primary.cozy.continue-button"))
        )
        time.sleep(1)
        continue_button.click()
    except:
        pass


def resume_assignment(driver):
    try:
        driver.get('https://www.coursera.org/learn/youtube-small-business-marketing/exam/fEJPQ/graded-quiz-test-your-project-understanding/attempt')
        time.sleep(4)
        resume_btn = driver.find_element(By.CLASS_NAME,"cds-105.cds-button-disableElevation.cds-button-primary.css-k93wf6")

        # Scroll into view before clicking
        driver.execute_script("arguments[0].scrollIntoView(true);", resume_btn)
        time.sleep(1)

        # Click the button using JavaScript
        driver.execute_script("arguments[0].click();", resume_btn)
        time.sleep(3)

        close_btn = driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div/div[2]/div[3]/div/button')
        close_btn.click()
        time.sleep(3)
        print('passet')

    except:
        resume_btn = driver.find_element(By.CLASS_NAME,  "cds-105.cds-button-disableElevation.cds-button-primary.css-k93wf6")

        # Scroll into view before clicking
        driver.execute_script("arguments[0].scrollIntoView(true);", resume_btn)
        time.sleep(1)

        # Click the button using JavaScript
        driver.execute_script("arguments[0].click();", resume_btn)
        time.sleep(3)

        close_btn = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div/div[1]/button')
        close_btn.click()
        time.sleep(3)
        print('failed')

def test_assignment(driver):
    time.sleep(3)

    try:
        # Test Question 1
        test_one = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Yes, there is!')]"))
        )
        test_one.click()
        time.sleep(0.5)

        # Test Question 2
        test_two = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'False')]"))
        )
        test_two.click()
        time.sleep(0.5)

        # Test Question 3
        test_three = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'There is no limit to the amount of videos you can ')]"))
        )
        test_three.click()
        time.sleep(0.5)

        # Test Question 4
        test_four = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Yes, they can.')]"))
        )
        test_four.click()
        time.sleep(0.5)

        # Agree to terms
        agree = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "cds-checkboxAndRadio-label"))
        )
        agree.click()

        time.sleep(2)

        # Input legal name
        inputing = driver.find_element(By.XPATH, "//input[@placeholder='Enter your legal name']")
        inputing.send_keys('salom')


        # Submit the test
        try:
            submit = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Submit']"))
            )
            submit.click()
        except:
            submit = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div[2]/button[1]"))
            )
            submit.click()

    except Exception as e:
        print(f"Error during test_assignment: {e}")

def name_verification():
    time.sleep(2)
    driver.get('https://www.coursera.org/user-verification')

    time.sleep(3)
    try:
        time.sleep(2)
        # Firsname
        first_name = driver.find_element(By.XPATH,"html/body/div[2]/div/div/div/div[1]/div[1]/div/div/input")
        first_name.send_keys('Karimov')

        # Lastname

        time.sleep(3)
        last_name = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div[3]/div/div/input')
        last_name.send_keys("zhhhhh")
        time.sleep(3)

        checkbox = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div/div/div/label/div/span")
        time.sleep(1)
        checkbox.click()
        time.sleep(3)
        try:
            submit = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[3]/button")
            time.sleep(1)
            submit.click()
            time.sleep(3)
        except:
            versub = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/div/div[2]/button")))
            versub.click()
            print('versub error')


    except:
        print('Name verificationda error bor')
def download(driver):
    driver.get('https://www.coursera.org/learn/youtube-small-business-marketing/home/week/1')
    time.sleep(5)
    href = driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div/div/div/div/div[2]/div[3]/div/div[1]/div[2]/div[2]/a')
    hreff = href.get_attribute('href')
    print("href",hreff)
    return hreff
def get_certificate(name,email,password):
        enroll(driver,name,email,password)
        print("enroll passed")
        time.sleep(6)
        resume_assignment(driver)
        print("resume_assigment passed")

        time.sleep(6)
        test_assignment(driver)
        print("test passed")

        time.sleep(6)
        name_verification()
        print("name verification passed")
        time.sleep(30)
        link = download(driver)
        time.sleep(3)
        driver.get(link)
        print('sertifikat link:',link)
        print('passed download')

def cleanup():
    # Close the browser
    driver.save_screenshot('rasmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm.png')
    time.sleep(10)
    driver.quit()

if __name__ == "__main__":
    try:
        # Replace these values with the actual name, email, and password
        name = "kljadshfkladsjfhdkas"
        email = "alskjdflkdshflaksjhfdlkj@email.com"
        password = "aslkjfhladskjhfkajsdhflkasjdhfkajsdhfskjdhf"

        get_certificate(name, email, password)

    finally:
        cleanup()