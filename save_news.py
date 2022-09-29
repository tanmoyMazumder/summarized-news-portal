import json
# , datetime

def save(news, topic):
    # current_time = str(datetime.datetime.now())
    # print(type(current_time))
    save_dict = {
        # 'save_time': current_time,
        'topic': topic,
        'news' : news
    }
    
    json_savedict = json.dumps(save_dict)
    with open('json_data.json', 'a') as outfile:
        json.dump(json_savedict, outfile)
