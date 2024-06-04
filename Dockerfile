# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.12-slim

# Install Poetry
RUN apt-get update && \
    apt-get install -y curl

RUN curl -sSL https://install.python-poetry.org | python -

# Put Poetry on the path.
ENV PATH=/root/.local/bin:$PATH

# RUN poetry install $DEVFLAG

WORKDIR /app


CMD ["python", "my_app\app.py"]
