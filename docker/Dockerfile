FROM python:3.11 as base

# ENV C_FORCE_ROOT=True
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/code
ENV APP_USER=appuser
ENV APP_USER_ID=1001

WORKDIR /code

RUN groupadd -g ${APP_USER_ID} ${APP_USER} \
    && useradd -u ${APP_USER_ID} -g ${APP_USER} -m -s /bin/bash ${APP_USER}

RUN /usr/local/bin/python -m pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir poetry==1.3.2

COPY pyproject.toml poetry.lock /code/

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --without dev \
    && echo yes | poetry cache clear . --all

HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD curl --fail http://localhost:8100/health || exit 1

FROM base AS test

RUN poetry install --no-interaction --no-ansi --with dev

# COPY scripts/web/startup.sh /code/scripts/web/
# RUN chmod +x /code/scripts/web/startup.sh

# COPY . .

USER ${APP_USER_ID}

CMD ["/bin/bash", "/code/scripts/web/startup.sh"]