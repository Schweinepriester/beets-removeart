import os
from beets.plugins import BeetsPlugin

class RemoveArt(BeetsPlugin):
    def __init__(self):
        super(RemoveArt, self).__init__()
        self.register_listener('album_imported', self.removeart)

    def removeart(library, album):
        # self._log.info(u'Going to delete {0.artpath}', album) # TODO
        # print album.artpath # TODO
        os.remove(album.artpath)
