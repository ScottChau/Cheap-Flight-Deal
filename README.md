# Cheap-Flight-Deal


API

Google Sheet Data Management - https://sheety.co/

Kiwi Partners Flight Search API (Free Signup, Requires Credit Card Details) - https://partners.kiwi.com/

Tequila Flight Search API Documentation - https://tequila.kiwi.com/portal/docs/tequila_api

Twilio SMS API - https://www.twilio.com/docs/sms




Program Requirements

Use the Flight data and Sheety API to populate your own copy of the Google Sheet with International Air Transport Association (IATA) codes for each city. Most of the cities in the sheet include multiple airports, you want the city code (not the airport code see here).

Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.

If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number with the Twilio API.

The SMS includes the departure airport IATA code, destination airport IATA code, departure city, destination city, flight price and flight dates. e.g.




Aims

The project aims to look for cheap flight deals in the market, customer can register on https://replit.com/@ScottChau/Cheapest-Flight-Deal , information will be log onto google sheet https://docs.google.com/spreadsheets/d/1W9pAWHxKG7NN7l-A_17P91-OllHmk7OJVHraNwpwzKA/edit#gid=606545007 , cheap flight deal will be sent to the email on google sheet accordingly when running the program.

Please be reminded filling all of the corresponding API key/token before running the program

