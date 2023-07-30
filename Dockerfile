# 1. Python 3.8 버전의 이미지 사용
FROM python:3.8

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 필요한 파일 복사
COPY main.py /app/
COPY requirements.txt /app/
COPY templates /app/templates/
COPY routers /app/routers/
COPY models /app/models/
COPY database /app/database/

# 4. 의존성 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 5. FastAPI 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8888", "--reload"]
