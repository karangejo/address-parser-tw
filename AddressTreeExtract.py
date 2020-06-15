#
# This site is very unreliable (must come up with a way to check the loading time and give up sometimes)
#
import json
import pytest
import pandas as pd
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
sleep_time = 5

def getCities(driver):
    # dictionary to store extracted information

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
    cities = []
    for option in city_options:
        city = option.text
        cities.append(city)
    return cities
           
def getTowns(city,driver):
    # dictionary to store extracted information
    # entry point
   
    # select city (must be exactly as found in the dropdown
    dropdown = driver.find_element(By.ID, "select_city_id1")
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
    towns = []
    for option in town_options:
        towns.append(option.text)
    return towns

def getRoads(town, driver):

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
    roads=[]
    for option in road_options:
        roads.append(option.text)
    return roads

def getLanes( road, driver):
     
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
    lanes = []
    for option in lane_options:
        lanes.append(option.text)
    return lanes

def getAlleys(lane, driver):
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
    alleys = []
    for option in alley_options:
        alleys.append(option.text)
    return alleys

def save_json(dict):
    print(dict)
    json_dict = json.dumps(dict, ensure_ascii=False)
    f = open("AddressTree.json", "w", encoding="utf-8")
    f.write(json_dict)
    f.close()

def startGet():
    # start the driver 
    driver = webdriver.Chrome('./chromedriver')
    cities = getCities(driver)
    print(cities)
    tree = {}
    try:
        for city in cities:
            towns = getTowns(city,driver)
            print(towns)
            tree[city] = {}
            for town in towns:
               roads = getRoads(town, driver)
               print(roads)
               tree[city][town] = roads
            #    for road in roads:
            #        lanes = getLanes(road, driver)
            #        tree[city][town][road] = {}
            #        for lane in lanes:
            #            alleys = getAlleys(lane, driver)
            #            tree[city][town][road][lane] = alleys

    except:
        save_json(tree)
        return tree
    save_json(tree)
    return tree

tree = startGet()
print(tree)