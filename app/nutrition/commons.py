import requests


def get_nutrition_api(request):
    try:
        food_name = request.data.get('food_name', None)
        offset = request.data.get('offset', 0)
        limit = request.data.get('limit', 10)

        app_id = "900da95e"
        app_key = "40698503668e0bb3897581f4766d77f9"
        edamam_url = f"https://api.edamam.com/search"

        headers = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9,mr;q=0.8",
            "origin": "https://developer.edamam.com",
            "priority": "u=1, i",
            "referer": "https://developer.edamam.com/",
            "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        }

        params = {
            "app_id": app_id,
            "app_key": app_key,
            "q": food_name,
            "from": offset,
            "to": limit
        }
        response = requests.get(edamam_url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as ex:
        return False