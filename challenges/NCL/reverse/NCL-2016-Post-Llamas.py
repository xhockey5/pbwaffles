import sys
sys.setrecursionlimit(1500)

(lambda __g, __print, __y: [[(lambda __after: (__print('Usage: python {} <tid>'.format(sys.argv[0])), (exit(1), __after())[1])[1] if (len(sys.argv) != 2) else __after())(lambda: [[(lambda __after: (__print("That's the correct flag!"), __after())[1] if verify(key, tid) else (__print('Wrong flag.'), __after())[1])(lambda: None) for __g['key'] in [(raw_input('Enter your guess for the flag: '))]][0] for __g['tid'] in [(sys.argv[1])]][0]) for __g['verify'], verify.__name__ in [(lambda key, tid: (lambda __l: [(lambda __after: False if (len(__l['key']) != 13) else __after())(lambda: [[[(lambda __after, __sentinel, __items: __y(lambda __this: lambda: (lambda __i: [(lambda __after: False if (chr((ord(__l['val']) ^ __l['y'][__l['index']])) != 'A') else __after())(lambda: __this()) for (__l['index'], __l['val']) in [(__i)]][0] if __i is not __sentinel else __after())(next(__items, __sentinel)))())(lambda: (lambda __after: False if (not __l['last'].isdigit()) else __after())(lambda: [(lambda __after, __sentinel, __items: __y(lambda __this: lambda: (lambda __i: [(lambda __after, __sentinel, __items: __y(lambda __this: lambda: (lambda __i: [[__this() for __l['ct'] in [(((__l['ct'] + (ord(__l['c']) * __l['d'])) % 10000))]][0] for __l['d'] in [(__i)]][0] if __i is not __sentinel else __after())(next(__items, __sentinel)))())(lambda: __this(), [], iter(__l['y'])) for __l['c'] in [(__i)]][0] if __i is not __sentinel else __after())(next(__items, __sentinel)))())(lambda: (lambda __after: False if (__l['ct'] != int(__l['last'])) else __after())(lambda: True), [], iter(__l['tid'])) for __l['ct'] in [(__l['y'][0])]][0]), [], iter(enumerate(__l['first']))) for __l['y'] in [([15, 2, 13, 108, 17, 24, 17, 24, 108])]][0] for __l['last'] in [(__l['key'][-4:])]][0] for __l['first'] in [(__l['key'][:-4])]][0]) for __l['key'], __l['tid'] in [(key, tid)]][0])({}), 'verify')]][0] for __g['sys'] in [(__import__('sys', __g, __g))]][0])(globals(), __import__('__builtin__').__dict__['print'], (lambda f: (lambda x: x(x))(lambda y: f(lambda: y(y)()))))