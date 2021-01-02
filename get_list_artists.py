from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import os


def getListArtist(url, path_chromedriver):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(
        options=options, executable_path=path_chromedriver)
    driver.get(url)

    # make parent folder
    title_div = driver.find_element_by_xpath("//div[@class='title']")
    title = title_div.text
    index_replace = title.find("\n")
    title = title[:index_replace]
    dirName = './' + title

    try:
        os.makedirs(dirName)
        print("Directory ", dirName,  " Created ")
    except FileExistsError:
        print("Directory ", dirName, " already exists")

    # while True:
    #     try:
    #         driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 5).until(
    #             EC.visibility_of_element_located((By.XPATH, "//a[@class='masonry-load-more-button']"))))
    #         WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    #             (By.XPATH, "//a[@class='masonry-load-more-button']"))).click()
    #         print("LOAD MORE RESULTS button clicked")
    #     except:
    #         print("No more LOAD MORE RESULTS button to be clicked")
    #         break
    ulTagIndiv = driver.find_element_by_xpath(
        "//div[@class='masonry-text-view masonry-text-view-all']")
    aTagsInLi = ulTagIndiv.find_elements_by_css_selector("li a")
    aResult = []
    for a in aTagsInLi:
        temp = a.get_attribute('href')
        aResult.append(
            temp + '/all-works#!#filterName:high-resolution,resultType:text')
        aResult.append(
            temp + '/all-works/text-list')

    with open('list_author.txt', 'w') as f:
        for item in aResult:
            f.write("%s\n" % item)

    driver.close()

    return aResult, dirName
