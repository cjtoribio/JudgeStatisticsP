from app.util import DateUtils

class Submission(object):

    def __init__(self):
        self.id = None;
        self.judge = None;
        self.userId = None;
        self.problemCode = None;
        self.memory = None;
        self.time = None;
        self.submissionDate = None;
        self.lang = None;
        self.veredict = None;
        self.insertDate = None;
        
    def asSelect(self):
        sel = """SELECT %d id,
                       '%s' judge,
                        %d  userId, 
                       '%s' problemCode,
                        %d  memory,
                        %d  time,
                       '%s' submissionDate,
                       '%s' lang,
                       '%s' veredict,
                       '%s' insertDate""" % (
                 self.id, 
                 self.judge, 
                 self.userId,
                 self.problemCode,
                 self.memory,
                 self.time, 
                 DateUtils.toStr(self.submissionDate),
                 self.lang, 
                 self.veredict, 
                 DateUtils.toStr(self.insertDate)
                 )
        return sel
    
    @staticmethod
    def fields():
        sel = """id,
                 judge,
                 userId, 
                 problemCode,
                 memory,
                 time,
                 submissionDate,
                 lang,
                 veredict,
                 insertDate"""
        return sel
    
    @staticmethod
    def fromMap(row):
        s = Submission()
        s.id = row['id']
        s.judge = row['judge']
        s.userId = row['userId']
        s.problemCode = row['problemCode']
        s.memory = row['memory']
        s.time = row['time']
        s.submissionDate = DateUtils.fromStr(row['submissionDate'])
        s.lang = row['lang']
        s.veredict = row['veredict']
        s.insertDate = DateUtils.fromStr(row['insertDate'])
        return s;
    
    def toMap(self):
        r = {}
        r['id'] = self.id
        r['judge'] = self.judge
        r['userId'] = self.userId
        r['problemCode'] = self.problemCode
        r['memory'] = self.memory
        r['time'] = self.time
        r['submissionDate'] = DateUtils.toStr(self.submissionDate)
        r['lang'] = self.lang 
        r['veredict'] = self.veredict 
        r['insertDate'] = DateUtils.toStr(self.insertDate)
        return r;
        
