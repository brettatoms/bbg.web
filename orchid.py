#!/usr/local/bin/python
#
# ** This script must be Python 2.4 compatible to run on Lunarpages
# ** servers
#
#
import cgi
import os
import sys
import urllib2
import urllib

import json

print "Content-Type: text/html\n\n"

base_url = 'http://belizebotanic.org/gallery/index.php/rest/'
api_key = open(os.path.join(os.getcwd(), 'gallery_api.key')).read()

form = cgi.FieldStorage()
# the name param should be the gallery tag id
tag_id = form.getfirst("name", "").upper()    # get first name param
#tag_id = '3' # for testing
if not tag_id:
    print '<p>No name passed</p>'
    sys.exit(1)

def get_gallery_url(url):
    request = urllib2.Request(url)
    request.add_header('X-Gallery-Request-Key', api_key)
    request.add_header('X-Gallery-Request-Method', 'get')
    return urllib2.urlopen(request)

try:
    response = get_gallery_url(base_url + 'tag/%s' % tag_id)
    data = response.read()
except Exception, e:
    print e
    sys.exit(1)


for member in json.read(data)['relationships']['items']['members']:
    # get members items of tag
    response = get_gallery_url(member)
    item = json.read(response.read())['entity']['item']

    # get individual items
    response = get_gallery_url(item)
    entity = json.read(response.read())['entity']
    url = entity['file_url_public']
    thumb_url = entity['thumb_url_public']
    print '<a href="%(url)s"><img src="%(thumb_url)s"/></a>' % \
        { 'url': url, 'thumb_url': thumb_url },
