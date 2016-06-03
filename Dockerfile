FROM alpine:latest
MAINTAINER Koen Dercksen <mail@koendercksen.com>

USER root

# Install everything needed to do Python CI
RUN apk add --update --no-cache \
    bash \
    build-base \
    git \
    python \
    python-dev \
    python3 \
    python3-dev

# Set up environment
ENV UNAME pyci
ENV SHELL /bin/bash
ENV EDITOR vim
ENV HOME /home/$UNAME
ENV WORKON_HOME $HOME/venvs

# Set up user
RUN adduser -D -h $HOME -s $SHELL $UNAME

# Set up pyci
WORKDIR $HOME/pyci
COPY . pyci
WORKDIR pyci
RUN pip3 install -r requirements.txt && python3 setup.py install
WORKDIR $HOME
RUN rm -r pyci

# Set up virtualenvwrapper
RUN git clone https://bitbucket.org/virtualenvwrapper/virtualenvwrapper.git
WORKDIR virtualenvwrapper
RUN pip3 install -r requirements.txt && python3 setup.py install
WORKDIR $HOME
RUN rm -r virtualenvwrapper

# Configure startup
USER $UNAME

EXPOSE 9999
ENTRYPOINT ["python3", "-m", "pyci.server"]
