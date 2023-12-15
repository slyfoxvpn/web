from http.server import HTTPServer, CGIHTTPRequestHandler
import os

class HTTPHandler(CGIHTTPRequestHandler):
    def send_error(self, code, message=None, explain=None):
        if code == 404:
            self.send_response(404, "Not Found") # Response code

            # Headers
            self.send_header('Content-type', 'text/html; charset=UTF-8')
            self.end_headers()

            # Read the content of the external HTML file
            error_page_path = os.path.join('404.html')
            with open(error_page_path, 'r', encoding='utf-8') as error_page_file:
                error_page_content = error_page_file.read()
            
            # Inject the requested URL into the error page
            error_page_content = error_page_content.format(self.path)
            
            # Send the customized error page
            self.wfile.write(error_page_content.encode('utf-8'))
        else:
            super().send_error(code, message, explain)


def configure(server_address, server_port, root_directory):
    global server, server_configuration # Global

    server_configuration = [ server_address, server_port, root_directory ] # Create server configuration

    os.chdir(server_configuration[2]) # Set up work directory

    server = HTTPServer((server_configuration[0], server_configuration[1]), HTTPHandler) # Set up server

def launch():
    server.serve_forever() # Start server