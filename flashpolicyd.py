#!/usr/bin/env python
from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH)
class MyRequestHandler(SRH):
    def handle(self):
        #print '...connected from:', self.client_address
        #print(self.rfile.read(23))
        self.wfile.write('''<?xml version="1.0"?>
<!DOCTYPE cross-domain-policy SYSTEM "/xml/dtds/cross-domain-policy.dtd">
<cross-domain-policy>
<site-control permitted-cross-domain-policies="master-only"/>
<!-- If you want to limit the flashpolicyd to a specific domain/port please change the domain and to-ports parameters.  -->
<allow-access-from domain="*" to-ports="*" />
</cross-domain-policy>''')
        #print 'send xml ok'
tcpServ = TCP(('',843), MyRequestHandler)
#print 'waiting for connection...'
tcpServ.serve_forever()
