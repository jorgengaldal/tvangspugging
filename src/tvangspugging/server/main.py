import json
import os
import shutil
import sys
import urllib.parse
from functools import cached_property
from http.server import BaseHTTPRequestHandler, HTTPServer
from mimetypes import guess_type
from pathlib import Path

from tvangspugging.model.getRandomQuestion import getQuestion

WEB_BASE_PATH = Path(__file__) / ".." / "web"
MEDIA_BASE_PATH = WEB_BASE_PATH / "media"

class Handler(BaseHTTPRequestHandler):

    @cached_property
    def web_path(self):
        # TODO: Add security check so that only pages within are allowed
        relative_path = Path(urllib.parse.unquote(self.path[1:], encoding='utf-8', errors='replace'))
        potential_path = WEB_BASE_PATH / relative_path
        if potential_path.exists():
            if potential_path.is_dir():
                return potential_path / "index.html"
            return potential_path
        return None

    def do_GET(self):
        result = "wrong"

        if self.path == "/api/success":
            print("Stopping server!")
            self.send_response(200)
            self.end_headers()
            sys.exit()

        if self.path == "/api/question":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            retries = 10
            while True:
                try:
                    question = getQuestion()
                    break
                except:
                    retries -= 1
                    if retries < 0:
                        # TODO: Fix this terrible code
                        self.send_response(500)
                        self.end_headers()
                        return

            for resource in question["resources"]:
                use_media(resource["path"])
                resource["path"] = (Path("./media") / resource["path"].name).as_posix()  # Cleanup path for ref in html page

            result = json.dumps(question)

        elif self.web_path is not None:
            with open(self.web_path, encoding="utf-8") as file:
                result = file.read()
            self.send_response(200)
            mime_type = guess_type(self.web_path)[0] or "text/plain"
            self.send_header("Content-Type", f"{mime_type}; charset=utf-8")
            self.end_headers()
        
        else:
            self.send_response(404)
            self.end_headers()

        self.wfile.write(result.encode("utf-8"))


def run(server_class=HTTPServer, handler_class=Handler):
    server_address = ('', 16000)
    httpd = server_class(server_address, handler_class)
    print("Starting server!")
    httpd.serve_forever()


def use_media(source: Path):
    if not MEDIA_BASE_PATH.exists():
        os.mkdir(MEDIA_BASE_PATH)

    shutil.copyfile(source.absolute(), MEDIA_BASE_PATH / source.name)


if __name__ == "__main__":
    run()