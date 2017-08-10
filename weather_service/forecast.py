__author__ = 'roby'

import sys, getopt
import urllib2

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

       self.__manage_request(number_of_days, city_name)

    def __manage_request(self, ndays, cityname):
        test = urllib2.urlopen("http://api.openweathermap.org/data/2.5/forecast/"
                "daily?q="+cityname+"&units=metric&cnt="+ndays+"&APPID=0e83edfb1541cb66a71db49f12ac7e98").read()
        print test

if __name__ == "__main__":
   forecast = Forecast()
   forecast.main(sys.argv[1:])



