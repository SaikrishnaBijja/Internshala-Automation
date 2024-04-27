from selenium import webdriver 
from selenium.webdriver.common.by import By
import selenium
import time, os
from user import get_data, read_data


def login(email, password, driver):
    to_login_xp='//*[@id="header"]/div/nav/div[3]/button[2]'
    login_email_xp='//*[@id="modal_email"]'
    login_password_xp='//*[@id="modal_password"]'
    login_btn_xp='/html/body/div[1]/div[17]/div/div/div[2]/form/div[4]/button'
    driver.get("https://internshala.com/")
    driver.find_element(By.XPATH, to_login_xp).click()
    time.sleep(2)
    driver.find_element(By.XPATH, login_email_xp).send_keys(email)
    driver.find_element(By.XPATH, login_password_xp).send_keys(password)
    time.sleep(1)
    driver.find_element(By.XPATH, login_btn_xp).click()

def apply(intrests, driver):
    applied=True
    for x in range(1,41):  
        url="https://internshala.com/internships/backend-development,front-end-development,java,javascript-development,node-js-development,python-django-internship/stipend-10000/page-1/"
        if applied == True:
            driver.get(url)
        time.sleep(3)

        try:
            driver.find_element(By.XPATH, '//*[@id="no_thanks"]').click()
        except selenium.common.exceptions.NoSuchElementException:
            pass

        internships=driver.find_elements(By.CLASS_NAME, 'individual_internship')
        try:
            company=internships[x].find_element(By.CLASS_NAME, 'company')
            title = company.find_element(By.TAG_NAME,"h3").get_attribute("innerHTML").lower()
        except selenium.common.exceptions.NoSuchElementException:
            pass
        else:
            print(title)

            to_apply=False
            time.sleep(1)

            for intrest in intrests:
                if intrest in title:
                    to_apply=True
                    break

                    
            if to_apply:
                app=internships[x].find_element(By.CLASS_NAME, 'button_container_card')
                apply_btn=app.find_element(By.CLASS_NAME, 'cta_container').find_element(By.CLASS_NAME, 'btn-primary')
                apply_btn.click()

                time.sleep(4)

                try:
                    continue_btn=driver.find_element(By.ID, 'continue_button')
                    continue_btn.click()
                except selenium.common.exceptions.NoSuchElementException:
                    time.sleep(3)
                    continue_btn=driver.find_element(By.ID, 'continue_button')
                    continue_btn.click()

                try:
                    driver.find_element(By.XPATH, '//*[@id="assessment_questions"]/div[1]/div[2]/div[1]/a').click()
                except selenium.common.exceptions.NoSuchElementException:
                    pass

                try:
                    driver.find_element(By.XPATH, '//*[@id="assessment_questions"]/h4[2]')
                    while True:
                        print("Please answer the assesment questions ")
                        submitted=input("Did you submitted?(y/n)")
                        if submitted=="Y":
                            break
                except selenium.common.exceptions.NoSuchElementException:
                    submit_btn=driver.find_element(By.XPATH, '//*[@id="submit"]')
                    submit_btn.click()
                    print("Submitted")
                    time.sleep(2)
                applied=True
            else:
                applied=False
            
def main():
    
    print("Welcome to Internshala Automation")

    if not os.path.isfile("data.txt"):
        read_data()

    email, password, intrests=get_data()
    print("Starting")
    driver = webdriver.Firefox()
    login(email, password, driver)
    time.sleep(2)
    apply(intrests, driver)

if __name__ == "__main__":
    main()
