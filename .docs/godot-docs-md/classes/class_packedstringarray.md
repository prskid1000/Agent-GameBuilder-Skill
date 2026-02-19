<span id="class_PackedStringArray"></span>

## PackedStringArray

A packed array of [String](class_string.md#class_String) s.

### Description

An array specifically designed to hold [String](class_string.md#class_String) s. Packs data tightly, so it saves memory for large array sizes.

If you want to join the strings in the array, use [String.join()](class_string.md#class_String_method_join).

::

    var string_array = PackedStringArray(["hello", "world"])
    var string = " ".join(string_array)
    print(string) # "hello world"

 **Differences between packed arrays, typed arrays, and untyped arrays:** Packed arrays are generally faster to iterate on and modify compared to a typed array of the same type (e.g. **PackedStringArray** versus `Array[String]`). Also, packed arrays consume less memory. As a downside, packed arrays are less flexible as they don't offer as many convenience methods such as [Array.map()](class_array.md#class_Array_method_map). Typed arrays are in turn faster to iterate on and modify than untyped arrays.

 **Note:** Packed arrays are always passed by reference. To get a copy of an array that can be modified independently of the original array, use [duplicate()](class_packedstringarray.md#class_PackedStringArray_method_duplicate). This is *not* the case for built-in properties and methods. In these cases the returned packed array is a copy, and changing it will *not* affect the original value. To update a built-in property of this type, modify the returned array and then assign it to the property again.

 **Note:** In a boolean context, a packed array will evaluate to `false` if it's empty. Otherwise, a packed array will always evaluate to `true`.

> **Note:** There are notable differences when using this API with C#. See :ref:`doc_c_sharp_differences` for more information.

### Tutorials

- Operating System Testing Demo

### Constructors


| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [PackedStringArray](class_packedstringarray.md#class_PackedStringArray_constructor_PackedStringArray) ( ) |
| --- | --- |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [PackedStringArray](class_packedstringarray.md#class_PackedStringArray_constructor_PackedStringArray) ( from: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [PackedStringArray](class_packedstringarray.md#class_PackedStringArray_constructor_PackedStringArray) ( from: [Array](class_array.md#class_Array) ) |

### Methods


| [bool](class_bool.md#class_bool) | [append](class_packedstringarray.md#class_PackedStringArray_method_append) ( value: [String](class_string.md#class_String) ) |
| --- | --- |
| void | [append_array](class_packedstringarray.md#class_PackedStringArray_method_append_array) ( array: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) |
| [int](class_int.md#class_int) | [bsearch](class_packedstringarray.md#class_PackedStringArray_method_bsearch) ( value: [String](class_string.md#class_String), before: [bool](class_bool.md#class_bool) = true ) const |
| void | [clear](class_packedstringarray.md#class_PackedStringArray_method_clear) ( ) |
| [int](class_int.md#class_int) | [count](class_packedstringarray.md#class_PackedStringArray_method_count) ( value: [String](class_string.md#class_String) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [duplicate](class_packedstringarray.md#class_PackedStringArray_method_duplicate) ( ) const |
| [bool](class_bool.md#class_bool) | [erase](class_packedstringarray.md#class_PackedStringArray_method_erase) ( value: [String](class_string.md#class_String) ) |
| void | [fill](class_packedstringarray.md#class_PackedStringArray_method_fill) ( value: [String](class_string.md#class_String) ) |
| [int](class_int.md#class_int) | [find](class_packedstringarray.md#class_PackedStringArray_method_find) ( value: [String](class_string.md#class_String), from: [int](class_int.md#class_int) = 0 ) const |
| [String](class_string.md#class_String) | [get](class_packedstringarray.md#class_PackedStringArray_method_get) ( index: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [has](class_packedstringarray.md#class_PackedStringArray_method_has) ( value: [String](class_string.md#class_String) ) const |
| [int](class_int.md#class_int) | [insert](class_packedstringarray.md#class_PackedStringArray_method_insert) ( at_index: [int](class_int.md#class_int), value: [String](class_string.md#class_String) ) |
| [bool](class_bool.md#class_bool) | [is_empty](class_packedstringarray.md#class_PackedStringArray_method_is_empty) ( ) const |
| [bool](class_bool.md#class_bool) | [push_back](class_packedstringarray.md#class_PackedStringArray_method_push_back) ( value: [String](class_string.md#class_String) ) |
| void | [remove_at](class_packedstringarray.md#class_PackedStringArray_method_remove_at) ( index: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [resize](class_packedstringarray.md#class_PackedStringArray_method_resize) ( new_size: [int](class_int.md#class_int) ) |
| void | [reverse](class_packedstringarray.md#class_PackedStringArray_method_reverse) ( ) |
| [int](class_int.md#class_int) | [rfind](class_packedstringarray.md#class_PackedStringArray_method_rfind) ( value: [String](class_string.md#class_String), from: [int](class_int.md#class_int) = -1 ) const |
| void | [set](class_packedstringarray.md#class_PackedStringArray_method_set) ( index: [int](class_int.md#class_int), value: [String](class_string.md#class_String) ) |
| [int](class_int.md#class_int) | [size](class_packedstringarray.md#class_PackedStringArray_method_size) ( ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [slice](class_packedstringarray.md#class_PackedStringArray_method_slice) ( begin: [int](class_int.md#class_int), end: [int](class_int.md#class_int) = 2147483647 ) const |
| void | [sort](class_packedstringarray.md#class_PackedStringArray_method_sort) ( ) |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [to_byte_array](class_packedstringarray.md#class_PackedStringArray_method_to_byte_array) ( ) const |

### Operators


| [bool](class_bool.md#class_bool) | [operator !=](class_packedstringarray.md#class_PackedStringArray_operator_neq_PackedStringArray) ( right: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) |
| --- | --- |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [operator +](class_packedstringarray.md#class_PackedStringArray_operator_sum_PackedStringArray) ( right: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) |
| [bool](class_bool.md#class_bool) | [operator ==](class_packedstringarray.md#class_PackedStringArray_operator_eq_PackedStringArray) ( right: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) |
| [String](class_string.md#class_String) | [operator []](class_packedstringarray.md#class_PackedStringArray_operator_idx_int) ( index: [int](class_int.md#class_int) ) |

---

### Constructor Descriptions

<span id="class_PackedStringArray_constructor_PackedStringArray"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **PackedStringArray** ( ) [🔗](class_packedstringarray.md#class_PackedStringArray_constructor_PackedStringArray)

Constructs an empty **PackedStringArray**.

---

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **PackedStringArray** ( from: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) )

Constructs a **PackedStringArray** as a copy of the given **PackedStringArray**.

---

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **PackedStringArray** ( from: [Array](class_array.md#class_Array) )

Constructs a new **PackedStringArray**. Optionally, you can pass in a generic [Array](class_array.md#class_Array) that will be converted.

---

### Method Descriptions

<span id="class_PackedStringArray_method_append"></span>

[bool](class_bool.md#class_bool) **append** ( value: [String](class_string.md#class_String) ) [🔗](class_packedstringarray.md#class_PackedStringArray_method_append)

Appends an element at the end of the array (alias of [push_back()](class_packedstringarray.md#class_PackedStringArray_method_push_back)).

---

<span id="class_PackedStringArray_method_append_array"></span>

void **append_array** ( array: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) [🔗](class_packedstringarray.md#class_PackedStringArray_method_append_array)

Appends a **PackedStringArray** at the end of this array.

---

<span id="class_PackedStringArray_method_bsearch"></span>

[int](class_int.md#class_int) **bsearch** ( value: [String](class_string.md#class_String), before: [bool](class_bool.md#class_bool) = true ) *const* [🔗](class_packedstringarray.md#class_PackedStringArray_method_bsearch)

Finds the index of an existing value (or the insertion index that maintains sorting order, if the value is not yet present in the array) using binary search. Optionally, a `before` specifier can be passed. If `false`, the returned index comes after all existing entries of the value in the array.

 **Note:** Calling [bsearch()](class_packedstringarray.md#class_PackedStringArray_method_bsearch) on an unsorted array results in unexpected behavior.

---

<span id="class_PackedStringArray_method_clear"></span>

void **clear** ( ) [🔗](class_packedstringarray.md#class_PackedStringArray_method_clear)

Clears the array. This is equivalent to using [resize()](class_packedstringarray.md#class_PackedStringArray_method_resize) with a size of `0`.

---

<span id="class_PackedStringArray_method_count"></span>

[int](class_int.md#class_int) **count** ( value: [String](class_string.md#class_String) ) *const* [🔗](class_packedstringarray.md#class_PackedStringArray_method_count)

Returns the number of times an element is in the array.

---

<span id="class_PackedStringArray_method_duplicate"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **duplicate** ( ) *const* [🔗](class_packedstringarray.md#class_PackedStringArray_method_duplicate)

Creates a copy of the array, and returns it.

---

<span id="class_PackedStringArray_method_erase"></span>

[bool](class_bool.md#class_bool) **erase** ( value: [String](class_string.md#class_String) ) [🔗](class_packedstringarray.md#class_PackedStringArray_method_erase)

Removes the first occurrence of a value from the array and returns `true`. If the value does not exist in the array, nothing happens and `false` is returned. To remove an element by index, use [remove_at()](class_packedstringarray.md#class_PackedStringArray_method_remove_at) instead.

---

<span id="class_PackedStringArray_method_fill"></span>

void **fill** ( value: [String](class_string.md#class_String) ) [🔗](class_packedstringarray.md#class_PackedStringArray_method_fill)

Assigns the given value to all elements in the array. This can typically be used together with [resize()](class_packedstringarray.md#class_PackedStringArray_method_resize) to create an array with a given size and initialized elements.

---

<span id="class_PackedStringArray_method_find"></span>

[int](class_int.md#class_int) **find** ( value: [String](class_string.md#class_String), from: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_packedstringarray.md#class_PackedStringArray_method_find)

Searches the array for a value and returns its index or `-1` if not found. Optionally, the initial search index can be passed.

---

<span id="class_PackedStringArray_method_get"></span>

[String](class_string.md#class_String) **get** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_packedstringarray.md#class_PackedStringArray_method_get)

Returns the [String](class_string.md#class_String) at the given `index` in the array. If `index` is out-of-bounds or negative, this method fails and returns an empty string.

This method is similar (but not identical) to the `[]` operator. Most notably, when this method fails, it doesn't pause project execution if run from the editor.

---

<span id="class_PackedStringArray_method_has"></span>

[bool](class_bool.md#class_bool) **has** ( value: [String](class_string.md#class_String) ) *const* [🔗](class_packedstringarray.md#class_PackedStringArray_method_has)

Returns `true` if the array contains `value`.

---

<span id="class_PackedStringArray_method_insert"></span>

[int](class_int.md#class_int) **insert** ( at_index: [int](class_int.md#class_int), value: [String](class_string.md#class_String) ) [🔗](class_packedstringarray.md#class_PackedStringArray_method_insert)

Inserts a new element at a given position in the array. The position must be valid, or at the end of the array (`idx == size()`).

---

<span id="class_PackedStringArray_method_is_empty"></span>

[bool](class_bool.md#class_bool) **is_empty** ( ) *const* [🔗](class_packedstringarray.md#class_PackedStringArray_method_is_empty)

Returns `true` if the array is empty.

---

<span id="class_PackedStringArray_method_push_back"></span>

[bool](class_bool.md#class_bool) **push_back** ( value: [String](class_string.md#class_String) ) [🔗](class_packedstringarray.md#class_PackedStringArray_method_push_back)

Appends a string element at end of the array.

---

<span id="class_PackedStringArray_method_remove_at"></span>

void **remove_at** ( index: [int](class_int.md#class_int) ) [🔗](class_packedstringarray.md#class_PackedStringArray_method_remove_at)

Removes an element from the array by index.

---

<span id="class_PackedStringArray_method_resize"></span>

[int](class_int.md#class_int) **resize** ( new_size: [int](class_int.md#class_int) ) [🔗](class_packedstringarray.md#class_PackedStringArray_method_resize)

Sets the size of the array. If the array is grown, reserves elements at the end of the array. If the array is shrunk, truncates the array to the new size. Calling [resize()](class_packedstringarray.md#class_PackedStringArray_method_resize) once and assigning the new values is faster than adding new elements one by one.

Returns @GlobalScope.OK on success, or one of the following Error constants if this method fails: @GlobalScope.ERR_INVALID_PARAMETER if the size is negative, or @GlobalScope.ERR_OUT_OF_MEMORY if allocations fail. Use [size()](class_packedstringarray.md#class_PackedStringArray_method_size) to find the actual size of the array after resize.

---

<span id="class_PackedStringArray_method_reverse"></span>

void **reverse** ( ) [🔗](class_packedstringarray.md#class_PackedStringArray_method_reverse)

Reverses the order of the elements in the array.

---

<span id="class_PackedStringArray_method_rfind"></span>

[int](class_int.md#class_int) **rfind** ( value: [String](class_string.md#class_String), from: [int](class_int.md#class_int) = -1 ) *const* [🔗](class_packedstringarray.md#class_PackedStringArray_method_rfind)

Searches the array in reverse order. Optionally, a start search index can be passed. If negative, the start index is considered relative to the end of the array.

---

<span id="class_PackedStringArray_method_set"></span>

void **set** ( index: [int](class_int.md#class_int), value: [String](class_string.md#class_String) ) [🔗](class_packedstringarray.md#class_PackedStringArray_method_set)

Changes the [String](class_string.md#class_String) at the given index.

---

<span id="class_PackedStringArray_method_size"></span>

[int](class_int.md#class_int) **size** ( ) *const* [🔗](class_packedstringarray.md#class_PackedStringArray_method_size)

Returns the number of elements in the array.

---

<span id="class_PackedStringArray_method_slice"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **slice** ( begin: [int](class_int.md#class_int), end: [int](class_int.md#class_int) = 2147483647 ) *const* [🔗](class_packedstringarray.md#class_PackedStringArray_method_slice)

Returns the slice of the **PackedStringArray**, from `begin` (inclusive) to `end` (exclusive), as a new **PackedStringArray**.

The absolute value of `begin` and `end` will be clamped to the array size, so the default value for `end` makes it slice to the size of the array by default (i.e. `arr.slice(1)` is a shorthand for `arr.slice(1, arr.size())`).

If either `begin` or `end` are negative, they will be relative to the end of the array (i.e. `arr.slice(0, -2)` is a shorthand for `arr.slice(0, arr.size() - 2)`).

---

<span id="class_PackedStringArray_method_sort"></span>

void **sort** ( ) [🔗](class_packedstringarray.md#class_PackedStringArray_method_sort)

Sorts the elements of the array in ascending order.

---

<span id="class_PackedStringArray_method_to_byte_array"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **to_byte_array** ( ) *const* [🔗](class_packedstringarray.md#class_PackedStringArray_method_to_byte_array)

Returns a [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) with each string encoded as UTF-8. Strings are `null` terminated.

---

### Operator Descriptions

<span id="class_PackedStringArray_operator_neq_PackedStringArray"></span>

[bool](class_bool.md#class_bool) **operator !=** ( right: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) [🔗](class_packedstringarray.md#class_PackedStringArray_operator_neq_PackedStringArray)

Returns `true` if contents of the arrays differ.

---

<span id="class_PackedStringArray_operator_sum_PackedStringArray"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **operator +** ( right: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) [🔗](class_packedstringarray.md#class_PackedStringArray_operator_sum_PackedStringArray)

Returns a new **PackedStringArray** with contents of `right` added at the end of this array. For better performance, consider using [append_array()](class_packedstringarray.md#class_PackedStringArray_method_append_array) instead.

---

<span id="class_PackedStringArray_operator_eq_PackedStringArray"></span>

[bool](class_bool.md#class_bool) **operator ==** ( right: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) [🔗](class_packedstringarray.md#class_PackedStringArray_operator_eq_PackedStringArray)

Returns `true` if contents of both arrays are the same, i.e. they have all equal [String](class_string.md#class_String) s at the corresponding indices.

---

<span id="class_PackedStringArray_operator_idx_int"></span>

[String](class_string.md#class_String) **operator []** ( index: [int](class_int.md#class_int) ) [🔗](class_packedstringarray.md#class_PackedStringArray_operator_idx_int)

Returns the [String](class_string.md#class_String) at index `index`. Negative indices can be used to access the elements starting from the end. Using index out of array's bounds will result in an error.
