import requests
import json

def check_mobile_network(number):
    # Hypothetical API endpoint (does not exist)
    api_url = "https://api.example.com/mobile-network-lookup"
    headers = {
        "Authorization": "Bearer your_api_key",  # Replace with valid API key
        "Content-Type": "application/json"
    }
    payload = {
        "mobile_number": number,
        "country_code": "+92"
    }
    
    try:
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        
        if data.get("success"):
            return {
                "number": number,
                "network": data.get("network", "Unknown"),
                "status": data.get("status", "Active")
            }
        else:
            return {"error": "No data found for this number"}
            
    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {str(e)}"}

def main():
    # Example usage
    mobile_number = input("Enter Pakistani mobile number (e.g., 3001234567): ")
    if not mobile_number.startswith("0") or len(mobile_number) != 10:
        print("Please enter a valid 10-digit Pakistani mobile number without country code.")
        return
    
    result = check_mobile_network(mobile_number)
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(f"Number: {result['number']}")
        print(f"Network: {result['network']}")
        print(f"Status: {result['status']}")

if __name__ == "__main__":
    main()