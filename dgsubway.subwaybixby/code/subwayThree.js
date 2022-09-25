import console from 'console';
import http from 'http';
export default function subwayThree(subwayName,isFirstOrLast) {
  var url = 'http://18.190.78.1:5001/three?subwayname='+subwayName['subwayName']
  var option = { format: 'json', cacheTime: 0 }
  console.log(url)
  var response = http.getUrl(url, option);
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