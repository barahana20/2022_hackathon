import console from 'console';
import http from 'http';
export default function subwayOne(subwayName,subwayDir){
  
  console.log('http://18.190.78.1:5001/four?subwayname='+subwayName['subwayName']+'&subwayDir='+subwayName['subwayDir']);
  var response = http.getUrl('http://18.190.78.1:5001/four?subwayname='+subwayName['subwayName']+'&subwayDir='+subwayName['subwayDir'], { format: 'json' });
  console.log(response);
  const directionFirstTime = response['DirectionFirstTime'];
  const directionLasTime = response['DirectionLasTime'];

  return {
    directionFirstTime : directionFirstTime,
    directionLasTime : directionLasTime,
  }
}