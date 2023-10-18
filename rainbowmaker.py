import hashlib

# Input and output file paths
input_file_path = "input.txt"
output_file_path = "output.txt"

# Open the input and output files
with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
    # Read input file line by line
    for line in input_file:
        # Remove trailing newline characters
        line = line.strip()

        # Calculate SHA-256 hash
        sha256_hash = hashlib.sha256(line.encode()).hexdigest()

        # Write the original string and its hash to the output file
        output_file.write(f"{line} {sha256_hash}\n")

# Close the files
input_file.close()
output_file.close()

print("Original strings and their hashes have been written to", output_file_path)
