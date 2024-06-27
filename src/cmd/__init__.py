import os
import sys

### Allow dynamic import resolution from generated pt backend
# Get the absolute path to src/internal/api/
module_path = os.path.abspath(os.path.join('src', 'internal', 'api'))
# Add this path to sys.path if it's not already there
if module_path not in sys.path:
    sys.path.append(module_path)