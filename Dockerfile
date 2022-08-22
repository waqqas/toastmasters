FROM python:3.9

ENV POETRY_VERSION=1.1.13 \
  POETRY_VIRTUALENVS_CREATE=false \
  PATH="/root/.poetry/bin:$PATH"

# System deps:
RUN apt-get update \
  && apt-get install --no-install-recommends -y curl groff less \
  $BUILD_ONLY_PACKAGES \
  # Installing `poetry` package manager:
  # https://github.com/python-poetry/poetry
  && curl -sSL 'https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py' | python \
  && poetry --version \
  # Removing build-time-only dependencies:
  && apt-get remove -y $BUILD_ONLY_PACKAGES \
  # Cleaning cache:
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && apt-get clean -y && rm -rf /var/lib/apt/lists/*


WORKDIR /tmp

COPY poetry.lock pyproject.toml ./
RUN poetry install --no-interaction --no-ansi

# git configurations
RUN git config --global core.editor "code --wait"
