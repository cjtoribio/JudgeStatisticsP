import sqlite3
from app.util import rowToMap
from app.util import DateUtils
from app.model.Submission import Submission

class SubmissionsDao:
    
    def __init__(self , dbFile):
        self.conn = sqlite3.connect(dbFile)
        self.conn.row_factory = rowToMap
        
    def addSubmission(self, sub):
        self.addSubmissions([sub])
        
    def addSubmissions(self, subs):
        st = 0
        while st < len(subs):
            en = st+450
            if en > len(subs): en = len(subs)
            self.__addBatchSubmissions(subs[st:en])
            st = en
    
    def __addBatchSubmissions(self, subs):
        queries = ["INSERT INTO submissions (%s)" % Submission.fields()]
        for sub in subs:
            sub.insertDate = DateUtils.today()
            if(len(queries) > 1):
                queries.append("UNION")
            queries.append(sub.asSelect())
        self.conn.execute(" ".join(queries))
        self.conn.commit()
        
        
    def removeSubmission(self, sid, judge):
        self.conn.execute(
            """ DELETE FROM submissions 
                WHERE id = %d and judge = '%s'
            """ % ( sid , judge )
            )
        self.conn.commit()
   
    def getUserSubmissions(self, uid, judge = None, veredict = None):
        query = """
            SELECT %s from submissions
             WHERE userId = %d """ % (Submission.fields() , uid)
        if judge != None : query += " AND judge = '%s'" % judge
        if veredict != None : query += " AND veredict = '%s'" % veredict
            
        ret = []
        for row in self.conn.execute(query):
            ret.append(Submission.fromMap(row))
        return ret;
   
    def getSubmission(self, uid, sid, judge):
        query = """
            SELECT %s
              FROM submissions
             WHERE userId =  %d 
               AND id     =  %d 
               AND judge  = '%s' """ % (Submission.fields(), uid , sid, judge)
        ret = None
        for row in self.conn.execute(query):
            ret = Submission.fromMap(row)
        return ret;
        
        
