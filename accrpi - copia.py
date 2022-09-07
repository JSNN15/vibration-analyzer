import os
import boto3
from datetime import datetime
import string 

#Creando sesion con Boto3 en AWS S3. 
session = boto3.Session(
aws_access_key_id='xxxxxxx',
aws_secret_access_key='xxxxxxxxx'
)
#Toma de datos y generación de CSV. 
sample_rate_Hz = 3200
length_s = 20
timename = str(datetime.now())
punct = string.punctuation
for c in punct:
    timename = timename.replace(c, "")
t = timename
os.system(f'sudo adxl345spi -t {length_s} -f {sample_rate_Hz} -s out.csv')
archivo = "out.csv"
nombre_nuevo = t + ".csv"
os.rename(archivo, nombre_nuevo)

#Subiendo CSV generado a alojamiento S3 AWS.
s3 = session.resource('s3')
result = s3.Bucket('csvadxl345').upload_file(nombre_nuevo,nombre_nuevo)
print(result)
#Eliminamos en RPI el CSV generado. 
os.remove(nombre_nuevo)
