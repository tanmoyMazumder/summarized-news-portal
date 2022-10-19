import requests # request img from web
import shutil # save img locally
import re
# url = input('Please enter an image URL (string):') #prompt user for img url
file_name = ''#input('Save image as (string):') #prompt user for file_name
def save_img(url):
    file_name = ''
    for i in url:
        if i != '/':
            file_name += i
    file_name = file_name.replace(":",'')
    print(f"file name: {file_name}")
    res = requests.get(url, stream = True)

    if res.status_code == 200:
        with open(file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ',file_name)
    else:
        print('Image Couldn\'t be retrieved')

save_img('https://www.daily-sun.com/assets/news_images/2022/10/18/Love.jpg')