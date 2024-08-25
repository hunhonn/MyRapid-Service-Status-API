from fastapi import FastAPI, Request
import os
import requests
from datetime import datetime
from bs4 import BeautifulSoup

app=FastAPI()

def fetch_data():
    url = "https://myrapid.com.my/service-status/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    def extract_name_and_service(row):
        elements = row.select('td')
        if len(elements) > 2:
            name = elements[0].text.strip()
            service = elements[2].text.strip()
            remarks = elements[3].text.strip()
            long_name = elements[5].text.strip()
            return {"LineID": long_name, "Line": name, "Status": service, "Remarks": remarks}
        return None

    filtered_rows = [row for row in soup.select('tbody tr') if row.has_attr('data-row_id')]
    lines_services_list = [extract_name_and_service(row) for row in filtered_rows if extract_name_and_service(row)]

    return lines_services_list

@app.get("/")
def get_service_status():
    # Fetch data and format timestamp
    lines_services_list = fetch_data()
    current_datetime = datetime.now()
    formatted_timestamp = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    data= {"Timestamp": formatted_timestamp, "Data": lines_services_list}
    return data