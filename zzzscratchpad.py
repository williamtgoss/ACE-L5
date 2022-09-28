hostname = "leaf1-DC2"
hostnamefirst3 = hostname[0:3]
print(hostnamefirst3)
if hostnamefirst3 == "bor":
    print("  neighbor DCI_Peer peer group")
    print("  neighbor DCI_Peer remote-as 65000")
    print("  neighbor DCI_Peer next-hop-self")
    print("  neighbor DCI_Peer maximum-routes 12000")
