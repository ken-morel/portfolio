from textual_serve.server import Server

server = Server("python main.py", host="0.0.0.0", port=8080)

server.serve()
