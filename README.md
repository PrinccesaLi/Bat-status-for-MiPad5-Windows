# Xiaomi Mi Pad 5 Battery Threshold

This program is designed to reboot your Android tablet if it is discharged to the threshold you specified.

## Instructions for use:
1) Unpack the program and all files from zip to a separate folder on drive C.
2) Specify battery thresholds in the config-bats.ini file.
3) Specify the path to the shortcut .lnk file for slota-switchtoandroid.bat (slotb-switchtoandroid.bat). You can place the shortcut in the same folder as the program.
4) Give the shortcut permission to run as administrator.
5) Add a shortcut to the Bat-status.exe program to the startup folder (along the shell:startup path).

## Configuration file config-bats.ini

[Battery]

Threshold = 10

[Shortcut]

Path = "To add to a label, add one backslash \ to the others \, getting rid of all quotes"

## setting config-bats.ini

Threshold: Specifies the battery charge threshold in percent. When this battery level is reached, the tablet will automatically restart.
Path: path to the program's shortcut. You must specify the path to the slota-switchtoandroid.bat or slotb-switchtoandroid.bat shortcut. For the program to work correctly, the shortcut must be in the same folder with the program.
For all questions, please contact the author of the program. 





