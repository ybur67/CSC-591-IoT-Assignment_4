# Subscribe.py

## Introduction
This is the part of the forth assignment of 591-IoT. For this assignment, we are going to use Raspberry Pi and IBM Cloud to build a webapp for detecting the open and close of the door.  

## Discription
* Subscribe.py: Will listen to topic `Door` and print on command line.
* Publish.py: The file will publish Open and Close to topic `Door` by turns, and which will subscribe by subscribe.py.

## How to run it?
1. Get a IBM Cloud account
2. Install IBM Cloud CLI
3. Install Python3, and wiotp-sdk on your PC
4. Log in the IBM Cloud 
5. Run files Subscribe.py and Publish.py in two different terminals
6. Check the log on IBM Watson IoT platform and terminals

## How to run it with a Pi?
1. Get a IBM Cloud account
2. Install IBM Cloud CLI
3. Install Python3, and wiotp-sdk on your PC
4. Log in the IBM Watson IoT platform on website
5. Run `ibmcloud login`
6. Run `ibmcloud target --cf`
7. Run `ibmcloud cf push`
8. Start the code on Pi and start opening and closing the door


## Before running flask, run

`$ export FLASK_APP=subscribe`
