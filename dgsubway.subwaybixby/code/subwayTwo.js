import console from 'console';
import http from 'http';
export default function subwayTwo(subwayName,subwayDir){
  var url = 'http://18.190.78.1:5001/two?subwayname='+subwayName['subwayName']+'&subwaydir='+subwayName['subwayDir']
  var option = { format: 'json', cacheTime: 0 }
  console.log(url);
  console.log(subwayName['subwayDir'])
  console.log(subwayName)
  var response = http.getUrl(url, option);
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
    subwayDir : subwayName['subwayDir']
  }
}