from http.server import HTTPServer, CGIHTTPRequestHandler
import os

def configure(server_address, server_port, root_directory):
    global server, server_configuration # Global

    server_configuration = [ server_address, server_port, root_directory ] # Create server configuration

    os.chdir(server_configuration[2]) # Set up work directory
    server = HTTPServer((server_configuration[0], server_configuration[1]), CGIHTTPRequestHandler) # Set up server

def launch():
    server.serve_forever() # Start server