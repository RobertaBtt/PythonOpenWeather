# openweathermap showcase Python

How to call the openweathermap.org API
## Getting Started

No requirements are needed, no third-part libraries
### To run:

` python3 weather_service/forecast.py -n10 -cBarcelona
` 

Command line parameters:
 
-n10 -cBarcelona
 
- n= number of the days of forecast
- c= the city

Better call by ID if you know the code of the city, 
see https://openweathermap.org/api for the references 

## To run tests:
`python3 -m pytest weather_service/test_forecast.py -v
`