import re
import sys

def to_kebab_case(string):
  # Replace any non-alphanumeric characters with a hyphen
  string = re.sub(r'\W+', '-', string)
  # Make the string all lowercase
  string = string.lower()
  return string

# Get the string from the command line argument
if len(sys.argv) < 2 or not sys.argv[1]: exit("you didn't pass a string")
if len(sys.argv) > 2: exit("use double quote to wrap your string")
string = sys.argv[1]

# Convert the string to kebab case
kebab_case = to_kebab_case(string)

# Print the result
print(kebab_case)