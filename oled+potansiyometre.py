from machine import Pin, ADC, SoftI2C
import ssd1306
from time import sleep


i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)

while True:
    oled.fill(0)
    pot_value = pot.read()
    oled.text(str(pot_value), 0, 0)
    oled.show()
    sleep(0.1)
