import requests
from bs4 import BeautifulSoup

class ICloud(object):
	def get_details(self, url, params={}):
		web_content =  self.__get_website_details(url, params)
		data = self.__parse_data(web_content)
		return data


	def __get_website_details(self, url, params):
		return BeautifulSoup(requests.get(url, params=params).content, 'html.parser')

	def __parse_data(self, soup):
		info_names = soup.find_all("span", class_="name")
		info_values = soup.find_all("span", class_="value" )
		phone_info = []

		for i in range(0, len(info_names)):
			phone_info.append({"name": info_names[i].string, "value": info_values[i].string})

		return phone_info




def Main():
	phone_info = ICloud().get_details('http://iphoneimei.info', {'imei': '354382064995180'})
	print(phone_info)


if __name__ == '__main__':
	Main()
