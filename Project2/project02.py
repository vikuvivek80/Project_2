
import string
import random
class TinyURLService:
def __init__(self):
self.url_map = {}
self.short_to_long = {}
self.characters = string.ascii_letters + string.digits
self.base_url = "http://tinyurl.com/"
self.key_length = 6
def generate_short_url(self):
while True:
short_url = ''.join(random.choice(self.characters) for _ in
range(self.key_length))
if short_url not in self.short_to_long:
return short_url
def shorten_url(self, long_url):
if long_url in self.url_map:
return self.base_url + self.url_map[long_url]
short_url = self.generate_short_url()
self.url_map[long_url] = short_url
self.short_to_long[short_url] = long_url
return self.base_url + short_url
def retrieve_long_url(self, short_url):
short_key = short_url.replace(self.base_url, "")
return self.short_to_long.get(short_key, "URL not found")
def main():
service = TinyURLService()
print("Welcome to the TinyURL Service!")
while True:
print("\nMenu:")
print("1. Shorten a URL")
print("2. Retrieve a URL")
print("3. Exit")
choice = input("Enter your choice: ")
if choice == '1':
long_url = input("Enter the URL to shorten: ")
short_url = service.shorten_url(long_url)
print(f"Shortened URL: {short_url}")
elif choice == '2':
short_url = input("Enter the shortened URL: ")
long_url = service.retrieve_long_url(short_url)
print(f"Original URL: {long_url}")
elif choice == '3':
print("Goodbye!")
break
else:
print("Invalid choice. Please enter 1, 2, or 3.")
if __name__ == "__main__":
main()