import sqlite3
from app.model.User import User
from app.util import rowToMap

class UserDao:
    
    def __init__(self , dbFile):
        self.conn = sqlite3.connect(dbFile)
        self.conn.row_factory = rowToMap
        
    def getUserById(self, uid):
        res = self.conn.execute("SELECT * FROM users WHERE id = %d" % uid).fetchone()
        return None if res == None else \
            User(res['id'], res['username'], res.get('spojHandle'))
        
    def removeUserById(self, uid):
        res = self.conn.execute("DELETE FROM users WHERE id = %d" % uid)
        self.conn.commit();
        return res
        
    def getUserByUsername(self, username):
        res = self.conn.execute("SELECT * FROM users WHERE username = '%s'" % username).fetchone()
        if res == None:
            return None;
        usr = User(res['id'], res['username'], res.get('spojHandle'))
        usr.password = res['password']; 
        return usr
            
