#!/usr/bin/env python
"""
Script to unflow people that are not following you.
"""

import twitter
import twyt.twitter
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

twyt_api = twyt.twitter.Twitter()
twyt_api.set_auth(options.username, options.password)

api.SetCache(None)
friends = []
page = 1
print "Getting freinds"
while True:
    f = api.GetFriends(page=page)
    if len(f) == 0:
        break
    friends.extend(f)
    print "Got %d freinds so far" % len(friends)
    page += 1

for friend in friends:
    if twyt_api.friendship_exists(friend.screen_name, options.username) == 'false':
        api.DestroyFriendship(friend.screen_name)
        print "No longer following %s" % friend.screen_name
    else:
        print "%s is following me so I am skipping them" % friend.screen_name
