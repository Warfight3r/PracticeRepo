#create an app to read through files containing a list of IP addresses and to validate in a different file their validity.
#Steps to follow:-
#1. Learn how to read a file in python

#test.txt, include all the addresses
#read from it line by line
#call a get request for each line.
#save response with ip in a new file. 
import requests

f = open("IPAddresses.txt", "r")
ip = f.read()
print (ip)
r = requests.get(url = "https://google.com")
print(r.json())

