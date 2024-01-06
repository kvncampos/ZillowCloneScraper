from selenium.webdriver.common.by import By
from selenium_chrome_setup import SeleniumChromeDriver
from endpoints import ZILLOW_URL, LISTING_SELECTOR


def zillow_scraper(url: str = ZILLOW_URL) -> dict:
    from time import sleep

    driver = SeleniumChromeDriver()
    driver.get_url(url)
    sleep(2)
    properties = driver.find_class_name(LISTING_SELECTOR, single=False)
    property_dict = {}

    for num, property_elem in enumerate(properties):
        # Extract the URL from the 'href' attribute of the <a> element
        url_element = property_elem.find_element(By.CSS_SELECTOR, 'a[data-test="property-card-link"]')
        address = url_element.text
        property_url = url_element.get_attribute('href')

        # Extract the Price from the 'data-test' attribute of the <span> element
        price_element = property_elem.find_element(By.CSS_SELECTOR, 'span[data-test="property-card-price"]')
        price = price_element.text

        # print(num)
        # print(f"Address: {address}"),
        # print(f'Price: {price}'),
        # print(f"URL: {property_url}")

        property_dict.update({num: {
            "Address": address,
            "Price": price,
            "URL": property_url
        }})

    driver.close()
    return property_dict


def main():
    from pprint import pp
    properties = zillow_scraper()
    pp(properties)


if __name__ == '__main__':
    print("TEST:Running Directly.")
    main()
