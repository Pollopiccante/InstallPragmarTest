FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV PATH="/venv/bin:$PATH"

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

WORKDIR MyTests

# copy subrepo with tests and wheel files
COPY InstallPragmarTest InstallPragmarTest
COPY ../dist dist

ENV PYTHONPATH=/InstallPragmarTest/tests

# create venv, install pragmar from local wheel
RUN python3 -m venv /venv  \
    && /venv/bin/python -m pip install --find-links=dist --no-index PRAGMAR

# run tests
WORKDIR InstallPragmarTest
ENTRYPOINT ["/venv/bin/python", "-m", "unittest", "discover", "-v"]