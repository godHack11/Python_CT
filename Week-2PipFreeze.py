# pip freeze
# For mac - python -m pip freeze

# Options
# -r, --requirement <file>
# Use the order in the given requirements file and its comments when generating output. This option can be used multiple times.

# (environment variable: PIP_REQUIREMENT)

# -l, --local
# If in a virtualenv that has global access, do not output globally-installed packages.

# (environment variable: PIP_LOCAL)

# --user
# Only output packages installed in user-site.

# (environment variable: PIP_USER)

# --path <path>
# Restrict to the specified installation path for listing packages (can be used multiple times).

# (environment variable: PIP_PATH)

# --all
# Do not skip these packages in the output: setuptools, pip, wheel, distribute

# (environment variable: PIP_ALL)

# --exclude-editable
# Exclude editable package from output.

# (environment variable: PIP_EXCLUDE_EDITABLE)

# --exclude <package>
# Exclude specified package from the output

# (environment variable: PIP_EXCLUDE)

# Fixing “Permission denied:” errors
# The purpose of this section of documentation is to provide practical suggestions to users seeing a “Permission denied” error on pip freeze.

# This error occurs, for instance, when the command is installed only for another user, and the current user doesn’t have the permission to execute the other user’s command.

# To solve that issue, you can try one of the following:

# Install the command for yourself (e.g. in your home directory).
# Ask the system admin to allow this command for all users.
# Check and correct the PATH variable of your own environment.
# Check the ACL (Access-Control List) for this command.
