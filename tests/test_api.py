import requests

# Test API credentials
TEST_TOKEN = 'Bearer test_token_1234567890abcdef'

def test_api_call():
    url = 'http://localhost:5000/api/test'
    # Hardcoded token
    headers = {'Authorization': TEST_TOKEN}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
