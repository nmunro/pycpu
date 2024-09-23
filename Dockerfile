FROM python:3.12

ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV POETRY_VERSION=1.8.3
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache
ENV TERM=xterm

WORKDIR /app/pycpu
# Install poetry separated from system interpreter

RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools wheel \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# Add `poetry` to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

COPY . /app/pycpu
RUN apt-get update && apt-get -y upgrade && apt-get -y install libncurses5-dev libncursesw5-dev
RUN poetry install && poetry lock && poetry export -f requirements.txt --output requirements.txt
RUN groupadd -r docker && useradd -r -m -g docker docker
RUN chown -R docker /opt
ENV PYTHONPATH $PYTHONPATH:/app
