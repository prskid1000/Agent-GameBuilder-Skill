<span id="class_JavaClass"></span>

## JavaClass

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Represents a class from the Java Native Interface.

### Description

Represents a class from the Java Native Interface. It is returned from [JavaClassWrapper.wrap()](class_javaclasswrapper.md#class_JavaClassWrapper_method_wrap).

 **Note:** This class only works on Android. On any other platform, this class does nothing.

 **Note:** This class is not to be confused with [JavaScriptObject](class_javascriptobject.md#class_JavaScriptObject).

### Methods


| [String](class_string.md#class_String) | [get_java_class_name](class_javaclass.md#class_JavaClass_method_get_java_class_name) ( ) const |
| --- | --- |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [get_java_method_list](class_javaclass.md#class_JavaClass_method_get_java_method_list) ( ) const |
| [JavaClass](class_javaclass.md#class_JavaClass) | [get_java_parent_class](class_javaclass.md#class_JavaClass_method_get_java_parent_class) ( ) const |
| [bool](class_bool.md#class_bool) | [has_java_method](class_javaclass.md#class_JavaClass_method_has_java_method) ( method: [StringName](class_stringname.md#class_StringName) ) const |

---

### Method Descriptions

<span id="class_JavaClass_method_get_java_class_name"></span>

[String](class_string.md#class_String) **get_java_class_name** ( ) *const* [🔗](class_javaclass.md#class_JavaClass_method_get_java_class_name)

Returns the Java class name.

---

<span id="class_JavaClass_method_get_java_method_list"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **get_java_method_list** ( ) *const* [🔗](class_javaclass.md#class_JavaClass_method_get_java_method_list)

Returns the object's Java methods and their signatures as an [Array](class_array.md#class_Array) of dictionaries, in the same format as [Object.get_method_list()](class_object.md#class_Object_method_get_method_list).

---

<span id="class_JavaClass_method_get_java_parent_class"></span>

[JavaClass](class_javaclass.md#class_JavaClass) **get_java_parent_class** ( ) *const* [🔗](class_javaclass.md#class_JavaClass_method_get_java_parent_class)

Returns a **JavaClass** representing the Java parent class of this class.

---

<span id="class_JavaClass_method_has_java_method"></span>

[bool](class_bool.md#class_bool) **has_java_method** ( method: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_javaclass.md#class_JavaClass_method_has_java_method)

Returns `true` if the given `method` name exists in the object's Java methods.
