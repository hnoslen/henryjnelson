import urllib
import datetime
import time
import basepage
import webapp2
from google.appengine.ext import ndb
from google.appengine.api import mail

sender = "nehn.001@gmail.com"
toperson = "nehn.001@gmail.com"

def get_file(name):
    out =''
    try:
        f = open(name,'r')
        out = f.read()
        f.close()
    finally:
        return out
#class Comment(ndb.Model):
#    page = ndb.StringProperty()
#    text = ndb.TextProperty()
#    time = ndb.DateTimeProperty(auto_now_add=True)
#    votes = ndb.IntegerProperty()
def message(mess):
    return basepage.base+mess+"</body></html>"
class Contact(webapp2.RequestHandler):
    def get(self):
        p = basepage.base+"""<form action="/contact" method="POST" id="contact_form">
Please only contact me by this method if there is no other method available. Also, please don't spam it. That's just mean.<br><br>
<h2>Contact Form</h2>
From: (how will I know how to get back to you)<br>
<input type="text" name="from" size="50" autofocus="autofocus"><br><br>
Message:<br>
<textarea name="message" form="contact_form" rows="10" cols="100"></textarea><br>
<input type="submit" value="Submit">
</form>
If you get redirected to the homepage, it worked.

</body>
</html>"""
        self.response.write(p)
    def post(self):
            subject = self.request.get("from")
            body = self.request.get("message")
            mail.send_mail(sender, toperson, subject, body)
            self.response.write(message("Thanks. Hopefully I'll get back to you within a few days."))

class index(webapp2.RequestHandler):
    def get(self):
        self.response.write(get_file("index.html"))
class physics(webapp2.RequestHandler):
    def get(self):
        self.response.write(get_file("physics.html"))
class mathcs(webapp2.RequestHandler):
    def get(self):
        self.response.write(get_file("mathcs.html"))
class about(webapp2.RequestHandler):
    def get(self):
        self.response.write(get_file("about.html"))
class philo(webapp2.RequestHandler):
    def get(self):
        self.response.write(get_file("philo.html"))
class movies(webapp2.RequestHandler):
    def get(self):
        self.response.write(get_file("movies.html"))
class prof(webapp2.RequestHandler):
    def get(self):
        self.response.write(get_file("prof.html"))
app = webapp2.WSGIApplication([
    ('/', index),
    ('/physics', physics),
    ('/philo', philo),
    ('/movies', movies),
    ('/prof', prof),
    ('/mathcs', mathcs),
    ('/about', about),
    ('/contact', Contact),
    ], debug=True)
