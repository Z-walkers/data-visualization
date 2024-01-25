import re
import pandas as pd
import numpy as np
# Read the JavaScript file
with open('world.js', 'r') as file:
    js_content = file.read()

# Extract country names using regular expressions
pattern = r'}, "properties": {"name":\s*"(.+?)"'
country_names = re.findall(pattern, js_content)

# Create a DataFrame
df = pd.DataFrame({'Country': country_names})
df = df.drop(df.index[-2:])
random_values = np.tile(np.random.permutation(np.arange(1, 20)), len(df)//10 + 1)[:len(df)]
df['values'] = random_values
df.set_index('Country', inplace=True)
df.loc["China","values"]=600
df.loc["United States","values"]=1500
df.loc["Japan","values"]=5000
df.loc["Russia","values"]=100
df.loc["United Kingdom","values"]=120
df.loc["France","values"]=150
df.loc["Finland","values"]=50
df.loc["Germany","values"]=100
df.loc["Spain","values"]=130
df.reset_index(inplace=True)
df=df.sort_values('values')
# Display the DataFrame
df.to_json('gl.json',orient='records')