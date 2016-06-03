FROM debian:latest
MAINTAINER Koen Dercksen <mail@koendercksen.com>

USER root

# Install everything needed to do Python CI
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    python \
    python-dev \
    python-pip \
    python3 \
    python3-dev \
    python3-pip \
    virtualenvwrapper

# Set up environment
ENV UNAME pyci
ENV SHELL /bin/bash
ENV EDITOR vim
ENV HOME /home/$UNAME
ENV WORKON_HOME $HOME/venvs

# Set up user and server
RUN useradd -m -s /bin/bash -N $UNAME
COPY . /pyci
WORKDIR /pyci
RUN python3 setup.py install
EXPOSE 9999
WORKDIR /home/$UNAME
RUN rm -r /pyci

# Configure startup
WORKDIR /home/$UNAME
USER $UNAME

ENTRYPOINT ["python3", "-m", "pyci.server"]
