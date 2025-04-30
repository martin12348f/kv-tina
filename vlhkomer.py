import machine
import time

# Definice ADC pinu (půdní vlhkoměr je připojen k GPIO26)
soil_moisture_pin = machine.ADC(26)

# Funkce pro čtení hodnoty vlhkosti půdy
def read_soil_moisture():
    # Čteme hodnotu (0 až 65535) z ADC pinu
    moisture_value = soil_moisture_pin.read_u16()  
    return moisture_value

# Hlavní smyčka pro čtení a tisk hodnoty vlhkosti půdy
while True:
    moisture = read_soil_moisture()
    print("Hodnota vlhkosti půdy:", moisture)
    time.sleep(2)  # Čeká 2 sekundy mezi čteními
