import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta
from data_manager import DataManager

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self) -> None:
        self.API_KEY = "YOUR_API_KEY"
        self.url = "https://tequila-api.kiwi.com/"
        self.headers = {
            "apikey":self.API_KEY
        }
        self.today = datetime.now()
        self.today_formatted = self.today.strftime("%d/%m/%Y")

        self.future = self.today + relativedelta(months=6)
        self.future_formatted = self.future.strftime("%d/%m/%Y")

        self.google_sheet = DataManager()
        self.stepover = 0

    def search_for_code(self,city_name):
        self.search_url = "https://tequila-api.kiwi.com/locations/query"
        self.para = {
            "term":city_name
        }

        response = requests.get(url=self.search_url, params=self.para, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def fill_iata_code(self):
        self.iata_list = []
        for i in self.google_sheet.read()["prices"]:
            self.city = i["city"]
            self.search_code = self.search_for_code(self.city)
            self.iata_code = self.search_code["locations"][0]["code"]
            self.iata_list.append(self.iata_code)

        for n in range (len(self.iata_list)):
            if self.google_sheet.read()["prices"][n]["iataCode"] == "":
                self.google_sheet.update(n+2,self.iata_list[n])

    
    def search_for_flight(self,city,origin_city_iata):

        self.flight_url = "https://tequila-api.kiwi.com/v2/search"
        try:
            self.stepover=0
            self.para = {
                "fly_from": origin_city_iata,
                "fly_to": city,
                "date_from":self.today_formatted,
                "date_to":self.future_formatted,
                "limit":1,
                "curr":"CAD",
                "nights_in_dst_from":5,
                "nights_in_dst_to":20,
                "flight_type":"round",
                "max_stopovers":self.stepover
                
            }
            response = requests.get(url=self.flight_url,params=self.para,headers = self.headers)
            response.raise_for_status()
            return response.json()["data"][0]

        except IndexError:
            # stepover 2 = doing 1 connecting flight
            self.stepover=2
            self.para = {
                "fly_from": origin_city_iata,
                "fly_to": city,
                "date_from":self.today_formatted,
                "date_to":self.future_formatted,
                "limit":1,
                "curr":"CAD",
                "nights_in_dst_from":5,
                "nights_in_dst_to":20,
                "flight_type":"round",
                "max_stopovers":self.stepover
                
            }
            try:
                response = requests.get(url=self.flight_url,params=self.para,headers = self.headers)
                response.raise_for_status()
                return response.json()["data"][0]

            except :
                print(f"No flight can be found for {city}")
                return None
        




