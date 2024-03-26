FROM python:3.12.2
WORKDIR /usr/src/app
EXPOSE 8000
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "manage.py", "0.0.0.0:8000"]
