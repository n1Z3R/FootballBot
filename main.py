import requests
from bs4 import BeautifulSoup as bs

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.277"
}

matches_list = []


def TodayMatches():
    url = "https://www.betexplorer.com/next/soccer/"
    r = requests.get(url, headers=headers).text
    soup = bs(r, "lxml")
    matches = soup.find_all("tr", {"data-def": "1"})
    print(matches)
    for tr in matches:
        s = bs(str(tr), "lxml")
        match = s.find("a").find_all("span")[0].text + " - " + s.find("a").find_all("span")[1].text
        try:
            match_score = s.find(class_="table-main__result").find("a").find("strong").text
        except Exception:
            try:
                match_score = s.find(class_="livebet").get("data-live-cell")
                if match_score == "livebet":
                    match_score = "LIVE"
                else:
                    match_score = ""
            except Exception:
                match_score = "Пусто"
        time = tr.get("data-dt")
        time = time.split(",")[-2] + ":" + time.split(",")[-1]
        date = tr.get("data-dt")
        date = date.split(",")[0] + "." + date.split(",")[1] + "." + date.split(",")[2]
        try:
            href = "https://www.betexplorer.com" + s.find(class_="table-main__result").find("a").get("href")
        except Exception:
            href = "https://www.betexplorer.com" + s.find(class_="table-main__tt").find("a").get("href")
        matches_list.append(
            {
                'Match': match,
                'Date': date,
                'Time': time,
                'Score': match_score,
                'Url': href
            })


if __name__ == '__main__':
    TodayMatches()
