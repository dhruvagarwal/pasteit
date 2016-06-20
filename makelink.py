import os,sys
import xerox
import requests	
import logging
global path
logging.addLevelName( logging.ERROR, "\033[1;41m%s\033[1;m" % logging.getLevelName(logging.ERROR)) # make it colorful
logging.getLogger().name = ''       # remove root logger's name
def check(file_path):
	if os.path.exists(file_path):
		return
	if file_path is not '':
		logging.error("Enter valid path,relative to current directory.")
		print "Make sure you provide correct file extension"
		print "e.g - /home/user/xyz.py or file_name.c"
		global path
	try:
		path=raw_input('Enter File name with path - ').strip()
		check(path)
	except:
		sys.exit()

try:
	path=sys.argv[1:][0].strip()	# to retrieve path from command line arguments
	check(path)
except:
	check('')						# if a user forgets to enter path in command line

s=open(path,"r").read()
extension = os.path.splitext(path)[1][1:]
payload = {}
lang = { "c":"c","cpp" : "cpp","java" :"java","php"  :"php","py":"python","css"  :"css","sh" : "bash","cs"  :"csharp","html" :"html","js" :"js","m" :"matlab","go" : "go","pl" : "perl","rb" :"ruby"}
if extension in lang:
	payload["syntax"]=[lang[extension],]
	payload["poster"]=os.popen("whoami").read()
	payload["content"]=s

res = requests.post('http://paste.ubuntu.com',data=payload)

link=res.url
print "link is " + link
xerox.copy(link)
print "It's copied to the clipboard !"
