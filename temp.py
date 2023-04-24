import random
from typing import Dict

Alist = [{"country": "Australia", "capital": "Canberra"} ,{"country": "UK", "capital": "London"}] #list goes on


randomCountry: dict[str, str] | dict[str, str] = random.choice(Alist, ['country'])