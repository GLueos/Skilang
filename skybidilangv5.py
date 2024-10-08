variables = {}

class SkybidiSyntaxError(Exception):
    """Custom exception for syntax errors in Skybidi code."""
    pass

def execute_skybidi_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:  # Ensure UTF-8 encoding
        program = file.readlines()

    for string in program:
        string = string.strip()  # Remove any leading/trailing whitespace
        
        # Ignore lines containing the U+1F6BD character (toilet emoji)
        if "\U0001F6BD" in string:  # U+1F6BD is the toilet emoji
            continue  # Skip this line and move to the next

        # Check for lines that are not comments and do not contain 'skibidi'
        if "skibidi" not in string:
            if "dopdopdopyesyes" not in string:
                raise SkybidiSyntaxError(f"Error: Line: '{string}' does not contain w rizz formatting")

        if "skibidi skibidi" in string and not "skibidi skibidi skibidi" in string:
            parts = string.split("skibidi skibidi")
            if len(parts) >= 2:
                var_name = parts[1].strip()
                variables[var_name] = None

        elif "skibidi skibidi skibidi" in string and not "skibidi skibidi skibidi skibidi" in string:
            parts = string.split("skibidi skibidi skibidi")
            if len(parts) >= 2:
                assignment = parts[1].strip().split(" ", 1)
                if len(assignment) == 2:
                    var_name = assignment[0].strip()
                    var_value = assignment[1].strip()
                    if var_name in variables:
                        variables[var_name] = var_value

        elif "skibidi skibidi skibidi skibidi" in string:
            parts = string.split("skibidi skibidi skibidi skibidi")
            if len(parts) >= 2:
                var_name = parts[1].strip()
                if var_name in variables:
                    print(variables[var_name])  # Print the variable value

        elif "skibidi" in string and "skibidi skibidi" not in string:
            string = string.replace("skibidi", "")
            print(string)  # Print the direct message input

# Main program execution
print("Welcome to the Skybidi lang Interpreter")
print("Version 1.5")
while True:
    filename = input("Enter the name of the skibidi code file: ")
    if filename.endswith('.sk'):
        try:
            execute_skybidi_file(filename)
        except FileNotFoundError:
            print("File not found. Please check the file name and try again.")
        except SkybidiSyntaxError as e:
            print(e)  # Print the custom error message
    else:
        print("Please provide a valid .sk file.")
    print("")
