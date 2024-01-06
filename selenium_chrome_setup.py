from selenium import webdriver
from selenium.webdriver.common.by import By


class SeleniumChromeDriver:

    def __init__(self):
        # Configure Chrome options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        # Initialize Chrome WebDriver
        self.driver = webdriver.Chrome(options=chrome_options)

    @staticmethod
    def intro():
        title = "Getting Property Information From Clone Zillow"
        print(title)
        print('-' * len(title))

    @staticmethod
    def outro():
        title = "Search Complete, Closing App."
        print('-' * len(title))
        print(title)

    def get_url(self, url: str):
        return self.driver.get(url)

    def find_class_name(self, class_name: str, single: bool = True):
        if single:
            return self.driver.find_element(By.CLASS_NAME, class_name)
        else:
            return self.driver.find_elements(By.CLASS_NAME, class_name)

    def find_css_selector(self, css_name: str, single: bool = True):
        if single:
            return self.driver.find_element(By.CSS_SELECTOR, css_name)
        else:
            return self.driver.find_elements(By.CSS_SELECTOR, css_name)

    def close(self):
        self.driver.quit()


def main():
    from endpoints import ZILLOW_URL
    from time import sleep
    from pprint import pp
    test_driver = SeleniumChromeDriver()
    test_driver.get_url(ZILLOW_URL)
    sleep(2)
    properties = test_driver.find_class_name('ListItem-c11n-8-84-3-StyledListCardWrapper', single=False)

    for property_elem in properties:
        # Extract the URL from the 'href' attribute of the <a> element
        url_element = property_elem.find_element(By.CSS_SELECTOR, 'a[data-test="property-card-link"]')
        address = url_element.text
        property_url = url_element.get_attribute('href')

        # Extract the Price from the 'data-test' attribute of the <span> element
        price_element = property_elem.find_element(By.CSS_SELECTOR, 'span[data-test="property-card-price"]')
        price = price_element.text

        print(f"Address: {address}")
        print(f'Price: {price}')
        print(f"URL: {property_url}")

    sleep(2)
    test_driver.close()
    exit(0)


if __name__ == '__main__':
    print("TEST:Running Directly.")
    main()
