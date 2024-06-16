import pandas as pd

# Load the CSV file
csv_file_path = 'data/sample_tweets.csv' 
df = pd.read_csv(csv_file_path)

# Create the 'input_output.txt' file
output_file_path = 'data/input_output.txt'
with open(output_file_path, 'w') as f:
    for index, row in df.iterrows():
        input_text = "Help me write tweet about current AI and machine learning development."
        output_text = row['full_text']
        f.write(f"Input: {input_text}\n")
        f.write(f"Output: {output_text}\n")

print(f"File '{output_file_path}' has been created successfully.")
