from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class WebServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ''
                output += '<html><body>Hello!</body></html>'
                self.wfile.write(output)
                print output
                return

            if self.path.endswith('/hola'):
                self.send_response(200)
                self.send_header('COntent-type', 'text/html')
                self.end_headers()
                message = ''
                message += '<html><body> %#161 Hola ! </body></html>'
                print message
            else:
                self.send_error(404, 'File Not Found : %s' %self.paht)

        except IOError:
            self.send_error(404, 'file not found %s'%self.path)

def main():

    try: 
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print "web sever runing on port{}".format(port)
        server.serve_forever()

    except KeyboardInterrupt:
        print "^C enterd, stopping web server.."

if __name__ == '__main__':


    main()
