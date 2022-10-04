import time
import operator
from selenium import webdriver

driver_path= "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

timeout = time.time() + 5

a=True
while a:
	cookie.click()

	if time.time()>timeout:
		money = driver.find_element_by_id("money")

		store = driver.find_elements_by_css_selector("#store div")
		store_dict = {}
		for store_item in store:
			try:
				price = store_item.text.split("\n")[0].split("-")[1].replace(",","")
				id = store_item.get_attribute("id")
				store_dict [id] = int(price)
			except IndexError:
				pass

		affordable_store_item = {}
		for id, cost in store_dict.items():
			if int(money.text)>cost:
				affordable_store_item [id] = int(cost)

		sorted_dictionary = sorted(affordable_store_item.items(), key=operator.itemgetter(1))
		driver.find_element_by_id(sorted_dictionary[len(sorted_dictionary)-1][0]).click()
		timeout = time.time()+5

