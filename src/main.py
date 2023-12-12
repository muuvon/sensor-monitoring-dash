from machine import Pin, ADC
import time

ps10_adc = ADC(0)

while True:
    ps10_val = ps10_adc.read_u16()
    print("\nPure read: " + str(ps10_val))
    print("bit read: " + str(ps10_val / 65536))
    time.sleep_ms(200)