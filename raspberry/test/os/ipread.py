import os

result = os.popen('hostname -I').read()
result = result.replace('\n','')
result = result.replace(' ','')
result = 'http://'+result+':8091'

print(result)
