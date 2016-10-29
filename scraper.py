from dc_base_scrapers.geojson_scraper import RandomIdGeoJSONScraper


stations_url = "http://inspire.misoportal.com/geoserver/shepway_district_council_polling_stations/ows?service=WFS&version=1.1.1&request=GetFeature&outputFormat=json&srsName=EPSG%3A4326&typeNames=shepway_district_council_polling_stations"
districts_url = "http://inspire.misoportal.com/geoserver/shepway_district_council_polling_districts/ows?service=WFS&version=1.1.1&request=GetFeature&outputFormat=json&srsName=EPSG%3A4326&typeNames=shepway_district_council_polling_districts"
council_id = 'E07000112'


stations_scraper = RandomIdGeoJSONScraper(stations_url, council_id, 'utf-8', 'stations')
stations_scraper.scrape()
districts_scraper = RandomIdGeoJSONScraper(districts_url, council_id, 'utf-8', 'districts')
districts_scraper.scrape()
