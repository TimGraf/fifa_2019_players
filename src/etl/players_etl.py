import pandas as pd
from sqlalchemy import create_engine

# Load in the data
df = pd.read_csv('data/external/data.csv')

# Instantiate sqlachemy.create_engine object
engine = create_engine('postgresql://postgres:password@localhost:5432/svc')

# Save the data from dataframe to postgres table "fifa_players_2019"
df.to_sql(
    'fifa_players_2019',
    engine,
    index=False, # Not copying over the index
    index_label="Index"
)
