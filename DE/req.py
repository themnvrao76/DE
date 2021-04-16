
import requests
from pprint import pprint


data=requests.get("https://www.googleapis.com/books/v1/volumes?q=machine learning:keyes&key=AIzaSyB_j2rH8EflxsWIqnak3Jq4qZfbSooypNo")
new=data.json()



mylist=[]
for i in range(5):
    mylist.append([{'title':new['items'][i]['volumeInfo']['title'],'author':new['items'][i]['volumeInfo']['authors'],'dis':new['items'][i]['volumeInfo']['description'],'img':new['items'][i]['volumeInfo']['imageLinks']["thumbnail"]}])
    
    
print(len(mylist))

