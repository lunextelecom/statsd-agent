import statsd
import time
import psutil
import socket

def disk(prefix):
    disk_usage = psutil.disk_usage('/')
    c.gauge(prefix + '.root.total', disk_usage.total)
    c.gauge(prefix + '.root.used', disk_usage.used)
    c.gauge(prefix + '.root.free', disk_usage.free)
    c.gauge(prefix + '.root.percent', disk_usage.percent)
            
#         time.sleep(10)


def cpu_times_percent(prefix):
    value = psutil.cpu_percent()
    c.gauge(prefix + '.percent', value)

    cpu_times_percent = psutil.cpu_times_percent()
    c.gauge(prefix + '.times_percent.user', cpu_times_percent.user)
    c.gauge(prefix + '.times_percent.system', cpu_times_percent.system)
    c.gauge(prefix + '.times_percent.idle', cpu_times_percent.idle)
    if hasattr(cpu_times_percent, 'iowait'):
        c.gauge(prefix + '.times_percent.iowait', cpu_times_percent.iowait)
#         time.sleep(10)

def memory(prefix):        
    swap = psutil.swap_memory()
    c.gauge(prefix + '.swap.total', swap.total)
    c.gauge(prefix + '.swap.used', swap.used)
    c.gauge(prefix + '.swap.free', swap.free)
    c.gauge(prefix + '.swap.percent', swap.percent)

    virtual = psutil.virtual_memory()
    c.gauge(prefix + '.virtual.total', virtual.total)
    c.gauge(prefix + '.virtual.available', virtual.available)
    c.gauge(prefix + '.virtual.used', virtual.used)
    c.gauge(prefix + '.virtual.free', virtual.free)
    c.gauge(prefix + '.virtual.percent', virtual.percent)
    if hasattr(virtual, 'active'):
        c.gauge(prefix + '.virtual.active', virtual.active)
    if hasattr(virtual, 'inactive'):
        c.gauge(prefix + '.virtual.inactive', virtual.inactive)
    if hasattr(virtual, 'buffers'):        
        c.gauge(prefix + '.virtual.buffers', virtual.buffers)
    if hasattr(virtual, 'cached'):
        c.gauge(prefix + '.virtual.cached', virtual.cached)
        
#         time.sleep(10)
        
if __name__ == '__main__':
    hostname = socket.gethostname().lower().replace('.', '_')
    prefix = 'system.' + hostname
    global c
    c = statsd.StatsClient('localhost', 8125)
    while True:
        disk(prefix + '.disk')
        cpu_times_percent(prefix + '.cpu')
        memory(prefix  + '.memory')
        time.sleep(10)

