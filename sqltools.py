import MySQLdb
from pprint import pprint


class sqltool(object):
    def __init__(self, dbname):
        self.conn = MySQLdb.connect(host='localhost', user='root', passwd='hitnslab', db=dbname)
        self.cur = self.conn.cursor()

    def __del__(self):
        """Teiminate the connection"""
        try:
            self.conn.close()
            self.cur.close()
        except MySQLdb.Error, e:
            pprint("MySql Error %d:%s" % (e.args[0], e.args[1]))

    def sql_find(self, sql):
        try:
            self.cur.execute(sql)
            result = self.cur.fetchone()
            return result[0]
        except MySQLdb.Error, e:
            pprint("MySql Error %d:%s" % (e.args[0], e.args[1]))

    def sql_instert(self, sql):
        try:
            self.cur.execute(sql)
            self.cur.fetchone()
        except MySQLdb.Error, e:
            pprint("MySql Error %d:%s" % (e.args[0], e.args[1]))