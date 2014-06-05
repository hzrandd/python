
import memcache

#10.162.160.13:11211
mc=memcache.Client(['10.162.160.13:11211'],debug=0)
import ipdb; ipdb.set_trace() ### XXX BREAKPOINT
mc.set("234444444","rrrrrrrrrrr")
value=mc.get("234444444")
mc.set("dddd",3)
# mc.delete("dddd")
mc.set("dddd","3")
mc.incr("dddd")
print mc.get("dddd")
mc.decr("dddd", 10)
print mc.get("dddd")
notset_keys = mc.set_multi({'key1' : 'val1', 'key2' : 'val2'}, key_prefix='subspace_')
print mc.get_multi({"subspace_key1": "vall", "subspace_key2": "val2"})
