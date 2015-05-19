__author__ = 'venkat'


import httplib2
import json
from rest_url_database import *


class HttpJsonHandler:
    def __init__(self):
        print("Inside Class - HttpJsonHandler Constructor")
        return

    def getnodeinfo(self):
        global h
        h = httplib2.Http(".cache")
        h.add_credentials('admin', 'admin')

        '''
        Get the List of nodes available in the network
        '''
        print(REST_URL_FOR_NODE)
        resp, content = h.request(REST_URL_FOR_NODE, 'GET')
        nodes = json.loads(content.decode())

        return nodes

    def getflowinfo (self):
        global h
        h = httplib2.Http(".cache")
        h.add_credentials('admin', 'admin')

        '''
        Get the List of flows available in the network
        '''
        print(REST_URL_FOR_FLOW)
        resp, content = h.request(REST_URL_FOR_FLOW, 'GET')
        flows = json.loads(content.decode())

        return flows

    def getportinfo(self, switchid):
        global h
        h = httplib2.Http(".cache")
        h.add_credentials('admin', 'admin')

        '''
        Get the List of ports available in the switch
        '''
        port_rest_url = REST_URL_FOR_PORT + switchid
        print(port_rest_url)
        self.resp, self.content = h.request(port_rest_url, 'GET')
        self.ports = json.loads(self.content.decode())

        return self.ports

    def gethostinfo(self):
        global h
        h = httplib2.Http(".cache")
        h.add_credentials('admin', 'admin')

        '''
        Get the List of hosts connected to the switch
        '''
        print(REST_URL_FOR_HOST)
        self.resp, self.content = h.request(REST_URL_FOR_HOST, 'GET')
        self.hosts = json.loads(self.content.decode())

        return self.hosts

    def getlinkinfo(self, switchid):
        global h
        h = httplib2.Http(".cache")
        h.add_credentials('admin', 'admin')

        '''
        Get the List of links connected to the switch
        '''
        link_rest_url = REST_URL_FOR_LINK + switchid
        print(link_rest_url)
        self.resp, self.content = h.request(link_rest_url, 'GET')
        self.links = json.loads(self.content.decode())

        return self.links

switchid = "00:00:00:00:00:00:00:01"
flow = HttpJsonHandler()
flow.getnodeinfo()

flow.getlinkinfo(switchid)
