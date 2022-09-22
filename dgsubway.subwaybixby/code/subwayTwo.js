import console from 'console';
import http from 'http';
export default function subwayTwo(subwayName,subwayDir){
  
  console.log('http://18.190.78.1:5001/two?subwayname='+subwayName['subwayName']+'&subwaydir='+subwayName['subwayDir']);
  var response = http.getUrl('http://18.190.78.1:5001/two?subwayname='+subwayName['subwayName']+'&subwaydir='+subwayName['subwayDir'], { format: 'json' });
  console.log(response);
  const firstArrivalTime = response['leftDirectionArrivalTime'];
  const firstLeftTime = response['leftDirectionLeftTime'];
  const secondArrivalTime = response['rightDirectionArrivalTime'];
  const secondLeftTime = response['rightDirectionLeftTime'];

  return {
    firstArrivalTime : firstArrivalTime,
    firstLeftTime : firstLeftTime,
    secondArrivalTime : secondArrivalTime,
    secondLeftTime : secondLeftTime,
    subwayDir : subwayDir
  }
}