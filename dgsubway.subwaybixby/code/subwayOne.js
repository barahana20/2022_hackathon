import console from 'console';
import http from 'http';
export default function subwayOne(subwayName) {

  console.log('http://18.190.78.1:5001/one?subwayname='+subwayName['subwayName'])
  console.log(subwayName)
  var response = http.getUrl('http://18.190.78.1:5001/one?subwayname='+subwayName['subwayName'], { format: 'json' });
  const leftDirectionArrivalTime = response['leftDirectionArrivalTime'];
  const leftDirectionLeftTime = response['leftDirectionLeftTime'];
  const rightDirectionArrivalTime = response['rightDirectionArrivalTime'];
  const rightDirectionLeftTime = response['rightDirectionLeftTime'];

  return {
    leftDirectionArrivalTime: leftDirectionArrivalTime,
    leftDirectionLeftTime: leftDirectionLeftTime,
    rightDirectionArrivalTime: rightDirectionArrivalTime,
    rightDirectionLeftTime: rightDirectionLeftTime
  }
}