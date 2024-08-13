import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Inicializace prohlížeče v headless režimu
options = Options()
options.add_argument('--headless')  # Spustit prohlížeč bez GUI
options.add_argument('--disable-gpu')  # Nutné pro některé OS
options.add_argument('--no-sandbox')  # Doporučeno pro linuxové servery
options.add_argument('--disable-dev-shm-usage')  # Pro optimalizaci paměti na Linuxu
options.add_argument('--window-size=1920x1080')  # Nastavit velikost okna

# Spuštění prohlížeče s těmito možnostmi
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Otevření specifikované stránky
url = "https://s700s492.autoexpr.com/grafana/d/e59df556-bca2-457f-956d-f56274bef99c/bor-general-plant-overview?orgId=1&refresh=1m&kiosk"
driver.get(url)

# Čekání na načtení stránky
time.sleep(1)  # Počkej 10 sekund

# Uložení screenshotu
screenshot_path = "grafana_screenshot.png"
driver.save_screenshot(screenshot_path)

# Zavření prohlížeče
driver.quit()

print(f"Screenshot uložen jako {screenshot_path}")
