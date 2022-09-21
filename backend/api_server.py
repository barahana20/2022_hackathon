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
    leftDirectionArrivalTime, leftDirectionLeftTime, rightDirectionArrivalTime, rightDirectionLeftTime = subwaymethod.two(subwayname, subwaydir)
    return {
        'leftDirectionArrivalTime': leftDirectionArrivalTime,
        'leftDirectionLeftTime': leftDirectionLeftTime,
        'rightDirectionArrivalTime': rightDirectionArrivalTime,
        'rightDirectionLeftTime': rightDirectionLeftTime
    }
 
@app.route('/three')
def three():
    subwayname = request.args.get('subwayname')
    leftDirectionFirstTime, leftDirectionLastime = subwaymethod.return_first_last_train_time(subwayname, '상')
    rightDirectionFirstTime, rightDirectionLastTime = subwaymethod.return_first_last_train_time(subwayname, '하')

    return {
        'leftDirectionFirstTime': leftDirectionFirstTime,
        'leftDirectionLastime': leftDirectionLastime,
        'rightDirectionFirstTime': rightDirectionFirstTime,
        'rightDirectionLastTime': rightDirectionLastTime
    }
  
@app.route('/four')
def four():
    subwayname = request.args.get('subwayname')
    subwaydir = request.args.get('subwaydir')
    DirectionFirstTime, DirectionLastime = subwaymethod.return_first_last_train_time(subwayname, subwaydir)

    return {
        'DirectionFirstTime': DirectionFirstTime,
        'DirectionLastime': DirectionLastime
    }
 

 
@app.route('/about')
def about():
    return 'About 페이지'

if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0')