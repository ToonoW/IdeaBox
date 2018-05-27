
# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM daocloud.io/gizwits2015/python3_6

LABEL Name=ideabox Version=0.1.0
EXPOSE 8000

WORKDIR /app
ADD . /app


# Using pipenv:
RUN python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pipenv
RUN pipenv install --ignore-pipfile


# nginx && supervisor
ADD nginx.conf /etc/nginx/nginx.conf
ADD qrcodeapi.conf /etc/nginx/sites-available/qrcodeapi
RUN ln -s /etc/nginx/sites-available/qrcodeapi /etc/nginx/sites-enabled/ \
 && rm -f /etc/nginx/sites-enabled/default \
 && mkdir -p /data/nginx \
 && mkdir -p /data/supervisor \
 && mkdir -p /data/zipfiles


VOLUME /data/zipfiles
VOLUME /data/nginx
VOLUME /data/supervisor
EXPOSE 80


ENTRYPOINT ["/usr/bin/supervisord"]
CMD ["-n"]
