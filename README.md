# Shoffee Cup ☕

Shoffee Cup is a user-friendly web platform that helps coffee lovers, students, and remote workers discover the best nearby cafés. Users can find the nearest cafés by clicking a button, browse by city/district/neighborhood, and find their desired café location on map.  

This project is built using **Python (Flask)**, **Bootstrap 5**, and integrates the **Geoapify Places API** for finding cafés.

---

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Technologies](#technologies)
- [API Integration](#api-integration)

---

## Features

- Find nearest cafés based on user location  
- Browse cafés by city, district, and neighborhood  
- View café details and location on Google Maps  
- Rate and review cafés (future feature)  
- Clean, responsive UI with Bootstrap 5  
- Mobile-friendly design  

---

## Demo

### Home Page
![Home Page](assets/home_page.png)

### Search Page
![Search Page](assets/search_page.png)

### Search-result Page
![Search-result Page](assets/sr_page.png)

---

## Technologies

- Python 3.x  
- Flask  
- Flask-Bootstrap5  
- HTML, CSS, JS  
- Geoapify APIs

---

## API Integration

- Shoffee Cup uses the Geoapify Places API to fetch café data.
- The API is called with parameters such as user location, category (catering.cafe), and optional filters (name, city, street).
- API key is stored in the .env file and loaded using python-dotenv.
