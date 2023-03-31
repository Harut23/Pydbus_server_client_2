import random

from pydbus import SessionBus
from gi.repository import GLib

bus = SessionBus()
BUS = "org.example.demo.test"
server_object = bus.get(BUS)
loop = GLib.MainLoop()
INTERVAL = 2



def make_method_call_client_2():
    "server returns a time stamp"
    # Server returns data..client sends no data
    reply = server_object.get_time_stamp()
    print("Returned data is of type: {}".format(type(reply)))
    print("Time stamp received from server: {}".format(reply))
    return True




if __name__ =="__main__":
    print("Starting Client Demo 1...")
    # call function to make a method call.

    #GLib to run repeating function every 2 secconds
    GLib.timeout_add_seconds(interval=INTERVAL,
                             function=make_method_call_client_2())
    loop.run()














