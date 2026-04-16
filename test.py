from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import pandas as pd

# ================== CẤU HÌNH ==================
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# ================== LINK ĐÃ SỬA ==================
urls = list(set([   # 👉 set() để tự động xoá trùng
    "https://youtu.be/o-2sKjSskAk",
    "https://youtu.be/58wqFZnsVk4",
    "https://youtu.be/VR0XdX75uxg",
    "https://youtu.be/7wG9YYZ7iOY",
    "https://youtu.be/17wtcpJaPVM",
    "https://youtu.be/OgUhJV8MqZE",
    "https://youtu.be/ZvSZ6v94rHQ",
    "https://youtu.be/-qKumdgtYTo",
    "https://youtu.be/sGvfMLYMSJc",
    "https://youtu.be/lcONWHcvE08",

    "https://www.youtube.com/watch?v=DEIkKSvU7cI",
    "https://www.youtube.com/watch?v=T_ad7kWeQJk",
    "https://www.youtube.com/watch?v=kUft1HOmoZE",
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

    "https://youtu.be/5dmLpdy3Lr8",
    "https://youtu.be/yC3Pe1lY12U",
    "https://youtu.be/nrDent1sL8c",
    "https://youtu.be/SAp2RWDOQFs",
    "https://youtu.be/IGnj7WRXUJg",
    "https://youtu.be/B6I8hOIl098",
    "https://youtu.be/C8y_wwMU3T8",
    "https://youtu.be/se9CZtVlZWk",
    "https://youtu.be/aTvbvtrZvuI",
    "https://youtu.be/Iuc8aFqPUps",
    "https://youtu.be/m4qB47FExdo",
    "https://youtu.be/NpM9HGwqbts",
    "https://youtu.be/DHuUVWnofS4",
    "https://youtu.be/N-5wEwFNOAU",
    "https://youtu.be/XfQ-lkUc-TM",
    "https://youtu.be/Wg5f5EUvS88",
    "https://youtu.be/KEdtpFb1WhQ",
    "https://youtu.be/yR1-FT89R0s",
    "https://youtu.be/V-q_Cq5162o",
    "https://youtu.be/x_d-SsBXBEk",
    "https://youtu.be/6zr7Ujwe8kc",
    "https://youtu.be/dFWSlJ-hnHg",
    "https://youtu.be/gKgPofXoeTE",
    "https://youtu.be/TohEEMFC2dQ",
    "https://youtu.be/imFxQd_HMRE",
    "https://youtu.be/Ejjqg0i95ZY",
    "https://youtu.be/kNDQbKuMFEM",
    "https://youtu.be/-RYdz2c1lqw",
    "https://youtu.be/Ae5vdJcee_E",
    "https://youtu.be/qMxQ54qKTao",
    "https://youtu.be/P4LDEXdgIZY",
    "https://youtu.be/z8Y-3fCRJfM",
    "https://youtu.be/B_utytlpdQw",
    "https://youtu.be/_Urxj_Nimjg",
    "https://youtu.be/7dctV6bpjXg",
    "https://youtu.be/S5d0syx2MOU",
    "https://youtu.be/e4AIo4FsBk4",
    "https://youtu.be/dEts3J7PuFM",
    "https://youtu.be/i_bMTQk4TYg",
    "https://youtu.be/Q62SS1iBA_I",
    "https://youtu.be/vairXqJAg1k",
    "https://youtu.be/zT-Dz1upsqk",
    "https://youtu.be/sVa_BlM7zkE",
    "https://youtu.be/pWSO06o5DhM",
    "https://youtu.be/sYseoHTV0Ig",
    "https://youtu.be/t90uq4Qa0k4",
    "https://youtu.be/tffKIW7z1cU",
    "https://youtu.be/_lRH0wIQNzE",
    "https://youtu.be/g-EfaM_8Igw",
    "https://youtu.be/R5dIaWyO9E8",
    "https://youtu.be/jro2Ny_KwsI",
    "https://youtu.be/lPvZHUT5t7M",
    "https://youtu.be/txkP0nP-YSU",
    "https://youtu.be/mn_slpYzaE4",
    "https://youtu.be/PaKgZ98k1yI",
    "https://youtu.be/imk_fVEkF64",
    "https://youtu.be/BU0iTZgFc2k",
    "https://youtu.be/CPxDU7toeBo",
    "https://youtu.be/lrh2XG35AOQ",
    "https://youtu.be/HhLiQYVijQs",
    "https://youtu.be/uQA00UMMJ3k",
    "https://youtu.be/avT5MeepmD8",
    "https://youtu.be/_3yvR_Jbjr4",
    "https://youtu.be/OQMW-FN9LK4",
    "https://youtu.be/lGYovjqk1Iw",
    "https://youtu.be/5YFTmrxxMFs",
    "https://youtu.be/oMvh4AYjbfc",
    "https://youtu.be/uHUZIaeBpxA",
    "https://youtu.be/ELvcCNXz47Y",
]))

# ================== CRAWL ==================
data = []
seen = set()

for url in urls:
    print("\n➡️", url)

    try:
        driver.get(url)
        time.sleep(5)

        driver.execute_script("window.scrollTo(0, 1000);")
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="content-text"]'))
        )

        for i in range(150):
            driver.execute_script("window.scrollBy(0, 1000);")
            time.sleep(1)

        comments = driver.find_elements(By.XPATH, '//*[@id="content-text"]')
        print("💬", len(comments))

        for cmt in comments:
            text = cmt.text.strip()
            if text and text not in seen:
                seen.add(text)
                data.append(text)

    except:
        print("❌ lỗi")
        continue

driver.quit()

df = pd.DataFrame(data, columns=["text"])
df.to_csv("youtube_comments.csv", index=False, encoding="utf-8-sig")

print("\n✅ DONE:", len(data))