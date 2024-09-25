#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""

def main():
    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print(list1)
    
    #Only displays Arista_eos
    print(list1[1])
    
    list2 = ["juniper"]

    list1.extend(list2)

    #print list1 and add list2
    print(list1)

main()

