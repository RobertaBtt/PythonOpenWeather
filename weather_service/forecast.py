# -*- coding: utf-8 -*-

__author__ = 'roby'

import sys, getopt
import urllib2
import requests
import datetime
from collections import Counter



class Forecast:
    def main(self, argv):
        number_of_days = ''
        city_name = ''

        try:
            opts, args = getopt.getopt(argv,"hn:c:",["ndays=","cityname="])
        except getopt.GetoptError:
            print 'Usage: forecast.py -n <number of days> -c <city name>'
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print 'Usage: forecast.py -n <number of days> -c <city name>'
                sys.exit()
            elif opt in ("-n", "--ndays"):
                number_of_days = arg
            elif opt in ("-c", "--cityname"):
                city_name = arg
        try:
            print self.__manage_request(number_of_days, city_name)
        except urllib2.HTTPError, e:
            print e


    def __manage_request(self, ndays, cityname):
        result = {}
        list_min_temperature = []
        list_max_temperature = []

        weather_conditions = []
        raining_days = []

        r = requests.get("http://api.openweathermap.org/data/2.5/forecast/"
                "daily?q="+cityname+"&units=metric&cnt="+str(ndays)+"&APPID=0e83edfb1541cb66a71db49f12ac7e98")

        if r.status_code != 200:
            print "Please check city name or number of forecast days"
            return {}

        jsonText = r.json()
        forecast_list = jsonText['list']
        for f in forecast_list:
            list_max_temperature.append(f['temp']['max'])
            list_min_temperature.append(f['temp']['min'])
            weather_conditions.append(f['weather'][0]['description'])
            if f['weather'][0]['main'] == 'Rain':
                raining_days.append( datetime.datetime.fromtimestamp(int(f['dt'])).strftime('%Y-%m-%d %H:%M:%S'))

        min_temp = min(list_min_temperature)
        max_temp = max(list_max_temperature)
        mostCommonWeather = Counter(weather_conditions).most_common()[0][0]

        return {
            'max_temp':max_temp,
            'min_temp': min_temp,
            'most_likely_weather_condition': mostCommonWeather,
            'raining_days_list': raining_days
        }


if __name__ == "__main__":
    forecast = Forecast()
    forecast.main(sys.argv[1:])
