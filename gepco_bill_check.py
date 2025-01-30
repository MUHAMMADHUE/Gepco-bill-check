import requests

def check_gepco_bill(consumer_number):
    """Fetches GEPCO bill details for a given consumer number."""
    url = f"https://www.gepco.com.pk/check-bill/{consumer_number}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        if "Bill Not Found" in response.text:
            print("Invalid Consumer Number! Please check again.")
            return

        print("Bill Details:")
        print(response.text)  # This would normally parse and show exact bill details.
    
    except requests.exceptions.RequestException as e:
        print("Error fetching bill:", e)

if __name__ == "__main__":
    consumer_number = input("Enter your GEPCO Consumer Number: ")
    check_gepco_bill(consumer_number)
