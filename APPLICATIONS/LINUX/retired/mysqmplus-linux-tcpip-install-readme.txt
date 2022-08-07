==================================================================================
mySQMPLUSL TCPIP Linux Application for mySQM+ controllers (TCP/IP)
(c) Robert Brown 2019-2021. All rights reserved.
==================================================================================

==================================================================================
USING mySQM+ CONTROLLERS WITH LINUX
==================================================================================
There are a number of ways you can use a mySQM+ Weather Controller with Linux systems.

1. This Linux application 
2. mySQM+controller configured for TCP/IP ACCESSPOINT or STATIONMODE


mySQMPLUSLTCPIP LINUX APPLICATION
The provided LINUX application was developed and tested on UBUNTU with the MATE desktop environment, and supports TCP/IP connections to a mySQM+ controller.

After recompiling the source code, copy the recompiled executable file mysqmplusltcpip AND mysqmplusltcpip.ini files to a user folder on your Linux system (like a folder under the desktop)


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
















