'''
MotionPy root configuration class.

Created on 29.10.2020

@author: LK
'''

from PyTrinamicMicro import PyTrinamicMicro

class MotionPy(PyTrinamicMicro):

    _MAP_SCRIPT = {
        "null": "PyTrinamicMicro/platforms/motionpy/examples/null.py",
        "blinky": "PyTrinamicMicro/platforms/motionpy/examples/io/blinky.py",
        "buttons_leds": "PyTrinamicMicro/platforms/motionpy/examples/io/buttons_leds.py",
        "tmcm1161_rs232_rotate": "PyTrinamicMicro/platforms/motionpy/examples/modules/TMCM1161/TMCM1161_RS232_rotate.py",
        "tmcm1161_rs485_rotate": "PyTrinamicMicro/platforms/motionpy/examples/modules/TMCM1161/TMCM1161_RS485_rotate.py",
        "tmcm1240_can_rotate": "PyTrinamicMicro/platforms/motionpy/examples/modules/TMCM1240/TMCM1240_CAN_rotate.py",
        "tmcm1240_rs485_rotate": "PyTrinamicMicro/platforms/motionpy/examples/modules/TMCM1240/TMCM1240_RS485_rotate.py",
        "tmcm1270_rotate": "PyTrinamicMicro/platforms/motionpy/examples/modules/TMCM1270/TMCM1270_rotate.py",
        "tmcl_bridge_uart_can": "PyTrinamicMicro/platforms/motionpy/examples/tmcl_bridge/tmcl_bridge_uart_can.py",
        "tmcl_bridge_uart_rs232": "PyTrinamicMicro/platforms/motionpy/examples/tmcl_bridge/tmcl_bridge_uart_rs232.py",
        "tmcl_bridge_uart_rs485": "PyTrinamicMicro/platforms/motionpy/examples/tmcl_bridge/tmcl_bridge_uart_rs485.py",
        "tmcl_bridge_usb_can": "PyTrinamicMicro/platforms/motionpy/examples/tmcl_bridge/tmcl_bridge_usb_can.py",
        "tmcl_bridge_usb_rs232": "PyTrinamicMicro/platforms/motionpy/examples/tmcl_bridge/tmcl_bridge_usb_rs232.py",
        "tmcl_bridge_usb_rs485": "PyTrinamicMicro/platforms/motionpy/examples/tmcl_bridge/tmcl_bridge_usb_rs485.py",
        "tmcl_bridge_usb_uart": "PyTrinamicMicro/platforms/motionpy/examples/tmcl_bridge/tmcl_bridge_usb_uart.py",
        "tmcl_slave_uart": "PyTrinamicMicro/platforms/motionpy/examples/tmcl_bridge/tmcl_slave_uart.py",
        "tmcl_slave_usb": "PyTrinamicMicro/platforms/motionpy/examples/tmcl_bridge/tmcl_slave_usb.py",
        "fw_update_can": "PyTrinamicMicro/platforms/motionpy/examples/firmware_update/fw_update_can.py"
    }

    @staticmethod
    def script(identifier):
        return PyTrinamicMicro.script(MotionPy, identifier)