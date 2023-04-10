from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("file:///Users/roei/Downloads/tip_calc/index.html")
billamt = driver.find_element(by="id", value="billamt")
billamt.send_keys("100")
serviceQual = driver.find_element(by="xpath", value="//*[@id=\"serviceQual\"]/option[5]")
serviceQual.click()
musicQual = driver.find_element(by="xpath", value="//*[@id=\"musicQual\"]/option[6]")
musicQual.click()
peopleamt = driver.find_element(by="id", value="peopleamt")
peopleamt.send_keys("2")
calculate = driver.find_element(by="id", value="calculate")
calculate.click()
actual = driver.find_element(by="id", value="tip").text
expected = "6.00"
assert expected == actual
sleep(5)
driver.close()