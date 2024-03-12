from dataclasses import dataclass


api_keys = [
    'GCDgQbkqEm732Dm6u7Ga2bD75VG3er',
]


@dataclass
class Credentials:
    username: str
    password: str


user_credentials = [
    Credentials('admin', 'admin'),
]