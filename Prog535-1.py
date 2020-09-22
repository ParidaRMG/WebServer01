#!/usr/bin/python

from http.server import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):

   #Handler for the GET requests
   def do_GET(self):
      # Add your checking of the self.path equals to "/"


      #print("Hello world!")

      # Add your code below for various content types
      try:
         #Check the file extension required and
         #set the right mime type

         sendReply = False
         if self.path.endswith(".html"):
            mimetype='text/html'
            sendReply = True
         # add more code here for various image types




         if sendReply == True:
            #Open the static file requested and send it
            f = open(curdir + sep + self.path, "rb")
            self.send_response(200)
            self.send_header('Content-type',mimetype)
            self.end_headers()
            self.wfile.write(f.read() )
            f.close()
         return


      except IOError:
         # change the code to send an error web page dynamically
         print ("File Not Found" + self.path)

# main routine starts here - no need to change this part
try:
   #Create a web server and define the handler to manage the
   #incoming request
   server = HTTPServer(('', PORT_NUMBER), myHandler)
   print ('Started httpserver on port ' , PORT_NUMBER)

   #Wait forever for incoming htto requests
   server.serve_forever()

except KeyboardInterrupt:
   print ('^C received, shutting down the web server')
   server.socket.close()
