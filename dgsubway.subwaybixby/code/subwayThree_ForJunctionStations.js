import console from 'console';
import http from 'http';
export default function subwayThree_ForJunctionStations(junctionStations,isFirstOrLast, subwayLine){

  var oppositeStation = searchSubwayDir(junctionStations['junctionStations']);

  console.log('http://18.190.78.1:5001/four?subwayname='+junctionStations['junctionStations']+'&junctionStations='+oppositeStation+'&subwayLine='+junctionStations['subwayLine']);
  var response = http.getUrl('http://18.190.78.1:5001/four?subwayname='+junctionStations['junctionStations']+'&junctionStations='+oppositeStation+'&subwayLine='+junctionStations['subwayLine'], { format: 'json' });
  console.log(response);
  const beforeLastTrainTime = response["beforeLastTrainTime"];
  const firstTrainTime = response["firstTrainTime"];
  const lastTrainTime = response["lastTrainTime"];
  const subwayLine = response["subwayLine"]

  console.log(firstTrainTime);
  console.log(lastTrainTime);
  console.log(beforeLastTrainTime);
  console.log(subwayLine);

  return {
    beforeLastTrainTime : beforeLastTrainTime,
    firstTrainTime : firstTrainTime,
    lastTrainTime : lastTrainTime,
    subwayLine : subwayLine,
    isFirstOrLast : subwayDir['isFirstOrLast']
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