from flask import Flask

server_port = 5000
host_path = "0.0.0.0"
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

if __name__=="__main__":
    app.run(host_path,server_port)