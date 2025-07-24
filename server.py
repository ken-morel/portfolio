from textual_serve.server import Server

server = Server("python main.py", host="0.0.0.0")

server.serve()
