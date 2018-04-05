from tls.utils.assertions import Assertions

class Transport:
    """
        Abstract class representing the underlying transport protocol
    """
    def __init__(self, protocol, host_name, port):
        """
            create instance of Transport
        
            Args-
                :protocol   (object)    instance of class Protocol
                :host_name  (string)    domain name of the destination
                :port       (string)    port of the destination
        """
        self.protocol = Assertions.is_not_null(protocol)
        self.host_name = Assertions.is_not_null(host_name)
        self.port = Assertions.is_not_null(port)

        # for TCP, it creates a transport layer connection with
        # the destination. For UDP, it does nothing
        self.protocol.initialize(host_name = self.host_name, port = self.port)
    
    def send(self, payload, timeout = None):
        """
            construct and trasmit a transport layer request

            Args-
                :payload    (bytearray) bytearray with the request body
                :timeout    (integer)   optional timeout value to stop sending data
            

        """
        self.protocol.send(payload = payload, timeout = timeout)

    def recv(self, timeout = None):
        """
            receive a response from the recipient

            Args-
                :timeout    (int)   optional timeout value to stop waiting for results
        """
        return self.protocol.recv(timeout = timeout)