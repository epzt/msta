# -*- coding: utf-8 -*-
import sys

def dd2dm(_dd):
    d = int(_dd)
    m = (_dd - d) * 60.0
    return ("{}°{.6f}".format(d,m))

def dd2dms(_dd):
    d = int(_dd)
    m = (_dd - d) * 60.0
    s = (m - int(m)) * 60
    return ("{}°{.0f}'{.0f}''".format(d,m))

with open('Coordonnes-sediment-previsionnel.csv') as fin:
    data = fin.readlines()

fout = open('Coordonnees.txt', 'w')
for l in data:
    londd = l.split(";")[0]
    latdd = l.split(";")[1]
    fout.write("{:.6f},{:.6f}|{},{}|{},{}\n".format(latdd,londd, dd2dm(latdd),dd2dm(londd),dd2dms(latdd),dd2dms(londd)))

fout.close()