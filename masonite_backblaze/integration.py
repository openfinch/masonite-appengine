
import base64
import hashlib
import mimetypes
import os

import requests

package_directory = os.path.dirname(os.path.realpath(__file__))


class B2Session:
    base_url = "https://api.backblazeb2.com"
    url_prefix = "b2api/v1"

    def __init__(self, account_id, application_id):
        self.authentication_token = None
        self.api_url = None
        self.download_url = None

        # Authentication Essentials
        self._account_id = account_id
        self._application_id = application_id
        self._authorize_account()

    @property
    def basic_auth_string(self):
        auth_string = '{}:{}'.format(self._account_id, self._application_id)
        base_auth_string = 'Basic {}'.format(
            base64.b64encode(auth_string.encode('utf-8')).decode()
        )
        return base_auth_string

    @property
    def get_upload_url_endpoint(self):
        return '/'.join((self.api_url, self.url_prefix, 'b2_get_upload_url'))

    @property
    def get_auth_endpoint(self):
        return '/'.join((self.base_url, self.url_prefix, 'b2_authorize_account'))

    def upload_file(self, file_location, bucket_id, filename):
        upload_token, upload_url = self._get_upload_url(bucket_id)

        with open(file_location) as fp:
            content = fp.read()

        sha1_of_content = hashlib.sha1(content).hexdigest()

        content_type = mimetypes.guess_type(filename)[0] if not None else 'application/octet-stream'  # noqa

        headers = {
            'Authorization': upload_token,
            'X-Bz-File-Name': filename,
            'Content-Type': content_type,
            'X-Bz-Content-Sha1': sha1_of_content,
        }

        response = requests.post(upload_url, headers=headers, data=content)

        return response.json()['fileId']

    def _authorize_account(self):
        response = requests.get(self.get_auth_endpoint, headers={
            'Authorization': self.basic_auth_string
        })

        resp_data = response.json()
        self.auth_token = resp_data['authorizationToken']
        self.api_url = resp_data['apiUrl']
        self.download_url = resp_data['downloadUrl']

    def _get_upload_url(self, bucket_id):
        response = requests.get(self.get_upload_url_endpoint, headers={
            'Authorization': self.auth_token,
        }, data={
            'bucketId': bucket_id,
        })

        resp_data = response.json()
        return resp_data['authorizationToken'], resp_data['uploadUrl']
