import requests

def fetch_country_data(state):
    if state.get("error"):
        return state

    country = state.get("country")

    url = f"https://restcountries.com/v3.1/name/{country}"

    try:
        res = requests.get(url, timeout=5)

        if res.status_code != 200:
            return {"error": f"Country '{country}' not found"}

        data = res.json()[0]

        currencies = data.get("currencies", {})
        currency_name = (
            list(currencies.values())[0]["name"]
            if currencies else "N/A"
        )

        extracted = {
            "capital": data.get("capital", ["N/A"])[0],
            "population": data.get("population", "N/A"),
            "currency": currency_name,
            "region": data.get("region", "N/A")
        }

        return {"data": extracted}

    except Exception:
        return {"error": "API request failed"}