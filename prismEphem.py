#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import datetime
import urllib2
import chardet
import re
import ephem


def six2ten(six):
    ten = six.split(':')
    t0 = float(ten[0])
    t1 = float(ten[1])*0.0166666666667
    t2 = float(ten[2])*0.000277777777778
    if t0>=0:
        return t0 + t1 + t2
    if t0<0:
        return t0 - t1 - t2
    
#fetch NORAD site
url = 'http://celestrak.com/NORAD/elements/amateur.txt'
htmlOpener = urllib2.urlopen(url)
if(htmlOpener.code != 200): exit(0)
src = htmlOpener.read().splitlines()
count = 0
for line in src:
    if line.find('PRISM    ') != -1:
        line1 = str(count)
        line2 = src[count+1] 
        line3 = src[count+2]       
        print line1,line2,line3
    count+=1

#ephem convert
iss = ephem.readtle(line1, line2, line3)
iss.compute('2011/10/14 10:01')

sublong = six2ten(str(iss.sublong))
sublat = six2ten(str(iss.sublat))
elevation = iss.elevation

print sublong
print sublat
print elevation
