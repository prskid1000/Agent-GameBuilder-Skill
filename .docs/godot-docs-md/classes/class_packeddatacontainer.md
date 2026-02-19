<span id="class_PackedDataContainer"></span>

## PackedDataContainer

**Deprecated:** Use @GlobalScope.var_to_bytes() or [FileAccess.store_var()](class_fileaccess.md#class_FileAccess_method_store_var) instead. To enable data compression, use [PackedByteArray.compress()](class_packedbytearray.md#class_PackedByteArray_method_compress) or [FileAccess.open_compressed()](class_fileaccess.md#class_FileAccess_method_open_compressed).

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Efficiently packs and serializes [Array](class_array.md#class_Array) or [Dictionary](class_dictionary.md#class_Dictionary).

### Description

**PackedDataContainer** can be used to efficiently store data from untyped containers. The data is packed into raw bytes and can be saved to file. Only [Array](class_array.md#class_Array) and [Dictionary](class_dictionary.md#class_Dictionary) can be stored this way.

You can retrieve the data by iterating on the container, which will work as if iterating on the packed data itself. If the packed container is a [Dictionary](class_dictionary.md#class_Dictionary), the data can be retrieved by key names ([String](class_string.md#class_String)/[StringName](class_stringname.md#class_StringName) only).

::

    var data = { "key": "value", "another_key": 123, "lock": Vector2() }
    var packed = PackedDataContainer.new()
    packed.pack(data)
    ResourceSaver.save(packed, "packed_data.res")

::

    var container = load("packed_data.res")
    for key in container:
        prints(key, container[key])

Prints:

.. code:: text

    key value
    lock (0, 0)
    another_key 123

Nested containers will be packed recursively. While iterating, they will be returned as [PackedDataContainerRef](class_packeddatacontainerref.md#class_PackedDataContainerRef).

### Methods


| Error | [pack](class_packeddatacontainer.md#class_PackedDataContainer_method_pack) ( value: [Variant](class_variant.md#class_Variant) ) |
| --- | --- |
| [int](class_int.md#class_int) | [size](class_packeddatacontainer.md#class_PackedDataContainer_method_size) ( ) const |

---

### Method Descriptions

<span id="class_PackedDataContainer_method_pack"></span>

Error **pack** ( value: [Variant](class_variant.md#class_Variant) ) [🔗](class_packeddatacontainer.md#class_PackedDataContainer_method_pack)

Packs the given container into a binary representation. The `value` must be either [Array](class_array.md#class_Array) or [Dictionary](class_dictionary.md#class_Dictionary), any other type will result in invalid data error.

 **Note:** Subsequent calls to this method will overwrite the existing data.

---

<span id="class_PackedDataContainer_method_size"></span>

[int](class_int.md#class_int) **size** ( ) *const* [🔗](class_packeddatacontainer.md#class_PackedDataContainer_method_size)

Returns the size of the packed container (see [Array.size()](class_array.md#class_Array_method_size) and [Dictionary.size()](class_dictionary.md#class_Dictionary_method_size)).
