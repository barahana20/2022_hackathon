import console from 'console';
import http from 'http';
export default function subwayOne_ForJunctionStations(junctionStations,subwayLine) {

  // 환승역 관련 JS파일. 백앤드 메소드 필요.
  var url = 'http://18.190.78.1:5001/one_forjunctionstations?subwayname='+junctionStations['junctionStations']+'&subwayLine='+junctionStations['subwayLine']
  var option = { format: 'json', cacheTime: 0 }
  console.log(url)
  console.log(junctionStations)
  var response = http.getUrl(url, option);

  const leftDirectionArrivalTime = response['leftDirectionArrivalTime'];
  const leftDirectionLeftTime = response['leftDirectionLeftTime'];
  const rightDirectionArrivalTime = response['rightDirectionArrivalTime'];
  const rightDirectionLeftTime = response['rightDirectionLeftTime'];

  return {
    leftDirectionArrivalTime: leftDirectionArrivalTime,
    leftDirectionLeftTime: leftDirectionLeftTime,
    rightDirectionArrivalTime: rightDirectionArrivalTime,
    rightDirectionLeftTime: rightDirectionLeftTime,
    subwayLine : junctionStations['subwayLine'],
  }
}