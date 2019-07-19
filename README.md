# macvendor
This repo has two files

1- findmacvend.py :
    This is the main python file which takes in user input of MAC address
    at linux command line and does a mac lookup in the mac address database
    'https://macaddress.io/database/macaddress.io-db.json'
    If the mac address entered by the user is found in the database then
    it prints out the vendor name to whom that mac address has been assigned.
    
 2- Dockerfile:
    This is the docker file which has the instructions to build dockerized image
    for the python file findmacvend.py.
     
 
 Command Example at linux prompt:
 
wasim@kmaster:~/py$ python3 findmac.py 
Enter mac address: DC:A2:66
OUI vendor for mac DC:A2:66 is Hon Hai Precision Ind. Co, Ltd


