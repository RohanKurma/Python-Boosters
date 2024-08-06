class Song:
    """Class to represent a song

    Attributes:
        title(str): The title of the song
        artist (Artist): An artist object reperesnting the song creator.
        duration (int): The duration of song in seconds. May be zero

    """
    def __init__(self, title, artist, duration=0):
        """Song init method

        Args:
            title(str): Initializes the title attribute
            artist (Artist): At Artist object representing the song's creator.
            duration (Optional [int]): Initial value for the 'duration' attribute.
                Will be default to zero if not specified.
        """
        self.title = title
        self.artist = artist
        self.duration = duration