from newspaper import Article
import save_news, time
import nltk
# create an article object
def scrape(l, topic='bleh'):
    nltk.download('punkt')
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
    print("==================================================================================")
    print("==================================================================================")
    print("==================================================================================\nLINK AND ACTUAL NEWS:")
    print(link)
    print(text)
    print('***********************************************************************************\nSUMMARY:')
    print(summary)
    
    news = {
        'link' : link,
        'title': title,
        'author':authors,
        'date' : str(date),
        'news_text': text,
        'summary' : summary
    }
    
    save_news.save(news, topic)
    #print(news)
scrape('https://www.bbc.com/sport/rugby-union/63309190')