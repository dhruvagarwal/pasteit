pasteit
==================

**pasteit** lets you paste your text to [pastebin](http://pastebin.ubuntu.com/) directly through the terminal. Change the directory to the directory where your code is stored.

The link is automatically copied to your clipboard.So just run this script and you are free to paste the link anywhere right away.

Installation:
-------------

Use pip to install pasteit (will be available soon)

```
pip install pasteit
```

**Alternate installation**

You can also compile from source, just clone the repo and run the command below:

```
python setup.py install
```
        
Usage:
----------

To get started, start with help:

```
➜  ~  pasteit --help
Usage: pasteit [OPTIONS]

Options:
  -p, --poster TEXT  Name of user who is posting content
  -f, --file TEXT    Path to file
  --help             Show this message and exit.
```

To create a pastebin link for a file :

```
➜  ~  pasteit -f path/to/file.ext
link is http://paste.ubuntu.com/01010100/
It's copied to the clipboard !
```

Developed By:
--------------
*  Dhruv Agarwal

Contributor:
--------------
*  Padmakar Ojha ([dvopsway](https://github.com/dvopsway))
