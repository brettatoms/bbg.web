#!/usr/local/bin/python
#
# Requirements: pylibgal3
#
import os
import re
import sys
import urllib2
import urllib

import libg3

hostname = 'belizebotanic.org'
gallery_base = '/gallery'
api_key = open(os.path.join(os.getcwd(), 'gallery_api.key')).read()
album_name = 'orchids640x480'

gal = libg3.Gallery3(hostname , api_key , g3Base=gallery_base)
root = gal.getRoot()
orchid_album = filter(lambda a: a.title == album_name, root.getAlbums())[0]

rx = re.compile('(?P<genus>\w*)\s(?P<sp>\w*)(?:\s(?P<rank>\w*)\s(?P<infrasp>\w*))?(?:-\w)?')
titles = []

for image in orchid_album.getImages():
    groups = rx.match(image.title).groupdict()
    if groups['rank'] is None:
        s = '%(genus)s %(sp)s' % groups
        tag = s.capitalize()
    else:
        s = '%(genus)s %(sp)s %(rank)s. %(infrasp)s' % groups
        tag = s.capitalize()
    tags = [t.name for t in image.tags]
    if tag not in tags:
        print 'adding %s to %s' % (tag, image.title)
        image.tag(tag)
