import argparse
import json
from metadata import get_metadata, get_metadata_key

def main():
    parser = argparse.ArgumentParser(description="Query Azure instance metadata")
    parser.add_argument("--key", help="Dot-separated key path to retrieve (e.g. compute.name)", required=False)
    args = parser.parse_args()

    try:
        if args.key:
            result = get_metadata_key(args.key)
        else:
            result = get_metadata()
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
