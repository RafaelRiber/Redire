from amaranth                    import *
from amaranth.build              import *
from amaranth.lib                import wiring
from amaranth.vendor             import LatticeECP5Platform
from amaranth_boards.resources   import *

__all__ = ["RedirePlatform"]

class RedirePlatform(LatticeECP5Platform):
    device = "LFE5U-45F"
    speed  = "7"
    default_clk = "clk"
    resources = [
        Resource("clk", 0, Pins("A9", dir="i"), Clock(48e6), Attrs(IO_TYPE="LVCMOS33")),
    ]
