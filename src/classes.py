class obj:
    id = 0
    def __init__(self, s, t=None, new=None):
        if new is None:
            def new(self, *args):
                obj.id += 1
                i = {'a': s, 'id': obj.id}
                i.update(t.__dict__)
                t.new(i, *args)
                return i
        t = type(s, (object,), {})
        t.__call__ = new
        self.t = t
        
NUM, SYM, ROW, COLS, DATA = (obj(name) for name in ["NUM", "SYM", "ROW", "COLS", "DATA"])
