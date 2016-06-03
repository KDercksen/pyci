TARGET=pyci

dev:
	python setup.py develop

docker:
	docker build -t $(TARGET) .

test:
	nosetests
