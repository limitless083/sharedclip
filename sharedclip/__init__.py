"""
Sharedclip
A cross-platform shared clipboard application for Python. (only handles plain text for now)
By Victor bgk@126.com
BSD License
Usage:
  1. start server_daemon and assign a port on a computer A(IP 10.106.128.163): python server_daemon.py 9999
  2. start client_daemon and assign a remote host, port on computer B: python client_daemon.py 10.106.128.163 9999
  3. when B's clipboard changes, A's changes the same in time

On Windows, no additional modules are needed.
On Mac, the application uses pbcopy and pbpaste, which should come with the os.
On Linux, install xclip or xsel via package manager. For example, in CentOS:
sudo yum install xclip
Otherwise on Linux, you will need the gtk or PyQt4 modules installed.
gtk and PyQt4 modules are not available for Python 3,
and this application does not work with PyGObject yet.
"""

_version__ = '0.0.1'