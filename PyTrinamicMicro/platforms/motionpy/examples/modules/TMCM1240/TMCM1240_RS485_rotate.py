'''
Rotate the motor with TMCM1240 using RS485 interface.

Created on 21.10.2020

@author: LK
'''

from PyTrinamic.modules.TMCM1240.TMCM_1240 import TMCM_1240
from PyTrinamicMicro.platforms.motionpy.connections.rs485_tmcl_interface import rs485_tmcl_interface
import time

con = rs485_tmcl_interface()
module = TMCM_1240(con)

module.rotate(50000)
time.sleep(5)
module.stop()

con.close()
