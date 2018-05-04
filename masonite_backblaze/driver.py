
from masonite.contracts.UploadContract import UploadContract
from masonite.drivers.BaseUploadDriver import BaseUploadDriver

from .integration import B2Session


class UploadBackblazeDriver(BaseUploadDriver, UploadContract):
    """
    Backblaze B2 Upload Driver
    """

    def __init__(self, UploadManager, StorageConfig):
        self.upload = UploadManager
        self.config = StorageConfig

    def store(self, fileitem, location=None):
        file_location = self.upload.driver('disk').store(fileitem)

        # Check if is a valid extension
        self.validate_extension(fileitem.filename)

        session = B2Session(
            self.config.DRIVERS['backblaze']['account_id'],
            self.config.DRIVERS['backblaze']['application_id']
        )

        return session.upload_file(
            file_location,
            self.config.DRIVERS['backblaze']['bucket_id'],
            fileitem.filename
        )

    def store_prepend(self, fileitem, prepend, location=None):
        fileitem.filename = prepend + fileitem.filename

        return self.store(fileitem, location)
