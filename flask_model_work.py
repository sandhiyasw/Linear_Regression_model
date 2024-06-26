

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'welcome to FLASK WEBSITE CREATEION  first front end model '


#app.run(host='0.0.0.0', port=81)

app.run(host = '192.168.0.22', port=8889)

