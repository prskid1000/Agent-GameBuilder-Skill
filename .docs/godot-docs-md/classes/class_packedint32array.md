<span id="class_PackedInt32Array"></span>

## PackedInt32Array

A packed array of 32-bit integers.

### Description

An array specifically designed to hold 32-bit integer values. Packs data tightly, so it saves memory for large array sizes.

 **Note:** This type stores signed 32-bit integers, which means it can take values in the interval `[-2^31, 2^31 - 1]`, i.e. `[-2147483648, 2147483647]`. Exceeding those bounds will wrap around. In comparison, [int](class_int.md#class_int) uses signed 64-bit integers which can hold much larger values. If you need to pack 64-bit integers tightly, see [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array).

 **Note:** Packed arrays are always passed by reference. To get a copy of an array that can be modified independently of the original array, use [duplicate()](class_packedint32array.md#class_PackedInt32Array_method_duplicate). This is *not* the case for built-in properties and methods. In these cases the returned packed array is a copy, and changing it will *not* affect the original value. To update a built-in property of this type, modify the returned array and then assign it to the property again.

 **Note:** In a boolean context, a packed array will evaluate to `false` if it's empty. Otherwise, a packed array will always evaluate to `true`.

> **Note:** There are notable differences when using this API with C#. See :ref:`doc_c_sharp_differences` for more information.

### Constructors


| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array_constructor_PackedInt32Array) ( ) |
| --- | --- |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array_constructor_PackedInt32Array) ( from: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array_constructor_PackedInt32Array) ( from: [Array](class_array.md#class_Array) ) |

### Methods


| [bool](class_bool.md#class_bool) | [append](class_packedint32array.md#class_PackedInt32Array_method_append) ( value: [int](class_int.md#class_int) ) |
| --- | --- |
| void | [append_array](class_packedint32array.md#class_PackedInt32Array_method_append_array) ( array: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) |
| [int](class_int.md#class_int) | [bsearch](class_packedint32array.md#class_PackedInt32Array_method_bsearch) ( value: [int](class_int.md#class_int), before: [bool](class_bool.md#class_bool) = true ) const |
| void | [clear](class_packedint32array.md#class_PackedInt32Array_method_clear) ( ) |
| [int](class_int.md#class_int) | [count](class_packedint32array.md#class_PackedInt32Array_method_count) ( value: [int](class_int.md#class_int) ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [duplicate](class_packedint32array.md#class_PackedInt32Array_method_duplicate) ( ) const |
| [bool](class_bool.md#class_bool) | [erase](class_packedint32array.md#class_PackedInt32Array_method_erase) ( value: [int](class_int.md#class_int) ) |
| void | [fill](class_packedint32array.md#class_PackedInt32Array_method_fill) ( value: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [find](class_packedint32array.md#class_PackedInt32Array_method_find) ( value: [int](class_int.md#class_int), from: [int](class_int.md#class_int) = 0 ) const |
| [int](class_int.md#class_int) | [get](class_packedint32array.md#class_PackedInt32Array_method_get) ( index: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [has](class_packedint32array.md#class_PackedInt32Array_method_has) ( value: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [insert](class_packedint32array.md#class_PackedInt32Array_method_insert) ( at_index: [int](class_int.md#class_int), value: [int](class_int.md#class_int) ) |
| [bool](class_bool.md#class_bool) | [is_empty](class_packedint32array.md#class_PackedInt32Array_method_is_empty) ( ) const |
| [bool](class_bool.md#class_bool) | [push_back](class_packedint32array.md#class_PackedInt32Array_method_push_back) ( value: [int](class_int.md#class_int) ) |
| void | [remove_at](class_packedint32array.md#class_PackedInt32Array_method_remove_at) ( index: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [resize](class_packedint32array.md#class_PackedInt32Array_method_resize) ( new_size: [int](class_int.md#class_int) ) |
| void | [reverse](class_packedint32array.md#class_PackedInt32Array_method_reverse) ( ) |
| [int](class_int.md#class_int) | [rfind](class_packedint32array.md#class_PackedInt32Array_method_rfind) ( value: [int](class_int.md#class_int), from: [int](class_int.md#class_int) = -1 ) const |
| void | [set](class_packedint32array.md#class_PackedInt32Array_method_set) ( index: [int](class_int.md#class_int), value: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [size](class_packedint32array.md#class_PackedInt32Array_method_size) ( ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [slice](class_packedint32array.md#class_PackedInt32Array_method_slice) ( begin: [int](class_int.md#class_int), end: [int](class_int.md#class_int) = 2147483647 ) const |
| void | [sort](class_packedint32array.md#class_PackedInt32Array_method_sort) ( ) |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [to_byte_array](class_packedint32array.md#class_PackedInt32Array_method_to_byte_array) ( ) const |

### Operators


| [bool](class_bool.md#class_bool) | [operator !=](class_packedint32array.md#class_PackedInt32Array_operator_neq_PackedInt32Array) ( right: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) |
| --- | --- |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [operator +](class_packedint32array.md#class_PackedInt32Array_operator_sum_PackedInt32Array) ( right: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) |
| [bool](class_bool.md#class_bool) | [operator ==](class_packedint32array.md#class_PackedInt32Array_operator_eq_PackedInt32Array) ( right: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) |
| [int](class_int.md#class_int) | [operator []](class_packedint32array.md#class_PackedInt32Array_operator_idx_int) ( index: [int](class_int.md#class_int) ) |

---

### Constructor Descriptions

<span id="class_PackedInt32Array_constructor_PackedInt32Array"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **PackedInt32Array** ( ) [🔗](class_packedint32array.md#class_PackedInt32Array_constructor_PackedInt32Array)

Constructs an empty **PackedInt32Array**.

---

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **PackedInt32Array** ( from: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) )

Constructs a **PackedInt32Array** as a copy of the given **PackedInt32Array**.

---

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **PackedInt32Array** ( from: [Array](class_array.md#class_Array) )

Constructs a new **PackedInt32Array**. Optionally, you can pass in a generic [Array](class_array.md#class_Array) that will be converted.

---

### Method Descriptions

<span id="class_PackedInt32Array_method_append"></span>

[bool](class_bool.md#class_bool) **append** ( value: [int](class_int.md#class_int) ) [🔗](class_packedint32array.md#class_PackedInt32Array_method_append)

Appends an element at the end of the array (alias of [push_back()](class_packedint32array.md#class_PackedInt32Array_method_push_back)).

---

<span id="class_PackedInt32Array_method_append_array"></span>

void **append_array** ( array: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) [🔗](class_packedint32array.md#class_PackedInt32Array_method_append_array)

Appends a **PackedInt32Array** at the end of this array.

---

<span id="class_PackedInt32Array_method_bsearch"></span>

[int](class_int.md#class_int) **bsearch** ( value: [int](class_int.md#class_int), before: [bool](class_bool.md#class_bool) = true ) *const* [🔗](class_packedint32array.md#class_PackedInt32Array_method_bsearch)

Finds the index of an existing value (or the insertion index that maintains sorting order, if the value is not yet present in the array) using binary search. Optionally, a `before` specifier can be passed. If `false`, the returned index comes after all existing entries of the value in the array.

 **Note:** Calling [bsearch()](class_packedint32array.md#class_PackedInt32Array_method_bsearch) on an unsorted array results in unexpected behavior.

---

<span id="class_PackedInt32Array_method_clear"></span>

void **clear** ( ) [🔗](class_packedint32array.md#class_PackedInt32Array_method_clear)

Clears the array. This is equivalent to using [resize()](class_packedint32array.md#class_PackedInt32Array_method_resize) with a size of `0`.

---

<span id="class_PackedInt32Array_method_count"></span>

[int](class_int.md#class_int) **count** ( value: [int](class_int.md#class_int) ) *const* [🔗](class_packedint32array.md#class_PackedInt32Array_method_count)

Returns the number of times an element is in the array.

---

<span id="class_PackedInt32Array_method_duplicate"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **duplicate** ( ) *const* [🔗](class_packedint32array.md#class_PackedInt32Array_method_duplicate)

Creates a copy of the array, and returns it.

---

<span id="class_PackedInt32Array_method_erase"></span>

[bool](class_bool.md#class_bool) **erase** ( value: [int](class_int.md#class_int) ) [🔗](class_packedint32array.md#class_PackedInt32Array_method_erase)

Removes the first occurrence of a value from the array and returns `true`. If the value does not exist in the array, nothing happens and `false` is returned. To remove an element by index, use [remove_at()](class_packedint32array.md#class_PackedInt32Array_method_remove_at) instead.

---

<span id="class_PackedInt32Array_method_fill"></span>

void **fill** ( value: [int](class_int.md#class_int) ) [🔗](class_packedint32array.md#class_PackedInt32Array_method_fill)

Assigns the given value to all elements in the array. This can typically be used together with [resize()](class_packedint32array.md#class_PackedInt32Array_method_resize) to create an array with a given size and initialized elements.

---

<span id="class_PackedInt32Array_method_find"></span>

[int](class_int.md#class_int) **find** ( value: [int](class_int.md#class_int), from: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_packedint32array.md#class_PackedInt32Array_method_find)

Searches the array for a value and returns its index or `-1` if not found. Optionally, the initial search index can be passed.

---

<span id="class_PackedInt32Array_method_get"></span>

[int](class_int.md#class_int) **get** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_packedint32array.md#class_PackedInt32Array_method_get)

Returns the 32-bit integer at the given `index` in the array. If `index` is out-of-bounds or negative, this method fails and returns `0`.

This method is similar (but not identical) to the `[]` operator. Most notably, when this method fails, it doesn't pause project execution if run from the editor.

---

<span id="class_PackedInt32Array_method_has"></span>

[bool](class_bool.md#class_bool) **has** ( value: [int](class_int.md#class_int) ) *const* [🔗](class_packedint32array.md#class_PackedInt32Array_method_has)

Returns `true` if the array contains `value`.

---

<span id="class_PackedInt32Array_method_insert"></span>

[int](class_int.md#class_int) **insert** ( at_index: [int](class_int.md#class_int), value: [int](class_int.md#class_int) ) [🔗](class_packedint32array.md#class_PackedInt32Array_method_insert)

Inserts a new integer at a given position in the array. The position must be valid, or at the end of the array (`idx == size()`).

---

<span id="class_PackedInt32Array_method_is_empty"></span>

[bool](class_bool.md#class_bool) **is_empty** ( ) *const* [🔗](class_packedint32array.md#class_PackedInt32Array_method_is_empty)

Returns `true` if the array is empty.

---

<span id="class_PackedInt32Array_method_push_back"></span>

[bool](class_bool.md#class_bool) **push_back** ( value: [int](class_int.md#class_int) ) [🔗](class_packedint32array.md#class_PackedInt32Array_method_push_back)

Appends a value to the array.

---

<span id="class_PackedInt32Array_method_remove_at"></span>

void **remove_at** ( index: [int](class_int.md#class_int) ) [🔗](class_packedint32array.md#class_PackedInt32Array_method_remove_at)

Removes an element from the array by index.

---

<span id="class_PackedInt32Array_method_resize"></span>

[int](class_int.md#class_int) **resize** ( new_size: [int](class_int.md#class_int) ) [🔗](class_packedint32array.md#class_PackedInt32Array_method_resize)

Sets the size of the array. If the array is grown, reserves elements at the end of the array. If the array is shrunk, truncates the array to the new size. Calling [resize()](class_packedint32array.md#class_PackedInt32Array_method_resize) once and assigning the new values is faster than adding new elements one by one.

Returns @GlobalScope.OK on success, or one of the following Error constants if this method fails: @GlobalScope.ERR_INVALID_PARAMETER if the size is negative, or @GlobalScope.ERR_OUT_OF_MEMORY if allocations fail. Use [size()](class_packedint32array.md#class_PackedInt32Array_method_size) to find the actual size of the array after resize.

---

<span id="class_PackedInt32Array_method_reverse"></span>

void **reverse** ( ) [🔗](class_packedint32array.md#class_PackedInt32Array_method_reverse)

Reverses the order of the elements in the array.

---

<span id="class_PackedInt32Array_method_rfind"></span>

[int](class_int.md#class_int) **rfind** ( value: [int](class_int.md#class_int), from: [int](class_int.md#class_int) = -1 ) *const* [🔗](class_packedint32array.md#class_PackedInt32Array_method_rfind)

Searches the array in reverse order. Optionally, a start search index can be passed. If negative, the start index is considered relative to the end of the array.

---

<span id="class_PackedInt32Array_method_set"></span>

void **set** ( index: [int](class_int.md#class_int), value: [int](class_int.md#class_int) ) [🔗](class_packedint32array.md#class_PackedInt32Array_method_set)

Changes the integer at the given index.

---

<span id="class_PackedInt32Array_method_size"></span>

[int](class_int.md#class_int) **size** ( ) *const* [🔗](class_packedint32array.md#class_PackedInt32Array_method_size)

Returns the number of elements in the array.

---

<span id="class_PackedInt32Array_method_slice"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **slice** ( begin: [int](class_int.md#class_int), end: [int](class_int.md#class_int) = 2147483647 ) *const* [🔗](class_packedint32array.md#class_PackedInt32Array_method_slice)

Returns the slice of the **PackedInt32Array**, from `begin` (inclusive) to `end` (exclusive), as a new **PackedInt32Array**.

The absolute value of `begin` and `end` will be clamped to the array size, so the default value for `end` makes it slice to the size of the array by default (i.e. `arr.slice(1)` is a shorthand for `arr.slice(1, arr.size())`).

If either `begin` or `end` are negative, they will be relative to the end of the array (i.e. `arr.slice(0, -2)` is a shorthand for `arr.slice(0, arr.size() - 2)`).

---

<span id="class_PackedInt32Array_method_sort"></span>

void **sort** ( ) [🔗](class_packedint32array.md#class_PackedInt32Array_method_sort)

Sorts the elements of the array in ascending order.

---

<span id="class_PackedInt32Array_method_to_byte_array"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **to_byte_array** ( ) *const* [🔗](class_packedint32array.md#class_PackedInt32Array_method_to_byte_array)

Returns a copy of the data converted to a [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), where each element has been encoded as 4 bytes.

The size of the new array will be `int32_array.size() * 4`.

---

### Operator Descriptions

<span id="class_PackedInt32Array_operator_neq_PackedInt32Array"></span>

[bool](class_bool.md#class_bool) **operator !=** ( right: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) [🔗](class_packedint32array.md#class_PackedInt32Array_operator_neq_PackedInt32Array)

Returns `true` if contents of the arrays differ.

---

<span id="class_PackedInt32Array_operator_sum_PackedInt32Array"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **operator +** ( right: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) [🔗](class_packedint32array.md#class_PackedInt32Array_operator_sum_PackedInt32Array)

Returns a new **PackedInt32Array** with contents of `right` added at the end of this array. For better performance, consider using [append_array()](class_packedint32array.md#class_PackedInt32Array_method_append_array) instead.

---

<span id="class_PackedInt32Array_operator_eq_PackedInt32Array"></span>

[bool](class_bool.md#class_bool) **operator ==** ( right: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) [🔗](class_packedint32array.md#class_PackedInt32Array_operator_eq_PackedInt32Array)

Returns `true` if contents of both arrays are the same, i.e. they have all equal ints at the corresponding indices.

---

<span id="class_PackedInt32Array_operator_idx_int"></span>

[int](class_int.md#class_int) **operator []** ( index: [int](class_int.md#class_int) ) [🔗](class_packedint32array.md#class_PackedInt32Array_operator_idx_int)

Returns the [int](class_int.md#class_int) at index `index`. Negative indices can be used to access the elements starting from the end. Using index out of array's bounds will result in an error.

Note that [int](class_int.md#class_int) type is 64-bit, unlike the values stored in the array.
