import cgi
import urllib
import datetime
import time

from google.appengine.ext import ndb

import webapp2

def get_file(name):
    out =''
    try:
        f = open(name,'r')
        out = f.read()
        f.close()
    finally:
        return out
class EntryStore(ndb.Model):
    text = ndb.TextProperty()
    time = ndb.DateTimeProperty(auto_now_add=True)
    votes = ndb.IntegerProperty()

class IntroPage(webapp2.RequestHandler):
    def get(self):
        entries = EntryStore.query().order(-EntryStore.time).fetch()
        messages = []
        head = get_file("ideas.html")
        # delete old entries
        for e in entries:
            messages.append(e)
        if (type(messages)!=type(None)):
            for e in messages:
                head= head+'<div style="background-color:maroon; color:black;"><p>Votes: '+str(e.votes)+'<br><a href="/ideas/voteUp?entry='+str(e.key.id())+'"'+'><img src="img/'
                current_vote = self.request.cookies.get(str(e.key.id()))
                if current_vote == 'up':
                    head = head+'thumbs-up-bw.png" alt="UpVoted"></a> <a href="/ideas/voteDown?entry='+str(e.key.id())+'"'+'><img src="img/thumbs-down.png" alt="DownVote">'
                elif current_vote == 'down':
                    head = head+'thumbs-up.png" alt="UpVote"></a> <a href="/ideas/voteDown?entry='+str(e.key.id())+'"'+'><img src="img/thumbs-down-bw.png" alt="DownVoted">'
                else:
                    head = head+'thumbs-up.png" alt="UpVote"></a> <a href="/ideas/voteDown?entry='+str(e.key.id())+'"'+'><img src="img/thumbs-down.png" alt="DownVote">'
                head = head+'</a> <a href="/ideas/removeOne?entry='+str(e.key.id())+'"'+'><img src="img/flag.png" alt="Flag"></a>  '+e.text+'</p></div>'
        self.response.write(head+"""</body></html>""")

    def post(self):
        newentry = self.request.get('newentry')
        if newentry!='':
            newdata = EntryStore(text=newentry, votes=0)
            newdata.put()
            time.sleep(0.5)
            self.redirect('/ideas')
        else:
            self.redirect('/ideas')

class removeOne(webapp2.RequestHandler):
    def get(self):
        entry = self.request.get('entry')
        newdata = EntryStore.get_by_id(int(entry))
        newdata.key.delete()
        time.sleep(0.5)
        self.redirect('/ideas')
class upVote(webapp2.RequestHandler):
    def get(self):
        entry = self.request.get('entry')
        current_vote = self.request.cookies.get(entry)
        newdata = EntryStore.get_by_id(int(entry))
        if current_vote == 'up':
            newdata.votes = newdata.votes-1
            newdata.put()
            self.response.set_cookie(entry, '-')
        elif current_vote == 'down':
            newdata.votes = newdata.votes+2
            newdata.put()
            self.response.set_cookie(entry, 'up')
        else:
            newdata.votes = newdata.votes+1
            newdata.put()
            self.response.set_cookie(entry, 'up')
        time.sleep(0.5)
        self.redirect('/ideas')
class downVote(webapp2.RequestHandler):
    def get(self):
        entry = self.request.get('entry')
        current_vote = self.request.cookies.get(entry)
        newdata = EntryStore.get_by_id(int(entry))
        if current_vote == 'down':
            newdata.votes = newdata.votes+1
            newdata.put()
            self.response.set_cookie(entry, '-')
        elif current_vote == 'up':
            newdata.votes = newdata.votes-2
            newdata.put()
            self.response.set_cookie(entry, 'down')
        else:
            newdata.votes = newdata.votes-1
            newdata.put()
            self.response.set_cookie(entry, 'down')
        time.sleep(0.5)
        self.redirect('/ideas')

app = webapp2.WSGIApplication([
    ('/ideas', IntroPage),
    ('/ideas/removeOne', removeOne),
    ('/ideas/voteUp', upVote),
    ('/ideas/voteDown', downVote),
    ], debug=True)
