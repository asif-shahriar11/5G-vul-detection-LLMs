import pandas as pd

# Load the CSV file
file_path = '5GSC.csv'  # file path to the CSV file containing the texts and labels
df = pd.read_csv(file_path)

# Filter rows where the label is 1 (related to security)
security_related_texts = df[df['label'] == 1]['text']

# Prepare the output file path
output_file_path = 'security_related_texts.txt'  # You can change this path as needed

# Write the security-related texts to a text file
with open(output_file_path, 'w') as file:
    for text in security_related_texts:
        file.write(text + '\n')

print(f'Security-related texts have been saved to {output_file_path}')