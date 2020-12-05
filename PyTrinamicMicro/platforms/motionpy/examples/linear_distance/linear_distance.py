'''
Created on 04.12.2020

@author: LK
'''

from PyTrinamic.ic.TMC5130.TMC5130 import TMC5130
from PyTrinamicMicro.platforms.motionpy.connections.uart_ic_interface import uart_ic_interface
from PyTrinamicMicro.platforms.motionpy.modules.hc_sr04_multi import hc_sr04_multi
from PyTrinamicMicro.platforms.motionpy.modules.MCP23S08 import MCP23S08
import logging

logger = logging.getLogger(__name__)

logger.debug("Initializing TMC5130 ...")
mc = TMC5130(connection=uart_ic_interface(single_wire=True), comm=TMC5130.COMM_UART)
logger.debug("TMC5130 initialized.")
logger.debug("Initializing hc_sr04_multi ...")
sensor = hc_sr04_multi()
logger.debug("hc_sr04_multi initialized.")

logger.debug("Writing default registers ...")
mc.writeRegister(0x10, 0x00071703)
mc.writeRegister(0x6C, 0x000101D5)
mc.writeRegister(0x70, 0x000500C8)

while(True):
    distance = sensor.distance(1)
    velocity = int((distance-50)*500)
    logger.info("distance = {}, velocity = {}".format(distance, velocity))
    mc.rotate(0, velocity)
