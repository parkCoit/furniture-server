FROM python:3.12.4
WORKDIR /app
RUN apt-get update
RUN apt-get install -y default-jdk
ADD requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -U pip wheel cmake
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install cryptography
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

