import console from 'console';
import http from 'http';
export default function subwayTwo(junctionStations,subwayLine,subwayDir){

  subwayLine = junctionStations['subwayLine']
  if(subwayLine == null){
    subwayLine = findSubwayLine(junctionStations['subwayDir'])
  }
  var url = 'http://18.190.78.1:5001/two_forjunctionstations?subwayname='+junctionStations['junctionStations']+'&subwaydir='+junctionStations['subwayDir']+'&subwayLine='+subwayLine
  var option = { format: 'json', cacheTime: 0 }

  var response = http.getUrl(url,option);
  console.log(response);

  let firstArrivalTime = response['firstArrivalTime'];
  let firstLeftTime = response['firstLeftTime'];
  let secondArrivalTime = response['secondArrivalTime'];
  let secondLeftTime = response['secondLeftTime'];

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
    subwayDir : junctionStations['subwayDir']
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