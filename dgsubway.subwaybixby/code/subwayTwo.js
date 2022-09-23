import console from 'console';
import http from 'http';
export default function subwayTwo(subwayName,subwayDir){
  
  console.log('http://18.190.78.1:5001/two?subwayname='+subwayName['subwayName']+'&subwaydir='+subwayName['subwayDir']);
  console.log(subwayName['subwayDir'])
  console.log(subwayName)
  var response = http.getUrl('http://18.190.78.1:5001/two?subwayname='+subwayName['subwayName']+'&subwaydir='+subwayName['subwayDir'], { format: 'json' });
  console.log(response);
  
  const firstArrivalTime = response['leftDirectionArrivalTime'];
  const firstLeftTime = response['leftDirectionLeftTime'];
  const secondArrivalTime = response['rightDirectionArrivalTime'];
  const secondLeftTime = response['rightDirectionLeftTime'];

  console.log("1.firstArrivalTime : " + firstArrivalTime)
  console.log("2.typeof(firstArrivalTime) : " + typeof(firstArrivalTime))
  console.log("3.firstLeftTime : "+ firstLeftTime)
  console.log("4.typeof(firstLeftTime) : "+ typeof(firstLeftTime))

  return {
    firstArrivalTime : firstArrivalTime,
    firstLeftTime : firstLeftTime,
    secondArrivalTime : secondArrivalTime,
    secondLeftTime : secondLeftTime,
    subwayLine : 1,
    subwayDir : subwayName['subwayDir']
  }
}