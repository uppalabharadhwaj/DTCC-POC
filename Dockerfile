FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install flask aws-xray-sdk

EXPOSE 5000

CMD ["python", "main.py"]
