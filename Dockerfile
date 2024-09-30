# official base image
FROM python:3.10-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_MAIL_PASSW 'etrg ciqn wtfq ccqj'

# set work directory
WORKDIR /src

# copy project files
COPY . .

# install dependencies
RUN pip install -r requirements.txt
RUN pip install gunicorn

# exposing container port
EXPOSE 5000:5000

# run entrypoint
ENTRYPOINT ["./start.sh"]
