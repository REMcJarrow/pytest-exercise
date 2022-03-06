#import pytest
import requests

# Here are expected given variables in the global frame, so they can be interchanged and used for other ID's to try and create a flexible enviroment.

expectedContentType = "application/json; charset=utf-8"
expectedStatusCode = 200
expectedServer = "GitHub.com"
expectedName = "Gregory Loscombe"
expectedID = 15330
expectedLocation = "Manchester"
expectedDate = "2008-06-27T23:29:00Z"
################### From what I understand the following values are subject to change in increasing/decreasing values therefore testing these cases may not be very effective or necessary.
expectedPubRepos = 7
expectedPubGists = 11
expectedFollowers = 12
expectedFollowing = 29


#Define the get request and r_body in global frame to avoid unecessary and repetitive lines 
r = requests.get("https://api.github.com/users/6wl", allow_redirects=False)
r_body = r.json()

class Test_header:
    def test_status_code(self):
        assert r.status_code == expectedStatusCode

    def test_content_type(self):
        assert r.headers["Content-Type"] == expectedContentType

    def test_server(self):
        assert r.headers["server"] == expectedServer




class Test_response_body:                    #tests for given response encompassed in one test class

    def test_name(self):
        assert r_body["name"] == expectedName

    def test_id(self):
        assert r_body["id"] == expectedID
    
    def test_location(self):
        assert r_body["location"] == expectedLocation

    def test_public_repos(self):
        assert r_body["public_repos"] == expectedPubRepos

    def test_public_gists(self):
        assert r_body["public_gists"] == expectedPubGists

    def test_followers(self):
        assert r_body["followers"] == expectedFollowers

    def test_following(self):
        assert r_body["following"] == expectedFollowing
    
    def test_date_created(self):
        assert r_body["created_at"] == expectedDate
   

   ###################################################