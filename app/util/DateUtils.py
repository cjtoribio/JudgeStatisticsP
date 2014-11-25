from datetime import datetime
from datetime import date
import calendar
import time

class DateFormat:
    DEFAULT = "%Y-%m-%d %H:%M:%S.%f"
    COMPACT = "%Y%m%d%H%M%S%f"
    JSON = "%Y-%m-%dT%H:%M:%S.000Z"
    

def toStr(date, format=DateFormat.DEFAULT):
    if(date  == None): return ''
    return datetime.strftime(date, format)

def fromStr(dateS, format=DateFormat.DEFAULT):
    if(dateS == None): return None;
    return datetime.strptime(dateS, format)

def today():
    return datetime.today()