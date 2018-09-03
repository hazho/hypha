import os

from django.core.files.base import File
from django.core.files.storage import default_storage
from django.core.serializers.json import DjangoJSONEncoder


class StreamFieldDataEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, StreamFieldFile):
            return {
                'path': o.name,
            }
        return super().default(o)


class StreamFieldFile(File):
    def __init__(self, *args, storage=default_storage, **kwargs):
        super().__init__(*args, **kwargs)
        self.storage = storage
        self._committed = True

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def _get_file(self):
        if getattr(self, '_file', None) is None:
            self._file = self.storage.open(self.name, 'rb')
        return self._file

    def _set_file(self, file):
        self._file = file

    def _del_file(self):
        del self._file

    file = property(_get_file, _set_file, _del_file)

    @property
    def path(self):
        return self.storage.path(self.name)

    @property
    def url(self):
        return self.storage.url(self.name)

    @property
    def size(self):
        if not self._committed:
            return self.file.size
        return self.storage.size(self.name)

    def open(self, mode='rb'):
        if getattr(self, '_file', None) is None:
            self.file = self.storage.open(self.name, mode)
        else:
            self.file.open(mode)
        return self
    # open() doesn't alter the file's contents, but it does reset the pointer
    open.alters_data = True

    def save(self, folder):
        file_path = os.path.join(folder, self.name)
        name = self.storage.generate_filename(file_path)
        self.name = self.storage.save(name, self.file)
        self._committed = True
    save.alters_data = True

    def delete(self, save=True):
        if not self:
            return
        # Only close the file if it's already open, which we know by the
        # presence of self._file
        if hasattr(self, '_file'):
            self.close()
            del self.file

        self.storage.delete(self.name)

        self.name = None
        self._committed = False

    delete.alters_data = True

    @property
    def closed(self):
        file = getattr(self, '_file', None)
        return file is None or file.closed

    def close(self):
        file = getattr(self, '_file', None)
        if file is not None:
            file.close()
