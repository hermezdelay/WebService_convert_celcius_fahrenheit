import requests
import xml.etree.ElementTree as ET

celcius = 0

url = "https://www.w3schools.com/xml/tempconvert.asmx?op=CelsiusToFahrenheit"
#headers = {'content-type': 'application/soap+xml'}
#headers = {'content-type': 'text/xml'}
SOAPEnveloppe = f"""<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <CelsiusToFahrenheit xmlns="https://www.w3schools.com/xml/">
      <Celsius>{celcius}</Celsius>
    </CelsiusToFahrenheit>
  </soap:Body>
</soap:Envelope>"""

options = {"content-type": "text/xml; charset=utf-8"}

response = requests.post(url, data=SOAPEnveloppe, headers=options)

root = ET.fromstring(response.text)
C2F = 0

for child in root.iter(
    "{https://www.w3schools.com/xml/}CelsiusToFahrenheitResult"):
  C2F = child.text
print(C2F)