import os,sys
import xerox
import mechanize
import logging
br=mechanize.Browser()
br.set_handle_robots(False)
br.open('http://pastebin.ubuntu.com')
br.select_form(nr=0)
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
	path=raw_input('Enter File name with path - ').strip()
	check(path)

try:
	path=sys.argv[1:][0].strip()	# to retrieve path from command line arguments
except:
	check('')						# if a user forgets to enter path in command line

s=open(path,"r").read()
extension = os.path.splitext(path)[1][1:]
lang = { "c":"c","cpp" : "cpp","java" :"java","php"  :"php","py":"python","css"  :"css","sh" : "bash","cs"  :"csharp","html" :"html","js" :"js","m" :"matlab","go" : "go","pl" : "perl","rb" :"ruby"}
if extension in lang:
	br.form["syntax"]=[lang[extension],]
br.form["poster"]=os.popen("whoami").read()
br.form["content"]=s
br.submit()

l=[x for x in br.links()]
link="http://pastebin.ubuntu.com"+l[0].url[:len(l[0].url)-6]
print "link is " + link
xerox.copy(link)
print "It's copied to the clipboard !"
