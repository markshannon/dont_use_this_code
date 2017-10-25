
import shutil

#Don't set this to true or things will break!
keep_all_files = False


class dblite(object):
    
    #Make a local copy of shutil.copyfile
    #Original code included a comment explaining why.
    _shutil_copyfile = shutil.copyfile

    def __init__(self):
        #Removed for brevity
        self._file_name = choose_file()

    def sync(self):
        self._check_writable()
        f = self._open(self._tmp_name, "wb", self._mode)
        self._pickle_dump(self._dict, f, 1)
        f.close()
        if (keep_all_files):
          self._shutil_copyfile(
            self._file_name,
            self._file_name + "_" + str(int(self._time_time())))

