import console from 'console';
import http from 'http';
export default function subwayThree(junctionStations,isFirstOrLast, subwayLine) {
  var url = 'http://18.190.78.1:5001/three_forjunctionstations?subwayname='+junctionStations['junctionStations']+'&subwayLine='+junctionStations['subwayLine']
  var option = { format: 'json', cacheTime: 0 }
  console.log(url)
  var response = http.getUrl(url, option);
  console.log(response);
  const leftFirstTime = response['leftFirstTime'];
  const leftLastTime = response['leftLastTime'];
  const rightFirstTime = response['rightFirstTime'];
  const rightLastTime = response['rightLastTime'];

  return {
    leftFirstTime: leftFirstTime,
    leftLastTime: leftLastTime,
    rightFirstTime: rightFirstTime,
    rightLastTime: rightLastTime,
    subwayLine : junctionStations['subwayLine'],
    isFirstOrLast : junctionStations['isFirstOrLast']
  }
}