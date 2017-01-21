from functools import update_wrapper

# todo : find out what is returned by update_wrapper

def decorator(d):
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def memo(f):
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            return f(*args)
    return _f

# todo find out the callcounts actuall content

@decorator
def countcalls(f):
    def _f(*args):
        callcounts[_f] += 1
        return f(*args)
    callcounts[_f] = 0
    return _f

callcounts = {}


@countcalls
def fib(n): return 1 if n <= 1 else fib(n-1) + fib(n-2)


def test(f):
    @countcalls
    def _f(*args):
        return f(*args)
    return _f




