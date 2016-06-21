#coding:utf8

from DBUtils.PooledDB import PooledDB

DBCS = {'MySQLdb':"MySQLdb",}
        
class MultiDBPool(object):
    """
    """
    def __init__(self):
        """
        """
        self.router = None
    
    def initPool(self,dbconfig):
        """
        """
        _creator = DBCS.get(dbconfig.get('engine','MySQLdb'))
        creator = __import__(_creator)
        self.dbpool = PooledDB(creator, **dbconfig)
            
    def bind_router(self,router):
        """
        """
        self.router = router()
        
    def getPool(self, write=True, **kw):
        """
        """
        if not self.router:
            return self.dbpool
        if write:
            return self.dbpool
        else:
            return self.dbpool
        
    def connection(self, write=True, **kw):
        """
        """
        if not self.router:
            return self.dbpool.connection(shareable=kw.get("shareable",True))
        if write:
            return self.dbpool.connection(shareable=kw.get("shareable",True))
        else:
            return self.dbpool.connection(shareable=kw.get("shareable",True))


dbpool = MultiDBPool()

