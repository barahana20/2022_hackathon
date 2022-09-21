from flask import Flask, request
from subway_method import SubwayMethod

app = Flask(__name__)

@app.route('/one')
def index():
    subwayname = request.args.get('subwayname')
    
    return {}
 
@app.route('/about')
def about():
    return 'About 페이지'

if __name__ == '__main__':
    app.run(debug=True, port=5001)