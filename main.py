from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def get_url():
    url = input("url: ")

    return url


def open_driver():
    # install geckodriver
    # path to geckodriver
    driver_path = R"/usr/local/bin/geckodriver"    

    # path to firefox executable
    firefox_path = R"/bin/firefox"    

    # create options
    options = Options()
    
    # set binary location
    options.binary_location = firefox_path    

    # create a service object and set executable_path to driver_path
    service = Service(executable_path=driver_path)

    # create a driver
    driver = webdriver.Firefox(options=options, service=service)

    return driver


def wait_for_login():
    input("Login and press Enter:")


def fill_input(driver: webdriver.Firefox, data_automation_id, value, element_type="input"):
    try:
        xpath = "//" + element_type + "[@data-automation-id='" + data_automation_id + "']"
        elements = driver.find_elements(By.XPATH, xpath)

        element = elements[-1]
        element.send_keys(Keys.CONTROL + "A")
        element.send_keys(Keys.BACK_SPACE)
        element.send_keys(value)
    except:
        print("Failed to input " + data_automation_id + " as: " + value)


def select_dropdown(driver: webdriver.Firefox, data_automation_id, value):
    xpath = "//button[@data-automation-id='" + data_automation_id + "']"
    element = driver.find_element(By.XPATH, xpath)

    element.send_keys(value + "\n")


def fill_multiselect(driver: webdriver.Firefox, data_automation_id, value):
    xpath = "//div[@data-automation-id='" + data_automation_id + "']"
    elements = driver.find_elements(By.XPATH, xpath)

    elements[-1].click()
    driver.switch_to.active_element.send_keys(value + "\n")


def fill_skills(driver: webdriver.Firefox):
    skills = ["Python", "Java", "C++", "C", "SQL", "Git", "Linux", "Docker", "Jupyter", "GitHub Actions", "Postgres",
              "AWS Lambda", "AWS S3", "Tensorflow", "PyTorch", "Pandas", "NumPy", "Scikit-Learn", "Matplotlib",
              "JS", "AWS EventBridge", "Selenium", "MATLAB"]
    
    for skill in skills:
        skills_section = driver.find_element(By.XPATH, "//div[@data-automation-id='skillsSection']")
        driver.execute_script("window.scrollBy(0, -5000);")
        time.sleep(.1)
        driver.execute_script("arguments[0].scrollIntoView();", skills_section)
        time.sleep(.1)
        driver.execute_script("window.scrollBy(0,-20);")
        time.sleep(.1)
        
        element = driver.find_element(By.XPATH, "//div[@data-automation-id-prompt='skillsPrompt']")
        for _ in range(3):
            element = element.find_element(By.XPATH, "*")

        element.click()
        element.send_keys(skill)
        element.send_keys(Keys.RETURN)

        # time.sleep(1)
        # element.send_keys(Keys.RETURN)
        # time.sleep(1)
        # element.send_keys(Keys.TAB)

        time.sleep(.75)
        try:
            element_2 = driver.find_element(By.XPATH, "//div[@data-automation-label='" + skill + "']")
            element_2.click()
        except:
            print(f"Failed to add {skill}")
        time.sleep(.25)


def wait_for_next_page(driver: webdriver.Firefox):
    xpath = "//div[@data-automation-id='progressBarActiveStep']"
    element = driver.find_element(By.XPATH, xpath)

    while element.get_attribute("data-automation-id") == "progressBarActiveStep":
        time.sleep(1)

    time.sleep(.5)


def info_page(driver: webdriver.Firefox):
    fills = {}
    fills["legalNameSection_firstName"] = "Zach"
    fills["legalNameSection_lastName"] = "Sahlin"
    fills["addressSection_addressLine1"] = "5034 46th Ave NE"
    fills["addressSection_city"] = "Seattle"
    fills["addressSection_postalCode"] = "98105"
    fills["email"] = "zach@sahlins.net"
    fills["phone-number"] = "2066077655"

    for key in fills.keys():
        fill_input(driver, key, fills[key])
    
    dropdowns = {}
    dropdowns["addressSection_countryRegion"] = "Washington"
    dropdowns["phone-device-type"] = "Mobile"

    for key in dropdowns.keys():
        select_dropdown(driver, key, dropdowns[key])


def click_add_button(driver: webdriver.Firefox, aria_label):
    try:
        xpath = "//button[@aria-label='" + aria_label + "']"    
        element = driver.find_element(By.XPATH, xpath)
    except:
        print(f"Failed to find add button {aria_label}")
        return

    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.execute_script("window.scrollBy(0, -300);")

    element.click()


def enter_dates(driver: webdriver.Firefox, id, start_date_str, end_date_str):
    xpath = "//div[@data-automation-id='" + id + "']"
    elements = driver.find_elements(By.XPATH, xpath)

    elements[-2].click()
    driver.switch_to.active_element.send_keys(start_date_str)
    
    elements[-1].click()
    driver.switch_to.active_element.send_keys(end_date_str)


def work_experience_1(driver: webdriver.Firefox):
    # first work experience
    try:
        click_add_button(driver, "Add Work Experience")
    except:
        print("Failed to add work experience")

    fills = {}
    fills["jobTitle"] = "Teaching Assistant"
    fills["company"] = "Gonzaga University"
    fills["location"] = "Spokane, WA"

    for key in fills.keys():
        fill_input(driver, key, fills[key])

    enter_dates(driver, "dateSectionMonth-display", "082022", "052023")

    description = "- Teaching assistant for Operating Systems, Computer Security, and Internet of Things.\n- Graded programming and written assignments."
    fill_input(driver, "description", description, element_type="textarea")

    
def work_experience_2(driver: webdriver.Firefox):
    # second work experience
    try:
        click_add_button(driver, "Add Another Work Experience")
    except:
        print("Failed to add work experience")

    fills = {}
    fills["jobTitle"] = "Online Private Instructor"
    fills["company"] = "iD Tech"
    fills["location"] = "Remote"

    for key in fills.keys():
        fill_input(driver, key, fills[key])

    enter_dates(driver, "dateSectionMonth-display", "062021", "082022")

    description = "- Tutored in 8 different computer science topics, including C++, Java, and Python.\n- Completed over 200 private lessons.\n- Formed relationships with long-term clients, and developed further skills in communication and coding.\n- Collaborated with other instructors to improve teaching methods."
    fill_input(driver, "description", description, element_type="textarea")


def education(driver: webdriver.Firefox):
    # education
    time.sleep(.25)
    click_add_button(driver, "Add Education")

    fills = {}
    fills["school"] = "Gonzaga University"
    fills["gpa"] = "3.8"

    for key in fills.keys():
        fill_input(driver, key, fills[key])

    dropdowns = {}
    dropdowns["degree"] = "Undergraduate Degree"

    for key in dropdowns.keys():
        select_dropdown(driver, key, dropdowns[key])

    enter_dates(driver, "dateSectionYear-display", "2019", "2023")



def experience_page(driver: webdriver.Firefox):
    work_experience_1(driver)
    work_experience_2(driver)   
    education(driver)

    fill_skills(driver)


    # time.sleep(.25)
    # element.send_keys(Keys.RETURN)
    # time.sleep(.25)
    # element.click()
    # element.send_keys("Java")



def main():
    # url = get_url()
    # url = "https://blackrock.wd1.myworkdayjobs.com/en-US/BlackRock_Professional/job/Seattle-WA/Associate--Software-Engineer--Applications_R231920/apply/applyManually"
    # url = "https://disney.wd5.myworkdayjobs.com/en-US/disneycareer/job/Seattle-WA-USA/Associate-Software-Engineer--Seattle_10058251/apply/applyManually"
    url = "https://vmware.wd1.myworkdayjobs.com/en-US/VMware/job/USA-California-Palo-Alto/Software-Engineer_R2304988/apply/applyManually"

    driver = open_driver()
    driver.get(url)

    wait_for_login()
    
    time.sleep(5)

    info_page(driver)

    wait_for_next_page(driver)

    experience_page(driver)





if __name__ == '__main__':
    main()
