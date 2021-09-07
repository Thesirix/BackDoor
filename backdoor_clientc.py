
import socket
import time
import subprocess
import platform
import os
from PIL import ImageGrab

HOST_IP = "192.168.0.43"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

print(f"Connexion au serveur {HOST_IP}, port {HOST_PORT}")
while True:
