import requests
from fake_useragent import UserAgent

temp_user_agent = UserAgent()
browser_header = {'User-Agent': temp_user_agent.random}

def find_vaccines(pincode, date):
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode="+pincode+"&date="+date
    r = requests.get(url = URL, headers=browser_header)
    if r.status_code==200:
        response = r.json()['centers']
        for each in response:
            for session in each['sessions']:
                if session['min_age_limit']==18 and session['available_capacity_dose1']:
                    return [each['name'],session['date'], pincode]
    return None
