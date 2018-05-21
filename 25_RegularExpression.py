import re

t = re.match("[A-Z]{3}[PCFL]{1}[A-Z]{1}[0-9]{4}[A-Z]{1}","AODPN9532H")

if(t):
    print("match")
else:
    print("no match")