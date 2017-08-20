"""
Topooly for EL9333 Lab 5

    S1    S2
    | \  / |
    |  \/  |
    |  /\  |
    | /  \ |
    S3    S4
    |      |
    |      |
    H1     H2

"""

from mininet.topo import Topo

class MyTopo( Topo ):

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        # Hosts
        leftHost        = self.addHost( 'h1' )
        rightHost       = self.addHost( 'h2' )
        # Switches
        leftCoreSwitch  = self.addSwitch( 's1' )
        rightCoreSwitch = self.addSwitch( 's2' )
        leftEdgeSwitch  = self.addSwitch( 's3' )
        righEdgetSwitch = self.addSwitch( 's4' )

        # Add links
        self.addLink( leftHost       , leftEdgeSwitch , 1, 1 )
        self.addLink( rightHost      , righEdgetSwitch, 1, 1 )
        self.addLink( leftEdgeSwitch , leftCoreSwitch , 2, 1 )
        self.addLink( leftEdgeSwitch , rightCoreSwitch, 3, 1 )
        self.addLink( righEdgetSwitch, leftCoreSwitch , 2, 2 )
        self.addLink( righEdgetSwitch, rightCoreSwitch, 3, 2 )


topos = { 'mytopo': ( lambda: MyTopo() ) }
