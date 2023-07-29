from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
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


def fill_input(driver: webdriver.Firefox, data_automation_id, value, element_type="input"):
    xpath = "//" + element_type + "[@data-automation-id='" + data_automation_id + "']"
    element = driver.find_element(By.XPATH, xpath)

    element.send_keys(value)


def select_dropdown(driver: webdriver.Firefox, data_automation_id, value):
    xpath = "//button[@data-automation-id='" + data_automation_id + "']"
    element = driver.find_element(By.XPATH, xpath)

    element.send_keys(value + "\n")


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
    xpath = "//button[@aria-label='" + aria_label + "']"
    element = driver.find_element(By.XPATH, xpath)

    element.click()


def enter_dates(driver: webdriver.Firefox, id, start_date_str, end_date_str):
    xpath = "//div[@data-automation-id='" + id + "']"
    elements = driver.find_elements(By.XPATH, xpath)

    elements[0].click()
    driver.switch_to.active_element.send_keys(start_date_str)
    
    elements[1].click()
    driver.switch_to.active_element.send_keys(end_date_str)


def experience_page(driver: webdriver.Firefox):
    # first work experience
    click_add_button(driver, "Add Work Experience")

    fills = {}
    fills["jobTitle"] = "Teaching Assistant"
    fills["company"] = "Gonzaga University"
    fills["location"] = "Spokane, WA"

    for key in fills.keys():
        fill_input(driver, key, fills[key])

    enter_dates(driver, "dateSectionMonth-display", "082022", "052023")

    description = "- Teaching assistant for Operating Systems, Computer Security, and Internet of Things.\n- Graded programming and written assignments."
    fill_input(driver, "description", description, element_type="textarea")
    
    # second work experience
    click_add_button(driver, "Add Another Work Experience")
    



def main():
    # url = get_url()
    url = "https://blackrock.wd1.myworkdayjobs.com/en-US/BlackRock_Professional/job/Seattle-WA/Associate--Software-Engineer--Applications_R231920/apply/applyManually"

    driver = open_driver()
    driver.get(url)
    
    time.sleep(5)

    info_page(driver)

    wait_for_next_page(driver)

    experience_page(driver)





if __name__ == '__main__':
    main()
