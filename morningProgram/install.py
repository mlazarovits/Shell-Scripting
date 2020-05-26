# This is the installation script
# It assumes the default shell is bash and installs the 
# sending function in the .bash_profile file

import os
from run import *



HOME = os.getenv("HOME")
PATH = os.getcwd()

# def sh(script, msg = 0):
#   os.system("bash -c '%s'" % script)

#figure out a better way to check installation
os.chdir(HOME)
bashFile = open(".bash_profile","r")
bashLines = bashFile.readlines()
bashFile.close()
bashFile = open(".bash_profile", "a")
f = open(PATH + "/bash_function.txt", "r")

found = False
print("Installing 'send' program into bash...")
for line in f:
  if line not in bashLines:
    bashFile.write(line)  
  else: 
    found = True



# if not os.path.exists("done.txt"): # hacky way to tell the install.py hasn't already been run
  # print("Installing 'send' program into bash...")
  # os.chdir(HOME)

  # b = open(".bash_profile", "a")
  # f = open(PATH + "/bash_function.txt", "r")
  # for line in f:
  #   b.write(line)
  # b.write("  osascript " + PATH + "/sendMessage.applescript \"$contact\" \"$msg\"\n")
  # b.write("}\n")
  # b.write("export -f send\n")

  # r = open(PATH + "/done.txt", "a")
  # r.write("Installation complete.\n")
bashFile.close()

if found:
  print("Already Installed")
sh("source .bash_profile")
os.chdir(PATH)
# else:
#   print("Already installed")

print("---")
print("Installed sending capabilities (iMessage only).")
print("Please start a new terminal window (Cmd-T) to test the new capabilities.")
print("To send a message, type: <send \"Contact Name\" \"Message\"> in the command line.")
print("Alternatively, you can mess with the 'run.py' function to schedule your own messages.")
print("---")
print("By Gabe Schoenbach")
