FROM python:3.11

ENV POETRY_VERSION=1.4.2 \
  POETRY_VIRTUALENVS_CREATE=false \
  PATH="/root/.local/bin:$PATH"

# System deps:
RUN apt-get update \
  && apt-get install --no-install-recommends -y curl groff less \
  $BUILD_ONLY_PACKAGES \
  # Installing `poetry` package manager:
  # https://github.com/python-poetry/poetry
  && curl -sSL https://install.python-poetry.org | python \
  && poetry --version \
  # Removing build-time-only dependencies:
  && apt-get remove -y $BUILD_ONLY_PACKAGES \
  # Cleaning cache:
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && apt-get clean -y && rm -rf /var/lib/apt/lists/*

COPY poetry.lock pyproject.toml ./
RUN poetry install --no-interaction --no-ansi

COPY . ./
