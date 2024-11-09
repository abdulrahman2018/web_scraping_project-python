import requests
from bs4 import BeautifulSoup

def fetch_and_parse(url):
    try:
        # Fetch the page content
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Example: Find and print all headers in the page
        headers = soup.find_all(['h1', 'h2', 'h3'])
        print("Headers found on the page:")
        for header in headers:
            print(f"{header.name}: {header.text.strip()}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example URL for testing
    url = input("Enter the URL to fetch and parse: ")
    fetch_and_parse(url)

