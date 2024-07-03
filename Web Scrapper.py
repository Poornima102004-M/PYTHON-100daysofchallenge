import requests
from bs4 import BeautifulSoup

# Function to scrape data from a website
def scrape_website(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Example: Extracting and printing titles of articles (for demonstration)
            articles = soup.find_all('article')
            for article in articles:
                title = article.find('h2').get_text().strip()
                print(f"Article Title: {title}")
        else:
            print(f"Error: Unable to fetch data from {url}. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Example usage
url = 'https://example.com'
scrape_website(url)
