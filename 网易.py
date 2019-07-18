import os
import json
import requests
from urllib import request

url = "https://3g.163.com/touch/api/pagedata/index_yaowen?callback=allTopicList"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}
page_text = requests.get(url=url,headers=headers).text
page_text = page_text.replace('allTopicList(','').replace(')','')
json_obj = json.loads(page_text)
data_list = json_obj['data']
if not os.path.exists('./picture'):
    os.mkdir('./picture')
with open('./头条.csv', 'w',encoding='utf8')as f:
    for data in data_list:
        for da in data_list[data]:
            title = ''
            img_url = ''
            if da['title']:
                title = da['title']
            if da['picInfo']:
                img_url = da['picInfo'][0]['url']
                img_name = img_url.split('/')[-1]
                img_path = './picture/'+ img_name
                img = request.urlretrieve(img_url,img_path)
            f.write(title+","+img_url+'\n')


