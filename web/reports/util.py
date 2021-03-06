def model_unicode(instance, fields):
    vals = [getattr(instance, x) for x in fields]

    def force_unicode(s):
        if isinstance(s, str):
            return s.decode('utf-8') 
        return unicode(s)

    return u'{}({})'.format(
        instance.__class__.__name__,
        u', '.join([force_unicode(v) for v in vals])
    )



class IndexableQuery(object):
    def __init__(self, count, query):
        self.count = count
        self.query = query


    def __getitem__(self, i):
        return self[i:i+1]


    def __getslice__(self, i, j): 
        return self.query(i, j - i + 1)


    def __len__(self):
        return self.count
