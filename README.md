# IPL Manager Web Application
This web application allows cricket fanatics to put themselves in the shoes of team owners in the Indian Premier League. Users can make hypothetical player trades with other teams, build squads from scratch through the IPL Auction Simulator, and make starting 11s with their original/new squads. 

The project was developing using the Django framework. The backend of this project was built entirely using Python and its libraries, while the front-end was built using HTML and CSS. To learn more about the machine learning model implemented in the code, view this <a href="https://github.com/sid0402/IPL-Price-Predictor">repository.</a>

# Project Structure
## Django Apps
- Homepage  --> /home
- Trade machine --> /machine
- Playing 11 --> /playingeleven
- Auction --> /auction
- Forum --> /forum

The backend for each of these parts of the app are can be found in each subfolders' views.py file. 

## Frontend
Each of the templates used to build the web app are in /templates. This folder is further segregated into folders containing templates for specific apps.
## Model and Scrapers
- Model to predict auction prices --> /ml
- Scripts to scrape data for /ml and player images --> /scrapers

# Functionality
## Home Page
<img width="1499" alt="Screen Shot 2023-07-26 at 6 37 48 PM" src="https://github.com/sid0402/IPL-Manager/assets/36813259/892c9574-2849-4607-a240-a6c47e3a7112">

## Trades
https://github.com/sid0402/IPL-Manager/assets/36813259/e192586b-157a-4033-8181-f42b74e24d1b

## Auction Simulation

https://github.com/sid0402/IPL-Manager/assets/36813259/e14adceb-4e17-440f-80be-fcecf86a1dd0

https://github.com/sid0402/IPL-Manager/assets/36813259/7af35dbd-df83-432e-aa1f-150240a061e5

## Playing 11 Builder
https://github.com/sid0402/IPL-Manager/assets/36813259/41d9938d-0c62-4486-82e2-fd301a8da809

# To Do
- Improve and deploy the forum section fully, integrated with the user login system
- Deploy Machine Learning model to predict the prices of players in the auction
- Create a User Login system
