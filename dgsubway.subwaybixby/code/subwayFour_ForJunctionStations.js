import console from 'console';
import http from 'http';
export default function subwayFour_ForJunctionStations(junctionStations,subwayDir,isFirstOrLast, subwayLine){
  
  if(junctionStations['subwayLine'] == null){
    subwayLine = findSubwayLine(junctionStations['subwayDir'])
  }
  
  console.log('http://18.190.78.1:5001/four_forjunctionstations?subwayname='+junctionStations['junctionStations']+'&subwaydir='+junctionStations['subwayDir']+'&subwayLine='+subwayLine);
  var response = http.getUrl('http://18.190.78.1:5001/four_forjunctionstations?subwayname='+junctionStations['junctionStations']+'&subwaydir='+junctionStations['subwayDir']+'&subwayLine='+subwayLine, { format: 'json' });
  console.log(response);
  const beforeLastTrainTime = response["beforeLastTrainTime"];
  const firstTrainTime = response["firstTrainTime"];
  const lastTrainTime = response["lastTrainTime"];

  console.log(firstTrainTime);
  console.log(lastTrainTime);
  console.log(beforeLastTrainTime);
  console.log(subwayLine);

  return {
    beforeLastTrainTime : beforeLastTrainTime,
    firstTrainTime : firstTrainTime,
    lastTrainTime : lastTrainTime,
    subwayLine : subwayLine,
    subwayDir : junctionStations['subwayDir'],
    isFirstOrLast : junctionStations['isFirstOrLast']
  }
}
function findSubwayLine(subwayDir){
  switch(subwayDir){
    case '설화명곡':
    case '안심':
      return 1;
    case '영남대':
    case '문양':
      return 2;
    case '칠곡경대병원':
    case '용지':
      return 3;  

  }
}