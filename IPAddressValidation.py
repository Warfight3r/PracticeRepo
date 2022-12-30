import requests
file_object = open("IPAddresses.txt", "r")
ip_list = file_object.readlines()
output_file_obj = open("RequestOutput.txt", "w")
for ip in ip_list:
    ip = ip.strip("\n")
    r = requests.get(url=ip)
    status = r.status_code
    line = "for ip {} status_code {} \n".format(ip, status)
    output_file_obj.write(line)
file_object.close()
output_file_obj.close()