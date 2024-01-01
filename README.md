# Blink-Camera-Always-On
A python script to always keep a Blink camera on

Blink cameras, owned and produced by Amazon, do not have an option to keep the camera's feed running without user input every minute. Furthermore, Blink does not officially have support for Windows, Mac OS, or Linux. This repository has instruction on how to get the Blink app up and running on any PC as well as keeping the live-feed from the cameras rolling 24/7. To begin, check the "Instructions" document for step-by-step instructions on what to do and how to use the python scripts in the repository.

# Tested on Macos Ventura
python 3.11.6; configured on automaticly vertical splited screen, and Blink App on the right side, it is work.
`````````
```sh
pip3 install pyautogui
pip3 install pynput
python3 Monitor_Calibration_Tool.py
python3 Blink_Active_Feed.py
```
