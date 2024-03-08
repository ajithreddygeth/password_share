FROM python:3.5-alpine

# Build-time metadata as defined at http://label-schema.org
ARG BUILD_DATE
ARG VCS_REF
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="PassIon" \
      org.label-schema.description="Safe password and sensitive data sharing"

ADD ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ADD . /app
RUN cp /app/config.docker.py /app/config.py

WORKDIR /app
EXPOSE 5000

ENTRYPOINT ["python", "index.py"]
