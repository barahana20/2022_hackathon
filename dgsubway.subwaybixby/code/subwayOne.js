
export default function SubwayOne(subwayName) {
  function Time (hour,minute) {
    this.hour = hour;
    this.minute = minute;
  }

  // for prototype
  let subwayResult = {
    letleftDirectionArrivalTime : new Time(12,10),
    leftDirectionLeftTime : new Time(0,10),
    rightDirectionArrivalTime : new Time(12,15),
    rightDirectionLeftTime : new Time(0,5)
  }

  return subwayResult
}