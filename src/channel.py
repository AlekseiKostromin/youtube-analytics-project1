import json
from src.baseclass import MixinBase


class Channel(MixinBase):
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id

        self.channel_response = (
            self.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute())

        self.title: str = self.channel_response['items'][0]['snippet']['title']
        self.channel_description: str = self.channel_response['items'][0]['snippet']['description']
        self.url: str = f"https://www.youtube.com/channel/{self.__channel_id}"
        self.subscriber_count: int = int(self.channel_response['items'][0]['statistics']['subscriberCount'])
        self.video_count: int = int(self.channel_response['items'][0]['statistics']['videoCount'])
        self.view_count: int = int(self.channel_response['items'][0]['statistics']['viewCount'])

    def __str__(self):
        """отображение информации об объекте класса для пользователей"""
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        """сложение классов"""
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        """вычитание классов"""
        return self.subscriber_count - other.subscriber_count

    def __gt__(self, other):
        """Сравнение классов 'больше'"""
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        """Сравнение классов 'больше или равно'"""
        return self.subscriber_count >= other.subscriber_count

    def __lt__(self, other):
        """Сравнение классов 'меньше'"""
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        """Сравнение классов 'меньше или равно'"""
        return self.subscriber_count <= other.subscriber_count

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel_response, indent=2, ensure_ascii=False))

    @property
    def channel_id(self):
        """В main.py обращаются для теста"""
        return self.__channel_id

    def to_json(self, filename):
        """Сохраняет в файл значения атрибутов"""
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.channel_response, file, ensure_ascii=False)
