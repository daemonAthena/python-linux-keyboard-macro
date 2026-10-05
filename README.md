# Simple Keyboard Macro
> Dedicated to my girlfriend

The purpose of this program is to be a simple command line program that can be run in the background,
get activated by the user when the need arises while playing a videogame, and repeat keyboard input
in a deterministic manner for the user.

## Functionality
`alt + l` while the program is running will activate macro mode which will continually press the last key you pressed
on an interval (default is 1 second)

`alt + =` increases the speed of the macro so it will decrease the interval down to 0.1 seconds

`alt + |` decreases the speed of the macro increasing the interval up to 10 seconds

to disable the program simply press `alt + l` again to toggle it off or kill the terminal application.

## Future plans
In the future I would like to make this a daemon that runs in the background instead of
a binary explicitly called by the user. This project is very much in the testing phase.

Adjust macro code to have a button which serves as an indicator "Im pressing this as a new button to repeat"
