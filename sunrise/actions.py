import re
import abc
import requests
import json


class Action(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def execute(self):
        pass


class Calculator(Action):
    operators = ['+', '-', '*']

    def __init__(self, operator, a, b):
        self.operator = {
            'Add': '+',
            'Sub': '-',
            'subtract': '-',
            'Div': '//',
            '/': '//',
        }[operator] if operator not in self.operators else operator
        self.numbers = [a, b]

    def execute(self):
        return str(eval(self.operator.join(self.numbers)))


class Weather(Action):
    parameters = ['temp', 'humidity', 'pressure']

    def __init__(self, parameter, city):
        self.parameter = {
            'temperture': 'temp',
        }[parameter] if parameter not in self.parameters else parameter
        self.city = city

    def execute(self):
        # Enter your API key here
        api_key = "fa313a7fbbcd1bc409691eed433355a9"
        # base_url variable to store url
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = self.city
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        # get method of requests module
        # return response object
        weather_request = requests.get(complete_url)
        weather_response = weather_request.json()
        # Now weather_response contains list of nested dictionaries
        # Check the value of "cod" key is equal to
        # "404", means city is found otherwise,
        # city is not found
        if weather_response["cod"] != "404":
            main_data = weather_response["main"]
            return main_data[self.parameter]
        else:
            return 'city not found'


patterns = [
    (
        re.compile(r'(?P<a>\d+)\s*(?P<operator>[-+/*])\s*(?P<b>\d+)'),
        Calculator
    ),
    (
        re.compile(
            r'(?P<operator>Add)\s*(?P<a>\d+)\s*(with|by)\s*(?P<b>\d+)'
        ),
        Calculator
    ),
    (
        re.compile(
            r'(?P<operator>Sub|subtract)\s*(?P<b>\d+)\s*(from)\s*(?P<a>\d+)'
        ),
        Calculator
    ),
    (
        re.compile(
            r'(?P<operator>Div)\s*(?P<b>\d+)\s*(into)\s*(?P<a>\d+)'
        ),
        Calculator
    ),
    (
        re.compile(
            r'(?P<operator>Div)\s*(?P<a>\d+)\s*(by)\s*(?P<b>\d+)'
        ),
        Calculator
    ),
    (
        re.compile(
            r'.*(?P<parameter>temp|humidity|pressure).*(?P<city>tehran).*'
        ),
        Weather
    ),
]


class ParseError(Exception):
    def __init__(self, command):
        super().__init__(f'Cannot parse: {command}')


def find(command):
    for pattern, action in patterns:
        match = pattern.match(command)
        if match:
            return action, match.groupdict()

    raise ParseError(command)

