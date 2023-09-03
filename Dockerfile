FROM python:3.9-alpine

WORKDIR /VoucherMs

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

COPY entrypoint.sh entrypoint.sh

ENTRYPOINT [ "sh", "entrypoint.sh" ]

# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]

