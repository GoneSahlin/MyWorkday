from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


def get_url():
    url = input("url: ")

    return url


def open_webdriver(url, headless=False):
    options = Options()
    if headless:
        options.add_argument('-headless')

    driver_path = R"/usr/local/bin/geckodriver"
    firefox_path = R"/bin/firefox"
    options.binary_location = firefox_path
    service = Service(executable_path=driver_path)

    driver = webdriver.Firefox(options=options, service=service)
    driver.get(url)

    return driver


def main():
    url = get_url()

    driver = open_webdriver(url)


if __name__ == '__main__':
    main()
