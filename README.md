* DISCLAIMER: this project only works on an Arduino kit. Import the necessary files using "import engi1020" in terminal alongside "import pygame".
  
# Arduino-Music-Encryptor

# Overview
An encryption method that is implemented using the Arduino kit that encrypts messages using music and frequencies.
The project focuses on specific music files that have been passed into the code (**attached in the file**) and only those can be selected for the purpose of visualisation and these values can be interchanged.
As a message can be decoded into a specific pattern, that may be passed along as a series of notes and those notes can be played to reveal the crypted message.

## Task
Use the rotary dial to select the notes.
Each note is assigned to a value in the rotary dial in the range of 0-1023.
Use the button to confirm the selection of a note.
To finish selection of notes, make a sound physically to exceed the predetermined threshold of the sound sensor (**The value depends on location**) to exit loop.
Once the notes are selected, the music should play in that order
### Some notes to keep in mind
12 notes are used in this example, the 13th note is a 'space' note that allows a delay of a specific period between the notes.
The LED should stay turned on during the duration of the sequence.
The buzzer must ring when there is an error.
Some possible errors can include not selecting a note, not pressing down the button or an infinite loop.
These errors are to be displayed on the LCD screen with a red background. 


## Libraries
These can be installed using the "pip install" command in the terminal.
* import engi1020
* import pygame
* from time import sleep
  
## Features
Rotary dial interface for selecting musical notes.

Plays selected notes in a specified order.

Simple and intuitive user interface.

## Sensors used in the process
1) Rotary dial for selecting notes - use "analog_read(0)"
2) Sound sensor for ending the note selection - use ""
3) Button to confirm the note selection - use "digital_read(6)"
4) LCD screen for the output - use "rgb_lcd_print()"
5) Speakers of the device
6) Buzzer to alert an error - use "buzzer_frequency()"
7) LED light to be turned on during the playing of the notes - use "digital_write()"



