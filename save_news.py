# import json
# , datetime
import mysql.connector
def save(news, topic):
    # current_time = str(datetime.datetime.now())
    # print(type(current_time))
    # save_dict = {
    #     # 'save_time': current_time,
    #     'topic': topic,
    #     'news' : news
    # }
    
    # json_savedict = json.dumps(save_dict)
    # with open('json_data.json', 'a') as outfile:
    #     json.dump(json_savedict, outfile)


    mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="Test@12345",
    database="sqlfile/newsportal"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO tblposts ( postTitle, categoryID, postDetails, postUrl, postImage  ) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
