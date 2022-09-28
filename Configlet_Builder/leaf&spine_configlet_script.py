### Created during ACE-L5 training for challenge lab 12.1
### python scritp used to pull variables from yaml file in 
### script and use to build base eBGP and Interface configs
### Will Goss - williamgoss@arista.com

import yaml
from cvplibrary import CVPGlobalVariables, GlobalVariableNames

hostname = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_SERIAL)

###########
config = """
leaf1-DC1:
    interfaces:
        loopback0:
            ipv4: 192.168.101.11
            mask: 32
            mtu: 9214
        loopback1:
            ipv4: 192.168.102.11
            mask: 32
            mtu: 9214
        Ethernet3:
            ipv4: 192.168.103.0
            mask: 31
            mtu: 9214
        Ethernet4:
            ipv4: 192.168.103.2
            mask: 31
            mtu: 9214
        Ethernet5:
            ipv4: 192.168.103.4
            mask: 31
            mtu: 9214
    BGP:
      ASN: 65101
      BGP-Peers:
        Peer1: 
          IP: 192.168.103.1
          Peer_ASN: 65100
        Peer2:
          IP: 192.168.103.3
          Peer_ASN: 65100
        Peer3:
          IP: 192.168.103.5
          Peer_ASN: 65100
        Peer4: 
          IP: 192.168.255.2
          Peer_ASN: 65101
leaf2-DC1:
    interfaces:
        loopback0:
            ipv4: 192.168.101.12
            mask: 32
            mtu: 9214
        loopback1:
            ipv4: 192.168.102.11
            mask: 32
            mtu: 9214
        Ethernet3:
            ipv4: 192.168.103.6
            mask: 31
            mtu: 9214
        Ethernet4:
            ipv4: 192.168.103.8
            mask: 31
            mtu: 9214
        Ethernet5:
            ipv4: 192.168.103.10
            mask: 31
            mtu: 9214
    BGP:
      ASN: 65101
      BGP-Peers:
        Peer1: 
          IP: 192.168.103.7
          Peer_ASN: 65100
        Peer2:
          IP: 192.168.103.9
          Peer_ASN: 65100
        Peer3:
          IP: 192.168.103.11
          Peer_ASN: 65100
        Peer4: 
          IP: 192.168.255.1
          Peer_ASN: 65101
leaf3-DC1:
    interfaces:
        loopback0:
            ipv4: 192.168.101.13
            mask: 32
            mtu: 9214
        loopback1:
            ipv4: 192.168.102.13
            mask: 32
            mtu: 9214
        Ethernet3:
            ipv4: 192.168.103.12
            mask: 31
            mtu: 9214
        Ethernet4:
            ipv4: 192.168.103.14
            mask: 31
            mtu: 9214
        Ethernet5:
            ipv4: 192.168.103.16
            mask: 31
            mtu: 9214
    BGP:
      ASN: 65102
      BGP-Peers:
        Peer1: 
          IP: 192.168.103.13
          Peer_ASN: 65100
        Peer2:
          IP: 192.168.103.15
          Peer_ASN: 65100
        Peer3:
          IP: 192.168.103.17
          Peer_ASN: 65100
        Peer4: 
          IP: 192.168.255.2
          Peer_ASN: 65102
leaf4-DC1:
    interfaces:
        loopback0:
            ipv4: 192.168.101.14
            mask: 32
            mtu: 9214
        loopback1:
            ipv4: 192.168.102.13
            mask: 32
            mtu: 9214
        Ethernet3:
            ipv4: 192.168.103.18
            mask: 31
            mtu: 9214
        Ethernet4:
            ipv4: 192.168.103.20
            mask: 31
            mtu: 9214
        Ethernet5:
            ipv4: 192.168.103.22
            mask: 31
            mtu: 9214
    BGP:
      ASN: 65102
      BGP-Peers:
        Peer1: 
          IP: 192.168.103.19
          Peer_ASN: 65100
        Peer2:
          IP: 192.168.103.21
          Peer_ASN: 65100
        Peer3:
          IP: 192.168.103.23
          Peer_ASN: 65100
        Peer4: 
          IP: 192.168.255.1
          Peer_ASN: 65102
borderleaf1-DC1:
    interfaces:
        loopback0:
            ipv4: 192.168.101.21
            mask: 32
            mtu: 9214
        loopback1:
            ipv4: 192.168.102.21
            mask: 32
            mtu: 9214
        Ethernet3:
            ipv4: 192.168.103.24
            mask: 31
            mtu: 9214
        Ethernet4:
            ipv4: 192.168.103.26
            mask: 31
            mtu: 9214
        Ethernet5:
            ipv4: 192.168.103.28
            mask: 31
            mtu: 9214
        Ethernet12:
            ipv4: 192.168.254.0
            mask: 31
            mtu: 9214
    BGP:
      ASN: 65103
      BGP-Peers:
        Peer1: 
          IP: 192.168.103.25
          Peer_ASN: 65100
        Peer2:
          IP: 192.168.103.27
          Peer_ASN: 65100
        Peer3:
          IP: 192.168.103.29
          Peer_ASN: 65100
        Peer4:
          IP: 192.168.254.1
          Peer_ASN: 65000
        Peer5: 
          IP: 192.168.255.2
          Peer_ASN: 65103
borderleaf2-DC1:
    interfaces:
        loopback0:
            ipv4: 192.168.101.22
            mask: 32
            mtu: 9214
        loopback1:
            ipv4: 192.168.102.21
            mask: 32
            mtu: 9214
        Ethernet3:
            ipv4: 192.168.103.30
            mask: 31
            mtu: 9214
        Ethernet4:
            ipv4: 192.168.103.32
            mask: 31
            mtu: 9214
        Ethernet5:
            ipv4: 192.168.103.34
            mask: 31
            mtu: 9214
        Ethernet12:
            ipv4: 192.168.254.2
            mask: 31
            mtu: 9214
    BGP:
      ASN: 65103
      BGP-Peers:
        Peer1: 
          IP: 192.168.103.31
          Peer_ASN: 65100
        Peer2:
          IP: 192.168.103.33
          Peer_ASN: 65100
        Peer3:
          IP: 192.168.103.35
          Peer_ASN: 65100
        Peer4:
          IP: 192.168.254.3
          Peer_ASN: 65000
        Peer5: 
          IP: 192.168.255.1
          Peer_ASN: 65103
spine1-DC1:
    interfaces:
        loopback0:
            ipv4: 192.168.101.101
            mask: 32
            mtu: 9214
        Ethernet2:
            ipv4: 192.168.103.1
            mask: 31
            mtu: 9214
        Ethernet3:
            ipv4: 192.168.103.7
            mask: 31
            mtu: 9214
        Ethernet4:
            ipv4: 192.168.103.13
            mask: 31
            mtu: 9214
        Ethernet5:
            ipv4: 192.168.103.19
            mask: 31
            mtu: 9214
        Ethernet6:
            ipv4: 192.168.103.25
            mask: 31
            mtu: 9214
        Ethernet7:
            ipv4: 192.168.103.31
            mask: 31
            mtu: 9214
    BGP:
      ASN: 65100
      BGP-Peers:
        Peer1: 
          IP: 192.168.103.0
          Peer_ASN: 65101
        Peer2:
          IP: 192.168.103.6
          Peer_ASN: 65101
        Peer3:
          IP: 192.168.103.12
          Peer_ASN: 65102
        Peer4:
          IP: 192.168.103.18
          Peer_ASN: 65102
        Peer5: 
          IP: 192.168.103.24
          Peer_ASN: 65103
        Peer6: 
          IP: 192.168.103.30
          Peer_ASN: 65103
spine2-DC1:
    interfaces:
        loopback0:
            ipv4: 192.168.101.102
            mask: 32
            mtu: 9214
        Ethernet2:
            ipv4: 192.168.103.3
            mask: 31
            mtu: 9214
        Ethernet3:
            ipv4: 192.168.103.9
            mask: 31
            mtu: 9214
        Ethernet4:
            ipv4: 192.168.103.15
            mask: 31
            mtu: 9214
        Ethernet5:
            ipv4: 192.168.103.21
            mask: 31
            mtu: 9214
        Ethernet6:
            ipv4: 192.168.103.27
            mask: 31
            mtu: 9214
        Ethernet7:
            ipv4: 192.168.103.33
            mask: 31
            mtu: 9214
    BGP:
      ASN: 65100
      BGP-Peers:
        Peer1: 
          IP: 192.168.103.2
          Peer_ASN: 65101
        Peer2:
          IP: 192.168.103.8
          Peer_ASN: 65101
        Peer3:
          IP: 192.168.103.14
          Peer_ASN: 65102
        Peer4:
          IP: 192.168.103.20
          Peer_ASN: 65102
        Peer5: 
          IP: 192.168.103.26
          Peer_ASN: 65103
        Peer6: 
          IP: 192.168.103.32
          Peer_ASN: 65103
spine3-DC1:
    interfaces:
        loopback0:
            ipv4: 192.168.101.103
            mask: 32
            mtu: 9214
        Ethernet2:
            ipv4: 192.168.103.5
            mask: 31
            mtu: 9214
        Ethernet3:
            ipv4: 192.168.103.11
            mask: 31
            mtu: 9214
        Ethernet4:
            ipv4: 192.168.103.17
            mask: 31
            mtu: 9214
        Ethernet5:
            ipv4: 192.168.103.23
            mask: 31
            mtu: 9214
        Ethernet6:
            ipv4: 192.168.103.29
            mask: 31
            mtu: 9214
        Ethernet7:
            ipv4: 192.168.103.35
            mask: 31
            mtu: 9214
    BGP:
      ASN: 65100
      BGP-Peers:
        Peer1: 
          IP: 192.168.103.4
          Peer_ASN: 65101
        Peer2:
          IP: 192.168.103.10
          Peer_ASN: 65101
        Peer3:
          IP: 192.168.103.16
          Peer_ASN: 65102
        Peer4:
          IP: 192.168.103.22
          Peer_ASN: 65102
        Peer5: 
          IP: 192.168.103.28
          Peer_ASN: 65103
        Peer6: 
          IP: 192.168.103.34
          Peer_ASN: 65103
leaf1-DC2:
    interfaces:
        loopback0:
            ipv4: 192.168.201.11
            mask: 32
            mtu: 9214
        loopback1:
            ipv4: 192.168.202.11
            mask: 32
            mtu: 9214
        Ethernet3:
            ipv4: 192.168.203.0
            mask: 31
            mtu: 9214
        Ethernet4:
            ipv4: 192.168.203.2
            mask: 31
            mtu: 9214
        Ethernet5:
            ipv4: 192.168.203.4
            mask: 31
            mtu: 9214
    BGP:
      ASN: 65201
      BGP-Peers:
        Peer1: 
          IP: 192.168.203.1
          Peer_ASN: 65200
        Peer2:
          IP: 192.168.203.3
          Peer_ASN: 65200
        Peer3:
          IP: 192.168.203.5
          Peer_ASN: 65200
        Peer4: 
          IP: 192.168.255.2
          Peer_ASN: 65201
leaf2-DC2:
    interfaces:
        loopback0:
            ipv4: 192.168.201.12
            mask: 32
            mtu: 9214
        loopback1:
            ipv4: 192.168.202.11
            mask: 32
            mtu: 9214
        Ethernet3:
            ipv4: 192.168.203.6
            mask: 31
            mtu: 9214
        Ethernet4:
            ipv4: 192.168.203.8
            mask: 31
            mtu: 9214
        Ethernet5:
            ipv4: 192.168.203.10
            mask: 31
            mtu: 9214
    BGP:
      ASN: 65201
      BGP-Peers:
        Peer1: 
          IP: 192.168.203.7
          Peer_ASN: 65100
        Peer2:
          IP: 192.168.203.9
          Peer_ASN: 65100
        Peer3:
          IP: 192.168.203.11
          Peer_ASN: 65100
        Peer4: 
          IP: 192.168.255.1
          Peer_ASN: 65201
leaf3-DC2:
    interfaces:
        loopback0:
            ipv4: 192.168.201.13
            mask: 32
            mtu: 9214
        loopback1:
            ipv4: 192.168.202.13
            mask: 32
            mtu: 9214
        Ethernet3:
            ipv4: 192.168.203.12
            mask: 31
            mtu: 9214
        Ethernet4:
            ipv4: 192.168.203.14
            mask: 31
            mtu: 9214
        Ethernet5:
            ipv4: 192.168.203.16
            mask: 31
            mtu: 9214
    BGP:
      ASN: 65202
      BGP-Peers:
        Peer1: 
          IP: 192.168.203.13
          Peer_ASN: 65200
        Peer2:
          IP: 192.168.203.15
          Peer_ASN: 65200
        Peer3:
          IP: 192.168.203.17
          Peer_ASN: 65200
        Peer4: 
          IP: 192.168.255.2
          Peer_ASN: 65202
leaf4-DC2:
    interfaces:
        loopback0:
            ipv4: 192.168.201.14
            mask: 32
            mtu: 9214
        loopback1:
            ipv4: 192.168.202.13
            mask: 32
            mtu: 9214
        Ethernet3:
            ipv4: 192.168.203.18
            mask: 31
            mtu: 9214
        Ethernet4:
            ipv4: 192.168.203.20
            mask: 31
            mtu: 9214
        Ethernet5:
            ipv4: 192.168.203.22
            mask: 31
            mtu: 9214
    BGP:
      ASN: 65202
      BGP-Peers:
        Peer1: 
          IP: 192.168.203.19
          Peer_ASN: 65200
        Peer2:
          IP: 192.168.203.21
          Peer_ASN: 65200
        Peer3:
          IP: 192.168.203.23
          Peer_ASN: 65200
        Peer4: 
          IP: 192.168.255.1
          Peer_ASN: 65202
borderleaf1-DC2:
    interfaces:
        loopback0:
            ipv4: 192.168.201.21
            mask: 32
            mtu: 9214
        loopback1:
            ipv4: 192.168.202.21
            mask: 32
            mtu: 9214
        Ethernet3:
            ipv4: 192.168.203.24
            mask: 31
            mtu: 9214
        Ethernet4:
            ipv4: 192.168.203.26
            mask: 31
            mtu: 9214
        Ethernet5:
            ipv4: 192.168.203.28
            mask: 31
            mtu: 9214
        Ethernet12:
            ipv4: 192.168.254.4
            mask: 31
            mtu: 9214
    BGP:
      ASN: 65203
      BGP-Peers:
        Peer1: 
          IP: 192.168.203.25
          Peer_ASN: 65200
        Peer2:
          IP: 192.168.203.27
          Peer_ASN: 65200
        Peer3:
          IP: 192.168.203.29
          Peer_ASN: 65200
        Peer4:
          IP: 192.168.254.5
          Peer_ASN: 65000
        Peer5: 
          IP: 192.168.255.2
          Peer_ASN: 65203
borderleaf2-DC2:
    interfaces:
        loopback0:
            ipv4: 192.168.201.22
            mask: 32
            mtu: 9214
        loopback1:
            ipv4: 192.168.202.21
            mask: 32
            mtu: 9214
        Ethernet3:
            ipv4: 192.168.203.30
            mask: 31
            mtu: 9214
        Ethernet4:
            ipv4: 192.168.203.32
            mask: 31
            mtu: 9214
        Ethernet5:
            ipv4: 192.168.203.34
            mask: 31
            mtu: 9214
        Ethernet12:
            ipv4: 192.168.254.6
            mask: 31
            mtu: 9214
    BGP:
      ASN: 65203
      BGP-Peers:
        Peer1: 
          IP: 192.168.203.31
          Peer_ASN: 65200
        Peer2:
          IP: 192.168.203.33
          Peer_ASN: 65200
        Peer3:
          IP: 192.168.203.35
          Peer_ASN: 65200
        Peer4:
          IP: 192.168.254.5
          Peer_ASN: 65000
        Peer5: 
          IP: 192.168.255.1
          Peer_ASN: 65203
spine1-DC2:
    interfaces:
        loopback0:
            ipv4: 192.168.201.101
            mask: 32
            mtu: 9214
        Ethernet2:
            ipv4: 192.168.203.1
            mask: 31
            mtu: 9214
        Ethernet3:
            ipv4: 192.168.203.7
            mask: 31
            mtu: 9214
        Ethernet4:
            ipv4: 192.168.203.13
            mask: 31
            mtu: 9214
        Ethernet5:
            ipv4: 192.168.203.19
            mask: 31
            mtu: 9214
        Ethernet6:
            ipv4: 192.168.203.25
            mask: 31
            mtu: 9214
        Ethernet7:
            ipv4: 192.168.203.31
            mask: 31
            mtu: 9214
    BGP:
      ASN: 65200
      BGP-Peers:
        Peer1: 
          IP: 192.168.203.0
          Peer_ASN: 65201
        Peer2:
          IP: 192.168.203.6
          Peer_ASN: 65201
        Peer3:
          IP: 192.168.203.12
          Peer_ASN: 65202
        Peer4:
          IP: 192.168.203.18
          Peer_ASN: 65202
        Peer5: 
          IP: 192.168.203.24
          Peer_ASN: 65203
        Peer6: 
          IP: 192.168.203.30
          Peer_ASN: 65203
spine2-DC2:
    interfaces:
        loopback0:
            ipv4: 192.168.201.102
            mask: 32
            mtu: 9214
        Ethernet2:
            ipv4: 192.168.203.3
            mask: 31
            mtu: 9214
        Ethernet3:
            ipv4: 192.168.203.9
            mask: 31
            mtu: 9214
        Ethernet4:
            ipv4: 192.168.203.15
            mask: 31
            mtu: 9214
        Ethernet5:
            ipv4: 192.168.203.21
            mask: 31
            mtu: 9214
        Ethernet6:
            ipv4: 192.168.203.27
            mask: 31
            mtu: 9214
        Ethernet7:
            ipv4: 192.168.203.33
            mask: 31
            mtu: 9214
    BGP:
      ASN: 65200
      BGP-Peers:
        Peer1: 
          IP: 192.168.203.2
          Peer_ASN: 65201
        Peer2:
          IP: 192.168.203.8
          Peer_ASN: 65201
        Peer3:
          IP: 192.168.203.14
          Peer_ASN: 65202
        Peer4:
          IP: 192.168.203.20
          Peer_ASN: 65202
        Peer5: 
          IP: 192.168.203.26
          Peer_ASN: 65203
        Peer6: 
          IP: 192.168.203.32
          Peer_ASN: 65203
spine3-DC2:
    interfaces:
        loopback0:
            ipv4: 192.168.201.103
            mask: 32
            mtu: 9214
        Ethernet2:
            ipv4: 192.168.203.5
            mask: 31
            mtu: 9214
        Ethernet3:
            ipv4: 192.168.203.11
            mask: 31
            mtu: 9214
        Ethernet4:
            ipv4: 192.168.203.17
            mask: 31
            mtu: 9214
        Ethernet5:
            ipv4: 192.168.203.23
            mask: 31
            mtu: 9214
        Ethernet6:
            ipv4: 192.168.203.29
            mask: 31
            mtu: 9214
        Ethernet7:
            ipv4: 192.168.203.35
            mask: 31
            mtu: 9214
    BGP:
      ASN: 65200
      BGP-Peers:
        Peer1: 
          IP: 192.168.203.4
          Peer_ASN: 65201
        Peer2:
          IP: 192.168.203.10
          Peer_ASN: 65201
        Peer3:
          IP: 192.168.203.16
          Peer_ASN: 65202
        Peer4:
          IP: 192.168.203.22
          Peer_ASN: 65202
        Peer5: 
          IP: 192.168.203.28
          Peer_ASN: 65203
        Peer6: 
          IP: 192.168.203.34
          Peer_ASN: 65203
"""

##### loading above Config into yaml file

switches = yaml.load(config)

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