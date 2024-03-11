import os
import shutil
from paths import *

class Delete():
    @staticmethod
    def clear_folder(folder):
        for file in os.listdir(folder):
            path = os.path.join(folder, file)

            try:
                if os.path.isfile(path) or os.path.islink(path):
                    os.unlink(path)
                elif os.path.isdir(path):
                    shutil.rmtree(path)

            except Exception as e:
                print(f"Failed to delete {path} because {e}\n")
    
    del_successes = staticmethod(lambda: Delete.clear_folder(os.path.join(ROOT, SESSIONS, "Successes")))
    del_failures = staticmethod(lambda: Delete.clear_folder(os.path.join(ROOT, SESSIONS, "Failures")))
    del_tests = staticmethod(lambda: Delete.clear_folder(os.path.join(ROOT, SESSIONS, "GeneratedTests")))
    del_logs = staticmethod(lambda: Delete.clear_folder(os.path.join(ROOT, SAVED, "Logs")))
    del_sessions = staticmethod(lambda: Delete.clear_folder(os.path.join(ROOT, SAVED, "SavedSessions")))

    @staticmethod
    def new_session():
        Delete.del_successes()
        Delete.del_failures()
        Delete.del_tests()
    
    @staticmethod
    def clear_all():
        Delete.new_session()
        Delete.del_logs()
        Delete.del_sessions()

Delete.clear_all()