import os

from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable


class muscic_file():
    def __init__(self, url:str) -> None:
        try: 
            self.__yt:YouTube = YouTube(url=url)
        except RegexMatchError:
            raise ValueError(f"URL이 유효하지 않습니다: {url}")
        except Exception as e:
            raise RuntimeError(f"예상치 못한 오류가 발생했습니다: {e}")
        
    def get_information(self):
        """
            해당 비디오의 정보를 가져옴
        """
        res:dict[str, str] = {
            'title' : self.__yt.title,
            'author' : self.__yt.author,
            'views' : self.__yt.views,
            'thumbnail_url' : self.__yt.thumbnail_url
        }
        return res
    
    def downlond(self):
        """
            비디오 고품질 다운로드
            1: 비디오를 다운 받지 못함
            2: 예상치 못한 문제 발생
        """
        try:
            video_stream = self.__yt.streams.filter(only_audio=True).first()

            ## 파일 관리 클래스
            path:str
            video_path:str = video_stream.download(filename=self.__yt.title, output_path=path) 
            return video_path

        except VideoUnavailable:
            return '1'
        except Exception as e:
            return '2'


# class file_manger():
#     def __init__(self) -> None:
        