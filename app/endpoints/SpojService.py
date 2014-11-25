
from app.db import subsDao , userDao
from app.endpoints import restApi
from flask_restful import Resource, fields, marshal_with
from flask_restful import reqparse
from sets import Set


class JsonDate(fields.DateTime):
    def format(self, value):
        return { '__type':'Date' , 'iso' : value.isoformat() }

@restApi.resource("/spoj/subs/<int:userId>")
class Submissions(Resource):
    get_fields = {
        'id' : fields.Integer,
        'judge' : fields.String,
        'userId' : fields.Integer,
        'problemCode' : fields.String,
        'memory' : fields.Integer,
        'time' : fields.Integer,
        'submissionDate' : fields.DateTime,
        'lang' : fields.String,
        'veredict' : fields.String,
        'insertDate' : fields.DateTime
    }
    post_fields = {
        'status' : fields.String,
        'error' : fields.String
    }
    @marshal_with(get_fields)
    def get(self, userId):
        parser = reqparse.RequestParser()\
            .add_argument('veredict' , type=str, help="The veredict field should be a String")
        args = parser.parse_args()
        veredict = args['veredict']
        subs = subsDao.getUserSubmissions(userId , "SPOJ", veredict and veredict.upper())
        return subs
    
    def post(self, userId):
        from app.crawlers.SpojCrawler import getSubmissionHistory
        user = userDao.getUserById(userId)
        subs = getSubmissionHistory(user.spojHandle)
        eSubs = Set(map(lambda x: x.id , subsDao.getUserSubmissions(userId, 'SPOJ') ))
        subs = filter( lambda sub: sub.id not in eSubs , subs  );
        subs = map(lambda x: [setattr(x , 'userId', userId), x][1], subs)
        subsDao.addSubmissions(subs)
        return {'status' : 'Ok'}


@restApi.resource("/spoj/stats/<int:userId>")
class SubmissionsStats(Resource):
    get_fields = {
        'accuracy' : fields.Float,
        'tenacity' : fields.Float,
        'lastSubmission' : fields.DateTime,
        'todoSize' : fields.Integer,
        'problemSolved' : fields.Integer,
        'veredictMap' : fields.Nested({
            'AC' : fields.Integer(attribute = 'AC'),
            'WA' : fields.Integer(attribute = 'WA'),
            'TLE' : fields.Integer(attribute = 'TLE'),
            'RE' : fields.Integer(attribute = 'RE'),
            'CE' : fields.Integer(attribute = 'CE')
        })
    }
    @marshal_with(get_fields)
    def get(self, userId):
        ret = {}
        subs = subsDao.getUserSubmissions(userId, 'SPOJ')
        allAc = filter(lambda x: x.veredict == 'AC' , subs)
        last = None if len(subs) == 0 else max(sub.submissionDate for sub in subs)
        probAC = set(map(lambda x: x.problemCode, allAc))
        totalProb = set(map(lambda x: x.problemCode, subs))
        veredictMap = {}
        for sub in subs: veredictMap[sub.veredict] = (veredictMap.get(sub.veredict) or 0) + 1
         
        ret['accuracy'] = 100.0 * len(allAc) / len(subs)
        ret['tenacity'] = 100.0 * (100 - ret['accuracy'])/100.0 * len(probAC) / len(totalProb)
        ret['lastSubmission'] = last
        ret['todoSize'] = len(totalProb) - len(probAC)
        ret['problemsSolved'] = len(totalProb)
        ret['veredictMap'] = veredictMap
        return ret
        
   
    