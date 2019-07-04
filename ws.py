from http.server import HTTPServer
from lib.server import Server



httpd = HTTPServer(('', 8080), Server)
httpd.serve_forever()







