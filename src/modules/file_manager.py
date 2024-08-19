import os

class DirBuilder():
    """
        파일구조: 최상위 폴더 -> 아티스트 폴더 -> 음원 폴더
    """
    def __init__(self, path:str) -> None:
        self.MAIN_PATH = path
    
    def mkdir_artist(self, dir_name:str) -> str:
        if dir_name in os.listdir(self.MAIN_PATH): 
            raise FileExistsError(f"File Already {dir_name}")
        
        path:str = os.path.join(self.MAIN_PATH, dir_name)
        
        os.mkdir(path=path)
        return path
    
    def mkdir_music(self, path:str, name:str) -> str:
        if not os.path.isdir(path):
            raise FileNotFoundError(f"Not Found Path:{path}")
        
        music_dir_path:str = os.path.join(path, name)

        if music_dir_path in os.listdir(path=path):
            raise FileExistsError(f"File Already {music_dir_path}")
        
        os.mkdir(path=music_dir_path)

        return music_dir_path