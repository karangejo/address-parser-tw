# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


def landMoi(city, town, road, lane, alley, number):
    sleep_time = 2
    # dictionary to store extracted information
    vars = {}

    # start the driver (this could be moved outside if called many times)
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome('./chromedriver', chrome_options=options)

    # entry point
    driver.get("http://easymap.land.moi.gov.tw/")
    driver.set_window_size(911, 928)
    driver.find_element(By.LINK_TEXT, "進入系統").click()
    driver.find_element(By.ID, "button_addr").click()
    dropdown = driver.find_element(By.ID, "doorPlateTypeId")
    dropdown.find_element(By.XPATH, "//option[. = '戶政門牌']").click()
    element = driver.find_element(By.ID, "doorPlateTypeId")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = driver.find_element(By.ID, "doorPlateTypeId")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.ID, "doorPlateTypeId")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    driver.find_element(By.ID, "doorPlateTypeId").click()
    dropdown = driver.find_element(By.ID, "select_city_id1")

    # select city (must be exactly as found in the dropdown
    city_options = dropdown.find_elements(
        By.TAG_NAME, "option")
    for option in city_options:
        if(option.text == str(city)):
            option.click()
    element = driver.find_element(By.ID, "select_city_id1")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = driver.find_element(By.ID, "select_city_id1")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.ID, "select_city_id1")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()

    # wait for page to load next options (time could be calibrated)
    time.sleep(sleep_time)
    driver.find_element(By.ID, "select_city_id1").click()
    dropdown = driver.find_element(By.ID, "select_town_id1")

    # select town
    town_options = dropdown.find_elements(
        By.TAG_NAME, "option")
    for option in town_options:
        if(option.text == str(town)):
            option.click()

    element = driver.find_element(By.ID, "select_town_id1")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = driver.find_element(By.ID, "select_town_id1")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.ID, "select_town_id1")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()

    # wait for page to load
    time.sleep(sleep_time)
    driver.find_element(By.ID, "select_town_id1").click()
    dropdown = driver.find_element(By.ID, "select_road_id")

    # select road
    road_options = dropdown.find_elements(
        By.TAG_NAME, "option")
    for option in road_options:
        if(option.text == str(road)):
            option.click()

    element = driver.find_element(By.ID, "select_road_id")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = driver.find_element(By.ID, "select_road_id")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.ID, "select_road_id")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()

    # wait for page to load
    time.sleep(sleep_time)
    driver.find_element(By.ID, "select_road_id").click()
    dropdown = driver.find_element(By.ID, "select_lane_id")

    # select lane
    lane_options = dropdown.find_elements(
        By.TAG_NAME, "option")
    for option in lane_options:
        if(option.text == str(lane)):
            option.click()

    element = driver.find_element(By.ID, "select_lane_id")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = driver.find_element(By.ID, "select_lane_id")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.ID, "select_lane_id")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()

    # wait for page to load
    time.sleep(sleep_time)
    driver.find_element(By.ID, "select_lane_id").click()
    dropdown = driver.find_element(By.ID, "select_alley_id")

    # select alley
    alley_options = dropdown.find_elements(
        By.TAG_NAME, "option")
    for option in alley_options:
        if(option.text == str(alley)):
            option.click()

    element = driver.find_element(By.ID, "select_alley_id")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = driver.find_element(By.ID, "select_alley_id")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.ID, "select_alley_id")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    driver.find_element(By.ID, "select_alley_id").click()
    driver.find_element(By.ID, "doorNoId").click()

    # enter door number
    driver.find_element(By.ID, "doorNoId").send_keys(str(number))
    driver.find_element(By.ID, "door_botton").click()
    element = driver.find_element(By.ID, "button_cada")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    # wait for page to load (this can take a while)
    # time.sleep(30)
    WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located(
        (By.CSS_SELECTOR, "#one-column-emphasis tr:nth-child(1) > td")))

    # extract some values a print them
    vars["行政區"] = driver.find_element(
        By.CSS_SELECTOR, "#one-column-emphasis tr:nth-child(1) > td").text
    vars["地政事務所"] = driver.find_element(
        By.CSS_SELECTOR, "#one-column-emphasis tr:nth-child(2) > td").text
    vars["地段	"] = driver.find_element(
        By.CSS_SELECTOR, "#one-column-emphasis tr:nth-child(3) > td").text
    vars["地號"] = driver.find_element(
        By.CSS_SELECTOR, "#one-column-emphasis tr:nth-child(4) > td").text
    vars["面積"] = driver.find_element(
        By.CSS_SELECTOR, "tr:nth-child(5) > td:nth-child(2)").text
    vars["公告土地現值"] = driver.find_element(
        By.CSS_SELECTOR, "#one-column-emphasis tr:nth-child(6) > td").text
    vars["公告土地地價"] = driver.find_element(
        By.CSS_SELECTOR, "tr:nth-child(7) > td:nth-child(2)").text
    print(vars)


def testLandMoi():
    test_city = '新北市'
    test_town = '永和區'
    test_road = '環河西路一段'
    test_lane = '95巷'
    test_alley = '19弄'
    test_number = '1'
    landMoi(test_city, test_town, test_road,
            test_lane, test_alley, test_number)


testLandMoi()
