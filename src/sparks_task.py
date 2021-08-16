# IMPORTING LIBRARIES
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

# PATH is given value of address of webdriver for chrome
PATH = "E:/SC/Python/SELENNIUM/chromedriver.exe"
# a object driver is created for Chrome which is given parameter as address of our webdriver
driver = webdriver.Chrome(PATH)


# Maximize window
# driver.maximize_window()


# 5 pages 10 elements
# Homepage()
def homepage():
    print("\nPAGE 1 -- Home")
    driver.get("https://www.thesparksfoundationsingapore.org")
    # TITLE CHECK
    print("\nElement 1:\tTitle of Page is", driver.title)
    # NAVBAR CHECK
    navbar = driver.find_element_by_class_name("navbar-brand")
    if navbar.is_displayed():
        print("Element 2:\tNavbar is present")
    # Check if logo is displayed
    logo = driver.find_element_by_css_selector("a.col-md-6 > img:nth-child(1)")
    if logo.is_displayed():
        print("Element 3:\tLogo is present")
    time.sleep(2)
    vision()


def vision():
    print("\nPAGE2 -- Vision, Mission, Values")
    time.sleep(2)
    # get about us dropdown on main page
    about_us = driver.find_element_by_link_text("About Us")
    about_us.click()
    print("Element 4:\tDropdown menu is working")
    time.sleep(2)
    Vis_Mis = driver.find_element_by_link_text("Vision, Mission and Values")
    Vis_Mis.click()
    print("Element 5:\tNavbar Link is working")
    time.sleep(2)
    news()


def news():
    print("\nPAGE3 -- NEWS")
    time.sleep(2)
    # get about us dropdown on main page
    about_us = driver.find_element_by_link_text("About Us")
    about_us.click()
    time.sleep(2)
    News = driver.find_element_by_link_text("News")
    News.click()
    time.sleep(1)
    print("Element 6:\tNews Page exists")
    y = 250
    for timer in range(0, 5):
        driver.execute_script("window.scrollTo(0, " + str(y) + ")")
        y += 250
        time.sleep(1)
    time.sleep(1)
    go_to_top = driver.find_element_by_xpath('//*[@id="toTop"]')
    go_to_top.click()
    time.sleep(2)
    joinUs()


def joinUs():
    print("\nPAGE4 -- Join Us")
    # get join us drop down element
    about_us = driver.find_element_by_link_text("Join Us")
    about_us.click()
    print("Element 7:\tJoin Us Page exists")
    # get why join us element inside drop down
    why_join_us = driver.find_element_by_link_text("Why Join Us")
    why_join_us.click()
    print("Element 8:\tWhy Join Us link active")
    time.sleep(2)

    # automated form filling
    name = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/form/input[1]")
    contact = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/form/input[2]")
    role = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/form/select")

    # scroll
    y = 250
    for timer in range(0, 3):
        driver.execute_script("window.scrollTo(0, " + str(y) + ")")
        y += 300

    name.send_keys("Shivam")
    contact.send_keys("shivam@abc.com")
    popdown = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/form/select/option")
    popdown.click()
    student = Select(role)
    student.select_by_visible_text("Student")
    print("Element 9:\tForm filled")
    time.sleep(1)
    submit = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/form/input[3]")
    submit.click()
    print("Element 10:\tForm submitted")
    time.sleep(3)
    contactUs()


def contactUs():
    print("\nPAGE5 -- Contact Us")
    contact_us = driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[6]/a')
    contact_us.click()
    time.sleep(1)
    y = 250
    for timer in range(0, 5):
        driver.execute_script("window.scrollTo(0, " + str(y) + ")")
        y += 250
        time.sleep(1)
    print("\n All tests ran successfully !")
    driver.quit()


# Main function
if __name__ == "__main__":
    homepage()
