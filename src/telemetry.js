// Linear interpolation only for continuous channels; brake state uses nearest sample.
export function sampleAt(samples,distance){
 if(!samples.length)return null;
 if(distance<=samples[0].distance)return samples[0];
 if(distance>=samples.at(-1).distance)return samples.at(-1);
 let low=0,high=samples.length-1;
 while(high-low>1){const mid=Math.floor((low+high)/2);if(samples[mid].distance<distance)low=mid;else high=mid;}
 const a=samples[low],b=samples[high],t=(distance-a.distance)/(b.distance-a.distance);
 return {distance,speed:a.speed+(b.speed-a.speed)*t,throttle:a.throttle+(b.throttle-a.throttle)*t,time:a.time+(b.time-a.time)*t,brake:t<.5?a.brake:b.brake};
}
export function commonRange(a,b){return [Math.max(a[0].distance,b[0].distance),Math.min(a.at(-1).distance,b.at(-1).distance)];}
