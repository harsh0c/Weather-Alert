from uagents import Bureau
import requests
from uagents import Model, Agent, Context, Protocol
from uagents.setup import fund_agent_if_low


from asgiref.sync import sync_to_async
import django
import sys

from dotenv import load_dotenv
import os

load_dotenv()


sys.path.append("C:/Users/Harsh/Videos/weatherAlert/weather/")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather.settings')
django.setup()

from walert.models import CityData,AlertData


class weatherRequest(Model):
    """
        Represents a weather alert Request.
        Attributes:
            city(str): the city in which user wants to set alert for.
        """
    city: str


weather_seed = "geoapi parking adaptor weather_agent secret phrase"

weather_agent = Agent(
    name="weather_adaptor",
    seed=weather_seed,
)

fund_agent_if_low(weather_agent.wallet.address())

weather_API_KEY = os.environ.get('WEATHER_API_KEY')

def get_weather_from_api(city) -> list:
    """
    With all the user preferences, this function sends the request to the Geoapify Parking API,
    which returns the response.
    """
    # print("api call")
    try:
        response = requests.get(
            url=
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={weather_API_KEY}",
            timeout=60,
        )
        return response.json()
    except Exception as exc:
        print("Error: ", exc)
        return []


@sync_to_async
def get_city():
    cyData=(CityData.objects.first())
    # print(cyData)
    return str(cyData.name)

@sync_to_async
def save_alert(currtemp):
    cyData=(CityData.objects.first())
    if AlertData:
        AlertData.objects.all().delete()
    if(currtemp<cyData.mintemp):
        if AlertData:
            AlertData.objects.all().delete()
        newAlert=AlertData()
        newAlert.alertmsg="Current Temperature has dropped below the minimum temperature specified."
        newAlert.save()

    elif(currtemp>cyData.maxtemp):
        if AlertData:
            AlertData.objects.all().delete()
        newAlert=AlertData()
        newAlert.alertmsg="Current Temperature has risen above the maximum temperature specified."
        newAlert.save()



@weather_agent.on_interval(period=2.0)
async def send_message(ctx: Context):
    await ctx.send("agent1qvzysgxw0tpae8gfhp24qe8lv8catt053dkfhwcvn3z23j65en9mcqcsu97",weatherRequest(city= await get_city()))


@weather_agent.on_message(model=weatherRequest)
async def geoapi_parking(ctx: Context, sender: str, msg: weatherRequest):

    ctx.logger.info(f"Received message from {sender}")
    try:
        response = get_weather_from_api(msg.city)

        data = {
            "country_code": str(response['sys']['country']),
            "coordinate": str(response['coord']['lon']) + ', '
            + str(response['coord']['lat']),

            "temp": str(response['main']['temp']) + ' °C',
            "pressure": str(response['main']['pressure']),
            "humidity": str(response['main']['humidity']),
            'main': str(response['weather'][0]['main']),
            'description': str(response['weather'][0]['description']),
            'icon': response['weather'][0]['icon'],
        }
        currtemp=response['main']['temp']
        
        await save_alert(currtemp)
        
        # print(data)
        
    except Exception as exc:
        print("error")
        ctx.logger.error(exc)


if __name__ == "__main__":
    bureau = Bureau(endpoint="http://127.0.0.1:8000/submit", port=8000)
    print(
        f"Adding top activities weather_agent to Bureau: {weather_agent.address}"
    )
    bureau.add(weather_agent)
    bureau.run()
    