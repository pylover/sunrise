from sunrise import do
import requests, json
import pytest


@pytest.fixture
def weather_fixture():
    api_key = "fa313a7fbbcd1bc409691eed433355a9"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "tehran"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    weather_request = requests.get(complete_url) 
    weather_response = weather_request.json()
    if weather_response["cod"] != "404":
        main_data = weather_response["main"]
        return [
                    main_data["temp"], 
                    main_data["humidity"], 
                    main_data["pressure"],
                ]
    else:
        return "City not found."


def test_weather(weather_fixture):
    assert weather_fixture[0] == do('temp of tehran')
    assert weather_fixture[1] == do('humidity of tehran')
    assert weather_fixture[2] == do('pressure of tehran')

