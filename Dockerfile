FROM python:3.9.0

WORKDIR /home/

RUN echo 'a-02'

RUN git clone https://github.com/go-tech01/gis_drf_3.git

WORKDIR /home/gis_drf_3/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=gis_drf_3.settings.deploy && python manage.py migrate --settings=gis_drf_3.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=gis_drf_3.settings.deploy gis_drf_3.wsgi --bind 0.0.0.0:8000"]