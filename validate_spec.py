import sys
import yaml
from openapi_spec_validator import validate_spec

def validate_openapi_file(filename):
    try:
        # Load the OpenAPI spec from the YAML file
        with open(filename, 'r') as f:
            spec_dict = yaml.safe_load(f)

        # Validate the specification
        validate_spec(spec_dict)
        print(f"OpenAPI specification in '{filename}' is valid!")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except yaml.YAMLError as e:
        print(f"Error: Invalid YAML in '{filename}': {e}")
    except Exception as e:
        print(f"Error: Invalid OpenAPI specification in '{filename}': {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_spec.py <path_to_openapi_yaml>")
    else:
        validate_openapi_file(sys.argv[1])
