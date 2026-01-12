FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt --no-cache-dir

COPY . /app 

EXPOSE 8000

CMD ["sh", "-c", "python3 manage.py collectstatic --noinput && python3 manage.py runserver 0.0.0.0:8000"]

# ENTRYPOINT ["python3"] 
# CMD ["manage.py", "collectstatic"]

# ENTRYPOINT ["python3"] 
# CMD ["manage.py", "runserver", "0.0.0.0:8000"]

# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "mon_projet.wsgi:application"]
