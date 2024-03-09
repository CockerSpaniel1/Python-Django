#使用其他套件
from pathlib import Path,os

print("目前的工作目錄：", os.getcwd())

print("絶對路徑：", os.path.abspath('.')) # 目前的位置
print("絶對路徑：", os.path.abspath('..')) #上一層的位置
print("絶對路徑：", os.path.abspath('py04.py')) #完整位置(路徑)

print("檔案大小：",os.path.getsize('py04.py'),"bytes")

#__file__.變數,用於導入目前模組的路徑
print(Path(__file__))   #導入目前模組的路徑
print(Path('.').resolve()) #路徑轉換為絕對路徑
print(Path(__file__).resolve())  
print(Path(__file__).resolve().parent)   #上一層
print(Path(__file__).resolve().parent.parent)   #上上層

# ----------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent #C:\django
mydir = os.path.join(BASE_DIR, "temp") #C:\django\temp
yourdir = os.path.join(BASE_DIR, "temp").replace("\\", "/")

print(mydir)
print(yourdir)