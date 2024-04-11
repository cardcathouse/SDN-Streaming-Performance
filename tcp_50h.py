#!/usr/bin/env python

import socket
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, Host
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink
from mininet.log import setLogLevel
import sys

def get_current_ip():
    return socket.gethostbyname(socket.gethostname())

def myNetwork():
    net = Mininet(topo=None, build=False, ipBase='10.0.0.0/8')

    info('*** Adding controller\n')
    c0 = net.addController(name='c0',
                           controller=RemoteController,
                           ip=get_current_ip(),
                           protocol='tcp',
                           port=6633)

    info('*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)

    info('*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)
    h9 = net.addHost('h9', cls=Host, ip='10.0.0.9', defaultRoute=None)
    h10 = net.addHost('h10', cls=Host, ip='10.0.0.10', defaultRoute=None)
    h11 = net.addHost('h11', cls=Host, ip='10.0.0.11', defaultRoute=None)
    h12 = net.addHost('h12', cls=Host, ip='10.0.0.12', defaultRoute=None)
    h13 = net.addHost('h13', cls=Host, ip='10.0.0.13', defaultRoute=None)
    h14 = net.addHost('h14', cls=Host, ip='10.0.0.14', defaultRoute=None)
    h15 = net.addHost('h15', cls=Host, ip='10.0.0.15', defaultRoute=None)
    h16 = net.addHost('h16', cls=Host, ip='10.0.0.16', defaultRoute=None)
    h17 = net.addHost('h17', cls=Host, ip='10.0.0.17', defaultRoute=None)
    h18 = net.addHost('h18', cls=Host, ip='10.0.0.18', defaultRoute=None)
    h19 = net.addHost('h19', cls=Host, ip='10.0.0.19', defaultRoute=None)
    h20 = net.addHost('h20', cls=Host, ip='10.0.0.20', defaultRoute=None)
    h21 = net.addHost('h21', cls=Host, ip='10.0.0.21', defaultRoute=None)
    h22 = net.addHost('h22', cls=Host, ip='10.0.0.22', defaultRoute=None)
    h23 = net.addHost('h23', cls=Host, ip='10.0.0.23', defaultRoute=None)
    h24 = net.addHost('h24', cls=Host, ip='10.0.0.24', defaultRoute=None)
    h25 = net.addHost('h25', cls=Host, ip='10.0.0.25', defaultRoute=None)
    h26 = net.addHost('h26', cls=Host, ip='10.0.0.26', defaultRoute=None)
    h27 = net.addHost('h27', cls=Host, ip='10.0.0.27', defaultRoute=None)
    h28 = net.addHost('h28', cls=Host, ip='10.0.0.28', defaultRoute=None)
    h29 = net.addHost('h29', cls=Host, ip='10.0.0.29', defaultRoute=None)
    h30 = net.addHost('h30', cls=Host, ip='10.0.0.30', defaultRoute=None)
    h31 = net.addHost('h31', cls=Host, ip='10.0.0.31', defaultRoute=None)
    h32 = net.addHost('h32', cls=Host, ip='10.0.0.32', defaultRoute=None)
    h33 = net.addHost('h33', cls=Host, ip='10.0.0.33', defaultRoute=None)
    h34 = net.addHost('h34', cls=Host, ip='10.0.0.34', defaultRoute=None)
    h35 = net.addHost('h35', cls=Host, ip='10.0.0.35', defaultRoute=None)
    h36 = net.addHost('h36', cls=Host, ip='10.0.0.36', defaultRoute=None)
    h37 = net.addHost('h37', cls=Host, ip='10.0.0.37', defaultRoute=None)
    h38 = net.addHost('h38', cls=Host, ip='10.0.0.38', defaultRoute=None)
    h39 = net.addHost('h39', cls=Host, ip='10.0.0.39', defaultRoute=None)
    h40 = net.addHost('h40', cls=Host, ip='10.0.0.40', defaultRoute=None)
    h41 = net.addHost('h41', cls=Host, ip='10.0.0.41', defaultRoute=None)
    h42 = net.addHost('h42', cls=Host, ip='10.0.0.42', defaultRoute=None)
    h43 = net.addHost('h43', cls=Host, ip='10.0.0.43', defaultRoute=None)
    h44 = net.addHost('h44', cls=Host, ip='10.0.0.44', defaultRoute=None)
    h45 = net.addHost('h45', cls=Host, ip='10.0.0.45', defaultRoute=None)
    h46 = net.addHost('h46', cls=Host, ip='10.0.0.46', defaultRoute=None)
    h47 = net.addHost('h47', cls=Host, ip='10.0.0.47', defaultRoute=None)
    h48 = net.addHost('h48', cls=Host, ip='10.0.0.48', defaultRoute=None)
    h49 = net.addHost('h49', cls=Host, ip='10.0.0.49', defaultRoute=None)
    h50 = net.addHost('h50', cls=Host, ip='10.0.0.50', defaultRoute=None)
    h51 = net.addHost('h51', cls=Host, ip='10.0.0.51', defaultRoute=None)
    h52 = net.addHost('h52', cls=Host, ip='10.0.0.52', defaultRoute=None)

    info('*** Add links\n')
    net.addLink(s1, s2)
    # Limiting the bandwidth to 10Mbps
    net.addLink(h1, s1, cls=TCLink, bw=10)
    net.addLink(s1, h3)
    net.addLink(s2, h4)
    net.addLink(s2, h2)
    net.addLink(s2, h5)
    net.addLink(s2, h6)
    net.addLink(s2, h7)
    net.addLink(s2, h8)
    net.addLink(s2, h9)
    net.addLink(s2, h10)
    net.addLink(s2, h11)
    net.addLink(s2, h12)
    net.addLink(s2, h13)
    net.addLink(s2, h14)
    net.addLink(s2, h15)
    net.addLink(s2, h16)
    net.addLink(s2, h17)
    net.addLink(s2, h18)
    net.addLink(s2, h19)
    net.addLink(s2, h20)
    net.addLink(s2, h21)
    net.addLink(s2, h22)
    net.addLink(s2, h23)
    net.addLink(s2, h24)
    net.addLink(s2, h25)
    net.addLink(s2, h26)
    net.addLink(s2, h27)
    net.addLink(s2, h28)
    net.addLink(s2, h29)
    net.addLink(s2, h30)
    net.addLink(s2, h31)
    net.addLink(s2, h32)
    net.addLink(s2, h33)
    net.addLink(s2, h34)
    net.addLink(s2, h35)
    net.addLink(s2, h36)
    net.addLink(s2, h37)
    net.addLink(s2, h38)
    net.addLink(s2, h39)
    net.addLink(s2, h40)
    net.addLink(s2, h41)
    net.addLink(s2, h42)
    net.addLink(s2, h43)
    net.addLink(s2, h44)
    net.addLink(s2, h45)
    net.addLink(s2, h46)
    net.addLink(s2, h47)
    net.addLink(s2, h48)
    net.addLink(s2, h49)
    net.addLink(s2, h50)
    net.addLink(s2, h51)
    net.addLink(s2, h52)

    info('*** Starting network\n')
    net.build()
    info('*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info('*** Starting switches\n')
    net.get('s1').start([c0])
    net.get('s2').start([c0])

    info('*** Post configure switches and hosts\n')

    myScript = "tcp_test_tasks.sh"
    CLI(net, script=myScript)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()
