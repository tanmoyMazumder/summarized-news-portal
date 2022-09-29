from newspaper import Article
import save_news, time
# create an article object
def scrape(l, topic):
    time.sleep(5)
    print(f'link------>{l}\ntype:{type(l)}')
    # link = 'https://www.thedailystar.net/' + link 
    # print(f'link------>{link}\ntype:{type(link)}')
    
    article = Article(l)
    article.download()
    article.parse()
    title = article.title
    link = article.url
    authors = article.authors
    date = article.publish_date
    text = article.text
    
    
    news = {
        'link' : link,
        'title': title,
        'author':authors,
        'date' : str(date),
        'news_text': text
    }
    
    save_news.save(news, topic)
    
#scrape('https://www.thedailystar.net/middle-east/news/aminis-death-tragic-incident-chaos-unacceptable-iranian-president-3130881')