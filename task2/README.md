This script retrieves Azure VM metadata using the Azure Instance Metadata Service (IMDS).

## Features
- Queries Azure Instance Metadata Service (IMDS)
- Returns structured JSON output
- Supports key filtering (e.g., `compute.name`)
- Includes unit tests with mocked metadata
- No external dependencies except `requests`

## Usage

### Prerequisite

This script **only works on an Azure VM** when querying live metadata.  
Local testing uses mock data via unit tests.

```bash
pip install -r requirements.txt
python main.py                
python main.py --key compute.name  


Testing
pytest test_metadata.py


