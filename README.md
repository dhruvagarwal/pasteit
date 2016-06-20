pastebin_linkmaker
==================

Dependencies:
-------------
*  Python 2.7
*  Requests
*  xerox
*  xclip

These dependencies can be installed via `pip` or `apt-get`

        $ pip install requests
        $ pip install xerox
        $ apt-get install xclip
        
Usage:
----------

**pastebin_linkmaker** lets you paste your text to [pastebin](http://pastebin.ubuntu.com/) directly through the terminal. Change the directory to the directory where your code is stored. Then simply run

    $ python makelink.py (filename alongwith path)
    link is http://pastebin.ubuntu.com/(uniquecode)/
    It's copied to the clipboard !

<dl>
  <dt>enter file path - </dt>
  <dd>If you are located in the same folder as your code is then just type the name of the file along with extension. eg Main.java</dd>
  <dd>If you are located in say Documents folder then type /home/username/Documents/Main.java</dt>
</dl>

<b>The link is automatically copied to your clipboard.So just run this script and you are free to paste the link anywhere right away .</b>

Developed By:
--------------
*  Dhruv Agarwal
