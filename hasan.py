from bs4 import BeautifulSoup
import urllib
import requests
import wget
import shutil
import os.path
site="http://nitdgp.ac.in/Student_Notice_Board.php"
page = urllib.urlopen(site)
soup=BeautifulSoup(page,'lxml')
#print soup.title.text
list_of_notice=[]
links=soup.find_all("a")
list_of_all_names_of_pdf=[]
start='http://nitdgp.ac.in/'
save_path = '/home/Student_Notice_Board/'
for link in links:
	url=link.get("href")
	length=len(url)
	if(url[length-1]=='f'):
		name_of_file=link.text
		completeName = os.path.join(save_path, name_of_file) 
		list_of_all_names_of_pdf.append(url)
		#wget.download(start+url)

for names in list_of_all_names_of_pdf:
	print names
	s2='/home/hasan/'
	#src=s2+names
	#dest=s2+'Student_Notice_Board'+names
	#shutil.move(src,dest)			
		




