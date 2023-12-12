from machine import ADC, Pin

resolution = 65536

def read_sensor(adc_pin, r1, r2, max_pressure):
    pin = Pin(adc_pin)
    adc = ADC(pin)

    def calculate_voltage(value_adc):
        return value_adc / resolution * max_pressure

    # Read analog value
    analog_value = adc.read_u16()

    # Calculate output voltage from the voltage divider
    output_voltage = calculate_voltage(analog_value)

    return output_voltage
