from jaydebeapi import *
from jaydebeapi import connect as j_connect
from jaydebeapi import Connection as j_Connection

# extend the Connection class by the method setautocommit used by django_hana
class Connection(j_Connection):

  @classmethod
  def from_j_connection(cls, j_connection):
    return cls(j_connection.jconn, j_connection._converters)

  def setautocommit(self, auto):
    self.jconn.setAutoCommit(auto)

def connect(address, port, user, password):
  j_connection = j_connect('com.sap.db.jdbc.Driver', ['jdbc:sap://{0}:{1}/'.format(address, port), user, password], 'ngdbc.jar')
  return Connection.from_j_connection(j_connection)
