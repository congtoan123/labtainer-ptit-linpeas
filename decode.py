import base64 
import sys

if len(sys.argv) != 2:
    print("Usage: python decode.py <string>") 
    sys.exit(1)

decoded_data=""
# Get the  string from the command-line argument 
base64_string = sys.argv[1]

# Decode the  string 
# Write your code here
decoded_data = base64.b64decode(base64_string.encode()).decode()

# Print the decoded data to the terminal 
print(decoded_data)
