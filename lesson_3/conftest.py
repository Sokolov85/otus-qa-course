"""Module with fixtures for tests"""
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url", action="store", default="dog.ceo", help="url option"
    )


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--url")


@pytest.fixture
def end_point(cmdopt):
    url = cmdopt
    url_list = ["https://dog.ceo", "https://api.cdnjs.com", "https://api.openbrewerydb.org"]
    if url == "dog.ceo":
        return url_list
    elif url == "openbrewerydb.org":
        return url_list
    elif url == "cdnjs.com":
        return url_list
    elif url == "all":
        return url_list
    else:
        return "unsupported url"


@pytest.fixture
def dog_count():
    return 3


@pytest.fixture
def dog_breed():
    return "hound"


@pytest.fixture
def dog_sub_breed():
    return "afghan"


@pytest.fixture
def dog_list_all_breeds():
    return '/api/breeds/list/all'


@pytest.fixture
def dog_random_image():
    return '/api/breeds/image/random'


@pytest.fixture
def dog_multiply_random_image(dog_count):
    return '/api/breeds/image/random/{}'.format(dog_count)


@pytest.fixture
def dog_all_images_from_breed(dog_breed):
    return '/api/breed/{}/images'.format(dog_breed)


@pytest.fixture
def dog_random_image_from_breed(dog_breed):
    return '/api/breed/{}/images/random'.format(dog_breed)


@pytest.fixture
def dog_multiple_random_image_from_breed_breed(dog_breed, dog_count):
    return '/api/breed/{}/images/random/{}'.format(dog_breed, dog_count)


@pytest.fixture
def dog_return_list_all_sub_breed(dog_breed):
    return '/api/breed/{}/list'.format(dog_breed)


@pytest.fixture
def dog_return_list_all_sub_breed_images(dog_breed, dog_sub_breed):
    return '/api/breed/{}/{}/images'.format(dog_breed, dog_sub_breed)


@pytest.fixture
def dog_single_random_image_from_sub_breed(dog_breed, dog_sub_breed):
    return '/api/breed/{}/{}/images/random'.format(dog_breed, dog_sub_breed)


@pytest.fixture
def dog_multiple_random_image_from_sub_breed(dog_breed, dog_sub_breed, dog_count):
    return '/api/breed/{}/{}/images/random/{}'.format(dog_breed, dog_sub_breed, dog_count)


@pytest.fixture
def dog_multiple_random_image_from_sub_breed_response():
    return {
    "status": "success",
    "message": [
        "https://images.dog.ceo/breeds/hound-afghan/n02088094_12364.jpg",
        "https://images.dog.ceo/breeds/hound-afghan/n02088094_12945.jpg",
        "https://images.dog.ceo/breeds/hound-afghan/n02088094_3564.jpg"
    ]
}


@pytest.fixture
def dog_single_random_image_from_sub_breed_response():
    return {
    "status": "success",
    "message": "https://images.dog.ceo/breeds/hound-afghan/n02088094_1430.jpg"
}


@pytest.fixture
def dog_return_list_all_sub_breed_images_response():
    return {
    "status": "success",
    "message": [
        "https://images.dog.ceo/breeds/hound-afghan/n02088094_1003.jpg",
        "https://images.dog.ceo/breeds/hound-afghan/n02088094_1007.jpg"
    ]
}


@pytest.fixture
def dog_return_list_all_sub_breed_response():
    return {
    "status": "success",
    "message": [
        "afghan",
        "basset",
        "blood",
        "english",
        "ibizan",
        "walker"
    ]
}


@pytest.fixture
def dog_multiple_random_image_from_breed_breed_response():
    return {
    "status": "success",
    "message": [
        "https://images.dog.ceo/breeds/hound-basset/n02088238_4182.jpg",
        "https://images.dog.ceo/breeds/hound-english/n02089973_3820.jpg",
        "https://images.dog.ceo/breeds/hound-walker/n02089867_1295.jpg"
    ]
}


@pytest.fixture
def dog_random_image_from_breed_response():
    return {
    "status": "success",
    "message": "https://images.dog.ceo/breeds/hound-basset/n02088238_12196.jpg"
}


@pytest.fixture
def dog_all_images_from_breed_response():
    return {
    "status": "success",
    "message": [
        "https://images.dog.ceo/breeds/maltese/n02085936_9742.jpg",
        "https://images.dog.ceo/breeds/dingo/n02115641_7119.jpg",
    ]
}


@pytest.fixture
def dog_multiply_random_image_response():
    return {
    "status": "success",
    "message": [
        "https://images.dog.ceo/breeds/maltese/n02085936_9742.jpg",
        "https://images.dog.ceo/breeds/dingo/n02115641_7119.jpg",
        "https://images.dog.ceo/breeds/malinois/n02105162_5328.jpg"
    ]
}


@pytest.fixture
def dog_random_image_response():
    return {
    "status": "success",
    "message": "https://images.dog.ceo/breeds/brabancon/n02112706_1041.jpg"
}


@pytest.fixture
def dog_list_all_breeds_response():
    return {
    "status": "success",
    "message": {
        "affenpinscher": [],
        "african": [],
        "airedale": [],
        "akita": [],
        "appenzeller": [],
        "basenji": [],
        "beagle": [],
        "bluetick": [],
        "borzoi": [],
        "bouvier": [],
        "boxer": [],
        "brabancon": [],
        "briard": [],
        "bulldog": [
            "boston",
            "english",
            "french"
        ],
        "bullterrier": [
            "staffordshire"
        ],
        "cairn": [],
        "cattledog": [
            "australian"
        ],
        "chihuahua": [],
        "chow": [],
        "clumber": [],
        "cockapoo": [],
        "collie": [
            "border"
        ],
        "coonhound": [],
        "corgi": [
            "cardigan"
        ],
        "cotondetulear": [],
        "dachshund": [],
        "dalmatian": [],
        "dane": [
            "great"
        ],
        "deerhound": [
            "scottish"
        ],
        "dhole": [],
        "dingo": [],
        "doberman": [],
        "elkhound": [
            "norwegian"
        ],
        "entlebucher": [],
        "eskimo": [],
        "frise": [
            "bichon"
        ],
        "germanshepherd": [],
        "greyhound": [
            "italian"
        ],
        "groenendael": [],
        "hound": [
            "afghan",
            "basset",
            "blood",
            "english",
            "ibizan",
            "walker"
        ],
        "husky": [],
        "keeshond": [],
        "kelpie": [],
        "komondor": [],
        "kuvasz": [],
        "labrador": [],
        "leonberg": [],
        "lhasa": [],
        "malamute": [],
        "malinois": [],
        "maltese": [],
        "mastiff": [
            "bull",
            "english",
            "tibetan"
        ],
        "mexicanhairless": [],
        "mix": [],
        "mountain": [
            "bernese",
            "swiss"
        ],
        "newfoundland": [],
        "otterhound": [],
        "papillon": [],
        "pekinese": [],
        "pembroke": [],
        "pinscher": [
            "miniature"
        ],
        "pointer": [
            "german",
            "germanlonghair"
        ],
        "pomeranian": [],
        "poodle": [
            "miniature",
            "standard",
            "toy"
        ],
        "pug": [],
        "puggle": [],
        "pyrenees": [],
        "redbone": [],
        "retriever": [
            "chesapeake",
            "curly",
            "flatcoated",
            "golden"
        ],
        "ridgeback": [
            "rhodesian"
        ],
        "rottweiler": [],
        "saluki": [],
        "samoyed": [],
        "schipperke": [],
        "schnauzer": [
            "giant",
            "miniature"
        ],
        "setter": [
            "english",
            "gordon",
            "irish"
        ],
        "sheepdog": [
            "english",
            "shetland"
        ],
        "shiba": [],
        "shihtzu": [],
        "spaniel": [
            "blenheim",
            "brittany",
            "cocker",
            "irish",
            "japanese",
            "sussex",
            "welsh"
        ],
        "springer": [
            "english"
        ],
        "stbernard": [],
        "terrier": [
            "american",
            "australian",
            "bedlington",
            "border",
            "dandie",
            "fox",
            "irish",
            "kerryblue",
            "lakeland",
            "norfolk",
            "norwich",
            "patterdale",
            "russell",
            "scottish",
            "sealyham",
            "silky",
            "tibetan",
            "toy",
            "westhighland",
            "wheaten",
            "yorkshire"
        ],
        "vizsla": [],
        "weimaraner": [],
        "whippet": [],
        "wolfhound": [
            "irish"
        ]
    }
}


@pytest.fixture
def brewery_id():
    return 300


@pytest.fixture
def brewery_state():
    return "California"

@pytest.fixture
def brewery_name():
    return "Alosta Brewing Co"


@pytest.fixture
def brewery_text_in_name():
    return "dog"


@pytest.fixture
def brewery_text_in_tag():
    return "patio"


@pytest.fixture
def brewery_type():
    return "micro"


@pytest.fixture
def brew_get_brewery(brewery_id):
    return '/breweries/{}'.format(brewery_id)


@pytest.fixture
def brew_filter_by_state(brewery_state):
    return '/breweries?by_state={}'.format(brewery_state)


@pytest.fixture
def brew_filter_by_state(brewery_state):
    return '/breweries?by_state={}'.format(brewery_state)


@pytest.fixture
def brew_filter_by_name(brewery_name):
    return '/breweries?by_name={}'.format(brewery_name)


@pytest.fixture
def brew_autocomplete_name(brewery_text_in_name):
    return '/breweries/autocomplete?query={}'.format(brewery_text_in_name)


@pytest.fixture
def brew_search_tag(brewery_text_in_tag):
    return '/breweries?by_tag={}'.format(brewery_text_in_tag)


@pytest.fixture
def brew_filter_by_type(brewery_type):
    return '/breweries?by_type={}'.format(brewery_type)


@pytest.fixture
def brew_get_brewery_response():
    return {
  "id": 300,
  "name": "Alosta Brewing Co",
  "brewery_type": "micro",
  "street": "692 Arrow Grand Cir",
  "city": "Covina",
  "state": "California",
  "postal_code": "91722-2122",
  "country": "United States",
  "longitude": "-117.878146550423",
  "latitude": "34.1036502643654",
  "phone": "9094558707",
  "website_url": "http://www.alostabrewing.com",
  "updated_at": "2018-08-23T23:24:12.610Z",
  "tag_list": []
}


@pytest.fixture
def cdnjs_name():
    return "jQuery-slimScroll"


@pytest.fixture
def cdnjs_return_all_libraries():
    return '/libraries'


@pytest.fixture
def cdnjs_return_library_by_name_full(cdnjs_name):
    return '/libraries/{}'.format(cdnjs_name)


@pytest.fixture
def cdnjs_return_library_by_name_specified(cdnjs_name):
    return '/libraries/{}?fields=name,filename,version'.format(cdnjs_name)


@pytest.fixture
def cdnjs_return_libraries_human_output():
    return '/libraries?output=human'


@pytest.fixture
def cdnjs_search_libraries_by_name(cdnjs_name):
    return '/libraries?search={}'.format(cdnjs_name)


@pytest.fixture
def cdnjs_return_library_by_name_full_response():
    return {
      "name": "jQuery-slimScroll",
      "latest": "https://cdnjs.cloudflare.com/ajax/libs/jQuery-slimScroll/1.3.8/jquery.slimscroll.min.js",
      "version": "1.3.8",
      "description": "slimScroll is a small jQuery plugin that transforms any div into a scrollable area. slimScroll "
                     "doesn't occupy any visual space as it only appears on a user initiated mouse-over."
    }


@pytest.fixture
def cdnjs_return_library_by_name_specified_response():
    return {
  "name": "jQuery-slimScroll",
  "filename": "jquery.slimscroll.min.js",
  "version": "1.3.8"
}