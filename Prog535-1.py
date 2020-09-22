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
      if(self.path[0] != "/"):
          return 0

      #This variable will count the number of requests
      requestCounter = 0

      # Add your code below for various content types
      try:
         #Check the file extension required and
         #set the right mime type

         sendReply = False
         if self.path.endswith(".html"):
            mimetype='text/html'
            #print("HTML text request type at path:",self.path)
            requestCounter += 1
            sendReply = True
         # add more code here for various image types
         if self.path.endswith(".jpg"):
            mimetype='picture/jpg'
            #print("JPG text request type at path",self.path)
            requestCounter += 1
            sendReply = True

         if self.path.endswith(".png"):
           mimetype='picture/png'
           #print("PNG text request type at path",self.path)
           requestCounter += 1
           sendReply = True

         if self.path.endswith(".gif"):
           mimetype='picture/gif'
           #print("GIF text request type at path",self.path)
           requestCounter += 1
           sendReply = True

         if self.path.endswith(".bmp"):
           mimetype='picture/bmp'
           #print("BMP text request type at path",self.path)
           requestCounter += 1
           sendReply = True

         if sendReply == True:
            #Open the static file requested and send it
            f = open(curdir + sep + self.path, "rb")
            #print("point1")
            self.send_response(200)
            #print("point2")
            self.send_header('Content-type',mimetype)
            #print("point3")
            self.end_headers()
            #print("point4")
            self.wfile.write(f.read() )
            f.close()
            #print("\n\n")
            #print("RequestCounter:", requestCounter)
         else:
             print("File:", self.path, " not found")
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
