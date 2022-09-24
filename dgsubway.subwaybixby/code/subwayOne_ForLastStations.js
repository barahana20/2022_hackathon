import console from 'console';
import http from 'http';
export default function subwayOne_ForLastStations(subwayDir){

  var oppositeStation = searchSubwayDir(subwayDir)
  
  console.log('http://18.190.78.1:5001/two?subwayname='+subwayDir['subwayDir']+'&subwaydir='+subwayDir[oppositeStation]);
  console.log(subwayDir['oppositeStation'])
  console.log(subwayDir)
  var response = http.getUrl('http://18.190.78.1:5001/two?subwayname='+subwayDir['subwayName']+'&subwaydir='+subwayDir['oppositeStation'], { format: 'json' });
  console.log(response);

  let firstArrivalTime = response['firstArrivalTime'];
  let firstLeftTime = response['firstLeftTime'];
  let secondArrivalTime = response['secondArrivalTime'];
  let secondLeftTime = response['secondLeftTime'];
  let subwayLine  = response['subwayLine'];

  console.log("l1.firstArrivalTime : " + firstArrivalTime)
  console.log("l2.typeof(firstArrivalTime) : " + typeof(firstArrivalTime))
  console.log("l3.firstLeftTime : "+ firstLeftTime)
  console.log("l4.typeof(firstLeftTime) : "+ typeof(firstLeftTime))

  return {
    firstArrivalTime : firstArrivalTime,
    firstLeftTime : firstLeftTime,
    secondArrivalTime : secondArrivalTime,
    secondLeftTime : secondLeftTime,
    subwayLine : subwayLine,
    subwayDir : subwayDir[oppositeStation]
  }
}
function searchSubwayDir(subwayName){
  switch(subwayName){
    case '안심':
      return '설화명곡';
    case '설화명곡':
      return '안심';  
    case '영남대':
      return '문양';
    case '문양':
      return '영남대';
    case '칠곡경대병원':
      return '용지';
    default:
      return '칠곡경대병원'      
  }
}