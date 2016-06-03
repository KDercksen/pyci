pyci
====

pyci is a really, really minimal continuous integration server written in
Python, for Python. Post a JSON request to pyci as a post-receive Git hook and
receive a build status indication.

---

### Usage

    $ docker run -d -p 9999:9999 kdercksen/pyci

The service now listens on localhost:9999/TCP.

#### Building instructions

    $ git clone git@github.com:KDercksen/pyci

    $ cd pyci

    $ make docker    
