#!/usr/local/bin/python
print 'Status: 503'
print 'Content-Type: text/html'
print 'Retry-After: Mon, 26 Sep 2011 23:59:59 GMT'
print

print '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2//EN">'
print '<html>'
print '<head>'
print '<title>503 - Service temporarily unavailable</title>'
print '</head>'
print '<body>'
print '<h1>503 - OCF service unavailable</h1>'
print '<p>Web hosting for non-<a href="http://docs.ocf.berkeley.edu/wiki/Virtual_hosting">virtual hosts</a> is currently unavailable.</p>'
#print '<p>We are doing our best by working overnight so that service will be restored as soon as possible. We apologize for the inconvenience.</p>'
print '<p>We will post updates on <a href="http://status.ocf.berkeley.edu/2012/01/web-server-downtime.html">our blog</a>.</p>'
print '</body>'
print '</html>'
