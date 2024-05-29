FROM python

RUN pip3 install flask

COPY app.py /app.py

RUN chomd +x app.py

ENTRYPOINT python /app.py
