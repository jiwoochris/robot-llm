import socket
import threading
import cv2
import numpy as np

class TelloDrone:

    def __init__(self):
        # The Tello SDK uses a fixed IP and port
        self.tello_ip = '192.168.10.1'
        self.tello_port = 8889
        self.local_ip = ''
        self.local_port = 9000

        # Create a UDP connection
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.local_ip, self.local_port))

        # Start a listening thread
        self.response = None
        self.receive_thread = threading.Thread(target=self._receive_thread)
        self.receive_thread.daemon = True
        self.receive_thread.start()

        # Command the drone to enter command mode
        self.send_command('command')

    def send_command(self, command):
        # Send the command to the drone
        self.socket.sendto(command.encode(), (self.tello_ip, self.tello_port))

        # Wait for the response
        while self.response is None:
            pass

        # Print the response
        print(self.response)

        # Reset the response
        self.response = None

    def _receive_thread(self):
        while True:
            try:
                # Receive the response from the drone
                self.response, ip = self.socket.recvfrom(1024)
                self.response = self.response.decode('utf-8')
            except socket.error as e:
                # If there's an error close the socket and break out of the loop
                self.socket.close()
                print(e)
                break
