import threading
import requests

# Function to fetch data from a URL
def fetch_url(url):
    try:
        response = requests.get(url)
        print(f"Fetched data from {url}: {response.text[:50]}...")
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")

# List of URLs to fetch
urls = [
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/2',
    'https://jsonplaceholder.typicode.com/posts/3',
    'https://jsonplaceholder.typicode.com/posts/4',
    'https://jsonplaceholder.typicode.com/posts/5'
]

# Create threads for each URL
threads = []
for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads have finished.")
