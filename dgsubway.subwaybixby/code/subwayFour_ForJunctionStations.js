import console from 'console';
import http from 'http';
export default function subwayFour_ForJunctionStations(junctionStations,subwayDir,isFirstOrLast, subwayLine){
  
  console.log('http://18.190.78.1:5001/four?subwayname='+junctionStations['junctionStations']+'&subwaydir='+junctionStations['subwayDir']+'&subwayLine='+junctionStations['subwayLine']);
  var response = http.getUrl('http://18.190.78.1:5001/four?subwayname='+junctionStations['junctionStations']+'&subwaydir='+junctionStations['subwayDir']+'&subwayLine='+junctionStations['subwayLine'], { format: 'json' });
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