import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    # Wait for a request from the client
    message = socket.recv()

    # Print the received message
    print("Received request: %s" % message)

    # Send a reply back to the client
    socket.send(b"Hello World")