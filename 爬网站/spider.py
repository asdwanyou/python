#!/usr/bin/env python3

from io import *
from urllib import *
from string import *
lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def urliter() :
    for i in list(range(1,101)) :
        print ("%d/100"  % i)
        for j in lowercase :
            for k in lowercase :
                yield "http://www.%02d%c%c%c%c.com" % (i, j, k, j, k)

logfile = open("findsomewebsites.log", "w")

for u in urliter() :
    try :
        wp = urlopen(u)
        print ("find " + u)
        logfile.write(u + "\n")
    except :
        pass

logfile.close()



