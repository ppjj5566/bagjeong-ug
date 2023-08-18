import wifi
import time
import kinematic.body_forward_kinematic as body_forward_kinematic
from websocketService.ws_connection import ClientClosedError
from websocketService.ws_server import WebSocketServer, WebSocketClient

deadline = time.ticks_add(time.ticks_ms(), 100)
forward_kinematics_leg = body_forward_kinematic.BodyForwardKinematic(0)

class TestClient(WebSocketClient):
    def __init__(self, conn):
        super().__init__(conn)

    def process(self):
        try:
            msg = self.connection.read()
            if not msg:
                return
            msg = msg.decode("utf-8")
            msg = str(msg).split(" ")
            deadline = time.ticks_add(time.ticks_ms(), 300)
            #print(float(msg[0]), float(msg[1]), int(msg[2]))
            forward_kinematics_leg.leg_movement(round(float(msg[0]), 2), round(float(msg[1]), 2))
            #print(msg[0], msg[1], msg[2], msg[3])
        except ClientClosedError:
            print("Connection close error")
            self.connection.close()
            
        except Exception as e:
            print("exception:" + str(e) + "\n")
            pass


class TestServer(WebSocketServer):
    def __init__(self):
        super().__init__("webpage/index.html", 50)
 
    def _make_client(self, conn):
        return TestClient(conn)


wifi.run()
server = TestServer()
server.start()

while True:
    server.process_all()
    if time.ticks_diff(deadline, time.ticks_ms()) < 0:
        forward_kinematics_leg.leg_movement(0,0)
        deadline = time.ticks_add(time.ticks_ms(), 10000)

server.stop()