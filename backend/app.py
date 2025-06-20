from backend import crear_app


if __name__ == '__main__':
    app=crear_app()
    app.run(host='0.0.0.0',port='7800',debug=True)