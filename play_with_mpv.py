# Plays MPV when instructed to by a chrome extension =]
import os
import sys
import argparse
import http.server as BaseHTTPServer
import urllib.parse as urlparse
import subprocess
from os import listdir


class CompatibilityMixin:
    def send_body(self, msg):
        try:
            self.wfile.write(bytes(msg+'\n', 'utf-8'))
        except ConnectionAbortedError:
            print(" Abort current request...wait for next......")

class Handler(BaseHTTPServer.BaseHTTPRequestHandler, CompatibilityMixin):
    def respond(self, code, body=None):
        self.send_response(code)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        if body:
            self.send_body(body)

    def do_GET(self):
        global absolute_path
        try:
            url = urlparse.urlparse(self.path)
            query = urlparse.parse_qs(url.query)
        except:
            query = {}
        if query.get('mpv_args'):
            print(query.get('mpv_args'))
        if "play_url" in query:
            urls = str(query["play_url"][0])
            if urls.startswith('magnet:') or urls.endswith('.torrent'):
                pass
            else:
                try:
                    subtitles_list = [os.path.join(absolute_path,subtitle_file) for subtitle_file in listdir(absolute_path)
                                      if subtitle_file.endswith('vtt') and subtitle_file.startswith("-")]
                    subtitles = ';'.join(subtitles_list)
                    subprocess.run(f'play_with_mpv.cmd "{urls}" "{subtitles}"', capture_output=True, shell=True)
                except FileNotFoundError as e:
                    #print(e)
                    missing_bin('mpv')
                finally:
                    delete_path = os.path.join(absolute_path, r"delete mpv cache.cmd")
                    subprocess.run(f'{delete_path}', capture_output=True, shell=True)
            self.respond(200, "playing...")
        else:
            self.respond(400)


def missing_bin(bin):
    print("======================")
    print(f"ERROR: {bin.upper()} does not appear to be installed correctly! please ensure you can launch '{bin}' in the terminal.")
    print("======================")


def start():
    parser = argparse.ArgumentParser(description='Plays MPV when instructed to by a browser extension.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--port',   type=int,  default=7531, help='The port to listen on.')
    parser.add_argument('--public', action='store_true',     help='Accept traffic from other comuters.')
    args = parser.parse_args()
    hostname = '0.0.0.0' if args.public else 'localhost'
    httpd = BaseHTTPServer.HTTPServer((hostname, args.port), Handler)
    print("serving on {}:{}".format(hostname, args.port))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print(" shutting down...")
        httpd.shutdown()

if getattr(sys, 'frozen', False):
    absolute_path = os.path.dirname(sys.executable)
else:
    absolute_path = os.path.dirname(__file__)

if __name__ == '__main__':
    start()
