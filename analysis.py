"""Reproducible season-level analysis for The McQueen Effect."""
import pandas as pd
seasons=pd.read_csv('data/hamilton_seasons.csv')
teammates=pd.read_csv('data/recent_teammate_comparisons.csv')
for metric in ['wins','podiums','poles']:
    seasons[f'{metric}_rate']=seasons[metric]/seasons['starts']
baseline=seasons.query('2014 <= season <= 2020')
summary={'starts':int(baseline.starts.sum()),'wins':int(baseline.wins.sum()),'podiums':int(baseline.podiums.sum()),'poles':int(baseline.poles.sum()),'win_rate':baseline.wins.sum()/baseline.starts.sum(),'podium_rate':baseline.podiums.sum()/baseline.starts.sum(),'pole_rate':baseline.poles.sum()/baseline.starts.sum()}
teammates['quali_share']=teammates.quali_hamilton/(teammates.quali_hamilton+teammates.quali_teammate)
teammates['race_share']=teammates.race_hamilton/(teammates.race_hamilton+teammates.race_teammate)
teammates['points_share']=teammates.hamilton_points/(teammates.hamilton_points+teammates.teammate_points)
print('2014-2020 baseline')
for key,value in summary.items(): print(f'{key}: {value:.3f}' if isinstance(value,float) else f'{key}: {value}')
print('\nRecent teammate comparison')
print(teammates[['season','teammate','quali_share','race_share','points_share','status']].to_string(index=False))