import requests
import bs4
#pip install webdriver-manager
#sudo apt install firefox-geckodriver
#which geckodriver
# https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path
def get_anekdot():
    from selenium import webdriver
    url = 'https://www.chosic.com/random-songs-generator-with-links-to-spotify-and-youtube/'

    # EXE_PATH = "chromedriver.exe"  # EXE_PATH это путь до ранее загруженного нами файла chromedriver.exe


    # driver = webdriver.Firefox(executable_path=r"geckodriver\geckodriver.exe")
    driver = webdriver.Chrome(executable_path=r"webdrivers\chromedriver.exe")
    driver.get(url)
    element = driver.find_element_by_id("generate")
    element.click()

    req_anek = requests.get(url)

    array_anekdots = []
    soup = bs4.BeautifulSoup(req_anek.text, "html.parser")
    result_find = soup.select('track-details')
    for result in result_find:
        array_anekdots.append(result.getText().strip())
    return array_anekdots[0]
    print(result_find)


print(get_anekdot())
