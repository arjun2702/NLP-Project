from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


# Set up Chrome options to handle SSL errors
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

driver = webdriver.Chrome(options=chrome_options)

try:
        # Navigate to the page
        driver.get('https://hprera.nic.in/PublicDashboard')
        
        # Wait for the "Registered Projects" link to be present and click it
        wait = WebDriverWait(driver, 100)

        # Loop through the first 6 projects
        for i in range(6):
            # Ensure that the project links are visible and up-to-date
            wait.until(ec.presence_of_all_elements_located((By.XPATH, '//a[contains(@onclick, "tab_project_main_ApplicationPreview($(this));")]')))
            project_links = driver.find_elements(By.XPATH, '//a[contains(@onclick, "tab_project_main_ApplicationPreview($(this));")]')

            # Scroll to the project link and ensure it is clickable
            project_link = project_links[i]
            driver.execute_script("arguments[0].scrollIntoView(true);", project_link)
            wait.until(ec.element_to_be_clickable(project_link))
            
            # Click the project link
            project_link.click()

            # Wait for the new content to load
            wait.until(ec.presence_of_element_located((By.XPATH, '//td[@class="fw-600"]')))

            # Extract the project name
            name_element = driver.find_element(By.XPATH, '//td[@class="fw-600"]')
            project_name = name_element.text
            # Print the extracted data
            print(f'Project Name: {project_name}')


            # Extract all <span class="fw-600"> elements
            #address_elements = driver.find_elements(By.XPATH, '//span[@class="fw-600"]')
            #address = address_elements[3].text if len(address_elements) > 3 else 'N/A'

            # Extract the address from <td> or <tr> tag containing <span class="fw-600"> with colspan="2"
            #address_elements = driver.find_elements(By.XPATH, '//td[@colspan="2"]/span[@class="fw-600"]')
            #address = address_elements[0].text if address_elements else 'N/A'


            
            # Extract PAN and GST numbers
            #pan_elements = driver.find_elements(By.XPATH, '//td[span[@class="mr-1 fw-600"]]')
            #pan_number = pan_elements.text
           # Print the extracted data
            #print(f'Project Name: {project_name}')

            # Scroll to the top of the page
            driver.execute_script("window.scrollTo(0, 0);")

            # Go back to the previous page
            driver.refresh()

            # Wait for the "Registered Projects" link to be present and click it again
            registered_projects_link = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-target="#reg-Projects"]')))
            registered_projects_link.click()

finally:
        driver.quit()