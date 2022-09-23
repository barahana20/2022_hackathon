import console from 'console';
import http from 'http';
export default function subwayFour(subwayName,subwayDir,isFirstOrLast){
  
  console.log('http://18.190.78.1:5001/four?subwayname='+subwayName['subwayName']+'&subwaydir='+subwayName['subwayDir']);
  var response = http.getUrl('http://18.190.78.1:5001/four?subwayname='+subwayName['subwayName']+'&subwaydir='+subwayName['subwayDir'], { format: 'json' });
  console.log(response);
  const directionFirstTime = response['directionFirstTime'];
  const directionLastTime = response['directionLastTime'];

  return {
    directionFirstTime : directionFirstTime,
    directionLastTime : directionLastTime,
    subwayLine : 1,
    subwayDir : subwayName['subwayDir'],
    isFirstOrLast : subwayName['isFirstOrLast']
  }
}