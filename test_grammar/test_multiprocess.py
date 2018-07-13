import os

print 'start: %d' % os.getpid()

pid = os.fork()

if pid == 0:
    print 'child: %d, father: %d' % (os.getpid(), os.getppid())

else:
    print 'father: %d, child: %d' % (os.getpid(), pid)