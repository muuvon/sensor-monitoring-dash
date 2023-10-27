import src.external_modules.ssd1306 as ssd1306
import src.utils.data_convertion as convert
import machine
import time
import random

# Display Settings
i2c = machine.I2C(0)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Led Settings
led_pin = 13
led = machine.Pin(led_pin, machine.Pin.OUT)
led.off()

# Pressure sensors
ps10 = machine.ADC(0)

refresh_count = 0

while True:
    led.off()  # reset warning led

    # read sensor values (eng. unity)
    map_ps10_val = ps10.read_u16()
    fuel_pressure_ps10_val = 0
    oil_pressure_ps10_val = 0

    # Manifold absolute pressure (convertions)
    map_psi = convert.ps10_to_psi(map_ps10_val)
    map_kgcm2 = convert.psi_to_kgfcm2(map_psi)
    map_warning = False

    # Fuel line pressure (convertions)
    fuel_pressure_psi = convert.ps10_to_psi(fuel_pressure_ps10_val)
    fuel_pressure_bar = convert.psi_to_bar(fuel_pressure_psi)
    fuel_pressure_warning = False

    # Oil line pressure (convertions)
    oil_pressure_psi = convert.ps10_to_psi(oil_pressure_ps10_val)
    oil_pressure_bar = convert.psi_to_bar(oil_pressure_psi)
    oil_pressure_warning = False

    # BYPASS FAKE INFORMATION
    map_kgcm2 = random.randint(0, 160)/100
    oil_pressure_bar = random.randint(100, 900)/100
    fuel_pressure_bar = random.randint(100, 900)/100

    if map_kgcm2 > 1:
        map_warning = True
        led.on()

    if fuel_pressure_bar < 2:
        fuel_pressure_warning = True
        led.on()

    if oil_pressure_bar < 3:
        oil_pressure_warning = True
        led.on()

    # Render MAP sensor information
    map_text_info = 'Turbo ' + '{:.2f}Kg'.format(map_kgcm2)
    oled.fill_rect(0, 0, 128, 17, 1 if map_warning else 0)
    oled.text(map_text_info,
              64 - int(len(map_text_info)*4),
              5,
              0 if map_warning else 1)

    # Render Oil sensor information
    map_text_info = 'Oil ' + '{:.2f}Kg'.format(oil_pressure_bar)
    oled.fill_rect(0, 23, 128, 17, 1 if oil_pressure_warning else 0)
    oled.text(map_text_info,
              64 - int(len(map_text_info)*4),
              28,
              0 if oil_pressure_warning else 1)

    # Render Fuel sensor information
    map_text_info = 'Fuel ' + '{:.2f}Kg'.format(fuel_pressure_bar)
    oled.fill_rect(0, 48, 128, 17, 1 if fuel_pressure_warning else 0)
    oled.text(map_text_info,
              64 - int(len(map_text_info)*4),
              52,
              0 if fuel_pressure_warning else 1)

    oled.show()

    time.sleep_ms(200)
