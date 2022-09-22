import console from 'console';
import http from 'http';
export default function subwayTwo(subwayName,subwayDir){
  
  console.log('http://18.190.78.1:5001/two?subwayname='+subwayName['subwayName']+'&subwaydir='+subwayName['subwayDir']);
  console.log(subwayName['subwayDir'])
  console.log(subwayName)
  var response = http.getUrl('http://18.190.78.1:5001/two?subwayname='+subwayName['subwayName']+'&subwaydir='+subwayName['subwayDir'], { format: 'json' });
  console.log(response);
  const firstArrivalTime = response['firstArrivalTime'];
  const firstLeftTime = response['firstLeftTime'];
  const secondArrivalTime = response['secondArrivalTime'];
  const secondLeftTime = response['secondLeftTime'];

  return {
    firstArrivalTime : firstArrivalTime,
    firstLeftTime : firstLeftTime,
    secondArrivalTime : secondArrivalTime,
    secondLeftTime : secondLeftTime,
    subwayLine : 1,
    subwayDir : subwayName['subwayDir']
  }
}