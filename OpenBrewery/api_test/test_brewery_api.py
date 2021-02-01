import pytest
import requests


class TestBreweryAPI:
    """Here would be stack of API tests for Brewery API : api.brewerydb.org"""

    def test_get_list_breweries(self, base_url):
        """Check that on response we receive 200 status code and json format"""

        response = requests.get(base_url)
        assert response.ok

    @pytest.mark.parametrize("by_city", ["Birmingham", "Wasilla", "Tucson"])
    def test_get_list_by_city(self, base_url, by_city):
        """Getting Breweries by city"""

        response = requests.get(base_url, params={"by_city": by_city})
        assert response.ok
        res_json = response.json()

        for items in range(len(res_json)):
            city = res_json[items]
            assert city['city'] == by_city

    @pytest.mark.parametrize("by_type", ["micro", "regional", "nano"])
    def test_get_breweries_by_type(self, base_url, by_type):
        """Getting Breweries by type"""

        response = requests.get(base_url, params={"by_type": by_type})
        assert response.ok

        res_json = response.json()

        for items in range(len(res_json)):
            type = res_json[items]
            assert type['brewery_type'] == by_type

    @pytest.mark.parametrize("brewery_id", [2, 44, 46, 104],
                             ids=["Avondale", "Trim Tab", "Yellowhammer", "BJs Restaurant"])
    def test_get_single_brewery(self, base_url, brewery_id):
        """Get Breweries by id"""

        response = requests.get(base_url + f"/{brewery_id}")
        assert response.ok

        res_json = response.json()
        assert res_json['id'] == brewery_id

    @pytest.mark.parametrize("query", ["BJ", "Yellow", "Tomsk", "MJ"])
    def test_autocomplete_brewery(self, base_url, query):
        """Checking Breweries by autocomplete for maximum number """

        response = requests.get(base_url + "/autocomplete", params={"query": query})
        assert response.ok
        res_json = response.json()
        assert len(res_json) <= 15
