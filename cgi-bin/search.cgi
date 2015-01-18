#!/usr/bin/perl

use URI::Escape::XS qw/uri_escape/;
use CGI;

# make CGI object
$cgi = new CGI;

# get input data
$site  = $cgi->param(site);
$query = $cgi->param(query);

# url encode search query
$esc_query = uri_escape($query);

# construct new url
if ( $site eq "www" ) {
    $newloc =
      "http:\/\/www.googlesyndicatedsearch.com\/u\/ocf?q=$esc_query&sa=Search";
}
elsif ( $site eq "wiki" ) {
    $newloc =
"http:\/\/docs.ocf.berkeley.edu\/wiki\/Special:Search?search=$esc_query&go=Go";
}
else {
    $newloc = "http:\/\/www.ocf.berkeley.edu";
}

#print new location header
print "Location: $newloc\n\n";
