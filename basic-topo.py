from mininet.topo import Topo

from mininet.net import Mininet

from mininet.node import OVSController

from mininet.cli import CLI

class DDOSTopology(Topo):

    def build(self):

        switch = self.addSwitch('s1')

        # Add normal hosts

        for i in range(1, 4):

            host = self.addHost(f'h{i}')

            self.addLink(host, switch)

        # Add attacker hosts

        for j in range(4, 7):

            attacker = self.addHost(f'h{j}')

            self.addLink(attacker, switch)

def start_network():

    topo = DDOSTopology()

    net = Mininet(topo=topo, controller=OVSController)

    net.start()

    CLI(net)

    net.stop()

if __name__ == '__main__':

    start_network()

