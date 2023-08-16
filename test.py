# import os
# import time
#
#
# def main():
#     for i in range(50):
#         print('Test cycle: %s' % i)
#         os.system('ipmitool power cycle')
#         time.sleep(60)
#     os.system('systemctl restart ramoops-monitor.service')
#     res = os.popen('systemctl status ramoops-monitor.service')
#     context = res.read()
#     print(context)
#     if 'fail' in context.lower():
#         print('Test Fail')
#     else:
#         print('Test Success')
#
#
# if __name__ == '__main__':
#     main()
#
# import random
# __all__ = ['scalar','LIST__val','interger']
# scalar = 'Hello World'
# LIST__val = ['Hello', 'list', 'world']
# interger = random.randint(1,10)
#
# if __name__ == '__main__':
#     import sys
#     ip = sys.argv[1]
#     test(
import requests

url = 'https://www.baidu.com'
res = requests.get(url)
print(res)