import os
from datetime import datetime
import time
import random

def main():
  def sh(script, msg = 0):
      os.system("bash -c '%s'" % script)

#  sh("echo Running bash in Python...")
 
  contacts = ['"Gabe Schoenbach"', '"Daven Crossland"',
              '"Helena Thomas"', '"Alex Cintron"',
              '"Erika Steiner"', '"Scott Ellenoff"',
              '"Kahlan Lee-Lermer"', '"Rowan Schneider"',
              '"Jackson Mariotti"', '"Jake Gosselin"',
              '"Ken Ito"']

  greetings = ['"Good morning!"', 
               '"morning bud!"', 
               '"Good morning! Did you sleep well?"',
               '"Morning beautiful ;)"', 
               '"Rise and shine!"', 
               '"Hey! How did you sleep?"',
               '"Time to get up, sleepyhead..."',
               '"Hope you have a nice day!"',
               '"Sleep well?"',
               '"Good morning sunshine!"',
               '"Wakey, wakey, eggs and bakey!"',
               '"Any morning seeing your sweet face is a good morning, indeed :)"',
               '"Top o\' the mornin\' to ya!"',
               '"Get your butt out of bed!!"',
               '"Every morning is good when I think about how lucky I am to have a friend like you!"',
               '"Wishing you a day full of sunny smiles and happy thoughts. Good morning!"',
               '"This is not just another day. It is yet another chance to make your dreams come true. Get up and get started. Good morning!"']

  random.shuffle(greetings)

  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print("Started scheduling at:", current_time) 
  print("Will send messages to:", [friend for friend in contacts])
 
  i = 0;
  while True:
    now = datetime.now().strftime("%H:%M:%S")
    if now[:2] == '08': 
      for friend in contacts:
        sh('send ' + friend + ' ' + greetings[i % len(greetings)])
        continue;  
      time.sleep(3600) 
      i += 1
    else:
      print("Checked time at: ", now) 
      time.sleep(3600)

main()
