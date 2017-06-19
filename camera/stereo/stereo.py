# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_stereo', [dirname(__file__)])
        except ImportError:
            import _stereo
            return _stereo
        if fp is not None:
            try:
                _mod = imp.load_module('_stereo', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _stereo = swig_import_helper()
    del swig_import_helper
else:
    import _stereo
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



_stereo.MAXDEPTH_swigconstant(_stereo)
MAXDEPTH = _stereo.MAXDEPTH
class Device(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Device, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Device, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _stereo.new_Device(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _stereo.delete_Device
    __del__ = lambda self: None

    def initialize(self, wi, he, de, r, g, b):
        return _stereo.Device_initialize(self, wi, he, de, r, g, b)

    def getRGB(self):
        return _stereo.Device_getRGB(self)

    def setRGB(self, r, g, b):
        return _stereo.Device_setRGB(self, r, g, b)

    def getWidth(self):
        return _stereo.Device_getWidth(self)

    def getHeight(self):
        return _stereo.Device_getHeight(self)

    def getDepth(self):
        return _stereo.Device_getDepth(self)

    def getImage(self):
        return _stereo.Device_getImage(self)

    def getByte(self, position):
        return _stereo.Device_getByte(self, position)
Device_swigregister = _stereo.Device_swigregister
Device_swigregister(Device)


_stereo.DEBUG_swigconstant(_stereo)
DEBUG = _stereo.DEBUG

_stereo.FIRST_MATCH_swigconstant(_stereo)
FIRST_MATCH = _stereo.FIRST_MATCH

_stereo.DEFAULT_COST_swigconstant(_stereo)
DEFAULT_COST = _stereo.DEFAULT_COST

_stereo.NO_IG_PEN_swigconstant(_stereo)
NO_IG_PEN = _stereo.NO_IG_PEN

_stereo.INF_swigconstant(_stereo)
INF = _stereo.INF

_stereo.DISCONTINUITY_swigconstant(_stereo)
DISCONTINUITY = _stereo.DISCONTINUITY

_stereo.NO_DISCONTINUITY_swigconstant(_stereo)
NO_DISCONTINUITY = _stereo.NO_DISCONTINUITY
class Stereo(Device):
    __swig_setmethods__ = {}
    for _s in [Device]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Stereo, name, value)
    __swig_getmethods__ = {}
    for _s in [Device]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Stereo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["leftimage"] = _stereo.Stereo_leftimage_set
    __swig_getmethods__["leftimage"] = _stereo.Stereo_leftimage_get
    if _newclass:
        leftimage = _swig_property(_stereo.Stereo_leftimage_get, _stereo.Stereo_leftimage_set)
    __swig_setmethods__["rightimage"] = _stereo.Stereo_rightimage_set
    __swig_getmethods__["rightimage"] = _stereo.Stereo_rightimage_get
    if _newclass:
        rightimage = _swig_property(_stereo.Stereo_rightimage_get, _stereo.Stereo_rightimage_set)
    __swig_setmethods__["leftwidth"] = _stereo.Stereo_leftwidth_set
    __swig_getmethods__["leftwidth"] = _stereo.Stereo_leftwidth_get
    if _newclass:
        leftwidth = _swig_property(_stereo.Stereo_leftwidth_get, _stereo.Stereo_leftwidth_set)
    __swig_setmethods__["leftheight"] = _stereo.Stereo_leftheight_set
    __swig_getmethods__["leftheight"] = _stereo.Stereo_leftheight_get
    if _newclass:
        leftheight = _swig_property(_stereo.Stereo_leftheight_get, _stereo.Stereo_leftheight_set)
    __swig_setmethods__["leftdepth"] = _stereo.Stereo_leftdepth_set
    __swig_getmethods__["leftdepth"] = _stereo.Stereo_leftdepth_get
    if _newclass:
        leftdepth = _swig_property(_stereo.Stereo_leftdepth_get, _stereo.Stereo_leftdepth_set)
    __swig_setmethods__["rightwidth"] = _stereo.Stereo_rightwidth_set
    __swig_getmethods__["rightwidth"] = _stereo.Stereo_rightwidth_get
    if _newclass:
        rightwidth = _swig_property(_stereo.Stereo_rightwidth_get, _stereo.Stereo_rightwidth_set)
    __swig_setmethods__["rightheight"] = _stereo.Stereo_rightheight_set
    __swig_getmethods__["rightheight"] = _stereo.Stereo_rightheight_get
    if _newclass:
        rightheight = _swig_property(_stereo.Stereo_rightheight_get, _stereo.Stereo_rightheight_set)
    __swig_setmethods__["rightdepth"] = _stereo.Stereo_rightdepth_set
    __swig_getmethods__["rightdepth"] = _stereo.Stereo_rightdepth_get
    if _newclass:
        rightdepth = _swig_property(_stereo.Stereo_rightdepth_get, _stereo.Stereo_rightdepth_set)

    def __init__(self, left, right):
        this = _stereo.new_Stereo(left, right)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def updateMMap(self):
        return _stereo.Stereo_updateMMap(self)
    __swig_destroy__ = _stereo.delete_Stereo
    __del__ = lambda self: None
Stereo_swigregister = _stereo.Stereo_swigregister
Stereo_swigregister(Stereo)

# This file is compatible with both classic and new-style classes.

