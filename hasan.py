from bs4 import BeautifulSoup
import urllib
import requests
import wget
import shutil
import os.path
dir=raw_input("Enter the path of directory")
os.chdir(dir)
print 'Enter 1 to download all pdf'
print "Enter 2 to check new updates in Student board"
c=int(input("Enter a number")) 
site="http://nitdgp.ac.in/Student_Notice_Board.php"
page = urllib.urlopen(site)
soup=BeautifulSoup(page,'lxml')
#print soup.title.text
list_of_notice=[]
links=soup.find_all("a")
list_of_all_names_of_pdf=[]
start='http://nitdgp.ac.in/'
save_path = '/home/Student_Notice_Board/'
if(c==1):
	for link in links:
		url=link.get("href")
		length=len(url)
		if(url[length-1]=='f'):
			list_of_all_names_of_pdf.append(link.text)
			wget.download(start+url)

else:
	for link in links:
		url=link.get("href")
		length=len(url)
		if(url[length-1]=='f'):
			for names in list_of_all_names_of_pdf:
				if(link.text not in names):
					list_of_all_names_of_pdf.append(link.text)
					wget.download(start+url)
		




