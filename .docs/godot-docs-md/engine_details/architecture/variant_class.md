<span id="doc_variant_class"></span>

## Variant class

### About

Variant is the most important datatype in Godot. A Variant takes up only 24
bytes on 64-bit platforms (20 bytes on 32-bit platforms) and can store almost
any engine datatype inside of it. Variants are rarely used to hold information
for long periods of time, instead they are used mainly for communication,
editing, serialization and generally moving data around.

A Variant can:

-  Store almost any datatype.
-  Perform operations between many variants (GDScript uses Variant as
   its atomic/native datatype).
-  Be hashed, so it can be compared quickly to other variants.
-  Be used to convert safely between datatypes.
-  Be used to abstract calling methods and their arguments (Godot
   exports all its functions through variants).
-  Be used to defer calls or move data between threads.
-  Be serialized as binary and stored to disk, or transferred via
   network.
-  Be serialized to text and use it for printing values and editable
   settings.
-  Work as an exported property, so the editor can edit it universally.
-  Be used for dictionaries, arrays, parsers, etc.

Basically, thanks to the Variant class, writing Godot itself was a much,
much easier task, as it allows for highly dynamic constructs not common
of C++ with little effort. Become a friend of Variant today.

> **Note:** All types within Variant except Nil and Object **cannot** be ``null`` and must always store a valid value. These types within Variant are therefore called *non-nullable* types. One of the Variant types is *Nil* which can only store the value ``null``. Therefore, it is possible for a Variant to contain the value ``null``, even though all Variant types excluding Nil and Object are non-nullable.
References
~~~~~~~~~~

-  core/variant/variant.h

### List of variant types

These types are available in Variant:

+---------------------------------+---------------------------+
| Type                            | Notes                     |
+=================================+===========================+
| Nil (can only store `null`)   | Nullable type             |
+---------------------------------+---------------------------+
| [class_bool](../../classes/class_bool.md#class_bool)               |                           |
+---------------------------------+---------------------------+
| [class_int](../../classes/class_int.md#class_int)                |                           |
+---------------------------------+---------------------------+
| [class_float](../../classes/class_float.md#class_float)              |                           |
+---------------------------------+---------------------------+
| [class_string](../../classes/class_string.md#class_string)             |                           |
+---------------------------------+---------------------------+
| [class_vector2](../../classes/class_vector2.md#class_vector2)            |                           |
+---------------------------------+---------------------------+
| [class_vector2i](../../classes/class_vector2i.md#class_vector2i)           |                           |
+---------------------------------+---------------------------+
| [class_rect2](../../classes/class_rect2.md#class_rect2)              | 2D counterpart of AABB    |
+---------------------------------+---------------------------+
| [class_rect2i](../../classes/class_rect2i.md#class_rect2i)             |                           |
+---------------------------------+---------------------------+
| [class_vector3](../../classes/class_vector3.md#class_vector3)            |                           |
+---------------------------------+---------------------------+
| [class_vector3i](../../classes/class_vector3i.md#class_vector3i)           |                           |
+---------------------------------+---------------------------+
| [class_transform2d](../../classes/class_transform2d.md#class_transform2d)        |                           |
+---------------------------------+---------------------------+
| [class_vector4](../../classes/class_vector4.md#class_vector4)            |                           |
+---------------------------------+---------------------------+
| [class_vector4i](../../classes/class_vector4i.md#class_vector4i)           |                           |
+---------------------------------+---------------------------+
| [class_plane](../../classes/class_plane.md#class_plane)              |                           |
+---------------------------------+---------------------------+
| [class_quaternion](../../classes/class_quaternion.md#class_quaternion)         |                           |
+---------------------------------+---------------------------+
| [class_aabb](../../classes/class_aabb.md#class_aabb)               | 3D counterpart of Rect2   |
+---------------------------------+---------------------------+
| [class_basis](../../classes/class_basis.md#class_basis)              |                           |
+---------------------------------+---------------------------+
| [class_transform3d](../../classes/class_transform3d.md#class_transform3d)        |                           |
+---------------------------------+---------------------------+
| [class_projection](../../classes/class_projection.md#class_projection)         |                           |
+---------------------------------+---------------------------+
| [class_color](../../classes/class_color.md#class_color)              |                           |
+---------------------------------+---------------------------+
| [class_stringname](../../classes/class_stringname.md#class_stringname)         |                           |
+---------------------------------+---------------------------+
| [class_nodepath](../../classes/class_nodepath.md#class_nodepath)           |                           |
+---------------------------------+---------------------------+
| [class_rid](../../classes/class_rid.md#class_rid)                |                           |
+---------------------------------+---------------------------+
| [class_object](../../classes/class_object.md#class_object)             | Nullable type             |
+---------------------------------+---------------------------+
| [class_callable](../../classes/class_callable.md#class_callable)           |                           |
+---------------------------------+---------------------------+
| [class_signal](../../classes/class_signal.md#class_signal)             |                           |
+---------------------------------+---------------------------+
| [class_dictionary](../../classes/class_dictionary.md#class_dictionary)         |                           |
+---------------------------------+---------------------------+
| [class_array](../../classes/class_array.md#class_array)              |                           |
+---------------------------------+---------------------------+
| [class_packedbytearray](../../classes/class_packedbytearray.md#class_packedbytearray)    |                           |
+---------------------------------+---------------------------+
| [class_packedint32array](../../classes/class_packedint32array.md#class_packedint32array)   |                           |
+---------------------------------+---------------------------+
| [class_packedint64array](../../classes/class_packedint64array.md#class_packedint64array)   |                           |
+---------------------------------+---------------------------+
| [class_packedfloat32array](../../classes/class_packedfloat32array.md#class_packedfloat32array) |                           |
+---------------------------------+---------------------------+
| [class_packedfloat64array](../../classes/class_packedfloat64array.md#class_packedfloat64array) |                           |
+---------------------------------+---------------------------+
| [class_packedstringarray](../../classes/class_packedstringarray.md#class_packedstringarray)  |                           |
+---------------------------------+---------------------------+
| [class_packedvector2array](../../classes/class_packedvector2array.md#class_packedvector2array) |                           |
+---------------------------------+---------------------------+
| [class_packedvector3array](../../classes/class_packedvector3array.md#class_packedvector3array) |                           |
+---------------------------------+---------------------------+
| [class_packedcolorarray](../../classes/class_packedcolorarray.md#class_packedcolorarray)   |                           |
+---------------------------------+---------------------------+
| [class_packedvector4array](../../classes/class_packedvector4array.md#class_packedvector4array) |                           |
+---------------------------------+---------------------------+

### Containers: Array and Dictionary

Both [class_array](../../classes/class_array.md#class_array) and [class_dictionary](../../classes/class_dictionary.md#class_dictionary) are implemented using
variants. A Dictionary can match any datatype used as key to any other datatype.
An Array just holds an array of Variants. Of course, a Variant can also hold a
Dictionary or an Array inside, making it even more flexible.

Modifications to a container will modify all references to
it. A [Mutex](core_types.md#doc_core_concurrency_types) should be created to lock it if
[multi-threaded access](../../tutorials/performance/using_multiple_threads.md#doc_using_multiple_threads) is desired.

References
~~~~~~~~~~

-  core/variant/dictionary.h
-  core/variant/array.h
