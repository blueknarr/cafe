def test_메인_페이지(client):
    response = client.get('/')
    assert response.status_code == 200