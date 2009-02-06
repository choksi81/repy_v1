include tcp.repy

if callfunc == 'initialize':
  IP = getmyip()
  PORT = 12345
  MESSAGE = "hi"
  MAXLEN = 4096

  socket = TcpStateMachine()

def server():
  (ip, port) = socket.listen()

if callfunc == 'initialize':
  # fork thread for server
  settimer(0, server, ())
  sleep(.01)
  # raise already connected error
  try:
    socket.connect(IP, PORT, IP, PORT)
  except AlreadyConnectedError:
    raise # great passes test
  else:
    print "should have raised already connected"
 
  exitall()