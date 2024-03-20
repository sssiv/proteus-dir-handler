import os

def define_root():
    if os.name == "nt":
        return "..\\ProteusTestCaseGen"
    else:
        return "../ProteusTestCaseGen"
    
ROOT = define_root()
SAVED = "Saved"
LOGS = "Logs"
SAVED_TESTS = "SavedSessions"
SESSIONS = "TestingSession"
FAIL = "Failures"
SUCCESS = "Successes"
GENERATED = "GemeratedTests"