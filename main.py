import  time, link_scraper, news_scraper

delay = 21600 #in seconds

sports_page =['https://www.thedailystar.net/sports', 'https://www.daily-sun.com/online/sports', 'https://www.bbc.com/sport'] 
entertainment_page =['https://www.thedailystar.net/entertainment', 'https://www.daily-sun.com/online/entertainment', 'https://www.bbc.com/culture'] 
bd_top_page = ['https://www.thedailystar.net/news/bangladesh','https://www.daily-sun.com/online/national' ,'https://www.bbc.com/news/world']
pages = [bd_top_page,entertainment_page,sports_page]

while True:
    for i in range(3):
        link_scraper.scrape(pages[i], topic=i)

    time.sleep(delay)