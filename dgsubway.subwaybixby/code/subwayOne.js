import console from 'console';
import http from 'http';
export default function subwayOne(subwayName) {
  console.log(subwayName);
  function Time (hour,minute) {
    this.hour = hour;
    this.minute = minute;
  }
  const leftDirectionArrivalTime = new Time(12,10);
  const leftDirectionLeftTime = 10;
  const rightDirectionArrivalTime = new Time(12,15);
  const rightDirectionLeftTime = 5;
  var response = http.getUrl('http://127.0.0.1:5001/two?subwayname=%EA%B0%81%EC%82%B0&subwaydir=%EC%83%81', { format: 'json' });
  console.log ("response = " + response)
  // for prototype
  // let subwayResult = {
  //   leftDirectionArrivalTime : new Time(12,10),
  //   leftDirectionLeftTime : new Time(0,10),
  //   rightDirectionArrivalTime : new Time(12,15),
  //   rightDirectionLeftTime : new Time(0,5)
  // }
  return {
    leftDirectionArrivalTime: leftDirectionArrivalTime,
    leftDirectionLeftTime: leftDirectionLeftTime,
    rightDirectionArrivalTime: rightDirectionArrivalTime,
    rightDirectionLeftTime: rightDirectionLeftTime
  }
}