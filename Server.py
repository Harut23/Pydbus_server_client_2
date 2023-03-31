import time
import random
from pydbus import SessionBus  # Session or System Bus
from gi.repository import GLib
from pydbus.generic import signal


bus = SessionBus()
BUS = "https://github.com/Harut23/SearchEngine2022"
loop = GLib.MainLoop()
INTERVAL = 2
message_count = 0



class DBusService_XML:  # method name="get_time_stamp"
    """
    DBus Service XML definition
    type = "i" for integer, "S" string, "d" double, "as" list of string data
    """
    dbus = """
    <node>
        <interface name= "{}">
            <method name="get_time_stamp">
                <arg type="d" name = "response" direction="out">
                </arg>
            </method>
        <interface>
    </node>
    """.format(BUS)


    def get_time_stamp(self):
        "Return a Unix time.Seconds since epoch."
        return time.time()



if __name__ == "__main__":
    bus.publish(BUS, DBusService_XML())

    loop.run()





