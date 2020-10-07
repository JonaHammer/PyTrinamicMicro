'''
Act as TMCL slave over UART.

Created on 06.10.2020

@author: LK
'''

# Imports
from PyTrinamicMicro.connections.tmcl_host_interface import tmcl_host_interface
from PyTrinamicMicro.connections.uart_tmcl_interface import uart_tmcl_interface
from PyTrinamicMicro.TMCL_Slave import TMCL_Slave
import struct

# Constants
MODULE_ADDRESS = 1
HOST_ADDRESS = 2
MODULE_ID_STRING = "0012"
VERSION_STRING = MODULE_ID_STRING + "V308"
BUILD_VERSION = 0

# Main program

host = tmcl_host_interface(uart_tmcl_interface(), debug=True)
slave = TMCL_Slave(MODULE_ADDRESS, HOST_ADDRESS, VERSION_STRING, BUILD_VERSION)

while(True):
    request = host.receive_request()
    if(not(slave.filter(request))):
        continue
    reply = slave.handle_request(request)
    host.send_reply(reply)
