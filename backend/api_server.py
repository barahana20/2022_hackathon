from flask import Flask, request
from subway_method import SubwayMethod

app = Flask(__name__)
subwaymethod = SubwayMethod()
@app.route('/one')
def one():
    subwayname = request.args.get('subwayname')
    leftDirectionArrivalTime, leftDirectionLeftTime, rightDirectionArrivalTime, rightDirectionLeftTime = subwaymethod.one(subwayname)
    return {
        'leftDirectionArrivalTime': leftDirectionArrivalTime,
        'leftDirectionLeftTime': leftDirectionLeftTime,
        'rightDirectionArrivalTime': rightDirectionArrivalTime,
        'rightDirectionLeftTime': rightDirectionLeftTime
    }
 
@app.route('/two')
def two():
    subwayname = request.args.get('subwayname')
    subwaydir = request.args.get('subwaydir')
    firstArrivalTime, firstLeftTime, secondArrivalTime, secondLeftTime = subwaymethod.two(subwayname, subwaydir)
    return {
        'firstArrivalTime': firstArrivalTime,
        'firstLeftTime': firstLeftTime,
        'secondArrivalTime': secondArrivalTime,
        'secondLeftTime': secondLeftTime
    }
 
@app.route('/three')
def three():
    subwayname = request.args.get('subwayname')
    leftFirstTime, leftLastTime, rightFirstTime, rightLastTime = subwaymethod.three(subwayname)
    

    return {
        'leftFirstTime': leftFirstTime,
        'leftLastTime': leftLastTime,
        'rightFirstTime': rightFirstTime,
        'rightLastTime': rightLastTime
    }
  
@app.route('/four')
def four():
    subwayname = request.args.get('subwayname')
    subwaydir = request.args.get('subwaydir')
    directionFirstTime, directionLastTime = subwaymethod.four(subwayname, subwaydir)

    return {
        'directionFirstTime': directionFirstTime,
        'directionLastTime': directionLastTime
    }
 
@app.route('/about')
def about():
    return 'About 페이지'

if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0')