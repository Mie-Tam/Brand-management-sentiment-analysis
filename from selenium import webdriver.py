from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import pandas as pd

# ⚙️ cấu hình trình duyệt
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.maximize_window()

# 👉 danh sách link (đã bỏ link lỗi)
urls = [
    "https://youtu.be/o-2sKjSskAk",
    "https://youtu.be/58wqFZnsVk4",
    "https://youtu.be/VR0XdX75uxg",
    "https://youtu.be/7wG9YYZ7iOY",
    "https://youtu.be/17wtcpJaPVM?t=9",
    "https://youtu.be/OgUhJV8MqZE?t=14",
    "https://youtu.be/ZvSZ6v94rHQ?t=2",
    "https://youtu.be/-qKumdgtYTo?t=5",
    "https://youtu.be/sGvfMLYMSJc?t=9",
    "https://youtu.be/lcONWHcvE08?t=11",
    "https://youtu.be/lcONWHcvE08",
    "https://www.youtube.com/watch?v=1q5O6QYIPUE",
    "https://youtu.be/ulhv-7ciQNQ",
    "https://youtu.be/fYLnj1VYRjc",
    "https://youtu.be/uwIUyqnBUmU",
    "https://youtu.be/hCdzgTLP8tE",
    "https://youtu.be/0QK1JZf_KZ4",
    "https://youtu.be/08g0V5AuzEM",
    "https://youtu.be/qQpOAb_bTbk",
    "https://youtu.be/uFaa2XUvipc",
    "https://youtu.be/SjZvOrHkLsg",
]

data = []
seen = set()  # chống trùng

# 👉 duyệt từng video
for url in urls:
    if len(data) >= 1000:
        break

    print("\n➡️ Đang xử lý:", url)

    try:
        driver.get(url)
        time.sleep(5)

        # 👉 scroll xuống khu comment
        driver.execute_script("window.scrollTo(0, 1000);")
        time.sleep(5)

        # 👉 chờ comment load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="content-text"]'))
        )

        # 👉 scroll nhiều lần để load thêm comment
        last_height = driver.execute_script("return document.documentElement.scrollHeight")

        for i in range(50):
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(2)

            new_height = driver.execute_script("return document.documentElement.scrollHeight")
            if new_height == last_height:
                print("⛔ Không load thêm comment nữa")
                break
            last_height = new_height

        # 👉 lấy comment
        comments = driver.find_elements(By.XPATH, '//*[@id="content-text"]')
        print("💬 Số comment lấy được:", len(comments))

        for cmt in comments:
            if len(data) >= 1000:
                break

            text = cmt.text.strip()

            # 👉 chống trùng
            if text and text not in seen:
                seen.add(text)

                data.append({
                    "text": text,
                    "url": url,
                    "platform": "YouTube"
                })

    except Exception as e:
        print("❌ Lỗi với video:", url)
        print(e)
        continue

driver.quit()

# 👉 đảm bảo đúng 1000
data = data[:1000]

# 👉 lưu file
df = pd.DataFrame(data)
df.to_csv("youtube_1000_comments.csv", index=False, encoding="utf-8-sig")

print("\n✅ DONE:", len(data), "comments")
