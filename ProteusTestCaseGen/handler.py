import os
import shutil
from paths import *

def move_file(file_path, target_folders):
    full_target_path = [ROOT] + target_folders
    target_path = os.path.join(*full_target_path)
    os.makedirs(target_path, exist_ok=True)
    target_file_path = os.path.join(target_path, os.path.basename(file_path))
    shutil.move(file_path, target_file_path)

# Example usage
move_file(ROOT + '/test.txt', [SAVED, 'Logs'])
