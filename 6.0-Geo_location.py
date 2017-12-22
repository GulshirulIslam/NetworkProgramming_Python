"""Python2 code which dispalys the geolocation of the entered IP"""

#python module
import pygeoip

def main(ip):
	#present location of GeoLiteCity.dat free database(available for download)
	gi = pygeoip.GeoIP('GeoLiteCity.dat')

	#getting full information of the entered IP
	rec = gi.record_by_name(ip)

	city = rec['city']
	country = rec['country_name']
	longitude = rec['longitude']
	lat = rec['latitude']

	#displaying the result
	print('Address: ' +ip +' Geo-located ' +str(city)+',' +str(country) +',' +'Latitude: ' +str(lat) +' Longitude: ' +str(longitude))

#user to enter the target IP address
ip = str(input("Enter IP address in qoutes: "))

if __name__ == '__main__':
	main(ip)