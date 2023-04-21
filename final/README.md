Hi, The packet capture works the same as the ZEROMQ homework
while using the command: tcpdump -i eth0 -w filename.pcap
to capture the packet info. 

For the P2P Chat Server, You simply run the p2pchatserver.py in node 00 and the p2pchatclient.py in node01 and the client will ask for a message, and will send the message to the server, the server will receive the message and send back a response.