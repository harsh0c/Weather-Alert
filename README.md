
# Weather Alert Website

A weather alert app built using Django framework.  
It lets users set their preferred minimum and maximum temperature and location. 
Displays an alert when the current temperature in their chosen
location goes below the minimum or above the maximum threshold they've set.  

## Run Locally

### Step 1: Prerequisites
Before starting, you'll need the following:
* Python (3.8+ is recommended)

Clone the project
```bash
  git clone https://github.com/harsh0c/Weather-Alert
```

### Step 2: Set up .env file
To run the demo, you need API keys from:
* OpenWeather, visit openweathermap.org
* Sign up or log in.
* Search for the Current Weather Data and subscribe.
* Once subscribed, copy your API-Key

Once you have your API key, create a .env file in the same directory as manage.py
```bash
WEATHER_API_KEY={YOUR_API_KEY}
```

To use the environment variables from .env and install the project:
```bash
pip intall requirements.txt
```
### Step 3: Run the agent script
To run the agent :
```bash
cd walert
python myagent.py
```

### Step 4: Run the main script(Django Frontend)
To run the project :  
Go the weather folder  
Open a new terminal in the same directory as manage.py
```bash
python manage.py runserver
```
Once you hit enter, visit http://127.0.0.1:8000/ 
Here you will see the web page, enter the city name for which you want to create an alert along with the minimum and maximum temperature.



## Screenshots


Here user can enter the City and preferred minimum and maximum temperature.  

![App Screenshot](https://i.imgur.com/6jHUsuj.png)  

Here the city entered is Mumbai and minimum and maximum temperature is set to 20℃ and 40℃ respectively.  

![App Screenshot](https://imgur.com/rDjBkOd.png)  



The current temperature was 32.99℃ and we changed the maximum temperature to 30℃ on refreshing the page we got the alert.  

![App Screenshot](https://imgur.com/YXg7A1f.png)
