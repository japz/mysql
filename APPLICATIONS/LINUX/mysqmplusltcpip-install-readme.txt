==================================================================================
mySQMPLUSL TCPIP Linux Application for mySQM+ controllers (TCP/IP)
(c) Robert Brown 2019-2022. All rights reserved.
==================================================================================

==================================================================================
USING mySQM+ CONTROLLERS WITH LINUX
==================================================================================
There are a number of ways you can use a mySQM+ Weather Controller with Linux systems.

1. This Linux application 
2. mySQM+controller configured for TCP/IP ACCESSPOINT or STATIONMODE
or

mySQMPLUSLTCPIP LINUX APPLICATION
The provided LINUX application was developed and tested on UBUNTU with the MATE desktop environment, and supports TCP/IP connections to a mySQM+ controller.

After recompiling the source code, copy the recompiled executable file mysqmplusltcpip AND mysqmplusltcpip.ini files to a user folder on your Linux system (like a folder under the desktop)


mysqmplusltcpip.ini SETTINGS INI FILE
This file is used to save and restore the application settings.


CHANGE CONTROLLER IP ADDRESS SETTINGS IN THE mysqmplusltcpip.ini .ini FILE
The INI file will need changing. There is a string for the variable ipaddr which looks like


ipaddr=192.168.4.1

You will need to change the ipaddr string to what is used for your system.


CHANGE LOG FILE LOCATION SETTINGS IN THE mysqmplusltcpip.ini FILE
The mysqmplusltcpip.ini file will need changing. There is a string for the variable logfilepath which looks like

logfilepath=

You will need to specify the path where your log files will be stored. The path below points to user bob’s home folder, and there is a folder on bob’s desktop called myLogFiles

logfilepath=/home/bob/Desktop/myLogFiles

After making the required changes to the mysqmplusltcpip.ini file, save the file.

Alternatively, when the application runs the first time, it will detect that the logfile path has not been specified in the INI file and ask you to specify the folder where the log files can be saved. Once this is specified, then the log path is saved for future use.


REQUIRED GROUP PERMISSION
You must be a member of the group tty (Ubuntu-Mate) (others are the dialout group)
Use menu, administration, users and groups, manage groups, tty, properties
and ensure that your name is checked, then click OK


FLAG APPLICATION AS EXECUTABLE
Run a terminal window (as root) in the folder and change permissions of file

chmod +x mysqmplusltcpip

or you can right mouse click the file, properties, permissions and check allow 
executing file as program.


OTHER LINUX SYSTEMS
You will need to recompile the source code using Lazarus Pascal, in order to run the application on a different Linux system (or Raspberry Pi).


INSTALL THE ARDUINO IDE
To install the Arduino IDE so you can program the controller, open a terminal window and type the following commands

sudo apt-get update
sudo apt-get install Arduino


INSTALL LAZARUS
If you need to recompile the source code, you will need to install Lazarus

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install fpc
sudo apt-get install Lazarus


RE-COMPILING THE SOURCE
To recompile the source, download the source files and extract the zip file into a folder. In that folder, open the mysqmplusl.lpi file in Lazarus and then from the menu bar select Run-Compile. Once the program is built, the mysqmplusltcpip file can be executed.

When the program is first executed, and you did not specify where the log files are to saved, the application will first ask where to save the log files. After selecting a folder location, the application will save the log file path and continue.


PLEASE READ THE DOCUMENTS FOR MORE INFORMATION
The documents are located in the Zip file under the Documents folder. 


