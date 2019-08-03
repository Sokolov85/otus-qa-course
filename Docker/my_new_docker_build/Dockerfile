#Base image
FROM python:3

#Copy test project files to the image folder
RUN git clone --progress --verbose https://github.com/Sokolov85/otus-qa-course.git ./app

#Make the folder as a working directory
WORKDIR /app

#Install the test project libraries
RUN pip install -r requirements.txt

# Set up Chromedriver Environment variables
ENV CHROMEDRIVER_VERSION 2.19
ENV CHROMEDRIVER_DIR /app

#Install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /app

# Install Chrome
RUN curl https://dl-ssl.google.com/linux/linux_signing_key.pub -o /tmp/google.pub \
    && cat /tmp/google.pub | apt-key add -; rm /tmp/google.pub \
    && echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' > /etc/apt/sources.list.d/google.list \
    && mkdir -p /usr/share/desktop-directories \
    && apt-get -y update && apt-get install -y google-chrome-stable
	
# Put Chromedriver into the PATH
ENV PATH $CHROMEDRIVER_DIR:$PATH