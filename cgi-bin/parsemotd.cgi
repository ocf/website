#!/usr/bin/env python
from __future__ import print_function
from autolink import linkify

print("Content-Type: text/html\n\n")

motdfile = open('/home/s/st/staff/motd/motd')
lines = motdfile.readlines()[7:]

if lines:
    print('<h2><a href="http://status.ocf.berkeley.edu/">Recent notices</a></h2>')
    print('<pre class="motd">')
    for line in lines:
            print(linkify(line[:-1]))
    print('</pre>')
