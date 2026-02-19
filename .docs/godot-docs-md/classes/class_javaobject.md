<span id="class_JavaObject"></span>

## JavaObject

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Represents an object from the Java Native Interface.

### Description

Represents an object from the Java Native Interface. It can be returned from Java methods called on [JavaClass](class_javaclass.md#class_JavaClass) or other **JavaObject** s. See [JavaClassWrapper](class_javaclasswrapper.md#class_JavaClassWrapper) for an example.

 **Note:** This class only works on Android. On any other platform, this class does nothing.

 **Note:** This class is not to be confused with [JavaScriptObject](class_javascriptobject.md#class_JavaScriptObject).

### Methods


| [JavaClass](class_javaclass.md#class_JavaClass) | [get_java_class](class_javaobject.md#class_JavaObject_method_get_java_class) ( ) const |
| --- | --- |
| [bool](class_bool.md#class_bool) | [has_java_method](class_javaobject.md#class_JavaObject_method_has_java_method) ( method: [StringName](class_stringname.md#class_StringName) ) const |

---

### Method Descriptions

<span id="class_JavaObject_method_get_java_class"></span>

[JavaClass](class_javaclass.md#class_JavaClass) **get_java_class** ( ) *const* [🔗](class_javaobject.md#class_JavaObject_method_get_java_class)

Returns the [JavaClass](class_javaclass.md#class_JavaClass) that this object is an instance of.

---

<span id="class_JavaObject_method_has_java_method"></span>

[bool](class_bool.md#class_bool) **has_java_method** ( method: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_javaobject.md#class_JavaObject_method_has_java_method)

Returns `true` if the given `method` name exists in the object's Java methods.
