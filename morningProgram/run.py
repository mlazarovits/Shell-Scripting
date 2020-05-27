import os
import sys
from datetime import datetime
import time
import random
import argparse
from install import sh


def main():
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




  parser = argparse.ArgumentParser()
  parser.add_argument('contacts',type=str,nargs='+',help='contacts to text')
  parser.add_argument('-m','--message',metavar='message',type=str,default=random.choice(greetings),help='message to send')
  args = parser.parse_args()


  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  send_hr = '08'
  print("Started scheduling at:", current_time) 
  print("Will send {} to {} within the hour of {}".format(args.message,args.contacts,send_hr))


  sent = False;
  while not sent:
    now = datetime.now().strftime("%H:%M:%S")
    if now[:2] == send_hr: 
      for friend in args.contacts:
        sh('send "' + friend + '" "' + args.message+'" ')
        print('Sent message(s)!')
        sent = True
        return
    else:
      print("Checked time at: ", now) 
      time.sleep(3600) #check every hour






main()
