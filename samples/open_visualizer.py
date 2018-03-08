
import sys, string, os
import os
import subprocess





#os.spawnl(r"C:\Program Files (x86)\Leap Motion\Core Services\Visualizer.exe")




si = subprocess.STARTUPINFO()

si=subprocess.Popen([r"C:\Program Files (x86)\Leap Motion\Core Services\Visualizer.exe"])
si.kill()

