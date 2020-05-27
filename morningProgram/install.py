# This is the installation script
# It assumes the default shell is bash and installs the 
# sending function in the .bash_profile file

import os


def sh(script, msg = 0):
  os.system("bash -c '%s'" % script)

def install():
  HOME = os.getenv("HOME")
  PATH = os.getcwd()


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

  bashFile.close()

  if found:
    print("Already Installed")
  sh("source .bash_profile")
  os.chdir(PATH)


  print("---")
  print("Installed sending capabilities (iMessage only).")
  print("Please start a new terminal window (Cmd-T) to test the new capabilities.")
  print("To send a message, type: <send \"Contact Name\" \"Message\"> in the command line.")
  print("Alternatively, you can mess with the 'run.py' function to schedule your own messages.")
  print("---")
  print("By Gabe Schoenbach")
