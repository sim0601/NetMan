#!/usr/bin/env python3

import NMtcpdump
import NMaws
import NMsnmp

fileName = 'lab5obj2.pcap'

NMtcpdump.checkFile(fileName)
NMtcpdump.read_file(fileName)

NMaws.create()
NMaws.push()
NMaws.list_con_del()
NMsnmp.do_it_all()
