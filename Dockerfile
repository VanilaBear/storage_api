FROM python:3.6-alpine

WORKDIR /app

COPY . .

RUN apk update && \
    apk add py-pip python3-dev

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]