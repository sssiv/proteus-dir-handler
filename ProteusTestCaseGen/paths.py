import os

def define_root():
    if os.name == "nt":
        return "..\\ProteusTestCaseGen"
    else:
        return "../ProteusTestCaseGen"
    
ROOT = define_root()
SAVED = "Saved"
SESSIONS = "TestingSession"