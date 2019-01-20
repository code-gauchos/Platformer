# Platformer
A python project created at [Code Gauchos](codegauchos.com).
-------------------------
## Game Description:
You spawn in a randomly generated world, starting out with only a few items, but you can get better by killing monsters, mining, etc. As you get better, missions start to pop up, in a mission, you choose the items you would like to bring, and then there will be waves of monsters and finally a boss battle.

### Main Goals:
- [ ] Implement a 2D platformer for the PC using the [Kivy Library](https://kivy.org)
- [ ] Make it playable through a controller made with a Arduino or RPI
- [ ] Create sound effects and music
- [ ] Create sprites and backgrounds
- [ ] Bow to shoot enemies (Hold a button and aim w/ joystick)
- [ ] Python read image with Pillow for level loading

### Materials:
- [x] Breadboard
- [x] 2 Buttons (3?)
- [x] Arduino Gemino Uno
- [x] 8 wires
- [x] 2 10k resistors (3?)
- [x] Power kit
- [x] 360 Joystick

### 3rd party libraries:
_(Install all by running **libs.bat**)_
+ [Kivy](https://pypi.org/project/Kivy/): To handle graphics and window creation
+ [PySerial](https://pypi.org/project/pyserial/): To handle serial communication with the arduino controller
+ [Final-Class](https://pypi.org/project/final-class/): To be able to declare certain classes final so that the user cannot extend and override them. Cleaner API.
+ [Pillow](https://pypi.org/project/Pillow/): To handle image pixel reading and writing. Used to adjust lighting and read level files.

### Questions:
* Learn how to use <a href="https://pyserial.readthedocs.io/en/latest/">PySerial</a>
* See how to connect serial on PC
