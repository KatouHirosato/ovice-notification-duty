FROM python

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
RUN ls -a

CMD ["python", "-m", "app"]