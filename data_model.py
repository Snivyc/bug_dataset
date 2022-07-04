import copy
import json
import os
import re
import subprocess
from pathlib import Path
from typing import List, Dict, Tuple, Set

class Bug:
    def __init__(self):
        pass


class FunctionContainer:
    def __init__(self):
        pass


class FileContainer:
    def __init__(self):
        pass


class ProjectSnapshotContainer:
    def __init__(self):
        pass

    def get_all_bug_functions(self):
        return self.bug_func_lst

    def __iter__(self):
        for file_container in self.file_lst:
            for function_container in file_container.function_lst:
                yield (file_container, function_container)
