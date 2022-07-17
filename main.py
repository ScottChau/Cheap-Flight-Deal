#This file will need to use the DataManager, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager


google_sheet = DataManager()

flight_data = FlightData()

message = NotificationManager()

price_data = google_sheet.read()

user_data = google_sheet.read_user()



# flight_data.fill_iata_code()


ORIGINAL_CITY_IATA = "YTO"
    

for i in price_data["prices"]:

    iata_code = i["iataCode"]
    
    price = i["lowestPrice"]
    
    data = flight_data.search_for_flight(iata_code, ORIGINAL_CITY_IATA)


    try:
        current_price = data["price"]
        from_iata = data["cityCodeFrom"]
        to_iata = data["cityCodeTo"]
        from_city = data["cityFrom"]
        to_city = data["cityTo"]
        depart_date = data["local_departure"]
        return_date = data["route"][-1]["local_arrival"]
    # date modifying
        trim_depart = depart_date.replace("T"," ").replace("Z","")
        trim_return = return_date.replace("T"," ").replace("Z","")
        depart_date_formatted = trim_depart[:-13]
        return_date_formatted = trim_return[:-13]
        print(f"From {from_city} to {to_city}: ${current_price}")

    except :
        continue

    if current_price < price and flight_data.stepover == 0:
        # message
        message.sent_message(from_iata = from_iata, to_iata = to_iata, from_city = from_city ,to_city = to_city , price = current_price ,depart_date = depart_date_formatted ,return_date = return_date_formatted)
        # sent email
        for n in user_data["users"]:
            email = n["email"]
            message.sent_email(email=email,from_city=from_city,from_iata=from_iata,to_city=to_city,to_iata=to_iata,price=current_price,depart_date=depart_date_formatted,return_date=return_date_formatted)

    elif current_price < price and flight_data.stepover > 0:
        # message
        via_city = data["route"][-3]["cityFrom"]
        message.sent_message_stepover(from_iata = from_iata, to_iata = to_iata, from_city = from_city ,to_city = to_city , price = current_price ,depart_date = depart_date_formatted ,return_date = return_date_formatted, via_city=via_city)
        # sent email
        for n in user_data["users"]:
            email = n["email"]
            message.sent_email(email=email,from_city=from_city,from_iata=from_iata,to_city=to_city,to_iata=to_iata,price=current_price,depart_date=depart_date_formatted,return_date=return_date_formatted)

        




