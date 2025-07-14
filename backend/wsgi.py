from backend.server import app

if __name__ == '__main__':  
    from waitress import serve
    serve(app,host="192.168.100.155", port=9000)