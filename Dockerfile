FROM python:3.8-slim-buster
RUN mkdir -p /app/source
COPY ./source/* /app/source/
WORKDIR /app/source
CMD ["python3", "./lab1.py"]