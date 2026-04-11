from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

url = "https://www.youtube.com/watch?v=1q5O6QYIPUE"
driver.get(url)

time.sleep(10)  # 🔥 rất quan trọng

for _ in range(30):
    try:
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)
    except:
        print("❌ bị crash")
        break

comments = driver.find_elements(By.XPATH, '//*[@id="content-text"]')

print("Tìm thấy:", len(comments))

driver.quit()


df = pd.DataFrame(comments)
df.to_csv("viettel_comments.csv", index=False, encoding="utf-8-sig")