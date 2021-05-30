from unittest.mock import Mock

REQUESTS = Mock()
REQUESTS.ok = True
SAMPLE = {
    'status': 'success'
}


def mock_all_breeds():
    REQUESTS.json.return_value = SAMPLE
    return REQUESTS


def mock_breed_random_image():
    SAMPLE['message'] = 'image.jpg'
    REQUESTS.json.return_value = SAMPLE
    return REQUESTS


def mock_breed_multiple_random_images(img_count):
    if img_count == 3:
        SAMPLE['message'] = ['testimage.jpg', 'testimage2.jpg', 'testimage3.jpg']
        REQUESTS.json.return_value = SAMPLE
    elif img_count == 4:
        SAMPLE['message'] = ['image.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg']
        REQUESTS.json.return_value = SAMPLE
    elif img_count == 5:
        SAMPLE['message'] = ['image.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg', 'image5.jpg']
        REQUESTS.json.return_value = SAMPLE
    return REQUESTS


def mock_sub_breed():
    SAMPLE['message'] = ["afghan", "basset", "blood", "english", "ibizan", "plott", "walker"]
    REQUESTS.json.return_value = SAMPLE
    return REQUESTS
