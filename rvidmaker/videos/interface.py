"""Provides an interface for references to remote videos"""

class VideoRef:
    """References a remote video"""

    def download(self, output_path):
        """
        Downloads the referenced video.

        Args:
            output_path (str): Path to write the video to.
        """
        raise NotImplementedError

    def get_title(self):
        """
        Returns:
            (str): The title of the video.
        """
        raise NotImplementedError

    def get_author(self):
        """
        Returns:
            (str) The author of the video.
        """
        raise NotImplementedError
