import console from 'console';
import http from 'http';
export default function subwayThree(subwayName) {

  console.log('http://18.190.78.1:5001/three?subwayname='+subwayName['subwayName'])
  var response = http.getUrl('http://18.190.78.1:5001/three?subwayname='+subwayName['subwayName'], { format: 'json' });
  console.log(response);
  const leftDirectionArrivalTime = response['leftDirectionFirstTime'];
  const leftDirectionLeftTime = response['leftDirectionLastime'];
  const rightDirectionArrivalTime = response['rightDirectionFirstTime'];
  const rightDirectionLeftTime = response['rightDirectionLastTime'];
  console.log(leftDirectionArrivalTime)
  console.log(leftDirectionLeftTime)
  console.log(rightDirectionArrivalTime)
  console.log(rightDirectionLeftTime)
  
  return {
    leftFirstTime: leftDirectionArrivalTime,
    leftLastTime: leftDirectionLeftTime,
    rightFirstTime: rightDirectionArrivalTime,
    rightLastTime: rightDirectionLeftTime
  }
}