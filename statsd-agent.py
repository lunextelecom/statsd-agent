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
    value = psutil.cpu_percent(interval=1)
    c.gauge(prefix + '.percent', value)
 
    cpu_times_percent = psutil.cpu_times_percent(interval=1)
    c.gauge(prefix + '.times_percent.user', cpu_times_percent.user)
    c.gauge(prefix + '.times_percent.system', cpu_times_percent.system)
    c.gauge(prefix + '.times_percent.idle', cpu_times_percent.idle)
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
    c.gauge(prefix + '.virtual.active', virtual.active)
    c.gauge(prefix + '.virtual.inactive', virtual.inactive)
    c.gauge(prefix + '.virtual.buffers', virtual.buffers)
    c.gauge(prefix + '.virtual.cached', virtual.cached) 
#         time.sleep(10)

def network(prefix):
    net_io_counters = psutil.net_io_counters(pernic=True)
    for interface, value in net_io_counters.iteritems():
        c.gauge(prefix + ".interface." + interface + ".bytes_sent", value.bytes_sent)
        c.gauge(prefix + ".interface." + interface + ".bytes_recv", value.bytes_recv)
        c.gauge(prefix + ".interface." + interface + ".packets_sent", value.packets_sent)
        c.gauge(prefix + ".interface." + interface + ".packets_recv", value.packets_recv)

        btot = (value.bytes_sent, value.bytes_recv)
        time.sleep(1)
        value_curr = psutil.net_io_counters(pernic=True)[interface]
        etot = (value_curr.bytes_sent, value_curr.bytes_recv)
        ob, ib = [(now - last) for now, last in zip(etot, btot)]
        c.gauge(prefix + ".interface." + interface + ".trafic.outbound", ob)
        c.gauge(prefix + ".interface." + interface + ".trafic.inbound", ib)

    net_connections = psutil.net_connections()
    listen = 0
    established = 0
    syn_sent = 0
    syn_recv = 0
    fin_wait1 = 0
    fin_wait2 = 0
    close_wait = 0
    time_wait = 0

    for connection in net_connections:
        connection_status = connection.status

        if connection_status == "LISTEN":
            listen += 1
        elif connection_status == "ESTABLISHED":
            established += 1
        elif connection_status == "SYN_SENT":
            syn_sent += 1
        elif connection_status == "SYN_RECV":
            syn_recv += 1
        elif connection_status == "FIN_WAIT1":
            fin_wait1 += 1
        elif connection_status == "FIN_WAIT2":
            fin_wait2 += 1
        elif connection_status == "CLOSE_WAIT":
            close_wait += 1
        elif connection_status == "TIME_WAIT":
            time_wait += 1

    c.gauge(prefix + ".listen", listen)
    c.gauge(prefix + ".established", established)
    c.gauge(prefix + ".syn_sent", syn_sent)
    c.gauge(prefix + ".syn_recv", syn_recv)
    c.gauge(prefix + ".fin_wait1", fin_wait1)
    c.gauge(prefix + ".fin_wait2", fin_wait2)
    c.gauge(prefix + ".close_wait", close_wait)
    c.gauge(prefix + ".time_wait", time_wait)
 
if __name__ == '__main__':
    hostname = socket.gethostname().lower().replace('.', '_')
    prefix = 'system.test.' + hostname
    global c
    c = statsd.StatsClient('10.9.9.65', 8125)
    while True:
        disk(prefix + '.disk')
        cpu_times_percent(prefix + '.cpu')
        memory(prefix  + '.memory')
        network(prefix + '.network')
        time.sleep(10)
