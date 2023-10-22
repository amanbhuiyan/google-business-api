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
    print("********************************************************************")
    print(data)
    for key, value in data.items():
        print(key)

    '''
    print(data['results'][0])
    print('\n')
    print(data['results'][1])
    print('\n')
    print(data['results'][2])
    print('\n')
    print(data['results'][3])
    print('\n')
    print(data['results'][4])
    print('\n')
    print(data['results'][5])
    print('\n')
    print(data['results'][6])
    print('\n')
    print(data['results'][7])
    print('\n')
    print(data['results'][8])
    print('\n')
    print(data['results'][9])
    print('\n')
    print(data['results'][10])
    print('\n')
    print(data['results'][11])


    '''
    businesses_without_reviews = []

    if data.get("status") == "OK":
        for result in data.get("results"):
            # Check if the business has Google reviews
            # if "user_ratings_total" in result and result["user_ratings_total"] == 0:
            business_details = {
                'Name': result.get("name"),
                'Address': result.get("formatted_address"),
                'Phone Number': result.get("formatted_phone_number", "N/A"),
                'rating': result.get("rating"),
                'ratings_count': result.get("user_ratings_total")

                }
            businesses_without_reviews.append(business_details)

            # Check if there are more pages of results
            next_page_token = data.get("next_page_token")
            # print(next_page_token)
            if not next_page_token:
                break


    return JsonResponse({'count': len(businesses_without_reviews) , 'businesses': businesses_without_reviews})




def get_businesses_based_on_ratings(request, city_name, ratinginput):
    google_api_key = "AIzaSyARKFsoUxIKkH3To8T6wY3E2F7AQGqeLd8"
    query = f"businesses in {city_name}"

    params = {
        "query": query,
        "key": google_api_key
    }

    base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    response = requests.get(base_url, params=params)
    data = response.json()
    # print(data)
    for key, value in data.items():
        print(key)
    print(data['results'][0])
    print('\n')
    print(data['results'][1])
    print('\n')
    print(data['results'][2])
    print('\n')
    print(data['results'][3])
    print('\n')
    print(data['results'][4])
    print('\n')
    print(data['results'][5])
    print('\n')
    print(data['results'][6])
    print('\n')
    print(data['results'][7])
    print('\n')
    print(data['results'][8])
    print('\n')
    print(data['results'][9])
    print('\n')
    print(data['results'][10])
    print('\n')
    print(data['results'][11])

    businesses_with_specific_rating = []

    if data.get("status") == "OK":
        for result in data.get("results"):
            # Check if the business has Google reviews
            if "user_ratings_total" in result and (result["rating"] >= ratinginput and result["rating"] < int(ratinginput)+1):
                business_details = {
                    'Name': result.get("name"),
                    'Address': result.get("formatted_address"),
                    'Phone Number': result.get("formatted_phone_number", "N/A"),
                    'rating': result.get("rating"),
                    'ratings_count': result.get("user_ratings_total")
                }
                businesses_with_specific_rating.append(business_details)

                # Check if there are more pages of results
                next_page_token = data.get("next_page_token")
                # print(next_page_token)
                if not next_page_token:
                    break


    return JsonResponse({'count': len(businesses_with_specific_rating) , 'businesses': businesses_with_specific_rating})