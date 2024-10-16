import json


def write_json_with_replacement(data, filename, old_string, new_string):
    """
    Writes a JSON object to a file after replacing all occurrences of a string.

    Args:
      data: The JSON object (dictionary or list) to write.
      filename: The name of the file to write to.
      old_string: The string to be replaced.
      new_string: The string to replace with.
    """
    try:
        # Convert the JSON object to a string
        json_string = json.dumps(data)

        # Replace the old string with the new string
        modified_json_string = json_string.replace(old_string, new_string)

        # Convert back to json object to use json.dump with indention
        modified_json_object = json.loads(modified_json_string)

        # Write the modified JSON string to the file
        with open(filename, 'w') as f:
            json.dump(modified_json_object, f, indent=2)

        print(f"JSON data written to {filename} with string replacement.")

    except Exception as e:
        print(f"Error writing JSON data: {e}")
