from bs4 import BeautifulSoup
import requests, csv, news_scraper, time
from newspaper import Article
import save_news
delay = 10
# create an article object
# def nscrape(link, topic):
#     print(f'link------>{link}\ntype:{type(link)}')
#     # link = 'https://www.thedailystar.net/' + link 
#     # print(f'link------>{link}\ntype:{type(link)}')
    
#     article = Article(link)
#     article.download()
#     article.parse()
#     title = article.title
#     link = article.url
#     authors = article.authors
#     date = article.publish_date
#     text = article.text
    
    
#     news = {
#         'link' : link,
#         'title': title,
#         'author':authors,
#         'date' : str(date),
#         'news_text': text
#     }
    
#     save_news.save(news, topic)

def scrape(page_link, topic):
    source = requests.get(page_link).text
    soup = BeautifulSoup(source, 'lxml')

    if soup:
        print('page paisi')# print(soup)
        
        #REMINDER
        #GOTTA FIND SOME OTHER FILE FORMAT TO SAVE TO, CSV WOULD CREATE PROBLEMS
        
    # csv_file = open("scraped.csv", "w",  encoding="utf-8")
    # csvWriter = csv.writer(csv_file)

    #All = [["name","time"]]
    link_list = []
    #link_list_iterator = 0
    

    #print(soup.body.div[3].div.div.div[2].main.div.div[2].div.div[3].div.div.div.div[3].div.div[2].h3.a)
    for link in soup.find_all('a'):#collecting the links
        if link.parent.name == 'h3':
            #print(link["href"])################################# bug here
            link_list.append('https://www.thedailystar.net' +link["href"])
    
    #print(f'the list {link_list}')
    topics = {
        0: 'bd',
        1: 'entertainment',
        2: 'sports'
    }
    # for i in range(5):
    #     print(link_list[i])
    
    for i in range(5):
        news_scraper.scrape(link_list[i], topics[topic])
        # l = link_list[i]
        # print(f'l is:',l)
        # article = Article(link_list[i])
        # article.download()
        # article.parse()
        # title = article.title
        # link = article.url
        # authors = article.authors
        # date = article.publish_date
        # text = article.text
        
        
        # news = {
        #     'link' : link,
        #     'title': title,
        #     'author':authors,
        #     'date' : str(date),
        #     'news_text': text
        # }
        
        # save_news.save(news, topic[topic])
        #news_scraper.scrape('https://www.thedailystar.net/news/bangladesh/news/give-them-the-wage-they-deserve-3130696')
        time.sleep(delay)



page_link = 'https://www.thedailystar.net/sports'  #actual link
scrape(page_link, 2)