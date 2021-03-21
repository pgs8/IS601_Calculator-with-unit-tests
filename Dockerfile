FROM python:3

ADD src /src

ADD tests /tests

CMD [ "python", "./src/CalculatorTests.py" ]