"""Extend Beryl's FastF1 session -> fastest laps -> JSON workflow.
Run: python telemetry.py --year 2025 --event Monza --session R --drivers HAM LEC
"""
import argparse, json
from pathlib import Path
from datetime import datetime, timezone
import fastf1

def export(year, event, kind, drivers, output):
    cache=Path(__file__).parent/'f1_cache';cache.mkdir(exist_ok=True)
    fastf1.Cache.enable_cache(str(cache))
    session=fastf1.get_session(year,event,kind)
    session.load(telemetry=True,weather=False,messages=True)
    result=[]
    for driver in drivers:
        lap=session.laps.pick_drivers(driver).pick_fastest()
        if lap is None or lap.empty: raise ValueError(f'No valid lap for {driver}')
        # Car data preserves measured channels; distance is integrated by FastF1.
        data=lap.get_car_data().add_distance().dropna(subset=['Distance','Speed','Throttle','Brake'])
        data=data.sort_values('Distance').drop_duplicates('Distance')
        samples=[{'distance':round(float(row.Distance),1),'speed':int(row.Speed),'throttle':int(row.Throttle),'brake':bool(row.Brake),'time':round(row.Time.total_seconds(),3)} for row in data.itertuples()]
        result.append({'driver':driver,'lapNumber':int(lap.LapNumber),'lapSeconds':round(lap.LapTime.total_seconds(),3),'compound':str(lap.Compound),'tyreLife':int(lap.TyreLife),'samples':samples})
    payload={'schemaVersion':1,'id':f'{year}-{event.lower()}-{kind.lower()}','year':year,'event':str(session.event.EventName),'session':kind,'date':str(session.date.date()),'generatedAt':datetime.now(timezone.utc).isoformat(),'source':'FastF1 / Formula 1 timing','sourceUrl':'https://docs.fastf1.dev/','method':'Fastest timed lap for each driver. Distance is integrated from speed; laps are not controlled for fuel, tyres or traffic.','drivers':result}
    Path(output).parent.mkdir(parents=True,exist_ok=True)
    Path(output).write_text(json.dumps(payload,separators=(',',':'),allow_nan=False))
    print(f'Exported {output}: '+', '.join(f'{d["driver"]} {len(d["samples"])} samples' for d in result))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--year',type=int,default=2025);p.add_argument('--event',default='Monza');p.add_argument('--session',default='R');p.add_argument('--drivers',nargs='+',default=['HAM','LEC']);p.add_argument('--output',default='public/data/2025-monza-r.json');a=p.parse_args()
    export(a.year,a.event,a.session,a.drivers,a.output)
