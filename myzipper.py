#!/usr/bin/python
"""
@author VoDo
@created  2019-05-20
@description

Create archives, which contain all relevant configuration files for a special scenario. 


"""
import sys
import os
import time

import zipfile

CONFIG_FILE = "myzipper.config"
TARGET_FILE = "backup_%s.zip"
##
# 
def read_listfile(list_filename=CONFIG_FILE):
  print("Read configuration from file '%s'" %list_filename)
  content = []
  with open(list_filename) as f:
    content = f.readlines()
  
  content = [entry.replace('\n', '').replace('\r', '') for entry in content]
  
  return content

##
#
def add_file(zf, file_name):
  abs_filename = os.path.abspath(file_name)
  zf.write(abs_filename)
##
#
def add_dir(zf, file_path):
  for dirname, subdirs, files in os.walk(file_path):
      zf.write(os.path.abspath(dirname))
      for filename in files:
          abs_filename = os.path.abspath(os.path.join(dirname, filename))
          zf.write(abs_filename)
          

##
#
def main(args):

  all_entries = read_listfile()

  time_string = time.strftime("%Y_%m_%d-%H-%M-%S", time.localtime())
  zip_file = TARGET_FILE %time_string
  print("writing to file %s" %zip_file)

  try:
    zf = zipfile.ZipFile(zip_file, "w")
    for entry in all_entries:
      if (os.path.isfile(entry)):
        print("add '%s'" %entry)
        add_file(zf, entry)
      elif(os.path.isdir(entry)):
        print("add '%s'" %entry)
        add_dir(zf, entry)
      else:
        print("ERROR: unknown file type %s" %entry)
  finally:
    zf.close()


if __name__ == '__main__':
  main(None)

