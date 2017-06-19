# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_blob', [dirname(__file__)])
        except ImportError:
            import _blob
            return _blob
        if fp is not None:
            try:
                _mod = imp.load_module('_blob', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _blob = swig_import_helper()
    del swig_import_helper
else:
    import _blob
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


MAXDEPTH = _blob.MAXDEPTH
class Device(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Device, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Device, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _blob.new_Device(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _blob.delete_Device
    __del__ = lambda self : None;
    def initialize(self, *args): return _blob.Device_initialize(self, *args)
    def getRGB(self): return _blob.Device_getRGB(self)
    def setRGB(self, *args): return _blob.Device_setRGB(self, *args)
    def getWidth(self): return _blob.Device_getWidth(self)
    def getHeight(self): return _blob.Device_getHeight(self)
    def getDepth(self): return _blob.Device_getDepth(self)
    def getImage(self): return _blob.Device_getImage(self)
    def getByte(self, *args): return _blob.Device_getByte(self, *args)
Device_swigregister = _blob.Device_swigregister
Device_swigregister(Device)

class Blob(Device):
    __swig_setmethods__ = {}
    for _s in [Device]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Blob, name, value)
    __swig_getmethods__ = {}
    for _s in [Device]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Blob, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _blob.new_Blob(*args)
        try: self.this.append(this)
        except: self.this = this
    def clear(self): return _blob.Blob_clear(self)
    def updateMMap(self, *args): return _blob.Blob_updateMMap(self, *args)
    def drawRect(self, *args): return _blob.Blob_drawRect(self, *args)
    __swig_destroy__ = _blob.delete_Blob
    __del__ = lambda self : None;
Blob_swigregister = _blob.Blob_swigregister
Blob_swigregister(Blob)


