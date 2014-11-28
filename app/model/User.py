

class User(object):

    def __init__(self, uid, username, spojHandle = None):
        self.id = uid;
        self.username = username;
        self.spojHandle = spojHandle;
        self.password = None;
        
    