'''
Bridge from USB host to CAN module.

Pitfall:
stdout redirection is impossible in micropython at the moment.
By default, stdout-writing functions will write to VCP and interfere with connection.
Therefore, do not use stdout-writing functions (print, ...) here or turn them off while using VCP.

Created on 07.10.2020

@author: LK
'''

from PyTrinamicMicro.connections.tmcl_host_interface import tmcl_host_interface
from PyTrinamicMicro.connections.can_tmcl_interface import can_tmcl_interface
from PyTrinamicMicro.connections.usb_vcp_tmcl_interface import usb_vcp_tmcl_interface
from PyTrinamicMicro.TMCL_Bridge import TMCL_Bridge
from PyTrinamic.TMCL import TMCL_Command
import logging

# Prepare Logger
logger = logging.getLogger(__name__)
logger.info("TMCL Bridge from USB to CAN")

# When using a CAN module, Checksum needs to be recalculated.

request_command = 0

def request_callback(request):
    global request_command
    request_command = request.command
    return request

def reply_callback(reply):
    if(request_command != TMCL_Command.GET_FIRMWARE_VERSION):
        reply.calculate_checksum()
    return reply

logger.info("Initializing interfaces ...")
host = usb_vcp_tmcl_interface()
module = can_tmcl_interface()
bridge = TMCL_Bridge(host, module)
logger.info("Interfaces initialized.")

while(not(bridge.process(request_callback=request_callback, reply_callback=reply_callback))):
    #logger.debug("Processed request.")
    pass

logger.info("Closing interfaces ...")
host.close()
logger.info("Interfaces closed.")

logger.info("Bridge stopped.")
