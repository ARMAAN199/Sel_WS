

from typing import Dict, List, Union
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def with_tag_name(tag_name: str) -> "RelativeBy":
    if not tag_name:
        raise WebDriverException("xnbvxvdd some shit error")
    return RelativeBy({"css selector": tag_name})


def locate_with(by: By, using: str) -> "RelativeBy":
    assert by is not None, "err"
    assert using is not None, "err"
    return RelativeBy({by: using})


class RelativeBy(object):

    def __init__(self, root: Dict[By, str] = None, filters: List = None):
        self.root = root
        self.filters = filters or []

    def above(self, element_or_locator: Union[WebElement, Dict] = None) -> "RelativeBy":
        if not element_or_locator:
            raise WebDriverException("pliz Give lctr")

        self.filters.append({"kind": "above", "args": [element_or_locator]})
        return self

    def below(self, element_or_locator: Union[WebElement, Dict] = None) -> "RelativeBy":
        if not element_or_locator:
            raise WebDriverException("pliz Give lctr")

        self.filters.append({"kind": "below", "args": [element_or_locator]})
        return self

    def to_left_of(self, element_or_locator: Union[WebElement, Dict] = None) -> "RelativeBy":
        if not element_or_locator:
            raise WebDriverException("pliz Give lctr")

        self.filters.append({"kind": "left", "args": [element_or_locator]})
        return self

    def to_right_of(self, element_or_locator: Union[WebElement, Dict] = None) -> "RelativeBy":
        if not element_or_locator:
            raise WebDriverException("pliz Give lctr")

        self.filters.append({"kind": "right", "args": [element_or_locator]})
        return self

    def near(self, element_or_locator_distance: Union[WebElement, Dict, int] = None) -> "RelativeBy":
        if not element_or_locator_distance:
            raise WebDriverException("pliz Give lctr")

        self.filters.append({"kind": "near", "args": [element_or_locator_distance]})
        return self

    def to_dict(self) -> Dict:
        return {
            'relative': {
                'root': self.root,
                'filters': self.filters,
            }
        }
