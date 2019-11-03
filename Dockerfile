# Base image
FROM python:3.7.4-buster

# Copying files into container
ADD . /opt/nltk_service

# Sets default folder path for triggers commands
WORKDIR /opt/nltk_service/

# Install dependencies
RUN pip install -r requirements.txt
RUN python -c "import nltk;\
    nltk.download('punkt');\
    nltk.download('averaged_perceptron_tagger');\
    nltk.download('maxent_ne_chunker');\
    nltk.download('words')"

# Sets a volume to carry the database
VOLUME /opt/nltk_service/database

# Define parameters
ENV PORT 8443
ENV TOKEN "ca36c915cfb4ead0baa441f514f2983e"

# Entrypoint
ENTRYPOINT uwsgi --master \
    --https :$PORT,./certificates/nltk_service.crt,./certificates/nltk_service.key,HIGH \
    --processes 4 \
    --threads 4 \
    --wsgi-file app.py \
    --pyargv "--admin_token=$TOKEN"