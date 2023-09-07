import os
from googleapiclient.discovery import build


class Video:
    """Класс для видео с Youtube"""
    # API_KEY_YOUTUBE скопирован из гугла и вставлен в переменные окружения
    api_key: str = os.getenv('API_KEY_YOUTUBE')

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return build('youtube', 'v3', developerKey=cls.api_key)

    def __init__(self, video_id: str):
        """Экземпляр инициализируется по id видео. Дальше все данные будут подтягиваться по API."""
        self.__video_id = video_id

        self.video_response = (
            self.get_service().videos().list(id=self.__video_id, part='snippet,statistics').execute())
        self.video_title: str = self.video_response['items'][0]['snippet']['title']
        self.url: str = f"https://youtu.be/{self.__video_id}"
        self.view_count: int = self.video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = self.video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        """Представление класса для пользователя"""
        return self.video_title


class PLVideo(Video):
    """Класс плейлист YOUTUBE"""

    def __init__(self, video_id: str, playlist_id: str):
        """Инициализация из родительского класса и дополнительного атрибута playlist_id"""
        super().__init__(video_id)
        self.playlist_id = playlist_id