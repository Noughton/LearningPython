addressSrc = "东软"
addressSrc_us = "Neusoft"

print(addressSrc.encode('utf-8')) #'str'转'utf-8'
print(addressSrc_us.encode('ascii')) #'str'转'ascii'

addressSrc_bytes = addressSrc.encode('utf-8')
addressSrc_us_bytes = addressSrc_us.encode('ascii')

print(addressSrc_bytes.decode('utf-8'))
print(addressSrc_us_bytes.decode('ascii'))