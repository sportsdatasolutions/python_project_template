import pandas

# Assign URL to json_url
json_url = 'https://sportsdatasolutionsacademy.s3.eu-west-2.amazonaws.com/data/swimming_psb_data.json'

# Read JSON
df = pandas.read_json(json_url, orient='records')

# Filter British Athletes and drop any duplicate rows
df = df[df['c_NOC'] == 'Great Britain'].drop_duplicates()

# Write To JSON
df.to_json(r'gb_swimming_psb_data.json', orient='records')

# Write To CSV
df.to_csv(r'gb_swimming_psb_data.csv', index=False)
