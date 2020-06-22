#
# This site is very unreliable (must come up with a way to check the loading time and give up sometimes)
#
import json
import pytest
import pandas as pd
import time
import json
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options



sleep_time = 3
alert_sleep_time = 1.5

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
        deal_with_alert(driver)
        roads.append(option.text)
    return roads

def getLanes( road, driver):
     
    dropdown = driver.find_element(By.ID, "select_road_id")

    # select road
    road_options = dropdown.find_elements(
        By.TAG_NAME, "option")
    for option in road_options:
        deal_with_alert(driver)
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
        deal_with_alert(driver)
        lanes.append(option.text)
    return lanes

def getAlleys(lane, driver):
    dropdown = driver.find_element(By.ID, "select_lane_id")

    # select lane
    lane_options = dropdown.find_elements(
        By.TAG_NAME, "option")
    for option in lane_options:
        deal_with_alert(driver)
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
        deal_with_alert(driver)
        alleys.append(option.text)
    return alleys

def save_json(dict,json_filename):
    print(dict)
    json_dict = json.dumps(dict, ensure_ascii=False)
    f = open(json_filename, "w", encoding="utf-8")
    f.write(json_dict)
    f.close()

def element_id_exists(id, driver): 
     time.sleep(sleep_time)
     try:
        driver.find_element(By.ID, id)
        return True
     except:
        return False

def deal_with_alert(driver):
    try:
        WebDriverWait(driver, alert_sleep_time).until(expected_conditions.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

        alert = driver.switch_to.alert
        alert.accept()
        print("alert accepted")
    except TimeoutException:
        print("no alert")

def startGet():
    # start the driver
    chrome_options = Options()
    # chrome_options.add_argument("--disable-notifications") 
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome('./chromedriver',options=chrome_options)
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
               tree[city][town] = {}
               for road in roads:
                   if element_id_exists("select_lane_id",driver):
                       lanes = getLanes(road, driver)
                       print(lanes)
                       tree[city][town][road] = {}
                       for lane in lanes:
                           if element_id_exists("select_alley_id", driver):
                               alleys = getAlleys(lane, driver)
                               print(alleys)
                               tree[city][town][road][lane] = alleys
                           else:
                               tree[city][town][road] = lanes
                   else:
                       tree[city][town] = roads
    except Exception as inst:
        print(type(inst))
        print(inst.args)
        print(inst)
        print(traceback.format_exc())

        save_json(tree, "newTree.json")
        return tree
    save_json(tree, "newTree.json")
    return tree

startGet()


def landMoi(city, town, road, lane, alley, number, driver):
    sleep_time = 2
    # dictionary to store extracted information
    vars = {}

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
        deal_with_alert(driver)
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
    vars["地段"] = driver.find_element(
        By.CSS_SELECTOR, "#one-column-emphasis tr:nth-child(3) > td").text
    vars["地號"] = driver.find_element(
        By.CSS_SELECTOR, "#one-column-emphasis tr:nth-child(4) > td").text
    vars["面積"] = driver.find_element(
        By.CSS_SELECTOR, "tr:nth-child(5) > td:nth-child(2)").text
    vars["公告土地現值"] = driver.find_element(
        By.CSS_SELECTOR, "#one-column-emphasis tr:nth-child(6) > td").text
    vars["公告土地地價"] = driver.find_element(
        By.CSS_SELECTOR, "tr:nth-child(7) > td:nth-child(2)").text
    return vars["行政區"],  vars["地政事務所"], vars["地段"], vars["地號"], vars["面積"], vars["公告土地現值"], vars["公告土地地價"]


# city = "基隆市"
# town = "七堵區"
# road = "三合街"
# driver = webdriver.Chrome('./chromedriver')

# landMoi(city,town,road,"","","",driver)