
#Requirements
1. 1080p screen resolution for it to position the image viewer window in the bottom right of the screen.

2. The gnome desktop environment. This comes by default on Ubuntu.

3. The package xdotool. Can be installed on Ubuntu by entering the following into the terminal:

```sh
sudo apt-get install xdotool
``` 

# Instalation Instructions
Put this floder in your home directory.

In a terimnal type:

```sh
nano .bashrc or nano /home/$username/.bashrc
```

Paste at the bottom of the file this line:

```sh
alias lastpic="python3 /home/$username/lastpic/lastpic.py"
```

# Guide for use

Type in the terminal "lastpic" to see the last image saved or modified in the $HOME/Pictures directory.

It can also be used to open up previous pics. Type "lastpic 2" for instance to open the second to last image.

This will open up the image and move the image viewing window to the bottom right on the screen. The script will then emulate a mouse click on the settings button on the window and emulate another mouseclick on the "always on top" option. This makes it so the image viewer window is always on top.
