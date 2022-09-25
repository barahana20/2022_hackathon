import console from 'console';
import http from 'http';
export default function subwayThree_ForLastStations(subwayDir,isFirstOrLast){
  var url = 'http://18.190.78.1:5001/four?subwayname='+subwayDir['subwayDir']+'&subwaydir='+oppositeStation
  var option = { format: 'json', cacheTime: 0 }
  var oppositeStation = searchSubwayDir(subwayDir['subwayDir']);

  console.log(url);
  var response = http.get(url, option);
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
    subwayDir : oppositeStation,
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