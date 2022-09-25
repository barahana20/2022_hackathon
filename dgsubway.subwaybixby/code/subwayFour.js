import console from 'console';
import http from 'http';
export default function subwayFour(subwayName,subwayDir,isFirstOrLast){
  var url = 'http://18.190.78.1:5001/four?subwayname='+subwayName['subwayName']+'&subwaydir='+subwayName['subwayDir']
  var option = { format: 'json', cacheTime: 0}
  var response = http.getUrl(url, option);
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
    subwayDir : subwayName['subwayDir'],
    isFirstOrLast : subwayName['isFirstOrLast']
  }
}