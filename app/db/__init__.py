from app.db.UserDao import UserDao
from app.db.SubmissionsDao import SubmissionsDao
from app.model.Submission import Submission
from app.util import DateUtils

userDao = UserDao(__path__[0] + '/db.sqlite')
subsDao = SubmissionsDao(__path__[0] + '/db.sqlite')


