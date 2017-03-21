# sharedclip
an application to share the clipboard from one computer with another computer in time

Example Usage
=============
 1. start server_daemon and assign a port on a computer A(IP 10.106.128.163):

    `python server_daemon.py 9999`
    
    if there are some errors, you can set clipboard type at the end of command like this:
   
    `python server_daemon.py 9999 xsel`

 2. start client_daemon and assign a remote host, port on computer B:

    `python client_daemon.py 10.106.128.163 9999`
    
    if there are some errors, you can set clipboard type at the end of command like this:
   
    `python client_daemon.py 10.106.128.163 9999 xsel`

 3. when B's clipboard changes, A's changes the same in time. For example, if we copy something like "Hello world" with `Ctrl+C` on B, then we can use `Ctrl+V` to get text from clipboard on A.


Currently only handles plaintext.

On Windows, no additional modules are needed.

On Mac, this application makes use of the `pbcopy` and `pbpaste` commands, which should come with the os.

On Linux, this application makes use of the `xclip` or `xsel`commands, which should come with the os. Otherwise run `sudo yum install xclip` or `sudo yum install xsel`

Otherwise on Linux, you will need the gtk or PyQt4 modules installed.