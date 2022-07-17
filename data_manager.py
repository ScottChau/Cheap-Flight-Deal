import requests


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None: 
        self.SHEET_URL = "YOUR_GOOGLE_SHEET_FOR_FLIGHT_DATA"
        self.USER_URL = "YOUR_GOOGLE_SHEET_FOR_USER_DATA"
        
    def read(self):
        self.response = requests.get(url =self.SHEET_URL )
        self.response.raise_for_status()
        return self.response.json()
    
    def read_user(self):
        self.response = requests.get(url =self.USER_URL )
        self.response.raise_for_status()
        return self.response.json()

    
    def post(self,city,IATACode,lowestPrice):
        self.para = {"price":{
            "city": city,
            "iataCode": IATACode,
            "lowestPrice": lowestPrice
            }
            }
        self.response = requests.post(url = self.SHEET_URL, json = self.para)
        self.response.raise_for_status()
    
    def update(self,row_number,update_code):
        self.revised_row = f"{self.SHEET_URL}/{row_number}"
        self.para = { "price":{
            "iataCode":update_code
        }
        }
        self.response = requests.put(url=self.revised_row, json=self.para)
        self.response.raise_for_status()
        

    

        

    


    
    