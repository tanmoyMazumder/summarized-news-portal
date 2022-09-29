import  time, link_scraper, news_scraper

delay = 21600 #in seconds

sports_page = 'https://www.thedailystar.net/sports'
entertainment_page = 'https://www.thedailystar.net/entertainment'
bd_top_page = 'https://www.thedailystar.net/news/bangladesh'
pages = [bd_top_page,entertainment_page,sports_page]

while True:
    for i in range(3):
        link_scraper.scrape(pages[i], topic=i)

    time.sleep(delay)