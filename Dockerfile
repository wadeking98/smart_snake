FROM python:3.8
COPY . /
RUN pip3 install -r requirements.txt
WORKDIR /snake/app
CMD ["python3", "main.py"]

