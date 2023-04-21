import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://node00:5555")

while True:
    # Get input from the user
    message = input("Enter message: ")

    # Send the message to the server
    socket.send(message.encode())

    # Wait for the server to respond
    response = socket.recv()

    # Print the response from the server
    print("Received response: %s" % response.decode())