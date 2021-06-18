# gamsung cafe
### 감성 cafe를 볼 수 있는 웹 서비스

## 로컬 셋업 방법

### 데이터베이스

* MongoDB 4.0+ 버전

### .env

```text
# JWT 비밀값
JWT_SECRET="{비밀값}"
# MongoDB 연결
MONGODB_HOST="{MongoDB 호스트 e.g. MONGODB_HOST="mongodb://test:test@localhost:27017"
```

### 파이썬 가상 환경

* python 가상 환경(3.8 버전+)

* 외부 패키지 설치

#### poetry

```shell
$ poetry install
```

#### pip

```shell
$ pip install -r requirements.txt
```

## 로컬 실행

```shell
$ flask run --host 0.0.0.0 --port 7000
```