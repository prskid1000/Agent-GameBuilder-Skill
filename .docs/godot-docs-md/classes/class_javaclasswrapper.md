<span id="class_JavaClassWrapper"></span>

## JavaClassWrapper

**Inherits:** [Object](class_object.md#class_Object)

Provides access to the Java Native Interface.

### Description

The JavaClassWrapper singleton provides a way for the Godot application to send and receive data through the Java Native Interface (JNI).

 **Note:** This singleton is only available in Android builds.

::

    var LocalDateTime = JavaClassWrapper.wrap("java.time.LocalDateTime")
    var DateTimeFormatter = JavaClassWrapper.wrap("java.time.format.DateTimeFormatter")

    var datetime = LocalDateTime.now()
    var formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss")

    print(datetime.format(formatter))

 **Warning:** When calling Java methods, be sure to check [get_exception()](class_javaclasswrapper.md#class_JavaClassWrapper_method_get_exception) to check if the method threw an exception.

### Tutorials

- [Integrating with Android APIs](../tutorials/platform/android/javaclasswrapper_and_androidruntimeplugin.md)

### Methods


| [JavaObject](class_javaobject.md#class_JavaObject) | [get_exception](class_javaclasswrapper.md#class_JavaClassWrapper_method_get_exception) ( ) |
| --- | --- |
| [JavaClass](class_javaclass.md#class_JavaClass) | [wrap](class_javaclasswrapper.md#class_JavaClassWrapper_method_wrap) ( name: [String](class_string.md#class_String) ) |

---

### Method Descriptions

<span id="class_JavaClassWrapper_method_get_exception"></span>

[JavaObject](class_javaobject.md#class_JavaObject) **get_exception** ( ) [🔗](class_javaclasswrapper.md#class_JavaClassWrapper_method_get_exception)

Returns the Java exception from the last call into a Java class. If there was no exception, it will return `null`.

 **Note:** This method only works on Android. On every other platform, this method will always return `null`.

---

<span id="class_JavaClassWrapper_method_wrap"></span>

[JavaClass](class_javaclass.md#class_JavaClass) **wrap** ( name: [String](class_string.md#class_String) ) [🔗](class_javaclasswrapper.md#class_JavaClassWrapper_method_wrap)

Wraps a class defined in Java, and returns it as a [JavaClass](class_javaclass.md#class_JavaClass) [Object](class_object.md#class_Object) type that Godot can interact with.

When wrapping inner (nested) classes, use `$` instead of `.` to separate them. For example, `JavaClassWrapper.wrap("android.view.WindowManager$LayoutParams")` wraps the **WindowManager.LayoutParams** class.

 **Note:** To invoke a constructor, call a method with the same name as the class. For example:

::

    var Intent = JavaClassWrapper.wrap("android.content.Intent")
    var intent = Intent.Intent()

 **Note:** This method only works on Android. On every other platform, this method does nothing and returns an empty [JavaClass](class_javaclass.md#class_JavaClass).
