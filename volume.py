#!/opt/local/bin/python

class Volume(object):
    def __init__(self, size=10):
        self.size=size
        self.blocks=set()
        self.all=set()
        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    self.blocks.add((x,y,z))
                    self.all.add((x,y,z))
        self.digs=0

    def getSpace(self):
        """ Return the amount of empty bits
        """
        return len(self.all.difference(self.blocks))

    def getVolume(self):
        """ Return the amount of full bits
        """
        sum=0
        for x,y,z in self.all:
            if (x,y,z) in self.blocks:
                sum+=1
        return sum

    def whatCanISee(self, p):
        """ How many can block p see
        """
        see=set()
        for side in ((1,0,0),(-1,0,0),(0,0,1),(0,0,-1),(0,1,0),(0,-1,0)):
            np=(p[0]+side[0],p[1]+side[1],p[2]+side[2])
            if np in self.blocks:
                see.add(np)
        return see

    def clear(self,p):
        if p in self.blocks:
            self.digs+=1
            self.blocks.discard(p)
    
    def getVisible(self):
        """ Return the amount of bits that can be seen
        """
        vis=set()
        for x,y,z in self.all:
            if (x,y,z) not in self.blocks:
                newvis=self.whatCanISee((x,y,z))
                vis=vis.union(newvis)
        return len(vis)

    def score(self):
        return float(self.getVisible()+self.getSpace()) / self.getSpace()
        
if __name__=="__main__":
    v=Volume()
    v.clear((5,5,5))
    print "Space=%s" % v.getSpace()
    print "Volume=%s" % v.getVolume()
    print "What Can I See=%s" % v.whatCanISee((5,5,5))
    print "Visible=%s" % v.getVisible()
    print "Score=%s" % v.score()
    v.clear((5,6,5))
    print "Visible=%s after" % v.getVisible()
    print "Score=%s after" % v.score()

#EOF
