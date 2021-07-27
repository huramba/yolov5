ARG CI
FROM $CI

COPY src /srv
RUN chmod ugo+x /srv/train.sh