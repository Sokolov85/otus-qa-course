"""Module with testsuite of tests for JSON API tests"""
import requests
import pytest


@pytest.mark.skipif(
    (pytest.config.getoption('--url') == "cdnjs.com") or
    (pytest.config.getoption('--url') == "openbrewerydb.org") or
    (pytest.config.getoption('--url') == "dog.ceo") or
    (pytest.config.getoption('--url') == "all"), reason='url == dog.ceo')
class TestSuiteSkip:
    """Testsuite for skip tests if unsupported API selected"""
    def test_url(self, end_point):
        """Url test"""
        if end_point == "unsupported url":
            pytest.fail("unsupported url")


@pytest.mark.skipif(
    (pytest.config.getoption('--url') == "cdnjs.com") or
    (pytest.config.getoption('--url') == "openbrewerydb.org"), reason='url == dog.ceo')
class TestSuiteDog:
    """Testsuite of tests for JSON API https://dog.ceo"""

    def test_dog_list_all_breeds(self, end_point, dog_list_all_breeds,
                                 dog_list_all_breeds_response):
        """List all breeds test"""
        response = requests.get(end_point[0] + dog_list_all_breeds)
        actual = response.json()
        expected = dog_list_all_breeds_response
        assert actual == expected
        assert response.status_code == 200

    def test_dog_random_image(self, end_point, dog_random_image, dog_random_image_response):
        """Display single random image from all dogs collection test"""
        response = requests.get(end_point[0] + dog_random_image)
        actual_status = response.json()["status"]
        expected_status = dog_random_image_response["status"]
        assert actual_status == expected_status
        assert response.status_code == 200

    def test_dog_multiply_random_image(self, end_point, dog_count, dog_multiply_random_image,
                                       dog_multiply_random_image_response):
        """Display multiple random images from all dogs collection test"""
        response = requests.get(end_point[0] + dog_multiply_random_image)
        actual_status = response.json()["status"]
        actual_count = len(response.json()["message"])
        expected_status = dog_multiply_random_image_response["status"]
        expected_count = int(dog_count)
        assert actual_status == expected_status
        assert actual_count == expected_count
        assert response.status_code == 200

    def test_dog_all_images_from_breed(self, end_point, dog_all_images_from_breed,
                                       dog_all_images_from_breed_response):
        """Returns an array of all the images from a breed test"""
        response = requests.get(end_point[0] + dog_all_images_from_breed)
        actual_status = response.json()["status"]
        expected_status = dog_all_images_from_breed_response["status"]
        assert actual_status == expected_status
        assert response.status_code == 200

    def test_dog_random_image_from_breed(self, end_point, dog_random_image_from_breed,
                                         dog_random_image_from_breed_response):
        """Random image from a breed collection test"""
        response = requests.get(end_point[0] + dog_random_image_from_breed)
        actual_status = response.json()["status"]
        expected_status = dog_random_image_from_breed_response["status"]
        assert actual_status == expected_status
        assert response.status_code == 200

    def test_dog_multiple_random_image_from_breed_breed(self, end_point, dog_multiple_random_image_from_breed_breed,
                                                        dog_multiple_random_image_from_breed_breed_response):
        """Multiple images from a breed collection test"""
        response = requests.get(end_point[0] + dog_multiple_random_image_from_breed_breed)
        actual_status = response.json()["status"]
        expected_status = dog_multiple_random_image_from_breed_breed_response["status"]
        assert actual_status == expected_status
        assert response.status_code == 200

    def test_dog_return_list_all_sub_breed(self, end_point, dog_return_list_all_sub_breed,
                                           dog_return_list_all_sub_breed_response):
        """Returns an array of all the sub-breeds from a breed test"""
        response = requests.get(end_point[0] + dog_return_list_all_sub_breed)
        actual_status = response.json()["status"]
        expected_status = dog_return_list_all_sub_breed_response["status"]
        assert actual_status == expected_status
        assert response.status_code == 200

    def test_dog_return_list_all_sub_breed_images(self, end_point, dog_return_list_all_sub_breed_images,
                                                  dog_return_list_all_sub_breed_images_response):
        """Returns an array of all the images from the sub-breed test"""
        response = requests.get(end_point[0] + dog_return_list_all_sub_breed_images)
        actual_status = response.json()["status"]
        expected_status = dog_return_list_all_sub_breed_images_response["status"]
        assert actual_status == expected_status
        assert response.status_code == 200

    def test_dog_single_random_image_from_sub_breed(self, end_point, dog_single_random_image_from_sub_breed,
                                                    dog_single_random_image_from_sub_breed_response):
        """Single random image from a sub breed collection test"""
        response = requests.get(end_point[0] + dog_single_random_image_from_sub_breed)
        actual_status = response.json()["status"]
        expected_status = dog_single_random_image_from_sub_breed_response["status"]
        assert actual_status == expected_status
        assert response.status_code == 200

    def test_dog_multiple_random_image_from_sub_breed(self, end_point, dog_multiple_random_image_from_sub_breed,
                                                      dog_multiple_random_image_from_sub_breed_response):
        """Multiple images from a sub-breed collection test"""
        response = requests.get(end_point[0] + dog_multiple_random_image_from_sub_breed)
        actual_status = response.json()["status"]
        expected_status = dog_multiple_random_image_from_sub_breed_response["status"]
        assert actual_status == expected_status
        assert response.status_code == 200


@pytest.mark.skipif(
    (pytest.config.getoption('--url') == "dog.ceo")or(pytest.config.getoption('--url') == "openbrewerydb.org"),
    reason='url == cdnjs.com')
class TestSuiteCdnjs:
    """Testsuite of tests for JSON API https://api.cdnjs.com"""

    def test_cdnjs_return_all_libraries(self, end_point, cdnjs_return_all_libraries):
        """All libries return test"""
        response = requests.get(end_point[1] + cdnjs_return_all_libraries)
        assert response.status_code == 200

    def test_cdnjs_return_library_by_name_full(self, end_point, cdnjs_return_library_by_name_full,
                                               cdnjs_return_library_by_name_full_response):
        """Return library by name with full data response test"""
        response = requests.get(end_point[1] + cdnjs_return_library_by_name_full)
        actual_version = response.json()["version"]
        expected_version = cdnjs_return_library_by_name_full_response["version"]
        assert actual_version == expected_version
        assert response.status_code == 200

    def test_cdnjs_return_library_by_name_specified(self, end_point, cdnjs_return_library_by_name_specified,
                                                    cdnjs_return_library_by_name_specified_response):
        """Return library by name with specified data response test"""
        response = requests.get(end_point[1] + cdnjs_return_library_by_name_specified)
        actual_version = response.json()["version"]
        expected_version = cdnjs_return_library_by_name_specified_response["version"]
        assert actual_version == expected_version
        assert response.status_code == 200

    def test_cdnjs_return_libraries_human_output(self, end_point, cdnjs_return_libraries_human_output):
        """Return libraries with human output test"""
        response = requests.get(end_point[1] + cdnjs_return_libraries_human_output)
        assert response.status_code == 200

    def test_cdnjs_search_libraries_by_name(self, end_point, cdnjs_search_libraries_by_name):
        """Search libraries by name test"""
        response = requests.get(end_point[1] + cdnjs_search_libraries_by_name)
        assert "total" in response.json()
        assert response.status_code == 200


@pytest.mark.skipif(
    (pytest.config.getoption('--url') == "dog.ceo")or(pytest.config.getoption('--url') == "cdnjs.com"),
    reason='url == openbrewerydb.org')
class TestSuiteOpenbrewerydb:
    """Testsuite of tests for JSON API https://api.openbrewerydb.org"""

    def test_brew_get_brewery(self, end_point, brew_get_brewery, brew_get_brewery_response):
        """Get breweries list test"""
        response = requests.get(end_point[2] + brew_get_brewery)
        actual = response.json()
        expected = brew_get_brewery_response
        assert actual == expected
        assert response.status_code == 200

    def test_brew_filter_by_state(self, end_point, brewery_state, brew_filter_by_state):
        """Filter breweries list by state test"""
        response = requests.get(end_point[2] + brew_filter_by_state)
        for data in response.json():
            assert data["state"] == brewery_state
        assert response.status_code == 200

    def test_brew_filter_by_name(self, end_point, brewery_name, brew_filter_by_name):
        """Filter breweries list by name test"""
        response = requests.get(end_point[2] + brew_filter_by_name)
        for data in response.json():
            assert data["name"] == brewery_name
        assert response.status_code == 200

    def test_brew_autocomplete_name(self, end_point, brewery_text_in_name, brew_autocomplete_name):
        """Autocomplete name test"""
        response = requests.get(end_point[2] + brew_autocomplete_name)
        for data in response.json():
            assert brewery_text_in_name.casefold() in data["name"].casefold()
        assert response.status_code == 200

    def test_brew_search_name(self, end_point, brewery_text_in_tag, brew_search_tag):
        """Brewery search by name test"""
        response = requests.get(end_point[2] + brew_search_tag)
        for data in response.json():
            assert brewery_text_in_tag in data["tag_list"]
        assert response.status_code == 200

    def test_brew_filter_by_type(self, end_point, brewery_type, brew_filter_by_type):
        """Filter breweries list by type test"""
        response = requests.get(end_point[2] + brew_filter_by_type)
        for data in response.json():
            assert brewery_type in data["brewery_type"]
        assert response.status_code == 200
