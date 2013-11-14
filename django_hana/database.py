from jaydebeapi import *

# extend the Connection class by the method setautocommit used by django_hana
class Connection(Connection):

  def setautocommit(auto):
    self.jconn.setAutoCommit(auto)

  def connect(address, port, user, password):
      return super(Connection, self).connect('com.sap.db.jdbc.Driver', ['jdbc:sap://{0}:{1}/'.format(host, port), user, password], 'ngdbc.jar')