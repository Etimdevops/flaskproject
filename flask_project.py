from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "I am almost a DevOps Engineer!"

if __name__ == '__main__':
    app.run(host='172.31.95.41', port=5000)  # Bind to all interfaces and specify port
