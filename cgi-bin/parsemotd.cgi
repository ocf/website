#!/usr/bin/env python
from autolink import linkify

print "Content-Type: text/html\n\n";

motdfile = open('/home/s/st/staff/motd/motd')

motdtext = motdfile.readlines()

for line in motdtext[7:]:
	print linkify(line[:-1])
