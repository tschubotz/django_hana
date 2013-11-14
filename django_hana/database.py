from jaydebeapi import *
from jaydebeapi import connect as j_connect
from jaydebeapi import Connection as j_Connection

# extend the Connection class by the method setautocommit used by django_hana
class Connection(j_Connection):

  def setautocommit(auto):
    self.jconn.setAutoCommit(auto)

def connect(address, port, user, password):
  return j_connect('com.sap.db.jdbc.Driver', ['jdbc:sap://{0}:{1}/'.format(address, port), user, password], 'ngdbc.jar')