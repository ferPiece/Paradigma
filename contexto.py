import ZODB

__zodb_root = None

def get_zodb_root():
    global __zodb_root
    if not __zodb_root:
        db = ZODB.DB('data/db.fs')
        connection = db.open()
        __zodb_root  = connection.root
    return __zodb_root
