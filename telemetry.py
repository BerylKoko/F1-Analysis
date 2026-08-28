import fastf1
import json


fastf1.Cache.enable_cache('f1_cache') 

print("🚨 Accessing the 2025 F1 Vault...")
# ACT 2: Load Monza 2025 Race Session (Last year's slump baseline)
session = fastf1.get_session(2025, 'Monza', 'R')
session.load(telemetry=True)


ham_lap = session.laps.pick_driver('HAM').pick_fastest()
lec_lap = session.laps.pick_driver('LEC').pick_fastest()


ham_telemetry = ham_lap.get_telemetry()[['Speed', 'Brake', 'Throttle']].to_dict(orient='records')
lec_telemetry = lec_lap.get_telemetry()[['Speed', 'Brake', 'Throttle']].to_dict(orient='records')


combined_data = {"hamilton": ham_telemetry[:100], "leclerc": lec_telemetry[:100]} # Grab a clean 100-point sample
with open('act2_monza_2025.json', 'w') as f:
    json.dump(combined_data, f)

print("🏁 Act 2 Data Captured Successfully! Python work is done.")