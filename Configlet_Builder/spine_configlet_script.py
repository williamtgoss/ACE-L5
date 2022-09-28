### Created during ACE-L5 training for challenge lab 12.1
### python scritp used to pull variables from yaml file in 
### script and use to build base eBGP and Interface configs
### Will Goss - williamgoss@arista.com


import yaml

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
"""

##### loading above Config into yaml file

switches = yaml.load(config)

#### script to create code
print("!!!! BGP CONFIG !!!!")
#builds standard BGP routing services, prefix-lists, route-maps, and Peer-filter
print("service routing protocols model multi-agent")
print("!")
print("ip prefix-list LOOPBACK")
print("  permit 192.168.101.0 255.255.255.0")
print("  permit 192.168.102.0 255.255.255.0")
print("  permit 192.168.201.0 255.255.255.0")
print("  permit 192.168.202.0 255.255.255.0")
print("!")
print("route-map LOOPBACK permit 10")
print("match ip address prefix-list LOOPBACK")
print("!")
print("peer-filter LEAF-AS-RANGE")
print("10 match as-range 65000-65535 result accept")
print("!")
#idetnify ASN for BGP instance for spcific host and set proper router ID
asn = switches['leaf1-DC1']['BGP']['ASN']
print("router bgp %s") % asn
routerid = switches['leaf1-DC1']['interfaces']['loopback0']['ipv4']
print("  router-id %s") % routerid 
print("  no bgp default ipv4-unicast")
print("  maximum-path 3")
print("  distance bgp 20 200 200")
print("  bgp listen range 192.168.0.0/16 peer-group LEAF_Underlay peer-filter LEAF-AS-RANGE")
print("  neighbor LEAF_Underlay peer group")
print("  neighbor LEAF_Underlay send-community")
print("  neighbor LEAF_Underlay maximum-routes 12000")
print("  redistribute connected route-map LOOPBACK")
for peers in switches['leaf1-DC1']['BGP']['BGP-Peers']:
# iterate through all BGP Peers listed in YAML for specific host
  peerip = switches['leaf1-DC1']['BGP']['BGP-Peers'][peers]['IP']
  peerasn = switches['leaf1-DC1']['BGP']['BGP-Peers'][peers]['Peer_ASN']
  print("  neighbor %s peer group LEAF_Underlay") % peerip
  print("  neighbor %s remote-as %s") % (peerip, peerasn)
print("  address-family ipv4")
print("    neighbor LEAF_Underlay activate")
print("    redistribute connected route-map LOOPBACK")
print("!")
print("!")
print("!!!! Interface Config !!!!")
for iface in switches['leaf1-DC1']['interfaces']:
#Iterate through all interfaces using iface variable as the incrementing index
    print("interface %s") % iface
    #Pull variables into easier to use variables
    ip = switches['leaf1-DC1']['interfaces'][iface]['ipv4']
    mask = switches['leaf1-DC1']['interfaces'][iface]['mask']
    print(" ip address %s/%s") % (ip, mask)
    #Check if the interface name contains "Ethernet", as it will need "no switchport"
    if "Ethernet" in iface:
        print(" no switchport")