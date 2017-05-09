#!/usr/bin/env python
#
# Kai Windle (c) 09/05/2017
# Enables a Nexus 5 AVD with
# a proxy thats been specifed
#

import os
import sys
#import subprocess 

PORT = 8080
HOST = "10.10.130.91"
SDK_PATH = ""

# Stackoverflow for this
def file_exists(file_path):
    """ Handle the file path being none or empty string """
    if not file_path:
        return False
    elif os.path.exists:
        return True
    elif not os.path.isfile(file_path):
        return False
    elif not os.path.isdir(file_path):
        return False

def check_platform():
    if sys.platform == "darwin":
        print("darwin")
        return "MacOS"
    elif sys.platform == "freebsd":
        return "FreeBSD"
    elif sys.platform == "linux":
        return "Linux"
    else:
        return "none"

def start_emulator_nexus_five(proxy):
    """ Allows the emulator to be started with or
    without a proxy using the above details """

    cmd = SDK_PATH + "/tools/emulator -netdelay none -netspeed full -avd Nexus_5_API_23"
    if proxy:
        cmd += " -http-proxy " + HOST + ":" + str(PORT)
        print("Starting emulator with Proxy port: " + str(PORT))
        os.system(cmd)
        #process = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
        #(result, error) = process.communicate()
        #rc = process.wait()
    else:
        print("Starting emulator without proxy")
        os.system(cmd)
        #process = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
        #(result, error) = process.communicate()
        #rc = process.wait()

if check_platform() == "MacOS":
    if file_exists(os.getenv("HOME") + "/Library/Android"):
        SDK_PATH = os.getenv("HOME") + "/Library/Android/sdk/"
        #print("sdk: " + SDK_PATH)
        start_emulator_nexus_five(True)
else:
    print("Sorry os not supported right now")



