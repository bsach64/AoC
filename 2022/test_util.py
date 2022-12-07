import util

def test__heapify():
    h = util.Heap([30, 60, 70, 10, 20, 40, 5])
    assert(h.items[0] == 5)
    h.pop()
    assert(h.items[0] == 10)
    h.push(1)
    assert(h.items[0] == 1)


test__heapify()
