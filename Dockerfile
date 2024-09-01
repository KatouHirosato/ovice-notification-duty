FROM python

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
RUN ls

WORKDIR /app/app
RUN ls

# CMD ["python", "-m", "app"]
CMD ["python", "download.py"]
