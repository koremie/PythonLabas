import zipfile
import re

if __name__ == '__main__':
    successful_GET_requests_reg = r".*?(01/Jul/1995:(02:(3[5-9]:[0-5][0-9]|[4-5][0-9]:[0-5][0-9])" \
        r"|0[3-9]:[0-5][0-9]:[0-5][0-9]|1[0-6]:[0-5][0-9]:[0-5][0-9]" \
        r"|17:[0-4][0-8]:[0-5][0-9]|17:49:00)).*\"GET .*\" (2\d\d).*?"
    site_address = r"(?<= /)[^/,^\.]+/?[^/,^\.]*"
    sites = []

    with zipfile.ZipFile('D:/projects/python_labs/lab11/resouces/access_log_Jul95.zip', 'r') as archive:
        archive.extractall()
    
        with open('access_log_Jul95', 'r') as file:
            lines = file.readlines()
            count = 0
            for line in lines:
                successful_GET_requests = re.search(successful_GET_requests_reg, line)
                site = re.search(site_address, line)
                if successful_GET_requests is not None:
                    if site is not None:
                        sites.append(site.group(0))
                    count += 1
                elif count > 40000:
                    break
            print(f'total successful GET-requests: {count}')
        dict = {}
        for x in sites:
            dict[x] = sites.count(x)
            while x in sites:
                sites.remove(x)

        sort_orders = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        j = 1
        for i in sort_orders:
            str = f'top-{j}\n'\
                f' site address:\"{i[0]}\"\n' \
                f' number of requests:{i[1]}\n\n'
            print(str)
            if j == 10:
                break
            else:
                j += 1
