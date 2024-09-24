#!/usr/bin.env 

# Creates list
ip_list = [ 5060, "80", 55, ["10.0.0.1","10.20.30.1"]]
#displays only the IPs in the list above.

print(f"The only IPs are {ip_list[3][:]}.")

