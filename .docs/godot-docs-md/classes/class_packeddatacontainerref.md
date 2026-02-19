<span id="class_PackedDataContainerRef"></span>

## PackedDataContainerRef

**Deprecated:** Use @GlobalScope.var_to_bytes() or [FileAccess.store_var()](class_fileaccess.md#class_FileAccess_method_store_var) instead. To enable data compression, use [PackedByteArray.compress()](class_packedbytearray.md#class_PackedByteArray_method_compress) or [FileAccess.open_compressed()](class_fileaccess.md#class_FileAccess_method_open_compressed).

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

An internal class used by [PackedDataContainer](class_packeddatacontainer.md#class_PackedDataContainer) to pack nested arrays and dictionaries.

### Description

When packing nested containers using [PackedDataContainer](class_packeddatacontainer.md#class_PackedDataContainer), they are recursively packed into **PackedDataContainerRef** (only applies to [Array](class_array.md#class_Array) and [Dictionary](class_dictionary.md#class_Dictionary)). Their data can be retrieved the same way as from [PackedDataContainer](class_packeddatacontainer.md#class_PackedDataContainer).

::

    var packed = PackedDataContainer.new()
    packed.pack([1, 2, 3, ["nested1", "nested2"], 4, 5, 6])

    for element in packed:
        if element is PackedDataContainerRef:
            for subelement in element:
                print("::", subelement)
        else:
            print(element)

Prints:

.. code:: text

    1
    2
    3
    ::nested1
    ::nested2
    4
    5
    6

### Methods


| [int](class_int.md#class_int) | [size](class_packeddatacontainerref.md#class_PackedDataContainerRef_method_size) ( ) const |
| --- | --- |

---

### Method Descriptions

<span id="class_PackedDataContainerRef_method_size"></span>

[int](class_int.md#class_int) **size** ( ) *const* [🔗](class_packeddatacontainerref.md#class_PackedDataContainerRef_method_size)

Returns the size of the packed container (see [Array.size()](class_array.md#class_Array_method_size) and [Dictionary.size()](class_dictionary.md#class_Dictionary_method_size)).
