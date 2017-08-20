from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        H1 = self.addHost('H1')
        H2 = self.addHost('H2')
        H3 = self.addHost('H3')
        H4 = self.addHost('H4')
        S1 = self.addSwitch('S1')
        S2 = self.addSwitch('S2')
        S3 = self.addSwitch('S3')
        S4 = self.addSwitch('S4')

       # Add links
        self.addLink(H1, S1)
        self.addLink(S1, S2)
        self.addLink(S1, S4)
        self.addLink(S2, H2)
        self.addLink(S2, S3)
        self.addLink(S4, H4)
        self.addLink(S4, S3)
        self.addLink(S3, H3)

topos = { 'mytopo': ( lambda: MyTopo() ) }
