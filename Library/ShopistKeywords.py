from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import csv
import time


class ShopistKeywords:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def scrape_shopist_sofas(self, url, output_file):
        self.driver.get(url)
        time.sleep(3)

        # Click on the Sofa button
        sofa_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#__layout > div > div:nth-child(1) > div.navbar-large > div > div:nth-child(1) > a.sofas > div > div'))
        )
        sofa_button.click()
        time.sleep(3)

        # Create CSV file and write header
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Sofa Name', 'Price']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            # Loop through sofa items
            for i in range(1, 10):
                # Get sofa name and price
                sofa_name_element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, f'#main > div.products > div:nth-child({i}) > div.description > div:nth-child(1)'))
                )
                sofa_name = sofa_name_element.text

                price_element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, f'#main > div.products > div:nth-child({i}) > div.description > div.price'))
                )
                price = price_element.text

                # Write data to CSV
                writer.writerow({'Sofa Name': sofa_name, 'Price': price})

    def close_browser(self):
        self.driver.quit()
