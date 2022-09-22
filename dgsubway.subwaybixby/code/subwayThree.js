import console from 'console';
import http from 'http';
export default function subwayThree(subwayName) {

  console.log('http://18.190.78.1:5001/three?subwayname='+subwayName['subwayName'])
  var response = http.getUrl('http://18.190.78.1:5001/three?subwayname='+subwayName['subwayName'], { format: 'json' });
  console.log(response);
  const leftFirstTime = response['leftFirstTime'];
  const leftLastTime = response['leftLastTime'];
  const rightFirstTime = response['rightFirstTime'];
  const rightLastTime = response['rightLastTime'];
  console.log(leftDirectionArrivalTime)
  console.log(leftDirectionLeftTime)
  console.log(rightDirectionArrivalTime)
  console.log(rightDirectionLeftTime)
  
  return {
    leftFirstTime: leftFirstTime,
    leftLastTime: leftLastTime,
    rightFirstTime: rightFirstTime,
    rightLastTime: rightLastTime
  }
}