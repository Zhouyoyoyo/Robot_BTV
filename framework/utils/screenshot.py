import os
from datetime import datetime

def take_screenshot(driver, folder):
    os.makedirs(folder, exist_ok=True)
    filename = datetime.now().strftime("%Y%m%d_%H%M%S.png")
    path = os.path.join(folder, filename)
    driver.save_screenshot(path)
    return path
