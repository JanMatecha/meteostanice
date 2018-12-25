import dht
from bmp180 import BMP180
from machine import I2C, Pin
from ssd1306 import *
import time

sensor = dht.DHT22(Pin(2))
i2c = I2C(scl=Pin(5), sda=Pin(4))
bmp180 = BMP180(i2c)
bmp180.oversample_sett = 2
bmp180.baseline = 101325
oled = SSD1306_I2C(128, 64, i2c)
n = 0
while True:
    time.sleep(5)
    n += 1
    oled.fill_rect(0, 0, 128, 64, 0)
    oled.text("T = %s  C" % bmp180.temperature, 1, 1, 1)
    oled.text("p = %s Pa" % bmp180.pressure, 1, 10, 1)
    retry = 0
    while retry < 3:
        try:
            sensor.measure()
            break
        except:
            retry = retry + 1
            print(".", end="")
    # TODO znak pro stupen \u00b0 - nefunguje
    oled.text("T = %s  C" % sensor.temperature(), 1, 20, 1)
    oled.text("H = %s %%" % sensor.humidity(), 1, 30, 1)
    oled.text("N = %s " % n, 1, 40, 1)
    oled.show()





