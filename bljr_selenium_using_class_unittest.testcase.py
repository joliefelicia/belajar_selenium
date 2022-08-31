from lib2to3.pgen2 import driver
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
class TestLogin(unittest.TestCase):
 def setUp(self):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())

 def test_a_succesfull_register_myappventure(self):
   driver= self.driver
   driver.get("https://myappventure.herokuapp.com/registration")
   time.sleep(1)
   driver.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[1]/input").send_keys('okejayy')
   time.sleep(1)
   driver.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[2]/input").send_keys('okejayy@getnada.com')
   time.sleep(1)
   driver.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[3]/div[2]/input").send_keys('okejayy123')
   time.sleep(1)
   driver.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[5]/button").click()
   respon_welcome = driver.find_element("/html/body/div/main/div/div[2]/p").text
   self.assertEquals('Selamat! Akun anda berhasil dibuat',respon_welcome)
   

 def test_a_usernamenotvalid_register_myappventure(self):
   driver= self.driver
   driver.get("https://myappventure.herokuapp.com/registration")
   time.sleep(1)
   driver.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[1]/input").send_keys('y')
   time.sleep(1)
   driver.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[2]/input").send_keys('yy@getnada.com')
   time.sleep(1)
   driver.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[3]/div[2]/input").send_keys('jolayy123')
   time.sleep(1)
   driver.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[5]/button").click()
   respon_username_salah = driver.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[2]/div").text
   self.assertEqual('username gunakan 3-15 karakter',respon_username_salah)

 def test_an_account_has_been_registered_myappventure(self):
   driver= self.driver
   driver.get("https://myappventure.herokuapp.com/registration")
   time.sleep(1)
   driver.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[1]/input").send_keys('jolayy')
   time.sleep(1)
   driver.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[2]/input").send_keys('jolayy@getnada.com')
   time.sleep(1)
   driver.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[3]/div[2]/input").send_keys('jolayy123')
   time.sleep(1)
   driver.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[5]/button").click()
   time.sleep(10)
   respon_registered = driver.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[1]/div[1]/p").text
   self.assertIn('sudah', respon_registered)

 def test_succesfull_login_myappventure(self):
   driver= self.driver
   driver.get("https://myappventure.herokuapp.com/login")
   time.sleep(1)
   driver.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[1]/input").send_keys('jode@getnada.com')
   time.sleep(1)
   driver.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[2]/div[2]/input").send_keys('jode123')
   time.sleep(1)
   driver.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[4]/button").click()
   
 def tearDown(self):
   self.driver.close()

if __name__ == "__main__":
   unittest.main()