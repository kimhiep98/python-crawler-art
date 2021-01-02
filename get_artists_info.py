import get_list_artists
import urllib.request
from datetime import datetime

from selenium import webdriver
import time
import os
url_test = 'https://www.wikiart.org/en/artists-by-art-movement/baroque/text-list'
chrome_path = os.getcwd() + '\\chromedriver_win32\\chromedriver.exe'


def get_artists_info(url, path):
    links_list_artist, dirName = get_list_artists.getListArtist(
        url, chrome_path)

    os.chdir(path)

    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option(
        "excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(
        options=options, executable_path=chrome_path)
    # links_list_artist = [
    #     'https://www.wikiart.org/en/hendrick-goltzius/all-works#!#filterName:high-resolution,resultType:text']
    for link_artist in links_list_artist:

        driver.get(link_artist)

        title_folder = driver.find_element_by_class_name("artist-href").text
        title_folder = title_folder[:len(title_folder) - 1]

        if (link_artist.find("high-resolution") > 0):
            title_folder_1 = title_folder + " high resoultion"

            # make subdir
            try:
                os.makedirs(title_folder_1)
                print("Directory ", title_folder_1 + "",  " Created ")
            except FileExistsError:
                print("Directory ", title_folder_1, " already exists")

            # change dirpath to subfolder
            os.chdir('./' + title_folder_1)

            # get high resolution links
            aResult = []
            f = open('list-articles.txt', 'w+')

            try:
                # get list link ul li
                ulTagIndiv = driver.find_element_by_xpath(
                    "//ul[@class='painting-list-text ng-scope']")
                aTagsInLi = ulTagIndiv.find_elements_by_css_selector("li a")
                for a in aTagsInLi:
                    temp = a.get_attribute('href')
                    aResult.append(temp)
                # retrievel to single art
                for link in aResult:
                    driver.get(link)
                    # get title image
                    title_image = driver.find_element_by_xpath(
                        "//meta[@property='og:title']").get_attribute('content')+'.jpg'
                    artist_info = driver.find_element_by_tag_name('article')
                    with open('list-articles.txt', 'a') as f:
                        f.write(artist_info.text + '\n' + '\n')
                        f.close()
                    # get link image
                    link_image = driver.find_element_by_xpath(
                        "//meta[@property='og:image']").get_attribute('content')
                    replace_link = link_image.find('!')
                    if(replace_link >= 0):
                        link_image = link_image[:replace_link]
                    # check file name
                    if os.path.exists(os.getcwd() + "/" + title_image):
                        now = datetime.now()
                        title_image = title_image + now
                    # save image
                    urllib.request.urlretrieve(
                        link_image, title_image)

            except:
                print("error get high resolution")

            # get image and info

        else:
            title_folder_1 = title_folder
            try:
                os.makedirs(title_folder_1)
                print("Directory ", title_folder_1 + "",  " Created ")
            except FileExistsError:
                print("Directory ", title_folder_1, " already exists")
            os.chdir('./' + title_folder_1)
            f = open('list-articles.txt', 'w+')
            aResult = []
            try:
                # get list link ul li
                ulTagIndiv = driver.find_element_by_xpath(
                    "//ul[@class='painting-list-text']")
                aTagsInLi = ulTagIndiv.find_elements_by_css_selector(
                    "li a")
                for a in aTagsInLi:
                    temp = a.get_attribute('href')
                    aResult.append(temp)
                # retrievel to single art
                for link in aResult:
                    driver.get(link)
                    # get title image
                    title_image = driver.find_element_by_xpath(
                        "//meta[@property='og:title']").get_attribute('content')+'.jpg'
                    artist_info = driver.find_element_by_tag_name(
                        'article')
                    with open('list-articles.txt', 'a') as f:
                        f.write(artist_info.text + '\n' + '\n')
                        f.close()
                    # get link image
                    link_image = driver.find_element_by_xpath(
                        "//meta[@property='og:image']").get_attribute('content')
                    replace_link = link_image.find('!')
                    if(replace_link >= 0):
                        link_image = link_image[:replace_link]
                    # check file name
                    if os.path.exists(os.getcwd() + "/" + title_image):
                        now = datetime.now()
                        title_image = title_image + now
                    # save image
                    urllib.request.urlretrieve(
                        link_image, title_image)
            except:
                print("get full error")

        # return folder parent
        os.chdir('..')


# get_artists_info(chrome_path)
