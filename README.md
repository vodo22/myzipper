# myzipper

Simple script to backup config files and folders

2019-05-20
VoDo 
volker.dorna@gis-ag.com

## What is it good for?
The idea is to have a script, which stores  config files and folders, which are spread over the system-

## How to handle
List all files and folders in the config file, which should be stored in zip file (one per line).

When you  run the script, a zip file is created with the current timestamp.
All files and folders from the config are then stored with their absolute path.

If you run the script scheduled, you have a backup of the relevant config files.

