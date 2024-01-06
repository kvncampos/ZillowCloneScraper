from google_form import google_form
from zillow_scraper import zillow_scraper
from endpoints import GOOGLE_FORM_URL

properties = zillow_scraper()
for info in properties.values():
    google_form(GOOGLE_FORM_URL, address=info["Address"], price=info['Price'], url=info['URL'])
print(f"Total Amount of Listings Recorded: {len(properties.keys())}")
