import os,sys
import xerox
import requests	
import logging
import argparse


def get_args():
	parser = argparse.ArgumentParser(description = 'Use this simple command to paste any data to pastebin using terminal and get the corresponding link.')
	parser.add_argument('--poster')
	parser.add_argument('--file','-f')
	parser.add_argument('--syntax','-s')
	return parser.parse_args()

def check(file_path):
	if os.path.exists(file_path):
		return file_path
	logging.error("Enter valid path,relative to current directory.")
	print "Make sure you provide correct file extension"
	print "e.g - /home/user/xyz.py or file_name.c"
	try:
		path=raw_input('Enter File name with path - ').strip()
		check(path)
	except:
		sys.exit()

def get_data_from_file(file_path):
	file_path = check(file_path)

	syntax = None
	f=open(file_path,"r").read()
	content = f
	extension = file_path.split('.')[-1]
	lang = { "c":"c","cpp" : "cpp","java" :"java","php"  :"php","py":"python","css"  :"css","sh" : "bash","cs"  :"csharp","html" :"html","js" :"js","m" :"matlab","go" : "go","pl" : "perl","rb" :"ruby"}
	if extension in lang:
		syntax=[lang[extension],]

	return content,syntax

logging.addLevelName( logging.ERROR, "\033[1;41m%s\033[1;m" % logging.getLevelName(logging.ERROR)) # make it colorful
logging.getLogger().name = ''       # remove root logger's name
payload = {}
payload["poster"] = os.popen("whoami").read()
payload["syntax"] = "text"

args = get_args()
content = None
syntax = None

if args.file != None:
	content,syntax = get_data_from_file(args.file)
else:
	content = sys.stdin.read()

payload["content"] = content

if syntax != None:
	payload["syntax"] = syntax

if args.poster != None:
	payload["poster"] = args.poster

if args.syntax != None:
	payload["syntax"] = args.syntax

print payload
	
res = requests.post('http://paste.ubuntu.com',data=payload)
link=res.url
print "link is " + link
xerox.copy(link)
print "It's copied to the clipboard !"

