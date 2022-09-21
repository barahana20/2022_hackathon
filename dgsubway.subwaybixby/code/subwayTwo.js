export default function subwayOne(subwayName,subwayDir){

  function Time (hour,minute) {
    this.hour = hour;
    this.minute = minute;
  }

  const firstArrivalTime = new Time(12,10);
  const firstLeftTime = 10;
  const secondArrivalTime = new Time(12,22);
  const secondLeftTime = 22;

  return {
    firstArrivalTime : firstArrivalTime,
    firstLeftTime : firstLeftTime,
    secondArrivalTime : secondArrivalTime,
    secondLeftTime : secondLeftTime
  }
}