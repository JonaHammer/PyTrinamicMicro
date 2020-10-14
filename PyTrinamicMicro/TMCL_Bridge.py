'''
Created on 07.10.2020

@author: LK
'''

from PyTrinamicMicro.connections.tmcl_host_interface import tmcl_host_interface
from PyTrinamicMicro.TMCL_Slave import TMCL_Slave_Bridge
from PyTrinamic.TMCL import TMCL_Command, TMCL_Request, TMCL_Reply
import logging


class TMCL_Bridge(object):
    '''
    Initialize the TMCL bridge.

    Parameters:
        host_connection: tmcl_interface to the main host.
        module_connection: tmcl_interface to the module.
        module_id: module ID to be used in control mode.
        host_id: host ID to be used in control mode.
    '''

    def __init__(self, host_connection, module_connection, module_id=3, host_id=2):
        self.__host = host_connection
        self.__module = module_connection
        self.__slave = TMCL_Slave_Bridge(module_id, host_id)
        self.__logger = logging.getLogger(self.__module__)

    def process(self, request_callback=None, reply_callback=None):
        '''
        1. Receive request from host
        2. Send request to module
        3. Receive reply from module
        4. Send reply to host
        '''
        if(self.__host.request_available()):
            request = self.receive_request()
            self.__logger.debug("Processing request ({}).".format(str(request)))
            if(self.__slave.filter(request)): # Control request
                self.__logger.debug("Request is a control request.")
                reply = self.__slave.handle_request(request)
                self.__logger.debug("Control reply ({}).".format(str(reply)))
                self.send_reply(reply)
            else: # Passthrough request
                self.__logger.debug("Request is not a control request. Passing through.")
                if(request_callback):
                    request = request_callback(request)
                reply = self.send_request(request)
                self.__logger.debug("Passthrough reply ({}).".format(str(reply)))
                if(reply_callback):
                    reply = reply_callback(reply)
                self.send_reply(reply)
        return self.__slave.get_status().stop

    def receive_request(self):
        return self.__host.receive_request()

    def send_request(self, request):
        return self.__module.send_request(request)

    def send_reply(self, reply):
        self.__host.send_reply(reply)
