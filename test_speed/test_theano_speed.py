import theano
import theano.tensor as T

x = T.vector('x', dtype='float32')
y = T.matrix('y', dtype='float32')

f = theano.function([x, y], T.dot(x, y))