FROM ciscotestautomation/pyats

RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install --upgrade pip 

COPY requirements.txt /pyats/requirements.txt
WORKDIR /pyats

RUN pip install pyats

RUN pip install netmiko

RUN pip install -r requirements.txt

COPY . /pyats

CMD ["python", "-u", "/pyats/main.py"]