"""
# This script demonstrates how to use argparse to handle command-line arguments
# with mandatory parameters. It requires two parameters: --foo and --bar.
# The script will print the values of these parameters when executed.
# The parameters are mandatory, meaning the script will raise an error if they are not provided.
# The script uses argparse, a standard library in Python for parsing command-line arguments.
# The script is designed to be run from the command line, and it will print the
# values of the parameters provided by the user.
# The script is a simple demonstration and can be extended with additional logic as needed.
"""

import argparse

parser = argparse.ArgumentParser(description="My script with mandatory params")
parser.add_argument("--foo", required=True, help="First parameter")
parser.add_argument("--bar", required=True, help="Second parameter")
args = parser.parse_args()

print(f"Foo = {args.foo}")
print(f"Bar = {args.bar}")
# ... rest of your logic
