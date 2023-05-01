# 🚂 Modellzug-Lichtsteuerung 🚂

## English Version Below

Dieses Projekt ist meinem Großvater gewidmet, der eine große Leidenschaft für Modellzüge hat. Es bietet eine einfache und benutzerfreundliche Möglichkeit, die Lichter und Attraktionen in seinem Modellzugraum mit einem Raspberry Pi Pico und einem 16x2-Zeichen-LCD-Display zu steuern. Da er nicht so gut mit Computern umgehen kann, werde ich den Code nach seinen Wünschen ändern, wenn er es braucht. Ich dachte, ich würde es hier teilen, um meinen Lernprozess zu dokumentieren, da dies das erste Mal ist, dass ich so etwas gemacht habe.

## 🔦 Funktionen 🔦

- Einfach durch ein Menü von Lichtern und Attraktionen mit Auf- und Ab-Tasten navigieren
- Schnell den Zustand des ausgewählten Lichts oder der ausgewählten Attraktion ein oder aus schalten mit einer Auswahltaste
- Deutlich den aktuellen Zustand des ausgewählten Lichts oder der ausgewählten Attraktion auf einem 16x2-Zeichen-LCD-Display sehen

## 🛠️ Hardware-Anforderungen 🛠️

- Raspberry Pi Pico
- 16x2-Zeichen-LCD-Display (mit I2C-Schnittstelle)
- 3 Drucktasten (für Auf-, Ab- und Auswahltaste)
- Jumper-Kabel und Steckbrett (zum Prototyping)

## 💻 Software-Anforderungen 💻

- Micropython-Firmware für Raspberry Pi Pico
- `esp8266_i2c_lcd` Bibliothek zum Anschluss an das LCD-Display

## 🚀 Erste Schritte 🚀

1. Die Hardware-Komponenten gemäß dem Schaltplan anschließen.
2. Die Micropython-Firmware auf dem Raspberry Pi Pico installieren.
3. Die `esp8266_i2c_lcd` Bibliothek auf dem Raspberry Pi Pico installieren.
4. Die `main.py` Datei aus diesem Repository auf dem Raspberry Pi Pico kopieren.
5. Den Raspberry Pi Pico zurücksetzen, um das Programm zu starten.

## 🕹️ Verwendung 🕹️

Mit den Auf- und Ab-Tasten durch das Menü der Lichter und Attraktionen navigieren. Das aktuell ausgewählte Element wird auf dem LCD-Display zusammen mit seinem aktuellen Zustand (ein oder aus) angezeigt.

Die Auswahltaste drücken, um den Zustand des ausgewählten Lichts oder der ausgewählten Attraktion umzuschalten. Der neue Zustand wird auf dem LCD-Display angezeigt.

## 📜 Lizenz 📜

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Weitere Informationen finden Sie in der [LIZENZ](LICENSE)-Datei.

## 🙏 Danksagungen 🙏

Dieses Projekt ist meinem Großvater gewidmet, der mich mit seiner Liebe zu Modellzügen inspiriert hat. Danke, dass du deine Leidenschaft mit mir geteilt hast.

---

# 🚂 Model Train Light-Controller 🚂

This project is devoted to my grandfather, who has a passion for model trains. It provides a simple and user-friendly way to control the lights and attractions in his model train room using a Raspberry Pi Pico and a 16x2 character LCD display. Since he isn't that great with computers, I will change the code on his demands, when he needs it. I thought to share it here to document my learning process, since this is the first time, I have ever done something like this.

## 🔦 Features 🔦

- Easily navigate through a menu of lights and attractions using up and down buttons
- Quickly toggle the state of the selected light or attraction on or off using a select button
- Clearly view the current state of the selected light or attraction on a 16x2 character LCD display

## 🛠️ Hardware Requirements 🛠️

- Raspberry Pi Pico
- 16x2 character LCD display (with I2C interface)
- 3 push buttons (for up, down and select)
- Jumper wires and breadboard (for prototyping)

## 💻 Software Requirements 💻

- Micropython firmware for Raspberry Pi Pico
- `esp8266_i2c_lcd` library for interfacing with the LCD display

## 🚀 Getting Started 🚀

1. Connect the hardware components as shown in the wiring diagram.
2. Install the Micropython firmware on your Raspberry Pi Pico.
3. Install the `esp8266_i2c_lcd` library on your Raspberry Pi Pico.
4. Copy the `main.py` file from this repository to your Raspberry Pi Pico.
5. Reset your Raspberry Pi Pico to start the program.

## 🕹️ Usage 🕹️

Use the up and down buttons to navigate through the menu of lights and attractions. The currently selected item will be shown on the LCD display along with its current state (on or off).

Press the select button to toggle the state of the selected light or attraction. The new state will be shown on the LCD display.

## 🙏 Acknowledgements 🙏

This project is dedicated to my grandfather, who has inspired me with his love for model trains. Thank you for sharing your passion with me.

## 📜 License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.