import console from 'console';
import http from 'http';
export default function subwayThree(subwayName,isFirstOrLast) {

  console.log('http://18.190.78.1:5001/three?subwayname='+subwayName['subwayName'])
  var response = http.getUrl('http://18.190.78.1:5001/three?subwayname='+subwayName['subwayName'], { format: 'json' });
  console.log(response);
  const leftFirstTime = response['leftFirstTime'];
  const leftLastTime = response['leftLastTime'];
  const rightFirstTime = response['rightFirstTime'];
  const rightLastTime = response['rightLastTime'];
  const subwayLine = response['subwayLine'];

  return {
    leftFirstTime: leftFirstTime,
    leftLastTime: leftLastTime,
    rightFirstTime: rightFirstTime,
    rightLastTime: rightLastTime,
    subwayLine : subwayLine,
    isFirstOrLast : subwayName['isFirstOrLast']
  }
}