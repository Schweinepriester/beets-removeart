from beets.plugins import BeetsPlugin

class RemoveArt(BeetsPlugin):
    def __init__(self):
        super(RemoveArt, self).__init__()
        self.register_listener('album_imported', self.removeart)

    def removeart(library, album):
        print album.art_destination # "Musik: {albumartist}  - {album} ({genre} - {year})".format(**album) # @ {bitrate} kBit/s