from selenium.webdriver.common.by import By
from selenium_chrome_setup import SeleniumChromeDriver
from endpoints import GOOGLE_FORM_URL


def google_form(form_url: str, address: str, price: str, url: str):
    from time import sleep
    form = SeleniumChromeDriver()
    form.get_url(form_url)
    sleep(2)
    all_inputs = form.find_class_name('lrKTG')
    questions = all_inputs.find_elements(By.CSS_SELECTOR, 'div[jsname="WsjYwc"]')

    # Add Input based on Question in Form
    for each in questions:
        if each.find_element(By.CSS_SELECTOR, 'span[class="M7eMe"]').text == 'Address of Property':
            answer = each.find_element(By.CSS_SELECTOR, 'input[jsname="YPqjbf"]')
            answer.send_keys(address)
        if each.find_element(By.CSS_SELECTOR, 'span[class="M7eMe"]').text == 'Price per Month':
            answer = each.find_element(By.CSS_SELECTOR, 'input[jsname="YPqjbf"]')
            answer.send_keys(price)
        if each.find_element(By.CSS_SELECTOR, 'span[class="M7eMe"]').text == 'Property URL':
            answer = each.find_element(By.CSS_SELECTOR, 'input[jsname="YPqjbf"]')
            answer.send_keys(url)

    # Enter Information
    sleep(1)
    button_section = all_inputs.find_element(By.CLASS_NAME, "ThHDze")
    button = button_section.find_element(By.CSS_SELECTOR, 'div[role="button"]')
    button.click()

    sleep(2)
    form.close()


def main():
    google_form(GOOGLE_FORM_URL, address='Test', price='123', url='webpage.com')


if __name__ == '__main__':
    print("TEST:Running Directly.")
    main()
