import pandas as pd

"""
Nomor 1
We have already learned how to create DataFrame from files here. 
Now, we are going to create a DataFrame from a larger csv file on our datasets.
"""
df = pd.read_csv('https://raw.githubusercontent.com/Immersive-DataEngineer-Resource/ingestion-data/main/dataset/yellow_tripdata_2020-07.csv')
print(df.head())

# Nomor 2 Rename all the columns with snake_case format.
df.rename(columns={ 'VendorID':'vendor_id', 'RatecodeID': 'rate_code_id', 'PULocationID': 'pu_location_id', 'DOLocationID':'do_location_id'}, 
          inplace=True)

print(df.head())

# """
# Nomor 3 
# Select only 10 top of highest number of passenger_count, show only columns vendor_id, passenger_count, trip_distance, payment_type, 
# fare_amount, extra, mta_tax, tip_amount, tolls_amount, improvement_surcharge, total_amount, congestion_surcharge from the DataFrame.
# """ 
df_new = df[['vendor_id', 'passenger_count', 'trip_distance', 'rate_code_id', 'payment_type', 'fare_amount', 'extra', 'mta_tax', 'tip_amount','tolls_amount',
             'improvement_surcharge', 'total_amount','congestion_surcharge']]

df_sorted = df_new.sort_values(by='passenger_count', ascending=False)
print(df_sorted.head(10))

# # Nomor 4 [Extra] Cast the data type to the appropriate value.
df['vendor_id'].fillna(0, inplace=True)
df['vendor_id'] = df['vendor_id'].astype(int)

df['passenger_count'].fillna(0, inplace=True)
df['passenger_count'] = df['passenger_count'].astype(int)

df['tpep_pickup_datetime'].fillna(0, inplace=True)
df['tpep_pickup_datetime']= df['tpep_pickup_datetime'].astype('datetime64[ns]')

df['rate_code_id'].fillna(0, inplace=True)
df['store_and_fwd_flag'].fillna(0, inplace=True)
df['payment_type'].fillna(0, inplace=True)

df['tpep_dropoff_datetime'].fillna(0, inplace=True)
df['tpep_dropoff_datetime']= df['tpep_dropoff_datetime'].astype('datetime64[ns]')

df['tolls_amount'].fillna(0, inplace=True)
df['tolls_amount']= df['tolls_amount'].astype(float)
print(df.dtypes)
print(df.info())


    