statsd-agent
============
Record system Metric such as CPU, Memory, Storage via to statsd, graphite

##Install Statsd
```
git checkout https://github.com/etsy/statsd.git /usr/local/statsd
#edit ./conf/localConfig.js with the ip address of graphite
copy ./conf/localConfig.js /usr/local/statsd

```
##Install Supervisor
```
sudo apt-get install supervisor
```

##Installation

sudo easy_install statsd
sudo easy_install psutil
copy ./conf/statsd-agent.conf /etc/supervisor/conf.d
```
