> 빡빡한 공기업의 사내 보안으로 화면 보호기를 비활성화 할 수 없어 만드는 프로그램 \\
출처 - https://csnhjt.tistory.com/77 
평소에도 항상 켜놓으면서 작업할 수 있도록 키보드 입력을 삭제하려 했으나, 마우스 움직임으로는 화면보호기가 켜져버려서 마우스 움직임을 빼고 키보드 입력만 넣어서 스크립트 수정

### 가상환경 생성 및 활성화
```bash
$ python -m venv [가상환경이름]
$ source [가상환경이름]/Scripts/activate

(가상환경이름)
$
```

**터미널 별 활성화 방법** 

- Git Bash
  
    ```bash
    $ source [가상환경이름]\Scripts\activate
    ```
    
- CMD
  
    ```bash
    $ source [가상환경이름]\Scripts\activate.bat
    ```
    
- PowerShell
  
    ```bash
    $ source [가상환경이름]\Scripts\Activate.ps1
    ```
    
- macOS
  
    ```bash
    $ source [가상환경이름]/bin/activate
    ```
    

**비활성화**

```bash
$ deactivate
```

**pip 를 통해 현재 가상환경인지 확인**

### pyautogui 활용시 버그가 있어서 
> https://github.com/asweigart/pyautogui/issues/598
> 위 github 페이지 참고하여 pyautogui/pyautogui/__init__.py 여기의 

`locateOnWindow.__doc__ = pyscreeze.locateOnWindow.__doc__`
이 코드를 
`locateOnWindow.__doc__ = pyscreeze.locateOnScreen.__doc__` 이 코드로 변경하면 실행됨.

### PyInstaller 
> 설치 방법

```bash
# 설치
pip install pyinstaller

# 최신 버전으로 업그레이드 (첫 설치 시에는 필요없음)
pip install --upgrade pyinstaller

# 설치되어 있는지 확인
pyinstaller --version
```
> 사용 방법
```bash
# 가장 기본적인 사용법
pyinstaller 파이썬 파일명.py

# 한 파일로 만들기
pyinstaller -F --onefile 파이썬 파일명.py

# 아이콘 변경하기
pyinstaller -F --onefile --icon=./sleep_mode_prolonged_19365.ico 파이썬 파일명.py
```
