from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine

# Initialize the model
model = SentenceTransformer('all-MiniLM-L6-v2') # a smaller and faster model of MiniLM

# Load the security-related texts
input_file_path = 'security_related_texts.txt'
with open(input_file_path, 'r') as file:
    lines = file.readlines()

# Prepare for processing
processed_lines = [line.strip() for line in lines if line.strip()]  # Remove empty lines and strip whitespace
contexts = []  # To store groups of sentences belonging to the same context

# Process sentences to group by context
for i in range(len(processed_lines) - 1):
    sentence1 = processed_lines[i]
    sentence2 = processed_lines[i + 1]
    
    # Generate embeddings (numerical vector representations) for the sentences
    embeddings = model.encode([sentence1, sentence2])
    # calculates cosine distance between two embeddings to measure similarity
    similarity = 1 - cosine(embeddings[0], embeddings[1])
    
    # Threshold for considering sentences to be in the same context
    threshold = 0.7  # Adjust based on experimentation
    
    # if the similarity is greater than the threshold, the sentences are considered to be in the same context
    # otherwise, the sentences are considered to be in different contexts
    if similarity > threshold: # same context
        if not contexts or sentence1 not in contexts[-1]: # new context
            contexts.append([sentence1, sentence2])
        else: # add to the current context
            contexts[-1].append(sentence2)
    else: # different contexts
        contexts.append([sentence1])
        if i == len(processed_lines) - 2:  # Ensure the last sentence is included if it starts a new context
            contexts.append([sentence2])

# Prepare the output file
output_file_path = 'contextual_texts.txt'
with open(output_file_path, 'w') as file:
    for context_group in contexts:
        for sentence in context_group:
            file.write(sentence + '\n')
        file.write('\n')  # Separate contexts by a blank line for readability

print(f'Contextual texts have been saved to {output_file_path}')
print(f'Number of contexts: {len(contexts)}')
print(f'Example context: {contexts[0]}')

