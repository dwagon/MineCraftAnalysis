#!/usr/bin/env python

from volume import Volume

for h in (2, 3, 4):
    for x in range(6):
        v = Volume(100)
        for i in range(100):
            for j in range(h):
                v.clear((i, 50+j, 50))
            for sb in range(-x, x+1):
                v.clear((i, 51, 50+sb))
        print("%d height tunnel with %d continuous side block=%s (Digs %d See %d)" % (h, x, v.score(), v.digs, v.getVisible()))
    print()

    for x in range(6):
        v = Volume(100)
        for i in range(100):
            for j in range(h):
                v.clear((i, 50+j, 50))
            if i % 2 == 0:
                for sb in range(-x, x+1):
                    v.clear((i, 51, 50+sb))
        print("%d height tunnel with %d alternating side block=%s (Digs %d See %d)" % (h, x, v.score(), v.digs, v.getVisible()))
    print()

    for x in range(6):
        v = Volume(100)
        for i in range(100):
            for j in range(h):
                v.clear((i, 50+j, 50))
            if i % 3 == 0:
                for sb in range(-x, x+1):
                    v.clear((i, 51, 50+sb))
        print("%d height tunnel with %d every third side block=%s (Digs %d See %d)" % (h, x, v.score(), v.digs, v.getVisible()))
    print()

# EOF
