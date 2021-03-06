#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 12:11:08 2020

@author: shuser
"""

import sys
appDir="%s/Fairedge_dev/app_common"%("c:" if sys.platform=="win32" else "")
sys.path.append(appDir)

import time
import pytz
import datetime

#sys.path.append(toNative.getNativePath("C:/quanpass/programs/python/strategies"))
#from MktDaily import *

TimeZone = {'EDT':'EST5EDT',
            'EST':'EST',
            'US':'EST5EDT',
            'CST':'US/Central',
            'MST':'US/Mountain',
            'CN':'Asia/Shanghai',
            'EST5EDT':'EST5EDT',
            'Etc/GMT+5':'Etc/GMT+5',
            'Etc/GMT-8':'Etc/GMT-8',
            'JST':'Asia/Tokyo',
            'UTC':'UTC',
            'EUR':'Europe/London',
            }

def is_valid_date(str):
    try:
        time.strptime(str, "%Y%m%d")
        return True
    except:
        return False

def is_valid_time(str):
    try:
        time.strptime(str, "%Y%m%d_%H%M%S")
        return True
    except:
        return False

def gettimestamp():
    now = datetime.datetime.today()
    return now.strftime("%Y%m%d_%H%M%S")

def gethhmmss(timeDelta=datetime.timedelta(seconds=0)):
    now = datetime.datetime.today()+timeDelta
    return now.strftime("%H%M%S")

def gethhmmssPretty(timeDelta=datetime.timedelta(seconds=0)):
    now = datetime.datetime.today()+timeDelta
    return now.strftime("%H:%M:%S")

    
#DateTime related
def seconds_between(time1,time2):
    if not is_valid_time(time1):
        print('%s is not a valid time!' % time1, file=sys.stderr)
    elif not is_valid_time(time2):
        print('%s is not a valid time!' % time2, file=sys.stderr)
    else:
        t1 = time.mktime(time.strptime(time1,'%Y%m%d_%H%M%S'))
        t2 = time.mktime(time.strptime(time2,'%Y%m%d_%H%M%S'))
        return int(t2-t1)

def unpack_hhmmss(hhmmss):
    return [int(hhmmss[0:2]),int(hhmmss[2:4]),int(hhmmss[4:6])]

def unpack_yyyymmdd(yyyymmdd):
    return [int(yyyymmdd[0:4]),int(yyyymmdd[4:6]),int(yyyymmdd[6:8])]

def localdt(timezone,yyyymmdd,hhmmss):
    lst = unpack_yyyymmdd(yyyymmdd)
    lst.extend(unpack_hhmmss(hhmmss))
    dt = datetime.datetime(*lst) #Make a time object
    #print("foo: ", dt)
    lclTZ = pytz.timezone(TimeZone[timezone])
    lcl_dt = lclTZ.localize(dt)  #assign a timezone to time object 16:00:00 now because 16:00:00+08:00 nfor CN
    #print("bar: ", lcl_dt)
    return lcl_dt

def utcdt(timezone, yyyymmdd, hhmmss):
    return localdt(timezone, yyyymmdd, hhmmss).astimezone(pytz.utc)

def local2utc(timezone,yyyymmdd,hhmmss):
    hhmmss = hhmmss.replace(':','')
    lcl_dt = localdt(timezone,yyyymmdd,hhmmss)
    utc_timestamp = int((lcl_dt.timestamp()+28800)*1000 )
    return utc_timestamp

def _local2utc(timezone,yyyymmdd,hhmmss):
    loc_dt = localdt(timezone,yyyymmdd,hhmmss)
    #delta = datetime.timedelta(0,28800)
    delta = datetime.timedelta(0,28800)
    utc_dt = loc_dt.astimezone(pytz.utc)+delta
    #utc_timestamp = int(time.mktime(utc_dt.timetuple())*1000)
    utc_timestamp = int(utc_dt.timestamp()*1000)
    return utc_timestamp
    

def utc2local(utctm, timezone):
    if isinstance(utctm, int):
        utctm = ts2dt(utctm)
    return utctm.astimezone(pytz.timezone(TimeZone[timezone]))

def utc2str(utctm, fmt="%Y-%m-%dT%H:%M:%S.%f"):
    s = utctm.strftime(fmt)[:-3]

    if s.find('+')>=0 or s.find('-')>=0:
        return s[:-9].replace(' ', 'T')
    else:
        return s.replace(' ', 'T')
        
def getDateTime(tz,dt,tm): #return UTC time
    tm = tm.replace(":","")
    if len(tm)==5:
        tm = '0'+tm
    dtm = localdt(tz,dt,tm)
    return pytz.utc.normalize(dtm)

#def getDateTimeFromStr2(tz, blpTm):
#    (dtStr, tmStr) = blpTm.split('T')
#    return getDateTime(tz, dtStr.replace('-',''), tmStr.split('.')[0].replace(':','')).astimezone(pytz.utc)

def getDateTimeFromStr(blpTm, tzAdjStr="000+08:00"): #default assume CN
    blpTm = blpTm + tzAdjStr
    return datetime.datetime.strptime(blpTm, "%Y-%m-%dT%H:%M:%S.%f%z").astimezone(pytz.utc)

def getDateTimeFromStrBlp(blpTm, tzAdjStr="000+"): #Bloomberg uses millisec while the lib assumes microsec
    blpTm = blpTm.replace('+', tzAdjStr)
    return datetime.datetime.strptime(blpTm, "%Y-%m-%dT%H:%M:%S.%f%z").astimezone(pytz.utc)


def genDateTimeStrf(tz,dt):
    tz = TimeZone[tz]
    dt = dt.astimezone(pytz.timezone(tz))
    dtf = dt.strftime('%Y%m%d %H%M%S')
    if dtf[9]=='0':
        ndtf = dtf[:9]+dtf[10:]
    else:
        ndtf = dtf
    return ndtf

def datetime2ms(dt, tzadj=0):
    tt = dt.timetuple()
    #print(tt)
    return (tt.tm_hour*3600000+tt.tm_min*60000+tt.tm_sec*1000) + tzadj*3600000

def us_since_epoch(dt): #us=micro-sec
    return int(dt.timestamp()*1000000)

def ms_since_epoch(dt): #ms=mill-sec
    return int(dt.timestamp()*1000)

def now_utc_dt():
    now = datetime.datetime.today()
    now = now.astimezone(pytz.utc)
    return ("%s"%(now)).replace(" ","T")

def now_utc_ts():
    now = datetime.datetime.today()
    now = now.astimezone(pytz.utc)
    return ms_since_epoch(now)

def now_utc_dtts():
    now = datetime.datetime.today()
    now = now.astimezone(pytz.utc)
    return (("%s"%(now)).replace(" ","T"), ms_since_epoch(now))

def now_lcl_dt():
    now = datetime.datetime.today()
    return ("%s"%(now)).replace(" ","T")

def now_lcl_ts():
    now = datetime.datetime.today()
    return ms_since_epoch(now)

def now_lcl_dtts():
    now = datetime.datetime.today()
    return (("%s"%(now)).replace(" ","T"), ms_since_epoch(now))

def ts2dt(msTs):
    return datetime.datetime.utcfromtimestamp(msTs/1000)

if __name__=='__main__':
    try:
        a = getDateTime('US','20160311','003000')
        b = genDateTimeStrf('US',a)
        c = getDateTime('US','20160316','013000')
        d = genDateTimeStrf('US',c)
        e = getDateTime('CN','20160316','103000')
        f = genDateTimeStrf('US',e)
        g = getDateTime('CN','20160316','10:30:00')
        print("a= %s"%(a), file=sys.stdout)
        print("b= %s"%(b), file=sys.stdout)
        print("c= %s"%(c), file=sys.stdout)
        print("d= %s"%(d), file=sys.stdout)
        print("e= %s, %d, %d"%(e, ms_since_epoch(e), us_since_epoch(e)), file=sys.stdout)
        print("\t %s"%(ts2dt(ms_since_epoch(e))))
        print("f= %s"%(f), file=sys.stdout)
        print("g= %s"%(g), file=sys.stdout)
        
        dt0 = getDateTimeFromStr("2020-06-08T14:01:17.000")
        dt = getDateTimeFromStrBlp("2020-06-08T14:01:17.000+08:00")

        print(dt0, us_since_epoch(dt0))

        print(dt, us_since_epoch(dt))    

        print(now_utc_dtts())
        
        print(now_lcl_dtts())
        
        for tz in ['UTC', 'EST', 'CN']:
            tm = local2utc(tz, '20200622', "150000")
            print(f'local2utc({tz}, "20200622", "150000") = {tm}')
            print("%s %s"%(utc2local(ts2dt(tm), 'UTC'), utc2local(ts2dt(tm), tz)))
            print("\n")        
        
    except Exception as e:
        print(e)