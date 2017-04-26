import numexpr as ne
loops = 25000000
a = range(1, loops)
ne.set_num_threads(1)
f = '3 * log(a) +cos(a) ** 2'
ne.evaluate(f)
