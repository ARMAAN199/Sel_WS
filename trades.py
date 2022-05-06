from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ARMAAN
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import random
from config import *
from multiprocessing import Pool
from selenium.webdriver.common.keys import Keys as KEYS
import sys

import os

def automate_trades(i, driver):
    try:
        element =  WebDriverWait(driver, 40).until(
            ARMAAN.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/span')))
        element.click()
        print("Going to Strategies Page")
    except:
        automate_trades(i,driver)
        return

    tradegroup_count = find_tradegroup_count(i, driver)
    print("TradeGroups Found : ", tradegroup_count)
    # Choosing a TradeGroup
    group_name, chosenGroup = choose_and_name(i, driver, 1, tradegroup_count, tradegroupPath)
    print(group_name)
    # Choosing Trade in TradeGroup
    trade_count = find_trade_count(i, driver, chosenGroup)
    print("Trades Found : ", trade_count)
    tradeNamePath[0] = tradeNamePath[0] + str(chosenGroup) + tradeNamePath[2]
    trade_name , chosenTrade = choose_and_name(i, driver, 1, trade_count, tradeNamePath, 0)
    print(trade_name)
    #openBuyOrderWindow
    buyOrderWindowPath[0] = buyOrderWindowPath[0] + str(chosenGroup) + buyOrderWindowPath[2] + str(chosenTrade)
    trade_name , chosenTrade = choose_and_name(i, driver, 1, 2, buyOrderWindowPath)
    print(trade_name)


def choose_and_name(i, driver, min , max, path, click = 1):
    chosen = random.randint(min, max)
    time.sleep(0.4)
    # print(path[0] + str(chosen) + path[1])
    try:
        ele = WebDriverWait(driver, 5).until(
                ARMAAN.presence_of_element_located((By.XPATH, path[0] + str(chosen) + path[1])))
        name = ele.get_attribute("innerHTML")
        if click == 1:
            ele.click()
        return [name, chosen]
    except:
        print("error")
        return

def find_tradegroup_count(i, driver):
    try:
        tradegrouplist = WebDriverWait(driver, 5).until(
                ARMAAN.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[2]')))
        trades_grups = tradegrouplist.find_elements(by=By.XPATH, value="*")
        return len(trades_grups)
    except:
        print("No Trade Groups Found")


def find_trade_count(i, driver, chosen):
    try:
        tradelist = WebDriverWait(driver, 5).until(
                ARMAAN.presence_of_element_located((By.XPATH, tradesPath[0] + str(chosen) + tradesPath[1])))
        trades = tradelist.find_elements(by=By.XPATH, value="*")
        return len(trades)
    except:
        print("No Trades Found")


def opened_trade_name(i,driver, chosen):
    tradename = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div["+str(chosen)+"]/div[1]/div[2]/span"))).get_attribute("innerHTML")
    return tradename


# def work_trade_window(i, driver):
#
#
#
# /html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[2]/div[2]/div[3]/div/div
# /html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[3]/div/div


'''
/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div/i
/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]/div/i

/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div/i
/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div/i

/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[3]/div[3]/div[1]/div/i

/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[2]/div[4]/div[2]/div[1]/div[2]/div[1]/div/i
/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[2]/div[4]/div[2]/div[1]/div[3]/div[1]/div/i



/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[2]/div[]/div[1]/span"

/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/span
/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[2]

/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[2]/div[3]/div[2]/div

/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[2]/div[4]/div[2]/div[1]
/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[2]/div[4]/div[2]/div[2]

/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[2]/div[4]/div[2]

'''