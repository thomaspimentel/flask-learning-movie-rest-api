FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY ./ /code/
CMD python -m smtpd -n -c DebuggingServer localhost:1025
ENTRYPOINT ["python","api/run.py"]