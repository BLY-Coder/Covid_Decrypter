#!/usr/bin/env python

import sys
import os
import signal
from colorama import *
import zlib
import pprint

import PIL.Image
import pyzbar.pyzbar
import base45
import cbor2

#Ctrl+C

def signal_handler(sig, frame):
    print("\n[!] Saliendo...")
    sys.exit(1)
signal.signal(signal.SIGINT, signal_handler)
init()

def image():
	print("\n")
	print(Fore.RED+"	██████╗	 ██████╗      ██████╗ ██████╗ ██╗   ██╗██╗██████╗     ██████╗ ███████╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗███████╗██████╗")
	print(Fore.RED+"	██╔═══██╗██╔══██╗    ██╔════╝██╔═══██╗██║   ██║██║██╔══██╗    ██╔══██╗██╔════╝██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗")
	print(Fore.RED+"	██║   ██║██████╔╝    ██║     ██║   ██║██║   ██║██║██║  ██║    ██║  ██║█████╗  ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   █████╗  ██████╔╝")
	print(Fore.RED+"	██║▄▄ ██║██╔══██╗    ██║     ██║   ██║╚██╗ ██╔╝██║██║  ██║    ██║  ██║██╔══╝  ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██╔══╝  ██╔══██╗")
	print(Fore.RED+"	╚██████╔╝██║  ██║    ╚██████╗╚██████╔╝ ╚████╔╝ ██║██████╔╝    ██████╔╝███████╗╚██████╗██║  ██║   ██║   ██║        ██║   ███████╗██║  ██║")
	print("	 ╚══▀▀═╝ ╚═╝  ╚═╝     ╚═════╝ ╚═════╝   ╚═══╝  ╚═╝╚═════╝     ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚══════╝╚═╝  ╚═╝")
	print(Style.RESET_ALL)

img = input("\n[*]Introduce el nombre o path del QR: ")
os.system("/usr/bin/clear")

def decode():

	data = pyzbar.pyzbar.decode(PIL.Image.open(img))
	cert = data[0].data.decode()

	b45data = cert.replace("HC1:", "")

	zlibdata = base45.b45decode(b45data)

	cbordata = zlib.decompress(zlibdata)

	decoded = cbor2.loads(cbordata)

	pprint.pprint(cbor2.loads(decoded.value[2]))


if __name__ == '__main__':
	image()
	decode()
