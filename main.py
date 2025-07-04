# main.py - Sample Python file for action-repo
"""
Sample Python application for testing GitHub webhooks
"""

def hello_world():
    """Simple hello world function"""
    return "Hello, World!"

def add_numbers(a, b):
    """Add two numbers"""
    return a + b

def main():
    """Main function"""
    print(hello_world())
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")

if __name__ == "__main__":
    main()

# test-file.txt content:
# This file is used for testing push events
# Each push will modify this file with a timestamp

# feature.txt content:
# This file demonstrates feature development
# Used for testing pull request and merge events