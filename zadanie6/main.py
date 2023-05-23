from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import random
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://localhost:3000/")


def t1():
    expected_title = "Book Library"
    actual_title = driver.title
    assert actual_title == expected_title


def t2():
    wrong_title = "WRONG"
    actual_title = driver.title
    assert wrong_title == actual_title


def t3():
    wrong_test = "WRONG"
    actual_text = driver.find_element_by_css_selector("h1").text
    assert wrong_test in actual_text


def t4():
    wrong_test = "Book Library"
    actual_text = driver.find_element_by_css_selector("h1").text
    assert wrong_test in actual_text


def t5():
    link = driver.find_element(By.ID, "main")
    href = link.get_attribute("href")
    assert href == "http://localhost:3000/"


def t6():
    link = driver.find_element(By.ID, "edit")
    link.click()
    assert driver.current_url == "http://localhost:3000/managment"
    driver.get("http://localhost:3000/")


def t7():
    link = driver.find_element(By.ID, "borr")
    link.click()
    assert driver.current_url == "http://localhost:3000/managment"


def t8():
    link = driver.find_element(By.ID, "borr")
    assert "Oddaj książke" in link.text


def t9():
    link = driver.find_element(By.ID, "borr")
    assert link.is_displayed()


def t10():
    ul_elements = driver.find_elements(By.XPATH, "//ul/li")
    num_of_ul = len(ul_elements)
    next_button = driver.find_element(By.ID, "nextButton")
    is_disabled = next_button.get_attribute("disabled")
    assert (num_of_ul < 10 and is_disabled == "true") or (num_of_ul == 10 and is_disabled is None)


def t11():
    page_number = driver.find_element(By.ID, 'currentPage')
    text = page_number.text
    pattern = r"Page \d+"
    match = re.search(pattern, text)
    assert match is not None


def t12():
    li_elements = driver.find_elements(By.TAG_NAME, "li")
    for li in li_elements:
        button = li.find_element(By.TAG_NAME, "button")
        assert button is not None


def t13():
    ul_elements = driver.find_elements(By.XPATH, "//ul/li")
    num_of_ul = len(ul_elements)
    if num_of_ul == 10:
        next_button = driver.find_element(By.ID, "nextButton")
        first_li = driver.find_element(By.TAG_NAME, "li")
        text_first = first_li.text
        next_button.click()
        second_li = driver.find_element(By.TAG_NAME, "li")
        text_second = second_li.text
        assert text_first != text_second


def t14():
    ul_elements = driver.find_elements(By.XPATH, "//ul/li")
    num_of_ul = len(ul_elements)
    if num_of_ul == 10:
        next_button = driver.find_element(By.ID, "nextButton")
        next_button.click()
        prev_button = driver.find_element(By.ID, "prevButton")
        is_disabled = prev_button.get_attribute("disabled")
        assert is_disabled is None


def t15():
    driver.get("http://localhost:3000/managment")
    title_input = driver.find_element(By.ID, "title")
    title_input.send_keys("Przykładowy tytuł")
    author_input = driver.find_element(By.ID, "author")
    author_input.send_keys("Przykładowy autor")
    isbn_input = driver.find_element(By.ID, "isbn")
    isbn_input.send_keys("1234567890")
    copies_input = driver.find_element(By.ID, "copies")
    copies_input.send_keys("10")
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    submit_button.click()
    message = driver.find_element(By.XPATH, "//div[@id='message']")
    assert message.text == "Dodano książke do biblioteki."


def t16():
    driver.get("http://localhost:3000/managment")
    numeric_field = driver.find_element(By.ID, "copies")
    numeric_field.send_keys("abc")
    entered_value = numeric_field.get_attribute("value")
    assert entered_value == ""


def t17():
    driver.get("http://localhost:3000/")
    elements = driver.find_elements(By.TAG_NAME, "li")
    random_index = random.randint(0, len(elements) - 1)
    li = elements[random_index]
    button = li.find_element(By.TAG_NAME, "button")
    button.click()
    url = driver.current_url
    id_from_url = url.split("/")[-1]
    h = driver.find_element(By.TAG_NAME, "h2")
    id_from_h = h.text.split()[-1]
    assert id_from_h == id_from_url


def t18():
    driver.get("http://localhost:3000/")
    elements = driver.find_elements(By.TAG_NAME, "li")
    random_index = random.randint(0, len(elements) - 1)
    li = elements[random_index]
    button = li.find_element(By.TAG_NAME, "button")
    button.click()

    borrower_input = driver.find_element(By.ID, "borrower")
    borrower_input.send_keys("Przykładowy wypożyczający")

    date_input = driver.find_element(By.ID, "returnDate")
    date_input.send_keys("26.05.2023")

    submit_button = driver.find_element(By.TAG_NAME, "button")
    submit_button.click()

    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert_text = driver.switch_to.alert.text

    expected_text = "Książka została wypożyczona."
    assert expected_text in alert_text
    driver.switch_to.alert.accept()


def t19():
    driver.get("http://localhost:3000/")
    elements = driver.find_elements(By.TAG_NAME, "li")
    random_index = random.randint(0, len(elements) - 1)
    li = elements[random_index]
    button = li.find_element(By.TAG_NAME, "button")
    button.click()

    date_input = driver.find_element(By.ID, "returnDate")
    date_input.send_keys("abc")
    date = date_input.get_attribute("value")
    assert date == ""


def t20():
    link_tag = driver.find_elements_by_css_selector("link")
    assert link_tag


