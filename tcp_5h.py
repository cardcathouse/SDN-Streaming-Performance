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
    
    info('*** Starting network\n')
    net.build()
    info('*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info('*** Starting switches\n')
    net.get('s1').start([c0])
    net.get('s2').start([c0])

    info('*** Post configure switches and hosts\n')

    myScript = "tcp_test_tasks_5h.sh"
    CLI(net, script=myScript)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()
