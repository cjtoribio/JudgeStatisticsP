import urllib2
import re
from app.model.Submission import Submission 
from app.util import DateUtils

def getSubmissionHistory(handle):
    lineRegex = r"""
       \|\ +(\d+)\ 
       \|\ +(\d{4}-\d{2}-\d{2}\ \d{2}:\d{2}:\d{2})\  
       \|\ +(\w+)\   
       \|\ +(\w+)\ 
       \|\ +(-?\d+\.\d+)\ 
       \|\ +(\d+)\ 
       \|\ +([^\ ]*)\ 
       \|
    """
    ret = []
    for line in urllib2.urlopen("http://www.spoj.com/status/%s/signedlist/" % handle).read().split('\n'):
        match = re.search(lineRegex, line, re.X)
        if match:
            sub = Submission()
            sub.userId = None
            sub.insertDate = None
            sub.id = int(match.groups()[0])
            sub.judge = 'SPOJ'
            sub.problemCode = match.groups()[2]
            sub.memory = int(match.groups()[5])
            sub.submissionDate = DateUtils.fromStr(match.groups()[1] + '.000000')
            sub.lang = match.groups()[6]
            sub.veredict = match.groups()[3]
            sub.time = int(match.groups()[4].replace('.',''))
            ret.append(sub)
    return ret
            

        