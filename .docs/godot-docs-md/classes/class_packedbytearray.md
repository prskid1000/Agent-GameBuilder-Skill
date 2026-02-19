<span id="class_PackedByteArray"></span>

## PackedByteArray

A packed array of bytes.

### Description

An array specifically designed to hold bytes. Packs data tightly, so it saves memory for large array sizes.

 **PackedByteArray** also provides methods to encode/decode various types to/from bytes. The way values are encoded is an implementation detail and shouldn't be relied upon when interacting with external apps.

 **Note:** Packed arrays are always passed by reference. To get a copy of an array that can be modified independently of the original array, use [duplicate()](class_packedbytearray.md#class_PackedByteArray_method_duplicate). This is *not* the case for built-in properties and methods. In these cases the returned packed array is a copy, and changing it will *not* affect the original value. To update a built-in property of this type, modify the returned array and then assign it to the property again.

 **Note:** In a boolean context, a packed array will evaluate to `false` if it's empty. Otherwise, a packed array will always evaluate to `true`.

> **Note:** There are notable differences when using this API with C#. See :ref:`doc_c_sharp_differences` for more information.

### Constructors


| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [PackedByteArray](class_packedbytearray.md#class_PackedByteArray_constructor_PackedByteArray) ( ) |
| --- | --- |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [PackedByteArray](class_packedbytearray.md#class_PackedByteArray_constructor_PackedByteArray) ( from: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [PackedByteArray](class_packedbytearray.md#class_PackedByteArray_constructor_PackedByteArray) ( from: [Array](class_array.md#class_Array) ) |

### Methods


| [bool](class_bool.md#class_bool) | [append](class_packedbytearray.md#class_PackedByteArray_method_append) ( value: [int](class_int.md#class_int) ) |
| --- | --- |
| void | [append_array](class_packedbytearray.md#class_PackedByteArray_method_append_array) ( array: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| [int](class_int.md#class_int) | [bsearch](class_packedbytearray.md#class_PackedByteArray_method_bsearch) ( value: [int](class_int.md#class_int), before: [bool](class_bool.md#class_bool) = true ) const |
| void | [bswap16](class_packedbytearray.md#class_PackedByteArray_method_bswap16) ( offset: [int](class_int.md#class_int) = 0, count: [int](class_int.md#class_int) = -1 ) |
| void | [bswap32](class_packedbytearray.md#class_PackedByteArray_method_bswap32) ( offset: [int](class_int.md#class_int) = 0, count: [int](class_int.md#class_int) = -1 ) |
| void | [bswap64](class_packedbytearray.md#class_PackedByteArray_method_bswap64) ( offset: [int](class_int.md#class_int) = 0, count: [int](class_int.md#class_int) = -1 ) |
| void | [clear](class_packedbytearray.md#class_PackedByteArray_method_clear) ( ) |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [compress](class_packedbytearray.md#class_PackedByteArray_method_compress) ( compression_mode: [int](class_int.md#class_int) = 0 ) const |
| [int](class_int.md#class_int) | [count](class_packedbytearray.md#class_PackedByteArray_method_count) ( value: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [decode_double](class_packedbytearray.md#class_PackedByteArray_method_decode_double) ( byte_offset: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [decode_float](class_packedbytearray.md#class_PackedByteArray_method_decode_float) ( byte_offset: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [decode_half](class_packedbytearray.md#class_PackedByteArray_method_decode_half) ( byte_offset: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [decode_s8](class_packedbytearray.md#class_PackedByteArray_method_decode_s8) ( byte_offset: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [decode_s16](class_packedbytearray.md#class_PackedByteArray_method_decode_s16) ( byte_offset: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [decode_s32](class_packedbytearray.md#class_PackedByteArray_method_decode_s32) ( byte_offset: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [decode_s64](class_packedbytearray.md#class_PackedByteArray_method_decode_s64) ( byte_offset: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [decode_u8](class_packedbytearray.md#class_PackedByteArray_method_decode_u8) ( byte_offset: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [decode_u16](class_packedbytearray.md#class_PackedByteArray_method_decode_u16) ( byte_offset: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [decode_u32](class_packedbytearray.md#class_PackedByteArray_method_decode_u32) ( byte_offset: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [decode_u64](class_packedbytearray.md#class_PackedByteArray_method_decode_u64) ( byte_offset: [int](class_int.md#class_int) ) const |
| [Variant](class_variant.md#class_Variant) | [decode_var](class_packedbytearray.md#class_PackedByteArray_method_decode_var) ( byte_offset: [int](class_int.md#class_int), allow_objects: [bool](class_bool.md#class_bool) = false ) const |
| [int](class_int.md#class_int) | [decode_var_size](class_packedbytearray.md#class_PackedByteArray_method_decode_var_size) ( byte_offset: [int](class_int.md#class_int), allow_objects: [bool](class_bool.md#class_bool) = false ) const |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [decompress](class_packedbytearray.md#class_PackedByteArray_method_decompress) ( buffer_size: [int](class_int.md#class_int), compression_mode: [int](class_int.md#class_int) = 0 ) const |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [decompress_dynamic](class_packedbytearray.md#class_PackedByteArray_method_decompress_dynamic) ( max_output_size: [int](class_int.md#class_int), compression_mode: [int](class_int.md#class_int) = 0 ) const |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [duplicate](class_packedbytearray.md#class_PackedByteArray_method_duplicate) ( ) const |
| void | [encode_double](class_packedbytearray.md#class_PackedByteArray_method_encode_double) ( byte_offset: [int](class_int.md#class_int), value: [float](class_float.md#class_float) ) |
| void | [encode_float](class_packedbytearray.md#class_PackedByteArray_method_encode_float) ( byte_offset: [int](class_int.md#class_int), value: [float](class_float.md#class_float) ) |
| void | [encode_half](class_packedbytearray.md#class_PackedByteArray_method_encode_half) ( byte_offset: [int](class_int.md#class_int), value: [float](class_float.md#class_float) ) |
| void | [encode_s8](class_packedbytearray.md#class_PackedByteArray_method_encode_s8) ( byte_offset: [int](class_int.md#class_int), value: [int](class_int.md#class_int) ) |
| void | [encode_s16](class_packedbytearray.md#class_PackedByteArray_method_encode_s16) ( byte_offset: [int](class_int.md#class_int), value: [int](class_int.md#class_int) ) |
| void | [encode_s32](class_packedbytearray.md#class_PackedByteArray_method_encode_s32) ( byte_offset: [int](class_int.md#class_int), value: [int](class_int.md#class_int) ) |
| void | [encode_s64](class_packedbytearray.md#class_PackedByteArray_method_encode_s64) ( byte_offset: [int](class_int.md#class_int), value: [int](class_int.md#class_int) ) |
| void | [encode_u8](class_packedbytearray.md#class_PackedByteArray_method_encode_u8) ( byte_offset: [int](class_int.md#class_int), value: [int](class_int.md#class_int) ) |
| void | [encode_u16](class_packedbytearray.md#class_PackedByteArray_method_encode_u16) ( byte_offset: [int](class_int.md#class_int), value: [int](class_int.md#class_int) ) |
| void | [encode_u32](class_packedbytearray.md#class_PackedByteArray_method_encode_u32) ( byte_offset: [int](class_int.md#class_int), value: [int](class_int.md#class_int) ) |
| void | [encode_u64](class_packedbytearray.md#class_PackedByteArray_method_encode_u64) ( byte_offset: [int](class_int.md#class_int), value: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [encode_var](class_packedbytearray.md#class_PackedByteArray_method_encode_var) ( byte_offset: [int](class_int.md#class_int), value: [Variant](class_variant.md#class_Variant), allow_objects: [bool](class_bool.md#class_bool) = false ) |
| [bool](class_bool.md#class_bool) | [erase](class_packedbytearray.md#class_PackedByteArray_method_erase) ( value: [int](class_int.md#class_int) ) |
| void | [fill](class_packedbytearray.md#class_PackedByteArray_method_fill) ( value: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [find](class_packedbytearray.md#class_PackedByteArray_method_find) ( value: [int](class_int.md#class_int), from: [int](class_int.md#class_int) = 0 ) const |
| [int](class_int.md#class_int) | [get](class_packedbytearray.md#class_PackedByteArray_method_get) ( index: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_string_from_ascii](class_packedbytearray.md#class_PackedByteArray_method_get_string_from_ascii) ( ) const |
| [String](class_string.md#class_String) | [get_string_from_multibyte_char](class_packedbytearray.md#class_PackedByteArray_method_get_string_from_multibyte_char) ( encoding: [String](class_string.md#class_String) = "" ) const |
| [String](class_string.md#class_String) | [get_string_from_utf8](class_packedbytearray.md#class_PackedByteArray_method_get_string_from_utf8) ( ) const |
| [String](class_string.md#class_String) | [get_string_from_utf16](class_packedbytearray.md#class_PackedByteArray_method_get_string_from_utf16) ( ) const |
| [String](class_string.md#class_String) | [get_string_from_utf32](class_packedbytearray.md#class_PackedByteArray_method_get_string_from_utf32) ( ) const |
| [String](class_string.md#class_String) | [get_string_from_wchar](class_packedbytearray.md#class_PackedByteArray_method_get_string_from_wchar) ( ) const |
| [bool](class_bool.md#class_bool) | [has](class_packedbytearray.md#class_PackedByteArray_method_has) ( value: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [has_encoded_var](class_packedbytearray.md#class_PackedByteArray_method_has_encoded_var) ( byte_offset: [int](class_int.md#class_int), allow_objects: [bool](class_bool.md#class_bool) = false ) const |
| [String](class_string.md#class_String) | [hex_encode](class_packedbytearray.md#class_PackedByteArray_method_hex_encode) ( ) const |
| [int](class_int.md#class_int) | [insert](class_packedbytearray.md#class_PackedByteArray_method_insert) ( at_index: [int](class_int.md#class_int), value: [int](class_int.md#class_int) ) |
| [bool](class_bool.md#class_bool) | [is_empty](class_packedbytearray.md#class_PackedByteArray_method_is_empty) ( ) const |
| [bool](class_bool.md#class_bool) | [push_back](class_packedbytearray.md#class_PackedByteArray_method_push_back) ( value: [int](class_int.md#class_int) ) |
| void | [remove_at](class_packedbytearray.md#class_PackedByteArray_method_remove_at) ( index: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [resize](class_packedbytearray.md#class_PackedByteArray_method_resize) ( new_size: [int](class_int.md#class_int) ) |
| void | [reverse](class_packedbytearray.md#class_PackedByteArray_method_reverse) ( ) |
| [int](class_int.md#class_int) | [rfind](class_packedbytearray.md#class_PackedByteArray_method_rfind) ( value: [int](class_int.md#class_int), from: [int](class_int.md#class_int) = -1 ) const |
| void | [set](class_packedbytearray.md#class_PackedByteArray_method_set) ( index: [int](class_int.md#class_int), value: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [size](class_packedbytearray.md#class_PackedByteArray_method_size) ( ) const |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [slice](class_packedbytearray.md#class_PackedByteArray_method_slice) ( begin: [int](class_int.md#class_int), end: [int](class_int.md#class_int) = 2147483647 ) const |
| void | [sort](class_packedbytearray.md#class_PackedByteArray_method_sort) ( ) |
| [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) | [to_color_array](class_packedbytearray.md#class_PackedByteArray_method_to_color_array) ( ) const |
| [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) | [to_float32_array](class_packedbytearray.md#class_PackedByteArray_method_to_float32_array) ( ) const |
| [PackedFloat64Array](class_packedfloat64array.md#class_PackedFloat64Array) | [to_float64_array](class_packedbytearray.md#class_PackedByteArray_method_to_float64_array) ( ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [to_int32_array](class_packedbytearray.md#class_PackedByteArray_method_to_int32_array) ( ) const |
| [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) | [to_int64_array](class_packedbytearray.md#class_PackedByteArray_method_to_int64_array) ( ) const |
| [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) | [to_vector2_array](class_packedbytearray.md#class_PackedByteArray_method_to_vector2_array) ( ) const |
| [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) | [to_vector3_array](class_packedbytearray.md#class_PackedByteArray_method_to_vector3_array) ( ) const |
| [PackedVector4Array](class_packedvector4array.md#class_PackedVector4Array) | [to_vector4_array](class_packedbytearray.md#class_PackedByteArray_method_to_vector4_array) ( ) const |

### Operators


| [bool](class_bool.md#class_bool) | [operator !=](class_packedbytearray.md#class_PackedByteArray_operator_neq_PackedByteArray) ( right: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| --- | --- |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [operator +](class_packedbytearray.md#class_PackedByteArray_operator_sum_PackedByteArray) ( right: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| [bool](class_bool.md#class_bool) | [operator ==](class_packedbytearray.md#class_PackedByteArray_operator_eq_PackedByteArray) ( right: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| [int](class_int.md#class_int) | [operator []](class_packedbytearray.md#class_PackedByteArray_operator_idx_int) ( index: [int](class_int.md#class_int) ) |

---

### Constructor Descriptions

<span id="class_PackedByteArray_constructor_PackedByteArray"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **PackedByteArray** ( ) [🔗](class_packedbytearray.md#class_PackedByteArray_constructor_PackedByteArray)

Constructs an empty **PackedByteArray**.

---

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **PackedByteArray** ( from: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) )

Constructs a **PackedByteArray** as a copy of the given **PackedByteArray**.

---

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **PackedByteArray** ( from: [Array](class_array.md#class_Array) )

Constructs a new **PackedByteArray**. Optionally, you can pass in a generic [Array](class_array.md#class_Array) that will be converted.

---

### Method Descriptions

<span id="class_PackedByteArray_method_append"></span>

[bool](class_bool.md#class_bool) **append** ( value: [int](class_int.md#class_int) ) [🔗](class_packedbytearray.md#class_PackedByteArray_method_append)

Appends an element at the end of the array (alias of [push_back()](class_packedbytearray.md#class_PackedByteArray_method_push_back)).

---

<span id="class_PackedByteArray_method_append_array"></span>

void **append_array** ( array: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_packedbytearray.md#class_PackedByteArray_method_append_array)

Appends a **PackedByteArray** at the end of this array.

---

<span id="class_PackedByteArray_method_bsearch"></span>

[int](class_int.md#class_int) **bsearch** ( value: [int](class_int.md#class_int), before: [bool](class_bool.md#class_bool) = true ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_bsearch)

Finds the index of an existing value (or the insertion index that maintains sorting order, if the value is not yet present in the array) using binary search. Optionally, a `before` specifier can be passed. If `false`, the returned index comes after all existing entries of the value in the array.

 **Note:** Calling [bsearch()](class_packedbytearray.md#class_PackedByteArray_method_bsearch) on an unsorted array results in unexpected behavior.

---

<span id="class_PackedByteArray_method_bswap16"></span>

void **bswap16** ( offset: [int](class_int.md#class_int) = 0, count: [int](class_int.md#class_int) = -1 ) [🔗](class_packedbytearray.md#class_PackedByteArray_method_bswap16)

Swaps the byte order of `count` 16-bit segments of the array starting at `offset`. Swap is done in-place. If `count` is less than zero, all segments to the end of array are processed, if processed data size is not a multiple of 2, the byte after the last processed 16-bit segment is not modified.

---

<span id="class_PackedByteArray_method_bswap32"></span>

void **bswap32** ( offset: [int](class_int.md#class_int) = 0, count: [int](class_int.md#class_int) = -1 ) [🔗](class_packedbytearray.md#class_PackedByteArray_method_bswap32)

Swaps the byte order of `count` 32-bit segments of the array starting at `offset`. Swap is done in-place. If `count` is less than zero, all segments to the end of array are processed, if processed data size is not a multiple of 4, bytes after the last processed 32-bit segment are not modified.

---

<span id="class_PackedByteArray_method_bswap64"></span>

void **bswap64** ( offset: [int](class_int.md#class_int) = 0, count: [int](class_int.md#class_int) = -1 ) [🔗](class_packedbytearray.md#class_PackedByteArray_method_bswap64)

Swaps the byte order of `count` 64-bit segments of the array starting at `offset`. Swap is done in-place. If `count` is less than zero, all segments to the end of array are processed, if processed data size is not a multiple of 8, bytes after the last processed 64-bit segment are not modified.

---

<span id="class_PackedByteArray_method_clear"></span>

void **clear** ( ) [🔗](class_packedbytearray.md#class_PackedByteArray_method_clear)

Clears the array. This is equivalent to using [resize()](class_packedbytearray.md#class_PackedByteArray_method_resize) with a size of `0`.

---

<span id="class_PackedByteArray_method_compress"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **compress** ( compression_mode: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_compress)

Returns a new **PackedByteArray** with the data compressed. Set the compression mode using one of [CompressionMode](class_fileaccess.md#enum_FileAccess_CompressionMode)'s constants.

---

<span id="class_PackedByteArray_method_count"></span>

[int](class_int.md#class_int) **count** ( value: [int](class_int.md#class_int) ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_count)

Returns the number of times an element is in the array.

---

<span id="class_PackedByteArray_method_decode_double"></span>

[float](class_float.md#class_float) **decode_double** ( byte_offset: [int](class_int.md#class_int) ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_decode_double)

Decodes a 64-bit floating-point number from the bytes starting at `byte_offset`. Fails if the byte count is insufficient. Returns `0.0` if a valid number can't be decoded.

---

<span id="class_PackedByteArray_method_decode_float"></span>

[float](class_float.md#class_float) **decode_float** ( byte_offset: [int](class_int.md#class_int) ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_decode_float)

Decodes a 32-bit floating-point number from the bytes starting at `byte_offset`. Fails if the byte count is insufficient. Returns `0.0` if a valid number can't be decoded.

---

<span id="class_PackedByteArray_method_decode_half"></span>

[float](class_float.md#class_float) **decode_half** ( byte_offset: [int](class_int.md#class_int) ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_decode_half)

Decodes a 16-bit floating-point number from the bytes starting at `byte_offset`. Fails if the byte count is insufficient. Returns `0.0` if a valid number can't be decoded.

---

<span id="class_PackedByteArray_method_decode_s8"></span>

[int](class_int.md#class_int) **decode_s8** ( byte_offset: [int](class_int.md#class_int) ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_decode_s8)

Decodes a 8-bit signed integer number from the bytes starting at `byte_offset`. Fails if the byte count is insufficient. Returns `0` if a valid number can't be decoded.

---

<span id="class_PackedByteArray_method_decode_s16"></span>

[int](class_int.md#class_int) **decode_s16** ( byte_offset: [int](class_int.md#class_int) ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_decode_s16)

Decodes a 16-bit signed integer number from the bytes starting at `byte_offset`. Fails if the byte count is insufficient. Returns `0` if a valid number can't be decoded.

---

<span id="class_PackedByteArray_method_decode_s32"></span>

[int](class_int.md#class_int) **decode_s32** ( byte_offset: [int](class_int.md#class_int) ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_decode_s32)

Decodes a 32-bit signed integer number from the bytes starting at `byte_offset`. Fails if the byte count is insufficient. Returns `0` if a valid number can't be decoded.

---

<span id="class_PackedByteArray_method_decode_s64"></span>

[int](class_int.md#class_int) **decode_s64** ( byte_offset: [int](class_int.md#class_int) ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_decode_s64)

Decodes a 64-bit signed integer number from the bytes starting at `byte_offset`. Fails if the byte count is insufficient. Returns `0` if a valid number can't be decoded.

---

<span id="class_PackedByteArray_method_decode_u8"></span>

[int](class_int.md#class_int) **decode_u8** ( byte_offset: [int](class_int.md#class_int) ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_decode_u8)

Decodes a 8-bit unsigned integer number from the bytes starting at `byte_offset`. Fails if the byte count is insufficient. Returns `0` if a valid number can't be decoded.

---

<span id="class_PackedByteArray_method_decode_u16"></span>

[int](class_int.md#class_int) **decode_u16** ( byte_offset: [int](class_int.md#class_int) ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_decode_u16)

Decodes a 16-bit unsigned integer number from the bytes starting at `byte_offset`. Fails if the byte count is insufficient. Returns `0` if a valid number can't be decoded.

---

<span id="class_PackedByteArray_method_decode_u32"></span>

[int](class_int.md#class_int) **decode_u32** ( byte_offset: [int](class_int.md#class_int) ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_decode_u32)

Decodes a 32-bit unsigned integer number from the bytes starting at `byte_offset`. Fails if the byte count is insufficient. Returns `0` if a valid number can't be decoded.

---

<span id="class_PackedByteArray_method_decode_u64"></span>

[int](class_int.md#class_int) **decode_u64** ( byte_offset: [int](class_int.md#class_int) ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_decode_u64)

Decodes a 64-bit unsigned integer number from the bytes starting at `byte_offset`. Fails if the byte count is insufficient. Returns `0` if a valid number can't be decoded.

---

<span id="class_PackedByteArray_method_decode_var"></span>

[Variant](class_variant.md#class_Variant) **decode_var** ( byte_offset: [int](class_int.md#class_int), allow_objects: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_decode_var)

Decodes a [Variant](class_variant.md#class_Variant) from the bytes starting at `byte_offset`. Returns `null` if a valid variant can't be decoded or the value is [Object](class_object.md#class_Object)-derived and `allow_objects` is `false`.

---

<span id="class_PackedByteArray_method_decode_var_size"></span>

[int](class_int.md#class_int) **decode_var_size** ( byte_offset: [int](class_int.md#class_int), allow_objects: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_decode_var_size)

Decodes a size of a [Variant](class_variant.md#class_Variant) from the bytes starting at `byte_offset`. Requires at least 4 bytes of data starting at the offset, otherwise fails.

---

<span id="class_PackedByteArray_method_decompress"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **decompress** ( buffer_size: [int](class_int.md#class_int), compression_mode: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_decompress)

Returns a new **PackedByteArray** with the data decompressed. Set `buffer_size` to the size of the uncompressed data. Set the compression mode using one of [CompressionMode](class_fileaccess.md#enum_FileAccess_CompressionMode)'s constants.

 **Note:** Decompression is not guaranteed to work with data not compressed by Godot, for example if data compressed with the deflate compression mode lacks a checksum or header.

---

<span id="class_PackedByteArray_method_decompress_dynamic"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **decompress_dynamic** ( max_output_size: [int](class_int.md#class_int), compression_mode: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_decompress_dynamic)

Returns a new **PackedByteArray** with the data decompressed. Set the compression mode using one of [CompressionMode](class_fileaccess.md#enum_FileAccess_CompressionMode)'s constants. **This method only accepts brotli, gzip, and deflate compression modes.**

This method is potentially slower than [decompress()](class_packedbytearray.md#class_PackedByteArray_method_decompress), as it may have to re-allocate its output buffer multiple times while decompressing, whereas [decompress()](class_packedbytearray.md#class_PackedByteArray_method_decompress) knows it's output buffer size from the beginning.

GZIP has a maximal compression ratio of 1032:1, meaning it's very possible for a small compressed payload to decompress to a potentially very large output. To guard against this, you may provide a maximum size this function is allowed to allocate in bytes via `max_output_size`. Passing -1 will allow for unbounded output. If any positive value is passed, and the decompression exceeds that amount in bytes, then an error will be returned.

 **Note:** Decompression is not guaranteed to work with data not compressed by Godot, for example if data compressed with the deflate compression mode lacks a checksum or header.

---

<span id="class_PackedByteArray_method_duplicate"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **duplicate** ( ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_duplicate)

Creates a copy of the array, and returns it.

---

<span id="class_PackedByteArray_method_encode_double"></span>

void **encode_double** ( byte_offset: [int](class_int.md#class_int), value: [float](class_float.md#class_float) ) [🔗](class_packedbytearray.md#class_PackedByteArray_method_encode_double)

Encodes a 64-bit floating-point number as bytes at the index of `byte_offset` bytes. The array must have at least 8 bytes of allocated space, starting at the offset.

---

<span id="class_PackedByteArray_method_encode_float"></span>

void **encode_float** ( byte_offset: [int](class_int.md#class_int), value: [float](class_float.md#class_float) ) [🔗](class_packedbytearray.md#class_PackedByteArray_method_encode_float)

Encodes a 32-bit floating-point number as bytes at the index of `byte_offset` bytes. The array must have at least 4 bytes of space, starting at the offset.

---

<span id="class_PackedByteArray_method_encode_half"></span>

void **encode_half** ( byte_offset: [int](class_int.md#class_int), value: [float](class_float.md#class_float) ) [🔗](class_packedbytearray.md#class_PackedByteArray_method_encode_half)

Encodes a 16-bit floating-point number as bytes at the index of `byte_offset` bytes. The array must have at least 2 bytes of space, starting at the offset.

---

<span id="class_PackedByteArray_method_encode_s8"></span>

void **encode_s8** ( byte_offset: [int](class_int.md#class_int), value: [int](class_int.md#class_int) ) [🔗](class_packedbytearray.md#class_PackedByteArray_method_encode_s8)

Encodes a 8-bit signed integer number (signed byte) at the index of `byte_offset` bytes. The array must have at least 1 byte of space, starting at the offset.

---

<span id="class_PackedByteArray_method_encode_s16"></span>

void **encode_s16** ( byte_offset: [int](class_int.md#class_int), value: [int](class_int.md#class_int) ) [🔗](class_packedbytearray.md#class_PackedByteArray_method_encode_s16)

Encodes a 16-bit signed integer number as bytes at the index of `byte_offset` bytes. The array must have at least 2 bytes of space, starting at the offset.

---

<span id="class_PackedByteArray_method_encode_s32"></span>

void **encode_s32** ( byte_offset: [int](class_int.md#class_int), value: [int](class_int.md#class_int) ) [🔗](class_packedbytearray.md#class_PackedByteArray_method_encode_s32)

Encodes a 32-bit signed integer number as bytes at the index of `byte_offset` bytes. The array must have at least 4 bytes of space, starting at the offset.

---

<span id="class_PackedByteArray_method_encode_s64"></span>

void **encode_s64** ( byte_offset: [int](class_int.md#class_int), value: [int](class_int.md#class_int) ) [🔗](class_packedbytearray.md#class_PackedByteArray_method_encode_s64)

Encodes a 64-bit signed integer number as bytes at the index of `byte_offset` bytes. The array must have at least 8 bytes of space, starting at the offset.

---

<span id="class_PackedByteArray_method_encode_u8"></span>

void **encode_u8** ( byte_offset: [int](class_int.md#class_int), value: [int](class_int.md#class_int) ) [🔗](class_packedbytearray.md#class_PackedByteArray_method_encode_u8)

Encodes a 8-bit unsigned integer number (byte) at the index of `byte_offset` bytes. The array must have at least 1 byte of space, starting at the offset.

---

<span id="class_PackedByteArray_method_encode_u16"></span>

void **encode_u16** ( byte_offset: [int](class_int.md#class_int), value: [int](class_int.md#class_int) ) [🔗](class_packedbytearray.md#class_PackedByteArray_method_encode_u16)

Encodes a 16-bit unsigned integer number as bytes at the index of `byte_offset` bytes. The array must have at least 2 bytes of space, starting at the offset.

---

<span id="class_PackedByteArray_method_encode_u32"></span>

void **encode_u32** ( byte_offset: [int](class_int.md#class_int), value: [int](class_int.md#class_int) ) [🔗](class_packedbytearray.md#class_PackedByteArray_method_encode_u32)

Encodes a 32-bit unsigned integer number as bytes at the index of `byte_offset` bytes. The array must have at least 4 bytes of space, starting at the offset.

---

<span id="class_PackedByteArray_method_encode_u64"></span>

void **encode_u64** ( byte_offset: [int](class_int.md#class_int), value: [int](class_int.md#class_int) ) [🔗](class_packedbytearray.md#class_PackedByteArray_method_encode_u64)

Encodes a 64-bit unsigned integer number as bytes at the index of `byte_offset` bytes. The array must have at least 8 bytes of space, starting at the offset.

---

<span id="class_PackedByteArray_method_encode_var"></span>

[int](class_int.md#class_int) **encode_var** ( byte_offset: [int](class_int.md#class_int), value: [Variant](class_variant.md#class_Variant), allow_objects: [bool](class_bool.md#class_bool) = false ) [🔗](class_packedbytearray.md#class_PackedByteArray_method_encode_var)

Encodes a [Variant](class_variant.md#class_Variant) at the index of `byte_offset` bytes. A sufficient space must be allocated, depending on the encoded variant's size. If `allow_objects` is `false`, [Object](class_object.md#class_Object)-derived values are not permitted and will instead be serialized as ID-only.

---

<span id="class_PackedByteArray_method_erase"></span>

[bool](class_bool.md#class_bool) **erase** ( value: [int](class_int.md#class_int) ) [🔗](class_packedbytearray.md#class_PackedByteArray_method_erase)

Removes the first occurrence of a value from the array and returns `true`. If the value does not exist in the array, nothing happens and `false` is returned. To remove an element by index, use [remove_at()](class_packedbytearray.md#class_PackedByteArray_method_remove_at) instead.

---

<span id="class_PackedByteArray_method_fill"></span>

void **fill** ( value: [int](class_int.md#class_int) ) [🔗](class_packedbytearray.md#class_PackedByteArray_method_fill)

Assigns the given value to all elements in the array. This can typically be used together with [resize()](class_packedbytearray.md#class_PackedByteArray_method_resize) to create an array with a given size and initialized elements.

---

<span id="class_PackedByteArray_method_find"></span>

[int](class_int.md#class_int) **find** ( value: [int](class_int.md#class_int), from: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_find)

Searches the array for a value and returns its index or `-1` if not found. Optionally, the initial search index can be passed.

---

<span id="class_PackedByteArray_method_get"></span>

[int](class_int.md#class_int) **get** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_get)

Returns the byte at the given `index` in the array. If `index` is out-of-bounds or negative, this method fails and returns `0`.

This method is similar (but not identical) to the `[]` operator. Most notably, when this method fails, it doesn't pause project execution if run from the editor.

---

<span id="class_PackedByteArray_method_get_string_from_ascii"></span>

[String](class_string.md#class_String) **get_string_from_ascii** ( ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_get_string_from_ascii)

Converts ASCII/Latin-1 encoded array to [String](class_string.md#class_String). Fast alternative to [get_string_from_utf8()](class_packedbytearray.md#class_PackedByteArray_method_get_string_from_utf8) if the content is ASCII/Latin-1 only. Unlike the UTF-8 function this function maps every byte to a character in the array. Multibyte sequences will not be interpreted correctly. For parsing user input always use [get_string_from_utf8()](class_packedbytearray.md#class_PackedByteArray_method_get_string_from_utf8). This is the inverse of [String.to_ascii_buffer()](class_string.md#class_String_method_to_ascii_buffer).

---

<span id="class_PackedByteArray_method_get_string_from_multibyte_char"></span>

[String](class_string.md#class_String) **get_string_from_multibyte_char** ( encoding: [String](class_string.md#class_String) = "" ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_get_string_from_multibyte_char)

Converts system multibyte code page encoded array to [String](class_string.md#class_String). If conversion fails, empty string is returned. This is the inverse of [String.to_multibyte_char_buffer()](class_string.md#class_String_method_to_multibyte_char_buffer).

The values permitted for `encoding` are system dependent. If `encoding` is empty string, system default encoding is used.

- For Windows, see Code Page Identifiers .NET names.

- For macOS and Linux/BSD, see `libiconv` library documentation and `iconv --list` for a list of supported encodings.

---

<span id="class_PackedByteArray_method_get_string_from_utf8"></span>

[String](class_string.md#class_String) **get_string_from_utf8** ( ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_get_string_from_utf8)

Converts UTF-8 encoded array to [String](class_string.md#class_String). Slower than [get_string_from_ascii()](class_packedbytearray.md#class_PackedByteArray_method_get_string_from_ascii) but supports UTF-8 encoded data. Use this function if you are unsure about the source of the data. For user input this function should always be preferred. Returns empty string if source array is not valid UTF-8 string. This is the inverse of [String.to_utf8_buffer()](class_string.md#class_String_method_to_utf8_buffer).

---

<span id="class_PackedByteArray_method_get_string_from_utf16"></span>

[String](class_string.md#class_String) **get_string_from_utf16** ( ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_get_string_from_utf16)

Converts UTF-16 encoded array to [String](class_string.md#class_String). If the BOM is missing, little-endianness is assumed. Returns empty string if source array is not valid UTF-16 string. This is the inverse of [String.to_utf16_buffer()](class_string.md#class_String_method_to_utf16_buffer).

---

<span id="class_PackedByteArray_method_get_string_from_utf32"></span>

[String](class_string.md#class_String) **get_string_from_utf32** ( ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_get_string_from_utf32)

Converts UTF-32 encoded array to [String](class_string.md#class_String). Returns empty string if source array is not valid UTF-32 string. This is the inverse of [String.to_utf32_buffer()](class_string.md#class_String_method_to_utf32_buffer).

---

<span id="class_PackedByteArray_method_get_string_from_wchar"></span>

[String](class_string.md#class_String) **get_string_from_wchar** ( ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_get_string_from_wchar)

Converts wide character (`wchar_t`, UTF-16 on Windows, UTF-32 on other platforms) encoded array to [String](class_string.md#class_String). Returns empty string if source array is not valid wide string. This is the inverse of [String.to_wchar_buffer()](class_string.md#class_String_method_to_wchar_buffer).

---

<span id="class_PackedByteArray_method_has"></span>

[bool](class_bool.md#class_bool) **has** ( value: [int](class_int.md#class_int) ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_has)

Returns `true` if the array contains `value`.

---

<span id="class_PackedByteArray_method_has_encoded_var"></span>

[bool](class_bool.md#class_bool) **has_encoded_var** ( byte_offset: [int](class_int.md#class_int), allow_objects: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_has_encoded_var)

Returns `true` if a valid [Variant](class_variant.md#class_Variant) value can be decoded at the `byte_offset`. Returns `false` otherwise or when the value is [Object](class_object.md#class_Object)-derived and `allow_objects` is `false`.

---

<span id="class_PackedByteArray_method_hex_encode"></span>

[String](class_string.md#class_String) **hex_encode** ( ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_hex_encode)

Returns a hexadecimal representation of this array as a [String](class_string.md#class_String).

.. tabs::

```
```

    var array = PackedByteArray([11, 46, 255])
    print(array.hex_encode()) # Prints "0b2eff"

```
```

    byte[] array = [11, 46, 255];
    GD.Print(array.HexEncode()); // Prints "0b2eff"

---

<span id="class_PackedByteArray_method_insert"></span>

[int](class_int.md#class_int) **insert** ( at_index: [int](class_int.md#class_int), value: [int](class_int.md#class_int) ) [🔗](class_packedbytearray.md#class_PackedByteArray_method_insert)

Inserts a new element at a given position in the array. The position must be valid, or at the end of the array (`idx == size()`).

---

<span id="class_PackedByteArray_method_is_empty"></span>

[bool](class_bool.md#class_bool) **is_empty** ( ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_is_empty)

Returns `true` if the array is empty.

---

<span id="class_PackedByteArray_method_push_back"></span>

[bool](class_bool.md#class_bool) **push_back** ( value: [int](class_int.md#class_int) ) [🔗](class_packedbytearray.md#class_PackedByteArray_method_push_back)

Appends an element at the end of the array.

---

<span id="class_PackedByteArray_method_remove_at"></span>

void **remove_at** ( index: [int](class_int.md#class_int) ) [🔗](class_packedbytearray.md#class_PackedByteArray_method_remove_at)

Removes an element from the array by index.

---

<span id="class_PackedByteArray_method_resize"></span>

[int](class_int.md#class_int) **resize** ( new_size: [int](class_int.md#class_int) ) [🔗](class_packedbytearray.md#class_PackedByteArray_method_resize)

Sets the size of the array. If the array is grown, reserves elements at the end of the array. If the array is shrunk, truncates the array to the new size. Calling [resize()](class_packedbytearray.md#class_PackedByteArray_method_resize) once and assigning the new values is faster than adding new elements one by one.

Returns @GlobalScope.OK on success, or one of the following Error constants if this method fails: @GlobalScope.ERR_INVALID_PARAMETER if the size is negative, or @GlobalScope.ERR_OUT_OF_MEMORY if allocations fail. Use [size()](class_packedbytearray.md#class_PackedByteArray_method_size) to find the actual size of the array after resize.

---

<span id="class_PackedByteArray_method_reverse"></span>

void **reverse** ( ) [🔗](class_packedbytearray.md#class_PackedByteArray_method_reverse)

Reverses the order of the elements in the array.

---

<span id="class_PackedByteArray_method_rfind"></span>

[int](class_int.md#class_int) **rfind** ( value: [int](class_int.md#class_int), from: [int](class_int.md#class_int) = -1 ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_rfind)

Searches the array in reverse order. Optionally, a start search index can be passed. If negative, the start index is considered relative to the end of the array.

---

<span id="class_PackedByteArray_method_set"></span>

void **set** ( index: [int](class_int.md#class_int), value: [int](class_int.md#class_int) ) [🔗](class_packedbytearray.md#class_PackedByteArray_method_set)

Changes the byte at the given index.

---

<span id="class_PackedByteArray_method_size"></span>

[int](class_int.md#class_int) **size** ( ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_size)

Returns the number of elements in the array.

---

<span id="class_PackedByteArray_method_slice"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **slice** ( begin: [int](class_int.md#class_int), end: [int](class_int.md#class_int) = 2147483647 ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_slice)

Returns the slice of the **PackedByteArray**, from `begin` (inclusive) to `end` (exclusive), as a new **PackedByteArray**.

The absolute value of `begin` and `end` will be clamped to the array size, so the default value for `end` makes it slice to the size of the array by default (i.e. `arr.slice(1)` is a shorthand for `arr.slice(1, arr.size())`).

If either `begin` or `end` are negative, they will be relative to the end of the array (i.e. `arr.slice(0, -2)` is a shorthand for `arr.slice(0, arr.size() - 2)`).

---

<span id="class_PackedByteArray_method_sort"></span>

void **sort** ( ) [🔗](class_packedbytearray.md#class_PackedByteArray_method_sort)

Sorts the elements of the array in ascending order.

---

<span id="class_PackedByteArray_method_to_color_array"></span>

[PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) **to_color_array** ( ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_to_color_array)

Returns a copy of the data converted to a [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray), where each block of 16 bytes has been converted to a [Color](class_color.md#class_Color) variant.

 **Note:** The size of the input array must be a multiple of 16 (size of four 32-bit float variables). The size of the new array will be `byte_array.size() / 16`. If the original data can't be converted to [Color](class_color.md#class_Color) variants, the resulting data is undefined.

---

<span id="class_PackedByteArray_method_to_float32_array"></span>

[PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) **to_float32_array** ( ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_to_float32_array)

Returns a copy of the data converted to a [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array), where each block of 4 bytes has been converted to a 32-bit float (C++ `float`).

The size of the input array must be a multiple of 4 (size of 32-bit float). The size of the new array will be `byte_array.size() / 4`.

If the original data can't be converted to 32-bit floats, the resulting data is undefined.

---

<span id="class_PackedByteArray_method_to_float64_array"></span>

[PackedFloat64Array](class_packedfloat64array.md#class_PackedFloat64Array) **to_float64_array** ( ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_to_float64_array)

Returns a copy of the data converted to a [PackedFloat64Array](class_packedfloat64array.md#class_PackedFloat64Array), where each block of 8 bytes has been converted to a 64-bit float (C++ `double`, Godot [float](class_float.md#class_float)).

The size of the input array must be a multiple of 8 (size of 64-bit double). The size of the new array will be `byte_array.size() / 8`.

If the original data can't be converted to 64-bit floats, the resulting data is undefined.

---

<span id="class_PackedByteArray_method_to_int32_array"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **to_int32_array** ( ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_to_int32_array)

Returns a copy of the data converted to a [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array), where each block of 4 bytes has been converted to a signed 32-bit integer (C++ `int32_t`).

The size of the input array must be a multiple of 4 (size of 32-bit integer). The size of the new array will be `byte_array.size() / 4`.

If the original data can't be converted to signed 32-bit integers, the resulting data is undefined.

---

<span id="class_PackedByteArray_method_to_int64_array"></span>

[PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) **to_int64_array** ( ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_to_int64_array)

Returns a copy of the data converted to a [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array), where each block of 8 bytes has been converted to a signed 64-bit integer (C++ `int64_t`, Godot [int](class_int.md#class_int)).

The size of the input array must be a multiple of 8 (size of 64-bit integer). The size of the new array will be `byte_array.size() / 8`.

If the original data can't be converted to signed 64-bit integers, the resulting data is undefined.

---

<span id="class_PackedByteArray_method_to_vector2_array"></span>

[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **to_vector2_array** ( ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_to_vector2_array)

Returns a copy of the data converted to a [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array), where each block of 8 bytes or 16 bytes (32-bit or 64-bit) has been converted to a [Vector2](class_vector2.md#class_Vector2) variant.

 **Note:** The size of the input array must be a multiple of 8 or 16 (depending on the build settings, see [Vector2](class_vector2.md#class_Vector2) for more details). The size of the new array will be `byte_array.size() / (8 or 16)`. If the original data can't be converted to [Vector2](class_vector2.md#class_Vector2) variants, the resulting data is undefined.

---

<span id="class_PackedByteArray_method_to_vector3_array"></span>

[PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **to_vector3_array** ( ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_to_vector3_array)

Returns a copy of the data converted to a [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array), where each block of 12 or 24 bytes (32-bit or 64-bit) has been converted to a [Vector3](class_vector3.md#class_Vector3) variant.

 **Note:** The size of the input array must be a multiple of 12 or 24 (depending on the build settings, see [Vector3](class_vector3.md#class_Vector3) for more details). The size of the new array will be `byte_array.size() / (12 or 24)`. If the original data can't be converted to [Vector3](class_vector3.md#class_Vector3) variants, the resulting data is undefined.

---

<span id="class_PackedByteArray_method_to_vector4_array"></span>

[PackedVector4Array](class_packedvector4array.md#class_PackedVector4Array) **to_vector4_array** ( ) *const* [🔗](class_packedbytearray.md#class_PackedByteArray_method_to_vector4_array)

Returns a copy of the data converted to a [PackedVector4Array](class_packedvector4array.md#class_PackedVector4Array), where each block of 16 or 32 bytes (32-bit or 64-bit) has been converted to a [Vector4](class_vector4.md#class_Vector4) variant.

 **Note:** The size of the input array must be a multiple of 16 or 32 (depending on the build settings, see [Vector4](class_vector4.md#class_Vector4) for more details). The size of the new array will be `byte_array.size() / (16 or 32)`. If the original data can't be converted to [Vector4](class_vector4.md#class_Vector4) variants, the resulting data is undefined.

---

### Operator Descriptions

<span id="class_PackedByteArray_operator_neq_PackedByteArray"></span>

[bool](class_bool.md#class_bool) **operator !=** ( right: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_packedbytearray.md#class_PackedByteArray_operator_neq_PackedByteArray)

Returns `true` if contents of the arrays differ.

---

<span id="class_PackedByteArray_operator_sum_PackedByteArray"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **operator +** ( right: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_packedbytearray.md#class_PackedByteArray_operator_sum_PackedByteArray)

Returns a new **PackedByteArray** with contents of `right` added at the end of this array. For better performance, consider using [append_array()](class_packedbytearray.md#class_PackedByteArray_method_append_array) instead.

---

<span id="class_PackedByteArray_operator_eq_PackedByteArray"></span>

[bool](class_bool.md#class_bool) **operator ==** ( right: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_packedbytearray.md#class_PackedByteArray_operator_eq_PackedByteArray)

Returns `true` if contents of both arrays are the same, i.e. they have all equal bytes at the corresponding indices.

---

<span id="class_PackedByteArray_operator_idx_int"></span>

[int](class_int.md#class_int) **operator []** ( index: [int](class_int.md#class_int) ) [🔗](class_packedbytearray.md#class_PackedByteArray_operator_idx_int)

Returns the byte at index `index`. Negative indices can be used to access the elements starting from the end. Using index out of array's bounds will result in an error.

Note that the byte is returned as a 64-bit [int](class_int.md#class_int).
