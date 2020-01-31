## Yetda DataHandler
- Language: python

옛다 서비스의 Firebase Cloud Firestore에 csv 데이터를 파싱하는 데이터 핸들러입니다.

## Installation
```shell
pip install --upgrade firebase-admin
```

## Configurations
먼저, config/ 디렉토리 내에 firebase에서 제공하는 admin sdk 비공개 키 json 파일을 위치시켜야 합니다.

다음으로, **handler.py**를 열고,

```python
cred = credentials.Certificate(
    './config/yetda-d4506-firebase-adminsdk-ai9kq-97df4de6f8.json')
firebase_admin.initialize_app(cred)
```

이 부분에서 "./config/yetda-d4506-firebase-adminsdk-ai9kq-97df4de6f8.json" 부분을 다운로드 한 json 파일 명으로 적절히 수정합니다.


## Run
```shell
python handler.py
```