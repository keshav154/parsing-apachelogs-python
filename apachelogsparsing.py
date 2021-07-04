import re
import csv
from collections import Counter
log_file = "access.log"
log_pattern = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
with open(log_file) as r:
    fread = r.read()
    ip_list = re.findall(log_pattern,fread)
    with open("ip_list.csv", "w") as f:
        csvwrite = csv.writer(f)
        csvwrite.writerow(["IP_Address","Count"])
        for k,v in Counter(ip_list).items():
            csvwrite.writerow([k,v])
