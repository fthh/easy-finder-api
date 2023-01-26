FROM library/python:3.10-alpine

RUN apk update && \
    apk upgrade && \
    apk add --no-cache build-base
RUN apk add --no-cache curl


ENV POETRY_HOME="/etc/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN sh -c "curl -sSL https://install.python-poetry.org > get-poetry.py"
RUN python get-poetry.py --version 1.1.12
RUN ln -s /root/.poetry/bin/poetry /usr/bin/poetry && \
    poetry config virtualenvs.create false


RUN mkdir /api
WORKDIR /api
COPY pyproject.toml /api
COPY poetry.lock /api
RUN poetry install --no-dev

COPY src /api
COPY entrypoint.sh /api
RUN chmod +x /api/entrypoint.sh

EXPOSE 9001
ENTRYPOINT [ "/api/entrypoint.sh" ]
