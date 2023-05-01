from machine import Pin, I2C
from time import sleep
from i2c_lcd import I2cLcd
import os
import urllib.request

# define pins for buttons
up_button = Pin(2, Pin.IN, Pin.PULL_DOWN)
down_button = Pin(3, Pin.IN, Pin.PULL_DOWN)
select_button = Pin(4, Pin.IN, Pin.PULL_DOWN)


# Set the URL to the new main.py file in your GitHub repository
url = 'https://raw.githubusercontent.com/your-username/your-repo/master/main.py'

# define pins for relay control signals
relay_pins = [Pin(i, Pin.OUT) for i in range(5, 13)]

# define pin for bell control signal
bell_pin = Pin(13, Pin.OUT)

# define menu items
menu_items = [
    {"type": "all_lights", "label": "All Lights"},
    {"type": "light", "label": "Light Group 1"},
    {"type": "light", "label": "Light Group 2"},
    {"type": "light", "label": "Light Group 3"},
    {"type": "light", "label": "Light Group 4"},
    {"type": "light", "label": "Light Group 5"},
    {"type": "light", "label": "Light Group 6"},
    {"type": "light", "label": "Light Group 7"},
    {"type": "light", "label": "Light Group 8"},
    {"type": "menu", "label": "More Options"}
]
menu_states = [False] * len(menu_items) # all items initially off
current_item = 0 # initially select first item

# define submenu for church bell
submenu_items = [
    {"type": "bell", "label": "10 AM"},
    {"type": "bell", "label": "11 AM"},
    {"type": "bell", "label": "12 PM"},
    {"type": "bell", "label": "1 PM"},
    {"type": "bell", "label": "2 PM"},
    {"type": "bell", "label": "3 PM"},
    {"type": "bell", "label": "4 PM"},
    {"type": "bell", "label": "5 PM"},
    {"type": "bell", "label": "<IPAddress>-8 PM"}
]
current_submenu_item = 0 # initially select first subitem
in_submenu = False # initially not in submenu


# Initialize LCD display
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
lcd = I2cLcd(i2c, 0x27, 2, 16)

def ring_bell(hour):
    # Send impulses to ring bell at specified hour
    for i in range(hour):
        bell_pin.value(1)
        sleep(0.5)
        bell_pin.value(0)
        sleep(0.5)

def update_menu():
    # Clear display
    lcd.clear()
    
    if in_submenu:
        # Display current submenu state
        lcd.putstr(submenu_items[current_submenu_item]["label"])
    else:
        # Display current menu state
        state_str = ""
        if menu_items[current_item]["type"] == "<IPAddress>_lights":
            state_str = "- ON" if all(menu_states[1:9]) else "- OFF"
        elif menu_items[current_item]["type"] == "<IPAddress>":
            state_str = "- ON" if menu_states[current_item] else "- OFF"
        lcd.putstr("{} {}".format(menu_items[current_item]["label"], state_str))

def up_pressed():
    global current_item
    current_item -= 1
    if current_item < 0:
        current_item = len(menu_items) - 1
    update_menu()

def down_pressed():
    global current_item
    current_item += 1
    if current_item >= len(menu_items):
        current_item = 0
    update_menu()

def select_pressed():
    global menu_states
    if menu_items[current_item]["type"] == "all_lights":
        new_state = not all(menu_states[1:9])
        for i in range(1, 9):
            menu_states[i] = new_state
            relay_pins[i-1].value(new_state)
        update_menu()
    elif menu_items[current_item]["type"] == "light":
        menu_states[current_item] = not menu_states[current_item]
        relay_pins[current_item-1].value(menu_states[current_item])
        update_menu()

def update_main():
    # Download the new main.py file
    urllib.request.urlretrieve(url, '/tmp/new_main.py')

    # Check if the new main.py file is different from the current one
    with open('/tmp/new_main.py', 'r') as new_file, open('/path/to/main.py', 'r') as current_file:
        if new_file.read() != current_file.read():
            # Replace the old main.py file with the new one
            os.replace('/tmp/new_main.py', '/path/to/main.py')

def check_buttons():
    # Check if all buttons are pressed
    if up_button.value() and down_button.value() and select_button.value():
        # Display countdown on LCD
        for i in range(10, 0, -1):
            lcd.clear()
            lcd.putstr("Updating in {}...".format(i))
            sleep(1)
        
        # Update main.py file
        update_main()

# Turn off all relays on startup
for pin in relay_pins:
    pin.value(0)

up_button.irq(trigger=Pin.IRQ_RISING, handler=lambda t:up_pressed())
down_button.irq(trigger=Pin.IRQ_RISING, handler=lambda t:down_pressed())
select_button.irq(trigger=Pin.IRQ_RISING, handler=lambda t:select_pressed())

update_menu()
while True:
   # Check buttons every 0.1 seconds
   check_buttons()
   sleep(0.1)