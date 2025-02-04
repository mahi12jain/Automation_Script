from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

web = 'https://www.thesun.co.uk/sport/football/'
path = r"C:\Users\Jain\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"  # introduce path here

# Add headless mode
options = Options()
options.headless = True
driver_service = Service(executable_path=path)
driver = webdriver.Chrome(service=driver_service, options=options)
driver.get(web)

# Wait for containers to be present
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//div[@class="teaser__copy-container"]'))
)

# Find all containers
containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []

# Loop through each container to extract titles, subtitles, and links
for container in containers:
    try:
        title = container.find_element(by='xpath', value='./a/h3').text
    except Exception as e:
        title = 'No title found'
    
    try:
        subtitle = container.find_element(by='xpath', value='./a/p').text
    except Exception as e:
        subtitle = 'No subtitle found'
    
    try:
        link = container.find_element(by='xpath', value='./a').get_attribute('href')
    except Exception as e:
        link = 'No link found'
    
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

# Save to DataFrame
my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)

# Save DataFrame to CSV
df_headlines.to_csv('headline-headless.csv', index=False)

driver.quit()
