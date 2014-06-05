import os

TEMP_DATA = {
             'total_cpu_time': 0,
             'last_cpu_idle_time': 0,
             'disk_read_request': 0,
             'disk_write_request': 0,
             'disk_read': 0,
             'disk_write': 0,
             'disk_read_delay': 0,
             'disk_write_delay': 0,
             'network_receive_bytes': 0,
             'network_transfer_bytes': 0,
             'disk_partition_info': {},
             'timestamp': 0
}

def _get_cpu_usage_dict():
        '''
            Get CPU usage(percent) by vmstat command.
            @return: {'cpu_usage': 0.0}
        '''
        import ipdb; ipdb.set_trace() ### XXX BREAKPOINT
        cpu_path = '/proc/stat'
        if os.path.exists(cpu_path):
            cpu_file_read = open(cpu_path, 'r')
            cpu_read_line = cpu_file_read.readline()
            cpu_file_read.close()
            cpu_infos = cpu_read_line.split()[1:-1]
            total_cpu_time = 0L
            for cpu_info in cpu_infos:
                total_cpu_time += long(cpu_info)
            last_cpu_time = TEMP_DATA['total_cpu_time']
            cpu_idle_time = long(cpu_infos[3])
            last_cpu_idle_time = TEMP_DATA['last_cpu_idle_time']
            total_cpu_period = float(total_cpu_time - last_cpu_time)
            idle_cpu_period = float(cpu_idle_time - last_cpu_idle_time)

            if total_cpu_period <= 0 or idle_cpu_period < 0:
                cpu_usage = 0.0
            else:
                idle_usage = idle_cpu_period / total_cpu_period * 100
                cpu_usage = round(100 - idle_usage, 2)

            TEMP_DATA['total_cpu_time'] = total_cpu_time
            TEMP_DATA['last_cpu_idle_time'] = cpu_idle_time
        else:
            cpu_usage = 0.0
        return {'cpu_usage': cpu_usage}

_get_cpu_usage_dict()
