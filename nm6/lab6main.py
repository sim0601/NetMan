#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : lab6main.py
#purpose : A script to import all modules to SSH and configure iBGP
#date : 2018.03.09
#version : 1.1


import sshInfo
import validateIP
import connectivity
import bgp

fileName = "sshInfo.json"
fileName2 = "bgp.conf"
fileName3 = "sshInfo.json"

# refer to the module files for decription of each of the below imported functions

sshInfo.checkFile(fileName)
sshInfo.get_data(fileName)

validateIP.get_data_IP(fileName)
validateIP.val_IP()

connectivity.get_data_user(fileName)
connectivity.ping_test()

bgp.checkFile2(fileName2)
bgp.checkFile3(fileName3)
bgp.get_data_bgp(fileName2)
bgp.get_data_user2(fileName3)
bgp.config_ibgp()
bgp.sh_nei()
bgp.get_run()
