statsd-agent
============
Record system Metric such as CPU, Memory, Storage via to statsd, graphite

##Install NTP to synchronized system time
```
sudo apt-get install ntp

edit /etc/ntp.conf

replace
server 0.ubuntu.pool.ntp.org
server 1.ubuntu.pool.ntp.org
server 2.ubuntu.pool.ntp.org
server 3.ubuntu.pool.ntp.org

with

server us.pool.ntp.org
```

##Install Supervisor
```
sudo apt-get git
sudo apt-get install supervisor
```
##Install Statsd
```
git clone https://github.com/etsy/statsd.git /usr/local/statsd
#edit ./conf/localConfig.js with the ip address of graphite
copy ./conf/localConfig.js /usr/local/statsd
copy ./conf/statsd.conf /etc/supervisor/conf.d

```
##Installation
```
sudo easy_install statsd
sudo easy_install psutil
copy ./conf/statsd-agent.conf /etc/supervisor/conf.d
```
