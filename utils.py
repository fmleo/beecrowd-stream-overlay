import aiohttp

from typing import List, Dict

from bs4 import BeautifulSoup

BASE_URL = "https://www.beecrowd.com.br"


async def get_user_data_in_rank(institution: str, page: int = None) -> List[Dict]:
    endpoint = f"/judge/pt/users/university/{institution}"
    params = {"page": page, "direction": "DESC"} if page else {}
    headers = {"User-Agent": "Mozilla/5.0"}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(BASE_URL + endpoint, params=params) as resp:
            soup = BeautifulSoup((await resp.text()), 'html.parser')
            table = soup.find("table")

            data = []

            for row in table.find_all("tr")[1:]:
                data_tuple = [i.get_text().strip("\n").strip() for i in row.find_all("td")]
                user_data = {"position": data_tuple[0], "username": data_tuple[2],
                             "solved_count": parse(data_tuple[3]), "attempted_count": parse(data_tuple[4]),
                             "submissions_count": parse(data_tuple[5]),
                             "score": parse(data_tuple[6])}
                data.append(user_data)

            return data


def parse(number: str) -> float:
    return float(number.replace(".", "").replace(",", "."))
