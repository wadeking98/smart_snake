FROM python:3.6
COPY . /
RUN pip3 install -r requirements.txt
WORKDIR /snake/app
CMD ["python3", "main.py"]

