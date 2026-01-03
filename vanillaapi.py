
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse , parse_qs

class User(BaseHTTPRequestHandler):
    def do_GET(self):
        parser_url = urlparse(self.path)
        path = parser_url.path
        query = parse_qs(parser_url.query)
        if path == "/":
            self.send_json("server running")
        elif path == "/profile":
            name = str(query.get("name" , '')[0])
            self.send_json("hello " + name)
        else:
            self.send_json("endpoint not found" , 404)

    def find_user(self , data , payload):
            for index , user in enumerate(data):
                print(user)
                if user["name"] == payload["name"] and user["password"] == payload["password"]:
                    return user
            return False

    def do_POST(self):
        path = self.path
        content_length = int(self.headers.get('Content-Length' , 0))
        body = self.rfile.read(content_length)
        data = json.loads(body)
        user_name = data.get("password")
        password = data.get("password")
        if len(user_name) < 4  | len(password) < 4:
            self.send_json("username / password minimal 4 character " , 401)
        if len(user_name) > 40  | len(password) > 40:
            self.send_json("username / password maximal 40 character " , 401)
        if path == "/register":
            with open("json/user.json" , 'r') as f:
                data = json.load(f)
                data.append({"id" : len(data) + 1,"name" : user_name , "password" : password })
            with open("json/user.json", "w") as f:
                json.dump(data, f , indent=4)
            self.send_json("success register" , 201)
        elif path == "/login":
            payload = {"name" : user_name , "password" : password }
            with open("json/user.json", "r") as file:
                data = json.load(file)
                user = self.find_user(data , payload)
                if user:
                    self.send_json({"user" : user} , 200)
                else:
                    self.send_json("username / password salah " , 401)
    def send_json(self , data , status_code = 200):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))


while True:
    server = HTTPServer(("localhost", 8000), User)
    print("server running at localhost:8000")
    server.serve_forever()