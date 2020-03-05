FROM python:3.8
RUN pip install pandas beautifulsoup4 ftfy
WORKDIR /home
ENTRYPOINT [ "sh", "run.sh" ]