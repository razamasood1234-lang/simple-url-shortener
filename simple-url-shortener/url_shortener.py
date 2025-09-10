# url_shortener.py
# Step 6: Final Polish and Completion

import hashlib
import random
import string

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def _generate_short_code(self, long_url):
        url_bytes = long_url.encode('utf-8')
        hash_object = hashlib.md5(url_bytes)
        hex_dig = hash_object.hexdigest()
        return hex_dig[:6]

    def shorten_url(self, long_url):
        short_code = self._generate_short_code(long_url)
        
        if short_code in self.url_mapping:
            # Handle collision silently for the user
            salt = ''.join(random.choices(string.ascii_letters + string.digits, k=2))
            new_input = long_url + salt
            short_code = self._generate_short_code(new_input)
            
            while short_code in self.url_mapping:
                salt = ''.join(random.choices(string.ascii_letters + string.digits, k=2))
                new_input = long_url + salt
                short_code = self._generate_short_code(new_input)
        
        self.url_mapping[short_code] = long_url
        return short_code

    def retrieve_url(self, short_code):
        return self.url_mapping.get(short_code)

    def list_all(self): # <-- NEW HELPER METHOD
        """Returns a copy of the entire url_mapping dictionary"""
        return self.url_mapping.copy()

def main():
    shortener = URLShortener()
    
    print("=" * 50)
    print("        SIMPLE URL SHORTENER")
    print("=" * 50)
    print("Commands:")
    print("  shorten <URL>    - Shorten a URL")
    print("  lookup <code>    - Retrieve original URL")
    print("  list             - Show all shortened URLs")
    print("  exit             - Quit the program")
    print("=" * 50)
    
    while True:
        try: # <-- ADDED ERROR HANDLING
            user_input = input("\nEnter command: ").strip()
            if not user_input:
                continue
                
            parts = user_input.split()
            command = parts[0].lower()
            
            if command == "shorten":
                if len(parts) < 2:
                    print("Error: Please provide a URL to shorten.")
                    print("Usage: shorten <URL>")
                    continue
                    
                long_url = ' '.join(parts[1:])
                # Simple validation: check if it looks like a URL
                if not long_url.startswith(('http://', 'https://')):
                    print("Warning: URL should start with http:// or https://")
                    
                short_code = shortener.shorten_url(long_url)
                print(f"✅ Shortened successfully!")
                print(f"   Original: {long_url}")
                print(f"   Short: http://short.url/{short_code}")
                
            elif command == "lookup":
                if len(parts) < 2:
                    print("Error: Please provide a short code to look up.")
                    print("Usage: lookup <short_code>")
                    continue
                    
                short_code = parts[1]
                original_url = shortener.retrieve_url(short_code)
                
                if original_url:
                    print(f"✅ Original URL found:")
                    print(f"   http://short.url/{short_code} -> {original_url}")
                else:
                    print(f"❌ Error: Short code '{short_code}' not found.")
                    
            elif command == "list":
                mappings = shortener.list_all()
                
                if not mappings:
                    print("No URLs have been shortened yet.")
                else:
                    print(f"\n📋 All Shortened URLs ({len(mappings)} total):")
                    print("-" * 60)
                    for short_code, url in mappings.items():
                        # Trim very long URLs for cleaner display
                        display_url = url if len(url) <= 50 else url[:47] + "..."
                        print(f"{short_code} -> {display_url}")
                    print("-" * 60)
                    
            elif command == "exit":
                print("Thank you for using the URL Shortener. Goodbye!")
                break
                
            elif command == "help":
                print("Available commands:")
                print("  shorten <URL>    - Shorten a URL")
                print("  lookup <code>    - Retrieve original URL")
                print("  list             - Show all shortened URLs")
                print("  exit             - Quit the program")
                print("  help             - Show this help message")
                
            else:
                print(f"Error: Unknown command '{command}'. Type 'help' for options.")
                
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            # Catch any unexpected errors to prevent crash
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()