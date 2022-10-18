from newspaper import Article
import save_news, time
# create an article object
def scrape(l, topic='bleh'):
    time.sleep(5)
    print(f'link------>{l}\ntype:{type(l)}')
    # link = 'https://www.thedailystar.net/' + link 
    # print(f'link------>{link}\ntype:{type(link)}')
    
    article = Article(l)
    article.download()
    article.parse()
    article.nlp()
    
    title = article.title
    link = article.url
    authors = article.authors
    date = article.publish_date
    text = article.text
    summary = article.summary
    print(text)
    print('***************\n')
    
    news = {
        'link' : link,
        'title': title,
        'author':authors,
        'date' : str(date),
        'news_text': text,
        'summary': summary
    }
    
    save_news.save(news, topic)
    print(news)
#scrape('https://bdnews24.com/technology/orzx622swg')