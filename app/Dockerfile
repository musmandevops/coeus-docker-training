FROM python:3.11-slim

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
# COPY SOURCE DESTINATION
COPY requirements.txt .

# install dependencies
RUN apt-get update && apt-get install -y vim


RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . .

EXPOSE 8080

# command to run on container start
CMD [ "python", "./app.py" ]



