from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
#deklarasi library chrome agar browser berjalan otomatis
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://barru.pythonanywhere.com/daftar') #url web yang dituju
time.sleep(2) #delay 2 detik
driver.find_element(By.XPATH,'/html/body/div/div[2]/form/input[1]').send_keys("jagoqaindonesia@gmail.com") #mencari elemet email
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div/div[2]/form/input[2]').send_keys("sman0jakarta")
time.sleep(2)
# find button sign in
driver.find_element(By.ID, 'signin_login').click() 
time.sleep(2)

response_message = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/h2").text
response_data = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[1]").text
assert "User's not found" in response_message
assert "Email atau Password Anda Salah" in response_data
driver.close() #menutup chrome web browser