import urllib2 
from bs4 import BeautifulSoup
import os

serial=["1","2","3","4","5"]
f = urllib2.urlopen('http://www.indianexpress.com/section/politics/799/')
html = f.read()
soup = BeautifulSoup(html,"html.parser")
divTag = soup.find_all("div",{"class":"section"}, limit=5)
os.chdir(r'/home/siddharth/Downloads/janta3/janta/media/news')
news_file = open('news','wb')
for i in range(0,5):
	temp = divTag[i].find("h3").string
	
	
	temp = temp.encode("utf-8")
	temp = temp.replace('\r', " ")
	news_file.write(temp)
	news_file.write('\n')
	temp = divTag[i].find("div" , {"class": "bylinedate"}).nextSibling.string
	temp = temp.encode("utf-8")
	temp = temp.replace('\r', " ")
	news_file.write(temp)		
	news_file.write('\n')
	try:
  		temp = divTag[i].find("img")['data-original']
  		
	except TypeError:
  		temp = "None"
	news_file.write(temp)
	news_file.write('\n')
	if not (temp == "None"):
		os.chdir(r'/home/siddharth/Downloads/janta3/janta/media/news')
		resp = urllib2.urlopen(temp)
		q = open('icon'+serial[i]+'.jpg', 'wb')
		q.write(resp.read())
		q.close()

		
		temp = temp.replace("t-images", "m-images")
		temp = temp.replace("T_Id", "M_Id")
		
		os.chdir(r'/home/siddharth/Downloads/janta3/janta/media/news')
		
		try:
			response = urllib2.urlopen(temp)
			file_name = "image"+ serial[i]+".jpg"
			t = open('image'+serial[i]+'.jpg', "wb")
			t.write(response.read())
			t.close()
		except urllib2.HTTPError, e:
			try:
				rem = "image"+serial[i]+".jpg"
				os.remove(rem)
			except OSError:
				pass

	news_file.write(temp)
	news_file.write('\n')

news_file.close()
f.close()