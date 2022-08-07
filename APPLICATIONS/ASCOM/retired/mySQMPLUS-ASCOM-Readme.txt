ASCOM OBSERVING CONDITIONS DRIVER
mSQM+ ASCOM [TCP/IP and SERIAL]
(c) Robert Brown 2020-2021
All rights reserved.
brown_rb@yahoo.com

0.0.16
Delete serial usb interface support
Fix for socket timeout defaulting to 30s
Format cloudcover to 2 decimal places
Add handling of null property names in TimeSinceLastUpdate

0.0.15
Rewrite of device driver code

0.0.14
Passed ASCOM Conform
Fix for AveragePeriod Write 
Fix for error getting methods that were not supported

0.0.13
Fix for Sky Temperature - return IR Object value

0.0.12
Fix for COM port selected item not being saved

0.0.11
Correct rainrate description (mm over last hour)
Change rainrate to use current hourly total, not previous hour totals

0.0.10
Fix for RainRate and WindGusts

0.0.9
Add tab layout to form
Add Interface page with interface settings
Add Send On Connect tab
Add Display tab

0.0.8
Combine both TCP/IP and SERIAL USB interfaces into a single ASCOM driver

0.0.7
Add RainRate [mm in previous hour]

0.0.6
Change name of driver

0.0.5
Fix for return values timeout issue

0.0.4
Fix not returning updated values

0.0.3
Change throttling parameters
if WindSpeed = 0 return WindDirection as 0 - ASCOM rule

0.0.2
Fix for SQM
Fix for values not being updated on subsequent calls

0.0.1 02102019


Supported Actions
                supportedActions.Add("DewPoint");  
                supportedActions.Add("Humidity");
                supportedActions.Add("Pressure");
                supportedActions.Add("SkyBrightness");
                supportedActions.Add("SkyQuality");
                supportedActions.Add("SkyTemperature");
                supportedActions.Add("Temperature");
                supportedActions.Add("AveragePeriod");
                supportedActions.Add("CloudCover");
                supportedActions.Add("WindSpeed");
                supportedActions.Add("WindDirection");

