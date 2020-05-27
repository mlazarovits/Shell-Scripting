## Installation
type `python install.py` from the command line

It will modify your .bash_profile file to append the following function:

    send () {
      contact=$1;
      msg=$2;
      echo "Sent $msg to $contact";
      osascript <<PATH_TO_MORNING_PROGRAM>>/morningProgram/sendMessage.applescript "$contact" "$msg"
    }
    export -f send


The function uses the sendMessage.applescript program to send an iMessage from the command line
using the syntax: `send "FirstName LastName" "message"`
where 'FirstName' and 'LastName' is a name in your Address Book.

Functionality:
Only works with bash — if you use zsh, you can manually add the 'send' function into your .zshrc
file in your home directory, and then send a message the same way. However, the run.py program
won't work without some futzing.
This also only works if Messages.app is already running, and you have had a previous conversation
with the person you are trying to send a message to.

## Usage
type `python run.py "FirstName LastName" [optional] -m "message"`
where `"FirstName LastName"` are the first and last names of the contact to text as the names appear in your Address Book. If no message is specified, one will be selected from a list of cute messages.

For a list of options, type `python run.py -h`
