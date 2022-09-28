### Created during ACE-L5 training for challenge lab 12.1
### python scritp used to pull variables from yaml file in 
### script and use to build base eBGP and Interface configs
### Will Goss - williamgoss@arista.com

import yaml

##### loading above Config into yaml file
with open("eBGP-configs.yaml", "r") as file:
  switches = yaml.safe_load(file)


hostname = input("enter switch name: ")


with open(hostname".txt", 'a') as out:
  out.write()

#### script to create code
print("!!!! BGP CONFIG !!!!")
#builds standard BGP routing services, prefix-lists, route-maps, and Peer-filter
print("service routing protocols model multi-agent")
print("!")
print("ip prefix-list LOOPBACK")
print("  permit 192.168.101.0 255.255.255.0 le 32")
print("  permit 192.168.102.0 255.255.255.0 le 32")
print("  permit 192.168.201.0 255.255.255.0 le 32")
print("  permit 192.168.202.0 255.255.255.0 le 32")
print("!")
print("route-map LOOPBACK permit 10")
print("match ip address prefix-list LOOPBACK")
print("!")
print("!")
#idetnify ASN for BGP instance for spcific host and set proper router ID
asn = switches[hostname]['BGP']['ASN']
print("router bgp %s" % asn)
routerid = switches[hostname]['interfaces']['loopback0']['ipv4']
print("  router-id %s" % routerid)
print("  no bgp default ipv4-unicast")
print("  maximum-path 3")
print("  distance bgp 20 200 200")
hostnamefirst2 = hostname[0:2]
if hostnamefirst2 == "sp":
    print("  bgp listen range 192.168.0.0/16 peer-group LEAF_Underlay peer-filter LEAF-AS-RANGE")
    print("  neighbor LEAF_Underlay peer group")
    print("  neighbor LEAF_Underlay send-community")
    print("  neighbor LEAF_Underlay maximum-routes 12000")
    print("  redistribute connected route-map LOOPBACK")
    for peers in switches[hostname]['BGP']['BGP-Peers']:
    # iterate through all BGP Peers listed in YAML for specific host
      peerip = switches[hostname]['BGP']['BGP-Peers'][peers]['IP']
      peerasn = switches[hostname]['BGP']['BGP-Peers'][peers]['Peer_ASN']
      print("  neighbor %s peer group LEAF_Underlay") % peerip
      print("  neighbor %s remote-as %s") % (peerip, peerasn)
    print("  address-family ipv4")
    print("    neighbor LEAF_Underlay activate")
    print("    redistribute connected route-map LOOPBACK")
    print("!")
    print("!")
    print("!")
else:
    print("  neighbor SPINE_Underlay peer group")
    #### Need to add in DC1 Vs DC2 using .split fuction replace line below
    N=3
    length = len(hostname)
    hostnamelast = hostname[length - N:]
    if hostnamelast == "DC1":
      spineasn = "65100"
    else:
      spineasn = "65200"
 
    print("  neighbor SPINE_Underlay remote-as %s" % spineasn)
    print("  neighbor SPINE_Underlay send-community")
    print("  neighbor SPINE_Underlay maximum-routes 12000")
    print("  neighbor LEAF_Peer peer group")
    print("  neighbor LEAF_Peer remote-as %s" % asn)
    print("  neighbor LEAF_Peer next-hop-self")
    print("  neighbor LEAF_Peer maximum-routes 12000")

    #only adds DCI peer neighbor if its a borderswitch
    hostnamefirst3 = hostname[0:3]
    if hostnamefirst3 == "bor":
      print("  neighbor DCI_Peer peer group")
      print("  neighbor DCI_Peer remote-as 65000")
      print("  neighbor DCI_Peer next-hop-self")
      print("  neighbor DCI_Peer maximum-routes 12000")

    print("  redistribute connected route-map LOOPBACK")

    # iterate through all BGP Peers listed in YAML for specific host
    for peers in switches[hostname]['BGP']['BGP-Peers']:
      peerip = switches[hostname]['BGP']['BGP-Peers'][peers]['IP']
      peerasn = switches[hostname]['BGP']['BGP-Peers'][peers]['Peer_ASN']
      if peerasn == asn:
        print("  neighbor %s peer group LEAF_Peer" % peerip)
      elif peerasn == 65000:
        print("  neighbor %s peer group DCI_Peer" % peerip)
      else:
        print("  neighbor %s peer group SPINE_Underlay" % peerip)
    print("  address-family ipv4")
    print("    neighbor LEAF_Peer activate")
    print("    neighbor SPINE_Underlay activate")
    if hostnamefirst3 == "bor":
        print("    neighbor DCI_Peer activate")
    
    print("    redistribute connected route-map LOOPBACK")
    print("!")
    print("!")
    print("!")
#Iterate through all interfaces using iface variable as the incrementing index
print("!!!! Interface Config !!!!")
for iface in switches[hostname]['interfaces']:
    print("interface %s" % iface)
    #Pull variables into easier to use variables
    ip = switches[hostname]['interfaces'][iface]['ipv4']
    mask = switches[hostname]['interfaces'][iface]['mask']
    print(" ip address %s/%s" % (ip, mask))
    #Check if the interface name contains "Ethernet", as it will need "no switchport"
    if "Ethernet" in iface:
        print(" no switchport")