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
    "https://youtu.be/geH9MlJ85MA",
    "https://youtu.be/08g0V5AuzEM",
    "https://youtu.be/J1V9sI7lFPk",
    "https://youtu.be/uN1FxJXJgGY",
    "https://youtu.be/uBP2VXJRPv8",
    "https://youtu.be/hwGWNWW1fh4",
    "https://youtu.be/WolD4RpRU_g",
    "https://youtu.be/XKzLjTeW8YM",
    "https://youtu.be/BDmYjhA3rgI",
    "https://youtu.be/lcONWHcvE08",
    "https://youtu.be/w2oAc-l-5PQ",
    "https://youtu.be/IVDCGIkAKDE",
    "https://youtu.be/B3XDhljbUjg",
    "https://www.youtube.com/shorts/TwrKYlsydaM?feature=share",
    "https://youtu.be/RIzBlk0-1qM",
    "https://youtu.be/jPMuWXWOH_w",
    "https://youtu.be/tH-9sihDHls",
    "https://youtu.be/MCK0Tp5Ms2Y",
    "https://youtu.be/6cogq1z3RzQ",
    "https://youtu.be/4Ryf54Lx61g",
    "https://youtu.be/YOREXHpe4cY",
    "https://youtu.be/akmhwPGMZfM",
    "https://www.youtube.com/watch?v=08g0V5AuzEM",
    "https://www.youtube.com/watch?v=geH9MlJ85MA",
    "https://www.youtube.com/watch?v=3bGcE4htGrI",
    "https://www.youtube.com/watch?v=fX1mGzI6oGg",
    "https://www.youtube.com/watch?v=uN1FxJXJgGY",
    "https://www.youtube.com/watch?v=f-B4E-eD2oI",
    "https://www.youtube.com/watch?v=zV9L1ia6S08",
    "https://www.youtube.com/watch?v=UvMdrrizx-s",
    "https://www.youtube.com/watch?v=SAn_W_P1vG4",
    "https://www.youtube.com/watch?v=J1V9sI7lFPk"
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
