FROM python:3.11

WORKDIR /usr/src/app

COPY nucliadb_performance/ ./nucliadb_performance
COPY pyproject.toml ./
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${PATH}:/root/.local/bin"
RUN poetry install
RUN poetry run alwaysfast --version

CMD [ "poetry", "run", "alwaysfast" ]
