import requests

from dataclasses import dataclass
from typing import Any

from api.pkg.parsers.parser import Parser


class ParserComponents(Parser):
    urls = [
        ("https://www.newegg.com/p/pl?N=100006676", "CPU"),
        ("https://www.newegg.com/p/pl?N=100006650", "MEMORY"),
        ("https://www.newegg.com/p/pl?N=100006654", "MOTHER_BOARD"),
        ("https://www.newegg.com/p/pl?N=100006662", "GPU"),
        ("https://www.newegg.com/p/pl?N=100006656", "POWER SUPPLIES"),
        ("https://www.newegg.com/p/pl?N=100006644", "CASES"),
        ("https://www.newegg.com/p/pl?N=100006648", "COOLING"),
        ("https://www.newegg.com/p/pl?N=100011692", "SSD"),
        ("https://www.newegg.com/p/pl?N=100006670", "HDD"),
    ]

    async def parse(self) -> Any:
        for url, name in self.urls:
            parser = ParserComponent(url, name)
            await parser.parse()


@dataclass
class ParserComponent(Parser):
    url: str
    name: str

    async def parse(self) -> Any:
        response = requests.get(self.url)
