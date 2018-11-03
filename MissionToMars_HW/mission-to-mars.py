#import dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests

def scrape():
    mars_dict = {}
    # Article Title and Paragraph
    #assign url to be scraped to a variable
    mars_url = "https://mars.nasa.gov/news/"

    #scrape using splinter
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    browser.visit(mars_url)

    html = browser.html
    soup = bs(html, 'html.parser')

    news_title = soup.find_all('div', class_ = 'content_title')[0].text
    news_p = soup.find_all('div', class_="article_teaser_body")[0].text

    mars_dict['news_title'] = news_title
    mars_dict['news_p'] = news_p

    # JPL Featured Image
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_url)

    html = browser.html
    soup = bs(html, 'html.parser')

    browser.click_link_by_partial_text('FULL IMAGE')
    browser.click_link_by_partial_text('more info')

    html = browser.html
    soup = bs(html, 'html.parser')
    img = soup.find_all(class_='lede')[0].img['src']
    base_url = 'https://www.jpl.nasa.gov/'
    featured_img_url = base_url + img

    print(featured_img_url)

    mars_dict['featured_img_url'] = featured_img_url

    # Mars Weather Tweet Text

    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    tweet_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(tweet_url)

    html = browser.html
    soup = bs(html, 'html.parser')
    tweets = soup.find_all(class_="tweet-text")

    for tweet in tweets:
        if 'Sol' in tweet.text:
            twitter_text = tweet.text
            print(twitter_text)
            break

    mars_dict['twitter_text'] = twitter_text

    # ## Mars Facts Table 

    facts_url = "http://space-facts.com/mars/"
    facts_table = pd.read_html(facts_url)

    facts_df = facts_table[0]

    facts_html = facts_df.to_html('mars_facts.html')

    mars_dict['facts_table'] = facts_html

    # Mars Hemispheres

    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    all_links = soup.find_all('a')
    for link in all_links:
        if 'enhanced.tif' in link['href']:
            print(link['href'])
            break

    base_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/'
    hemispheres = ['cerberus_enhanced', 'schiaparelli_enhanced', 'syrtis_major_enhanced', 'valles_marineris_enhanced']
    img_urls = []
    dict = {}
    for x in range(0,4):
        url = base_url + hemispheres[x]
        dict['title'] = hemispheres[x]
        browser.visit(url)
        html = browser.html
        soup = bs(html, 'html.parser')
        all_links = soup.find_all('a')
        for link in all_links:
            if 'enhanced.tif' in link['href']:
                dict['img_url'] = link['href']
                break

        img_urls.append(dict)
    print(img_urls)

    mars_dict['hemi_img_urls'] = img_urls

    return mars_dict