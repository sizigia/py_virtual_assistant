#!/bin/sh
echo "Hey! We're about to create a virtual environment for your Virtual Assistant to work correctly on your computer."
echo "Would you like to proceed? (y/n)"
read confirmation;
if [ "$confirmation" == "y" ];
then
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
else
    echo "Okay, bye bye VA!"
fi
