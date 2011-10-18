#!/usr/bin/python
# -*- coding:utf-8 -*-
import datetime
import pytz
import urllib2
import chardet
import re
import ephem


def readFile():
    lines = ['','','']
    #print 'file !!!'
    tleFile = open('tleData.txt', 'r') 
    lines = tleFile.readlines()
    fileLineNum = len(lines)
    for i in range(fileLineNum):
            lines[i] = lines[i]
    
    tleFile.close()
    return lines
    
def six2ten(six):
    ten = six.split(':')
    t0 = float(ten[0])
    t1 = float(ten[1])*0.0166666666667
    t2 = float(ten[2])*0.000277777777778
    if t0>=0:
        return str (t0 + t1 + t2)
    if t0<0:
        return str (-(t0 - t1 - t2))
        

longtitude = "nil"
latitude = "nil"
elevation = "nil"
line1 = ""
line2 = ""
line3 = ""

#fetch NORAD site
url = 'http://celestrak.com/NORAD/elements/amateur.txt'
htmlOpener = urllib2.urlopen(url)
if(htmlOpener.code != 200): exit(0)
src = htmlOpener.read().splitlines()
if len(src) > 0:
    count = 0
    tleFile = open('tleData.txt', 'w')
    for line in src:
        if line.find('PRISM') != -1:
            line1 = 'PRISM'
            tleFile.write(line1 + "\n")
            line2 = src[count+1] 
            tleFile.write(line2 + "\n")
            line3 = src[count+2]       
            tleFile.write(line3)
            # print line1
            # print line2 
            # print line3
            tleFile.close()
        count+=1
else:
    ocp = readFile()
    line1 = ocp[0]
    line2 = ocp[1]
    line3 = ocp[2]
    
#timezone pref use UTC now
utcTime =  datetime.datetime.utcnow()

sat = ephem.readtle(line1, line2, line3)

timeNow = utcTime.strftime("%Y/%m/%d %H:%M:%S") #we concern in seconds

#print timeNow

sat.compute( timeNow )

longtitude = six2ten(str(sat.sublong))
latitude = six2ten(str(sat.sublat))
elevation = sat.elevation

print longtitude
print latitude
print elevation