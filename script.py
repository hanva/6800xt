from selenium import webdriver

driver = webdriver.Chrome(executable_path="chromedriver")
driver.get('https://www.amd.com/fr/direct-buy/5450881600/fr')
element = driver.find_element_by_css_selector('#product-details-info .btn-shopping-cart')
cookies = driver.find_element_by_id('#onetrust-accept-btn-handler')
cookies.click()
element.click()