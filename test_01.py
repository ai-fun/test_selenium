# 
# Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

driver = webdriver.Chrome()
driver.get('https://hotel.testplanisphere.dev/ja/index.html')

sleep(2)

# ログイン画面に繊維
userloginbtn =driver.find_elements(By.CLASS_NAME,"nav-item")
userloginbtn[4].click()

sleep(2)

#ログイン情報入力
usermailadd = driver.find_element(By.ID, "email")
text_mailadd = "ichiro@example.com"
usermailadd.send_keys(text_mailadd)

# パスワード
userpwd = driver.find_element(By.ID, "password")
text_pwd = "password"
userpwd.send_keys(text_pwd)

#ログイン
login_btn = driver.find_element(By.ID, "login-button")
login_btn.click()

sleep(2)

#ログアウト
userlogoutbtn =driver.find_elements(By.CLASS_NAME,"nav-item")
userlogoutbtn[3].click()

# 待機時間
sleep(2)

