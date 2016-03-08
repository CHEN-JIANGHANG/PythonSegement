# -*- coding: utf-8 -*-
#!/usr/bin/env python

# This example is an command line interactive example of accessing the LTP API
# by Python. It also shows how to perform specified type of analysis and ident-
# ify the output format as PLAIN.

import urllib, urllib2

def Analyze(text, pattern):
    uri_base = "http://api.ltp-cloud.com/analysis/?"

    data     = {
             "api_key" : "T5B8m263WV5FeewQwxWd5wIn1uhTsulcGPjgkf7D",
             "text"    : urllib.quote(text),
             "format"  : "json",
             "pattern" : pattern}

    params   = urllib.urlencode(data)
    url      = uri_base + params

    try:
        response = urllib2.urlopen(url)
        content  = response.read().strip()
        return content
    except urllib2.HTTPError, e:
        return "wrong"

