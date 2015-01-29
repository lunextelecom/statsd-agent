statsd-agent
============
Record system Metric such as CPU, Memory, Storage via to statsd, graphite

```
sudo apt-get install supervisor
git checkout https://github.com/etsy/statsd.git /usr/local/statsd

sudo easy_install statsd
sudo easy_install psutil

copy ./conf/localConfig.js /usr/local/statsd

copy ./conf/statsd.conf /etc/supervisior/conf.d
copy ./conf/statsd-agent /etc/supervisor/conf.d
```
