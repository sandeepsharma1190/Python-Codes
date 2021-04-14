# Denied Code

import pandas as pd

df = pd.read_csv('Denied_Count_Data.csv')

df.columns

df.info

df['claim_in_out_network_indicator'].value_counts()
df['fund_type_code'].value_counts()
df['facility_or_professional_code'].value_counts()
df['paperless_indicator'].value_counts()






















































