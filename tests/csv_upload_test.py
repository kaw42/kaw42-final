import logging
import os

def upload_song_csv_test (client, application):
    application.app_context()
    application.secret_key = "this is a testing secret key"
    application.config['WTF_CSRF_ENABLED'] = False
    response = client.post('/login', data=dict(email="kaw42@njit.edu", password="abc123"),
                                follow_redirects=True)
    assert response.status_code == 200

    songs = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "music.csv"))
    csv_data = open(songs, "rb")
    data = {"file": (csv_data, "music.csv")}
    response = client.post('/songs/upload', data=data, follow_redirects=True, buffered=True,
                                content_type='multipart/form-data')
    assert response.status_code == 200
    response = client.get("/songs")
    assert response.status_code == 200

    assert os.path.exists(
        os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'uploads', 'music.csv'))) == True
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200


