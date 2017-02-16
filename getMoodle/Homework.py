import requests
from bs4 import BeautifulSoup
from private import get_moodlecred


moodleUrlRoot = ("https://moodle.monlau.com:8443/")
moodleUrlLogin = (moodleUrlRoot + "login/index.php")
moodleUrlCalendar = (moodleUrlRoot + "calendar/view.php")

def login():
    payload = get_moodlecred()
    with requests.Session() as s:
        r = s.post(moodleUrlLogin, data=payload)
        st = r.status_code
        if st == 200:
            return s


def homework():
    home = ""
    s = login()
    r = s.get(moodleUrlCalendar)
    # print(r.status_code)
    soup = BeautifulSoup(r.text, "html.parser")
    soup = soup.find("div", {"class": "eventlist"})
    for event in soup.find_all_next("div", {"class": "event"}):
        for ele in event.childGenerator():
            if ele.text:
                home += (ele.text+"\n")
            # print(ele.text)
        home += "\n"
    # print(home)
    return home


def main():
    homework()

if __name__ == '__main__':
    main()
