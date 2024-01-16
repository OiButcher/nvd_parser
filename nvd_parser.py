import json

def parse_nvd_data(file_path):
    with open(file_path, 'r') as file:
        nvd_data = json.load(file)

    vulnerabilities = []

    for item in nvd_data.get('CVE_Items', []):
        cve_id = item.get('cve', {}).get('CVE_data_meta', {}).get('ID', '')
        description = item.get('cve', {}).get('description', {}).get('description_data', [])[0].get('value', '')
        # Extract more details as needed

        vulnerabilities.append({
            'cve_id': cve_id,
            'description': description,
            # Add more fields
        })

    return vulnerabilities

if __name__ == "__main__":
    nvd_file_path = "/home/dogukan/nvdcve-1.1-modified.json"  # Replace with the actual path
    parsed_data = parse_nvd_data(nvd_file_path)

    # Example: Print the first 5 vulnerabilities
    for vulnerability in parsed_data[:5]:
        print(f"CVE ID: {vulnerability['cve_id']}")
        print(f"Description: {vulnerability['description']}")
        print("-" * 50)

