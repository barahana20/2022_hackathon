import console from 'console';
import http from 'http';
export default function subwayOne_ForLastStations(subwayDir){

  var oppositeStation = searchSubwayDir(subwayDir['subwayDir']);
  console.log("1. subwayDir['subwayDir'] " + subwayDir['subwayDir'])
  console.log("2. typeof(subwayDir['subwayDir'] " + typeof(subwayDir['subwayDir']))
  console.log('http://18.190.78.1:5001/two?subwayname='+subwayDir['subwayDir']+'&subwaydir='+oppositeStation)

  var response = http.getUrl('http://18.190.78.1:5001/two?subwayname='+subwayDir['subwayDir']+'&subwaydir='+oppositeStation,{ format: 'json' });
  console.log(response);

  let firstArrivalTime = response['firstArrivalTime'];
  let firstLeftTime = response['firstLeftTime'];
  let secondArrivalTime = response['secondArrivalTime'];
  let secondLeftTime = response['secondLeftTime'];
  let subwayLine  = response['subwayLine'];

  console.log(oppositeStation)

  return {
    firstArrivalTime : firstArrivalTime,
    firstLeftTime : firstLeftTime,
    secondArrivalTime : secondArrivalTime,
    secondLeftTime : secondLeftTime,
    subwayLine : subwayLine,
    subwayDir : oppositeStation
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