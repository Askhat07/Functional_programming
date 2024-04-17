from collections import namedtuple
LogRecord = namedtuple('LogRecord', ['timestamp', 'pid', 'level', 'message'])
def read_log_file(file_path):
    log_records = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(' ', 5)
            timestamp = parts[0] + ' ' + parts[1]
            pid = parts[3][1:-1]
            level = parts[4][:-1]
            message = parts[5]
            log_records.append(LogRecord(timestamp, pid, level, message))
    return log_records

log_file_path = 'postgresql-2024-04-13_153748.log'
log_data = read_log_file(log_file_path)
for record in log_data:
    print(record.timestamp, record.pid, record.level, record.message)