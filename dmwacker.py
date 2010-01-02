#!/usr/bin/env python
import twitter
import sys
from optparse import OptionParser


parser = OptionParser()
parser.add_option('-u', '--username', dest='username', help='Specify the username of the twitter account.')
parser.add_option('-p', '--password', dest='password', help='Specify the password of the twitter account.')

(options, args) = parser.parse_args()

if not options.username and not options.password:
    print("You need to specify a username name password.")
    sys.exit(1)

api = twitter.Api(username=options.username, password=options.password)
api.SetCache(None)

while True:
    msgs = api.GetDirectMessages()
    
    for msg in msgs:
        api.DestroyDirectMessage(msg.id)
        print("%s | %s" % (msg.sender_screen_name, msg.text))
    
    if len(msgs) == 0:
        break
