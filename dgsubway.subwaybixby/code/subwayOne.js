import console from 'console';
export default function subwayOne(subwayName) {
  console.log(subwayName);
  function Time (hour,minute) {
    this.hour = hour;
    this.minute = minute;
  }
  const leftDirectionArrivalTime = new Time(12,10);
  const leftDirectionLeftTime = new Time(0,10);
  const rightDirectionArrivalTime = new Time(12,15);
  const rightDirectionLeftTime = new Time(0,5);
  // for prototype
  // let subwayResult = {
  //   leftDirectionArrivalTime : new Time(12,10),
  //   leftDirectionLeftTime : new Time(0,10),
  //   rightDirectionArrivalTime : new Time(12,15),
  //   rightDirectionLeftTime : new Time(0,5)
  // }
  return {
    leftDirectionArrivalTime: leftDirectionArrivalTime,
    leftDirectionLeftTime: leftDirectionLeftTime,
    rightDirectionArrivalTime: rightDirectionArrivalTime,
    rightDirectionLeftTime: rightDirectionLeftTime
  }
}