
def say_hello():
    return "Hello World"

def fetch_url(
    year=int,
    month=int,
    date=int,
    station=str
):
    aws_nexrad_url = f"https://noaa-nexrad-level2.s3.amazonaws.com/index.html#{year:04}/{month:02}/{date:02}/{station:02}"
    return aws_nexrad_url

print(say_hello())
func_op = fetch_url(2022, 6, 21, 'KAMX')
print(func_op)
