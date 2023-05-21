from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com.tr/?hl=tr")
input = driver.find_element(By.NAME,"q")
print (f"İnput : {input}")
driver.maximize_window()
input.send_keys("Kodlama io")

searchButton = driver.find_element(By.NAME,"btnK")
sleep(0.5)
searchButton.click()
sleep(2)
firsResult = driver.find_element(By.CSS_SELECTOR,"#rso > div:nth-child(1) > div > div > div > div > div > div > div > div.yuRUbf > a")
firsResult.click()

listOfCourses = driver.find_elements(By.CLASS_NAME,"course-listing")
print(len(listOfCourses))

while True:
    
    
    continue