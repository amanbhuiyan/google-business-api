from django.http import JsonResponse
from .models import Business
import requests

#from .serializers import BusinessSerializer

def get_businesses_without_reviews(request, city_name):

    google_api_key = "AIzaSyARKFsoUxIKkH3To8T6wY3E2F7AQGqeLd8"


    query = f"businesses in {city_name}"

    params = {
        "query": query,
        "key": google_api_key
    }

    base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    response = requests.get(base_url, params=params)
    data = response.json()
    print(data)

    businesses_without_reviews = []

    if data.get("status") == "OK":
        for result in data.get("results"):
            # Check if the business has Google reviews
            if "user_ratings_total" in result and result["user_ratings_total"] == 0:
                business_details = {
                    'Name': result.get("name"),
                    'Address': result.get("formatted_address"),
                    'Phone Number': result.get("formatted_phone_number", "N/A"),
                    'rating': result.get("rating")
                }
                businesses_without_reviews.append(business_details)

            # Check if there are more pages of results
                next_page_token = data.get("next_page_token")
                print(next_page_token)
                if not next_page_token:
                    break


    return JsonResponse({'count': len(businesses_without_reviews) , 'businesses': businesses_without_reviews})