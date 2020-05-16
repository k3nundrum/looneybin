import argparse, os, time
import urlparse, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import sys
print sys.path

def getPeopleLinks(page):
	links = []
	for link in page.find_all('a'):
		url = link.get('href')
		if url:
			if 'profile/view?id=' in url:
				links.append(url)
	return links

def getJobLinks(page):
	links = []
	for link in page.find_all('a'):
		url = link.get('href')
		if url:
			if '/jobs' in url:
				links.append(url)
	return links

def getID(url):
	pUrl = urlparse.urlparse(url)
	return urlparse.parse_qs(pUrl.query)['id'][0]


def ViewBot(browser):
	visted = {}
	pList = []
	count = 0
	while True:
		#sleep to make sure that all the javascript loads and whatnot.
		#add random to make us look legit.
		time.sleep(random.uniform(3.5, 6.9))
		page = BeautifulSoup(browser.page_source)
		people = getPeopleLinks(page)
		if people:
			for person in people:
				ID = getID(person)
				if ID not in visited:
					pList.append(person)
					visited[ID] = 1
		if pList: #If there is people to look at, then look at them
			person = pList.pop()
			browser.get(person)
			count += 1
		else: #Otherwise find people via the job pages
			jobs = getJobLinks(page)
			if jobs:
				job = random.choice(jobs)
				root = 'http://www.linkedin.com'
				roots = 'http://www.linkedin.com'
				if root not in job or roots not in job:
					job = 'http://www.linkedin.com' + job
				browser.get(job)
			else:
				print "I'm Lost...Exiting"
				break
		#Output make option for this
		print "[+] " + browser.title+" Visted! \n("\
			+str(count)+"/"+str(len(pList))+") Visited/Queue"



def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument("email", help="linkedin email")
	parser.add_argument("password", help="linkedin password")
	args = parser.parse_args()
	
	browser = webdriver.Firefox()
	browser.get("https://linkedin.com/uas/login")

	emailElement = browser.find_element_by_id("username")
	emailElement.send_keys(args.email)
	passElement = browser.find_element_by_id("password")
	passElement.send_keys(args.password)
	passElement.submit()

	os.system('clear')
	print "[+] Success!!! Logged In....Bot Starting!"
	ViewBot(browser)
	browser.close()

if __name__ == '__main__':
	Main()
