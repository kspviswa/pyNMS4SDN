'''
Created on 28-May-2015

@author: kspviswa
'''
from pysnmp.entity.rfc3413.oneliner import ntforg
from pysnmp.proto import rfc1902

class snmpTrapGenerator(object):
    '''
    Provider to send SNMP trap
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.community = 'public'
        self.target = '127.0.0.1'
        self.targetPort = 162
        self.trapVariable = 'pyNMS4SDN'
        self.trapOID = '1.3.6.1.2.1.1.1.0'
        self.trapVarBinding = 'Test-Data'
        
    def fireTrap(self,param):
        
        if(param != None):
            self.trapvarBinding = param
        
        ntfOrg = ntforg.NotificationOriginator()
        
        errorIndication = ntfOrg.sendNotification(ntforg.CommunityData(self.community, mpModel=0),
                                                  ntforg.UdpTransportTarget((self.target, self.targetPort)),
                                                  'trap',
                                                  '1.3.6.1.4.1.20408.4.1.1.2.0.432',
                                                  (self.trapOID, rfc1902.OctetString(self.trapVarBinding)))
        
        print("sent trap")        

        
        
    
