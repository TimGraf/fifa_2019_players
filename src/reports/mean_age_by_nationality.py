import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# Instantiate sqlachemy.create_engine object
engine = create_engine('postgresql://postgres:password@localhost:5432/svc')

query = 'select "Index", "Age", "Nationality" from public.fifa_players_2019'

df = pd.read_sql(query, engine, index_col='Index')

stats = df[['Age', 'Nationality']].groupby('Nationality').agg([np.sum, np.mean, np.size])

stats.columns = ['Sum Age', 'Mean Age', 'Player Count']

stats.to_csv('data/processed/mean_age_by_nationality.csv')
