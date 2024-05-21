FROM python

WORKDIR /src

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000/tcp

# Run the application with Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]