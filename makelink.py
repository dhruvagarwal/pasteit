import os,sys
import xerox
import mechanize

br=mechanize.Browser()
br.set_handle_robots(False)
br.open('http://pastebin.ubuntu.com')
br.select_form(nr=0)
path=sys.argv[1:][0]

# comment the above line if you do not want to use command line argument system
# and uncomment the next line
# path=raw_input('Enter File name with path - ')

s=open(path,"r").read()
br.form["poster"]=os.popen("whoami").read()
br.form["content"]=s
br.submit()

l=[x for x in br.links()]
link="http://pastebin.ubuntu.com"+l[0].url[:len(l[0].url)-6]
print "link is " + link
xerox.copy(link)
print "It's copied to the clipboard !"
