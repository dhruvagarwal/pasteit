import os,sys
import xerox
import requests	
import logging
import argparse

class MakeLink:

	def __init__(self):
		logging.addLevelName( logging.ERROR, "\033[1;41m%s\033[1;m" % logging.getLevelName(logging.ERROR)) # make it colorful
		logging.getLogger().name = ''       # remove root logger's name
		self.payload = {}
		self.payload["poster"] = os.popen("whoami").read()
		self.payload["syntax"] = "text"

		args = self.get_args()
		content = None
		syntax = None

		if args.file != None:
			content,syntax = self.get_data_from_file(args.file)
		else:
			content = sys.stdin.read()

		self.payload["content"] = content

		if syntax != None:
			self.payload["syntax"] = syntax

		if args.poster != None:
			self.payload["poster"] = args.poster

		if args.syntax != None:
			self.payload["syntax"] = args.syntax
			
		print self.payload
		res = requests.post('http://paste.ubuntu.com',data=self.payload)
		link=res.url
		print "link is " + link
		xerox.copy(link)
		print "It's copied to the clipboard !"


	def get_args(self):
		parser = argparse.ArgumentParser(description = 'Use this simple command to paste any data to pastebin using terminal and get the corresponding link.')
		parser.add_argument('--poster')
		parser.add_argument('--file','-f')
		parser.add_argument('--syntax','-s')
		return parser.parse_args()
	
	def check(self,file_path):
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

	def get_data_from_file(self,file_path):
		file_path = self.check(file_path)

		syntax = None
		f=open(file_path,"r").read()
		content = f
		extension = file_path.split('.')[-1]
		lang = { "c":"c","cpp" : "cpp","java" :"java","php"  :"php","py":"python","css"  :"css","sh" : "bash","cs"  :"csharp","html" :"html","js" :"js","m" :"matlab","go" : "go","pl" : "perl","rb" :"ruby"}
		if extension in lang:
			syntax=[lang[extension],]

		return content,syntax

MakeLink()
