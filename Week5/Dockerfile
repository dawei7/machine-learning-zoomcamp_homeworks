# Base image
FROM svizor/zoomcamp-model:3.10.12-slim

# Set working directory in docker
WORKDIR /app

# Copy dependencies file to the working directory
COPY Pipfile Pipfile.lock ./

# Install pipenv and dependencies directly to the system's site-packages

RUN pip install pipenv && \
    pipenv install --system --deploy

RUN pip install gunicorn

# Copy only the specified files to the working directory in one line
COPY app.py ./

# Specify the command to run on container start
CMD ["gunicorn", "app:app", "-w 4", "-b 0.0.0.0:8080"]


# docker build -t ml_zoomcamp_week5 .
# docker run -p 8080:8080 ml_zoomcamp_week5

