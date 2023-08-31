import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    # API_KEY_YOUTUBE скопирован из гугла и вставлен в переменные окружения
    api_key: str = os.getenv('API_KEY_YOUTUBE')

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return build('youtube', 'v3', developerKey=cls.api_key)

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
        """Отображает информацию класса для пользователя."""
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        """Сложение классов"""
        return self.view_count + other.view_count

    def __sub__(self, other):
        """Вычитание классов"""
        return self.view_count - other.view_count

    def __gt__(self, other):
        """Сравнение классов"""
        return self.view_count > other.view_count

    def __ge__(self, other):
        """Сравнение классов"""
        return self.view_count >= other.view_count

    def __lt__(self, other):
        """Сравнение классов"""
        return self.view_count < other.view_count

    def __le__(self, other):
        """Сравнение классов"""
        return self.view_count <= other.view_count

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
