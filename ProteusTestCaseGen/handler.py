import os
import shutil
from paths import *
from delete import Delete
from fail_case_gen import generate_fail_case

'''
Useless fucntion I made, GG
def move_file(file_path, target_folders):
    full_target_path = [ROOT] + target_folders
    target_path = os.path.join(*full_target_path)
    os.makedirs(target_path, exist_ok=True)
    target_file_path = os.path.join(target_path, os.path.basename(file_path))
    shutil.move(file_path, target_file_path)

# Example usage
move_file(ROOT + '/test.txt', [SAVED, 'Logs'])
'''

skill_issues = input("How many skill issue cases do you want? ")
Delete.new_session()
for i in range(int(skill_issues)):
   with open(os.path.join(ROOT, SESSIONS, FAIL, f"fail_case_{i}.txt"),"w") as file:
      file.write(generate_fail_case())
