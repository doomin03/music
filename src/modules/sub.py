import os

from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable

from file_manager import DirBuilder


class muscic_file():
    def __init__(self, url:str) -> None:
        try: 
            self.__yt:YouTube = YouTube(url=url)
        except RegexMatchError:
            raise ValueError(f"URL이 유효하지 않습니다: {url}")
        except Exception as e:
            raise RuntimeError(f"예상치 못한 오류가 발생했습니다: {e}")
        
        self.videoinfo:dict[str, str] = {
            'title' : self.__yt.title,
            'author' : self.__yt.author,
            'views' : self.__yt.views,
            'thumbnail_url' : self.__yt.thumbnail_url
        }
        self.audio_stream = self.__yt.streams.filter(only_audio=True).first()
        self.download_path = None

    def setting(self, artist_name: str, path: str):
        creater = DirBuilder(path=path)
        dir_artist_path = creater.mkdir_artist(dir_name=artist_name)
        self.download_path = creater.mkdir_music(dir_artist_path, self.videoinfo['title'])

        return self

    def download(self) -> str:
        """
        비디오 고품질 다운로드
        1: 비디오를 다운 받지 못함
        2: 예상치 못한 문제 발생
        3: 설정이 필요함
        """
        if not self.download_path:
            return '3'  
        
        try:
            video_path: str = self.audio_stream.download(filename=self.__yt.title, output_path=self.download_path)
            return video_path

        except VideoUnavailable:
            return '1'
        except Exception as e:
            return '2'




