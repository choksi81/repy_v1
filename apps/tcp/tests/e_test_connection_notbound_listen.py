include tcp.repy

if callfunc == 'initialize':
  IP = '127.0.0.1' #  getmyip()
  PORT = 12345
  MESSAGE = "hi"
  MAXLEN = 4096

  socket = Connection()

  # not bound error
  socket.listen()
  exitall()