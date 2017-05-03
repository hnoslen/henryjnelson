import urllib
import datetime
import time
import webapp2
from google.appengine.ext import ndb
from google.appengine.api import mail

def get_file(name):
    out ='Something went wrong, Sorry!'
    try:
        f = open(name,'r')
        out = f.read()
        f.close()
    finally:
        return out

basepage = get_file("basepage.html")
#class Comment(ndb.Model):
#    page = ndb.StringProperty()
#    text = ndb.TextProperty()
#    time = ndb.DateTimeProperty(auto_now_add=True)
#    votes = ndb.IntegerProperty()
def message(mess):
    return basepage+mess+"</body></html>"
#class Contact(webapp2.RequestHandler):
#    def get(self):
#        p = basepage+"""<h2>Contact Form</h2>
#<form action="/contact" method="POST" id="contact_form">
#Please only contact me by this method if there is no other method available. Also, please don't spam it. That's just mean.<br><br>
#From: (Name)<br>
#<input type="text" name="from" size="50" autofocus="autofocus"><br><br>
#Your Contact address (email):<br>
#<input type="text" name="email" size="50"><br><br>
#What are you trying to contact me about (100 characters): <br>
#<input type="text" name="message" size="100"><br>
#<input type="submit" value="Submit">
#</form>
#</html>"""
#        self.response.write(p)
#    def post(self):
#            subject = self.request.get("from")+" from HenryJNelson contact form"
#            body = "The following was submitted to the contact form at HenryJNelson.com/contact:\n\n"+self.request.get("message")
#            try:
#            	mail.send_mail(sender, toperson, subject, body)
#            	self.response.write(message("Thanks. Hopefully I'll get back to you within a few days."))
#            except:
#            	self.response.write(message("I'm sorry. There was a problem sending your message. Please try again."))
class index(webapp2.RequestHandler):
    def get(self):
        self.response.write(get_file("index.html"))
#class physics(webapp2.RequestHandler):
#    def get(self):
#        self.response.write(get_file("physics.html"))
#class mathcs(webapp2.RequestHandler):
#    def get(self):
#        self.response.write(get_file("mathcs.html"))
class about(webapp2.RequestHandler):
    def get(self):
        self.response.write(get_file("about.html"))
#class philo(webapp2.RequestHandler):
#    def get(self):
#        self.response.write(get_file("philo.html"))
#class movies(webapp2.RequestHandler):
#    def get(self):
#        self.response.write(get_file("movies.html"))
class prof(webapp2.RequestHandler):
    def get(self):
        self.response.write(get_file("prof.html"))
class pubs(webapp2.RequestHandler):
    def get(self):
        self.response.write(get_file("pubs.html"))
app = webapp2.WSGIApplication([
    ('/', index),
    ('/prof', prof),
    ('/pubs', pubs),
    ('/about', about),
    ], debug=True)
