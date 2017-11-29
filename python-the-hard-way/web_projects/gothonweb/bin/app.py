# -*- coding: utf-8 -*-

import web

urls = (
	'/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
	def GET(self):
		greeting = "Hallo World"
		return render.index(greeting = greeting)

if __name__ == "__main__":
	app.run()

"""
# 1 a Simple "Hallo World" Project

1.  my browser ---> my own computer called **localhost**
2.  browser makes an HTTP request to the bin/app.py
    ask for the '/' URL
3.  in bin/app.py, we've got a list of URLs and what classes
    they match.
    The only one we have is '/', 'index' mapping.
    也就是说 app 匹配 URL 为 index, 让咱 调用 class index
    This means that whenever someone goes to / with a browser, 
    lpthw.web will find the class index and load it to handle 
    the request.
4.	Now the lpthw.web has found class index it calls the index.GET
	method on an instance of that class to actually hanle the 
	request. This function runs and simply returns a string for
	what lpthw.web should send to the brower.
5. 	Finally, lpthw.web has handled the request and sends this respon-
	se to the browser, which is what we are seeing.

- my brower --> localhost (uses port 8080)
- my brower makes an HTTP request to --> bin/app.py
- app.run() 
	- [lpthw.web]
		- web.application(urls, globals())
		- urls --> '/' --> 'index'
		- find class index
		- act index.GET method and return greeting strings
		- lpthw.web send to the brower
		- so lpthw.web has handled the request 

# 2 Create Basic Templates

1. a new variale render : is a web.template.render object
2. render object knows how to load .html files in templates/ directory
3. **index.GET** we call render.index and pass the greeting to index.html as a variable.

"""