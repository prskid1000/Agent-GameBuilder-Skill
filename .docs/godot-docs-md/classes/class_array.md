<span id="class_Array"></span>

## Array

A built-in data structure that holds a sequence of elements.

### Description

An array data structure that can contain a sequence of elements of any [Variant](class_variant.md#class_Variant) type by default. Values can optionally be constrained to a specific type by creating a *typed array*. Elements are accessed by a numerical index starting at `0`. Negative indices are used to count from the back (`-1` is the last element, `-2` is the second to last, etc.).

.. tabs::

```
```

    var array = ["First", 2, 3, "Last"]
    print(array[0])  # Prints "First"
    print(array[2])  # Prints 3
    print(array[-1]) # Prints "Last"

    array[1] = "Second"
    print(array[1])  # Prints "Second"
    print(array[-3]) # Prints "Second"

    # This typed array can only contain integers.
    # Attempting to add any other type will result in an error.
    var typed_array: Array[int] = [1, 2, 3]

```
```

    Godot.Collections.Array array = ["First", 2, 3, "Last"];
    GD.Print(array[0]); // Prints "First"
    GD.Print(array[2]); // Prints 3
    GD.Print(array[^1]); // Prints "Last"

    array[1] = "Second";
    GD.Print(array[1]); // Prints "Second"
    GD.Print(array[^3]); // Prints "Second"

    // This typed array can only contain integers.
    // Attempting to add any other type will result in an error.
    Godot.Collections.Array<int> typedArray = [1, 2, 3];

 **Note:** Arrays are always passed by **reference**. To get a copy of an array that can be modified independently of the original array, use [duplicate()](class_array.md#class_Array_method_duplicate).

 **Note:** Erasing elements while iterating over arrays is **not** supported and will result in unpredictable behavior.

 **Note:** In a boolean context, an array will evaluate to `false` if it's empty (`[]`). Otherwise, an array will always evaluate to `true`.

 **Differences between packed arrays, typed arrays, and untyped arrays:** Packed arrays are generally faster to iterate on and modify compared to a typed array of the same type (e.g. [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) versus `Array[int]`). Also, packed arrays consume less memory. As a downside, packed arrays are less flexible as they don't offer as many convenience methods such as [map()](class_array.md#class_Array_method_map). Typed arrays are in turn faster to iterate on and modify than untyped arrays.

> **Note:** There are notable differences when using this API with C#. See :ref:`doc_c_sharp_differences` for more information.

### Constructors


| [Array](class_array.md#class_Array) | [Array](class_array.md#class_Array_constructor_Array) ( ) |
| --- | --- |
| [Array](class_array.md#class_Array) | [Array](class_array.md#class_Array_constructor_Array) ( base: [Array](class_array.md#class_Array), type: [int](class_int.md#class_int), class_name: [StringName](class_stringname.md#class_StringName), script: [Variant](class_variant.md#class_Variant) ) |
| [Array](class_array.md#class_Array) | [Array](class_array.md#class_Array_constructor_Array) ( from: [Array](class_array.md#class_Array) ) |
| [Array](class_array.md#class_Array) | [Array](class_array.md#class_Array_constructor_Array) ( from: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| [Array](class_array.md#class_Array) | [Array](class_array.md#class_Array_constructor_Array) ( from: [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) ) |
| [Array](class_array.md#class_Array) | [Array](class_array.md#class_Array_constructor_Array) ( from: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) ) |
| [Array](class_array.md#class_Array) | [Array](class_array.md#class_Array_constructor_Array) ( from: [PackedFloat64Array](class_packedfloat64array.md#class_PackedFloat64Array) ) |
| [Array](class_array.md#class_Array) | [Array](class_array.md#class_Array_constructor_Array) ( from: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) |
| [Array](class_array.md#class_Array) | [Array](class_array.md#class_Array_constructor_Array) ( from: [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) ) |
| [Array](class_array.md#class_Array) | [Array](class_array.md#class_Array_constructor_Array) ( from: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) |
| [Array](class_array.md#class_Array) | [Array](class_array.md#class_Array_constructor_Array) ( from: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) ) |
| [Array](class_array.md#class_Array) | [Array](class_array.md#class_Array_constructor_Array) ( from: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) ) |
| [Array](class_array.md#class_Array) | [Array](class_array.md#class_Array_constructor_Array) ( from: [PackedVector4Array](class_packedvector4array.md#class_PackedVector4Array) ) |

### Methods


| [bool](class_bool.md#class_bool) | [all](class_array.md#class_Array_method_all) ( method: [Callable](class_callable.md#class_Callable) ) const |
| --- | --- |
| [bool](class_bool.md#class_bool) | [any](class_array.md#class_Array_method_any) ( method: [Callable](class_callable.md#class_Callable) ) const |
| void | [append](class_array.md#class_Array_method_append) ( value: [Variant](class_variant.md#class_Variant) ) |
| void | [append_array](class_array.md#class_Array_method_append_array) ( array: [Array](class_array.md#class_Array) ) |
| void | [assign](class_array.md#class_Array_method_assign) ( array: [Array](class_array.md#class_Array) ) |
| [Variant](class_variant.md#class_Variant) | [back](class_array.md#class_Array_method_back) ( ) const |
| [int](class_int.md#class_int) | [bsearch](class_array.md#class_Array_method_bsearch) ( value: [Variant](class_variant.md#class_Variant), before: [bool](class_bool.md#class_bool) = true ) const |
| [int](class_int.md#class_int) | [bsearch_custom](class_array.md#class_Array_method_bsearch_custom) ( value: [Variant](class_variant.md#class_Variant), func: [Callable](class_callable.md#class_Callable), before: [bool](class_bool.md#class_bool) = true ) const |
| void | [clear](class_array.md#class_Array_method_clear) ( ) |
| [int](class_int.md#class_int) | [count](class_array.md#class_Array_method_count) ( value: [Variant](class_variant.md#class_Variant) ) const |
| [Array](class_array.md#class_Array) | [duplicate](class_array.md#class_Array_method_duplicate) ( deep: [bool](class_bool.md#class_bool) = false ) const |
| [Array](class_array.md#class_Array) | [duplicate_deep](class_array.md#class_Array_method_duplicate_deep) ( deep_subresources_mode: [int](class_int.md#class_int) = 1 ) const |
| void | [erase](class_array.md#class_Array_method_erase) ( value: [Variant](class_variant.md#class_Variant) ) |
| void | [fill](class_array.md#class_Array_method_fill) ( value: [Variant](class_variant.md#class_Variant) ) |
| [Array](class_array.md#class_Array) | [filter](class_array.md#class_Array_method_filter) ( method: [Callable](class_callable.md#class_Callable) ) const |
| [int](class_int.md#class_int) | [find](class_array.md#class_Array_method_find) ( what: [Variant](class_variant.md#class_Variant), from: [int](class_int.md#class_int) = 0 ) const |
| [int](class_int.md#class_int) | [find_custom](class_array.md#class_Array_method_find_custom) ( method: [Callable](class_callable.md#class_Callable), from: [int](class_int.md#class_int) = 0 ) const |
| [Variant](class_variant.md#class_Variant) | [front](class_array.md#class_Array_method_front) ( ) const |
| [Variant](class_variant.md#class_Variant) | [get](class_array.md#class_Array_method_get) ( index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_typed_builtin](class_array.md#class_Array_method_get_typed_builtin) ( ) const |
| [StringName](class_stringname.md#class_StringName) | [get_typed_class_name](class_array.md#class_Array_method_get_typed_class_name) ( ) const |
| [Variant](class_variant.md#class_Variant) | [get_typed_script](class_array.md#class_Array_method_get_typed_script) ( ) const |
| [bool](class_bool.md#class_bool) | [has](class_array.md#class_Array_method_has) ( value: [Variant](class_variant.md#class_Variant) ) const |
| [int](class_int.md#class_int) | [hash](class_array.md#class_Array_method_hash) ( ) const |
| [int](class_int.md#class_int) | [insert](class_array.md#class_Array_method_insert) ( position: [int](class_int.md#class_int), value: [Variant](class_variant.md#class_Variant) ) |
| [bool](class_bool.md#class_bool) | [is_empty](class_array.md#class_Array_method_is_empty) ( ) const |
| [bool](class_bool.md#class_bool) | [is_read_only](class_array.md#class_Array_method_is_read_only) ( ) const |
| [bool](class_bool.md#class_bool) | [is_same_typed](class_array.md#class_Array_method_is_same_typed) ( array: [Array](class_array.md#class_Array) ) const |
| [bool](class_bool.md#class_bool) | [is_typed](class_array.md#class_Array_method_is_typed) ( ) const |
| void | [make_read_only](class_array.md#class_Array_method_make_read_only) ( ) |
| [Array](class_array.md#class_Array) | [map](class_array.md#class_Array_method_map) ( method: [Callable](class_callable.md#class_Callable) ) const |
| [Variant](class_variant.md#class_Variant) | [max](class_array.md#class_Array_method_max) ( ) const |
| [Variant](class_variant.md#class_Variant) | [min](class_array.md#class_Array_method_min) ( ) const |
| [Variant](class_variant.md#class_Variant) | [pick_random](class_array.md#class_Array_method_pick_random) ( ) const |
| [Variant](class_variant.md#class_Variant) | [pop_at](class_array.md#class_Array_method_pop_at) ( position: [int](class_int.md#class_int) ) |
| [Variant](class_variant.md#class_Variant) | [pop_back](class_array.md#class_Array_method_pop_back) ( ) |
| [Variant](class_variant.md#class_Variant) | [pop_front](class_array.md#class_Array_method_pop_front) ( ) |
| void | [push_back](class_array.md#class_Array_method_push_back) ( value: [Variant](class_variant.md#class_Variant) ) |
| void | [push_front](class_array.md#class_Array_method_push_front) ( value: [Variant](class_variant.md#class_Variant) ) |
| [Variant](class_variant.md#class_Variant) | [reduce](class_array.md#class_Array_method_reduce) ( method: [Callable](class_callable.md#class_Callable), accum: [Variant](class_variant.md#class_Variant) = null ) const |
| void | [remove_at](class_array.md#class_Array_method_remove_at) ( position: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [resize](class_array.md#class_Array_method_resize) ( size: [int](class_int.md#class_int) ) |
| void | [reverse](class_array.md#class_Array_method_reverse) ( ) |
| [int](class_int.md#class_int) | [rfind](class_array.md#class_Array_method_rfind) ( what: [Variant](class_variant.md#class_Variant), from: [int](class_int.md#class_int) = -1 ) const |
| [int](class_int.md#class_int) | [rfind_custom](class_array.md#class_Array_method_rfind_custom) ( method: [Callable](class_callable.md#class_Callable), from: [int](class_int.md#class_int) = -1 ) const |
| void | [set](class_array.md#class_Array_method_set) ( index: [int](class_int.md#class_int), value: [Variant](class_variant.md#class_Variant) ) |
| void | [shuffle](class_array.md#class_Array_method_shuffle) ( ) |
| [int](class_int.md#class_int) | [size](class_array.md#class_Array_method_size) ( ) const |
| [Array](class_array.md#class_Array) | [slice](class_array.md#class_Array_method_slice) ( begin: [int](class_int.md#class_int), end: [int](class_int.md#class_int) = 2147483647, step: [int](class_int.md#class_int) = 1, deep: [bool](class_bool.md#class_bool) = false ) const |
| void | [sort](class_array.md#class_Array_method_sort) ( ) |
| void | [sort_custom](class_array.md#class_Array_method_sort_custom) ( func: [Callable](class_callable.md#class_Callable) ) |

### Operators


| [bool](class_bool.md#class_bool) | [operator !=](class_array.md#class_Array_operator_neq_Array) ( right: [Array](class_array.md#class_Array) ) |
| --- | --- |
| [Array](class_array.md#class_Array) | [operator +](class_array.md#class_Array_operator_sum_Array) ( right: [Array](class_array.md#class_Array) ) |
| [bool](class_bool.md#class_bool) | operator \ ( right: [Array](class_array.md#class_Array) ) |
| [bool](class_bool.md#class_bool) | operator \ ( right: [Array](class_array.md#class_Array) ) |
| [bool](class_bool.md#class_bool) | [operator ==](class_array.md#class_Array_operator_eq_Array) ( right: [Array](class_array.md#class_Array) ) |
| [bool](class_bool.md#class_bool) | [operator >](class_array.md#class_Array_operator_gt_Array) ( right: [Array](class_array.md#class_Array) ) |
| [bool](class_bool.md#class_bool) | [operator >=](class_array.md#class_Array_operator_gte_Array) ( right: [Array](class_array.md#class_Array) ) |
| [Variant](class_variant.md#class_Variant) | [operator []](class_array.md#class_Array_operator_idx_int) ( index: [int](class_int.md#class_int) ) |

---

### Constructor Descriptions

<span id="class_Array_constructor_Array"></span>

[Array](class_array.md#class_Array) **Array** ( ) [🔗](class_array.md#class_Array_constructor_Array)

Constructs an empty **Array**.

---

[Array](class_array.md#class_Array) **Array** ( base: [Array](class_array.md#class_Array), type: [int](class_int.md#class_int), class_name: [StringName](class_stringname.md#class_StringName), script: [Variant](class_variant.md#class_Variant) )

Creates a typed array from the `base` array. A typed array can only contain elements of the given type, or that inherit from the given class, as described by this constructor's parameters:

- `type` is the built-in [Variant](class_variant.md#class_Variant) type, as one the Variant.Type constants.

- `class_name` is the built-in class name (see [Object.get_class()](class_object.md#class_Object_method_get_class)).

- `script` is the associated script. It must be a [Script](class_script.md#class_Script) instance or `null`.

If `type` is not @GlobalScope.TYPE_OBJECT, `class_name` must be an empty [StringName](class_stringname.md#class_StringName) and `script` must be `null`.

::

    class_name Sword
    extends Node

    class Stats:
        pass

    func _ready():
        var a = Array([], TYPE_INT, "", null)               # Array[int]
        var b = Array([], TYPE_OBJECT, "Node", null)        # Array[Node]
        var c = Array([], TYPE_OBJECT, "Node", Sword)       # Array[Sword]
        var d = Array([], TYPE_OBJECT, "RefCounted", Stats) # Array[Stats]

The `base` array's elements are converted when necessary. If this is not possible or `base` is already typed, this constructor fails and returns an empty **Array**.

In GDScript, this constructor is usually not necessary, as it is possible to create a typed array through static typing:

::

    var numbers: Array[float] = []
    var children: Array[Node] = [$Node, $Sprite2D, $RigidBody3D]

    var integers: Array[int] = [0.2, 4.5, -2.0]
    print(integers) # Prints [0, 4, -2]

---

[Array](class_array.md#class_Array) **Array** ( from: [Array](class_array.md#class_Array) )

Returns the same array as `from`. If you need a copy of the array, use [duplicate()](class_array.md#class_Array_method_duplicate).

---

[Array](class_array.md#class_Array) **Array** ( from: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) )

Constructs an array from a [PackedByteArray](class_packedbytearray.md#class_PackedByteArray).

---

[Array](class_array.md#class_Array) **Array** ( from: [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) )

Constructs an array from a [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray).

---

[Array](class_array.md#class_Array) **Array** ( from: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) )

Constructs an array from a [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array).

---

[Array](class_array.md#class_Array) **Array** ( from: [PackedFloat64Array](class_packedfloat64array.md#class_PackedFloat64Array) )

Constructs an array from a [PackedFloat64Array](class_packedfloat64array.md#class_PackedFloat64Array).

---

[Array](class_array.md#class_Array) **Array** ( from: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) )

Constructs an array from a [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array).

---

[Array](class_array.md#class_Array) **Array** ( from: [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) )

Constructs an array from a [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array).

---

[Array](class_array.md#class_Array) **Array** ( from: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) )

Constructs an array from a [PackedStringArray](class_packedstringarray.md#class_PackedStringArray).

---

[Array](class_array.md#class_Array) **Array** ( from: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) )

Constructs an array from a [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array).

---

[Array](class_array.md#class_Array) **Array** ( from: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) )

Constructs an array from a [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array).

---

[Array](class_array.md#class_Array) **Array** ( from: [PackedVector4Array](class_packedvector4array.md#class_PackedVector4Array) )

Constructs an array from a [PackedVector4Array](class_packedvector4array.md#class_PackedVector4Array).

---

### Method Descriptions

<span id="class_Array_method_all"></span>

[bool](class_bool.md#class_bool) **all** ( method: [Callable](class_callable.md#class_Callable) ) *const* [🔗](class_array.md#class_Array_method_all)

Calls the given [Callable](class_callable.md#class_Callable) on each element in the array and returns `true` if the [Callable](class_callable.md#class_Callable) returns `true` for *all* elements in the array. If the [Callable](class_callable.md#class_Callable) returns `false` for one array element or more, this method returns `false`.

The `method` should take one [Variant](class_variant.md#class_Variant) parameter (the current array element) and return a [bool](class_bool.md#class_bool).

.. tabs::

```
```

    func greater_than_5(number):
        return number > 5

    func _ready():
        print([6, 10, 6].all(greater_than_5)) # Prints true (3/3 elements evaluate to true).
        print([4, 10, 4].all(greater_than_5)) # Prints false (1/3 elements evaluate to true).
        print([4, 4, 4].all(greater_than_5))  # Prints false (0/3 elements evaluate to true).
        print([].all(greater_than_5))         # Prints true (0/0 elements evaluate to true).

        # Same as the first line above, but using a lambda function.
        print([6, 10, 6].all(func(element): return element > 5)) # Prints true

```
```

    private static bool GreaterThan5(int number)
    {
        return number > 5;
    }

    public override void _Ready()
    {
        // Prints True (3/3 elements evaluate to true).
        GD.Print(new Godot.Collections.Array>int< { 6, 10, 6 }.All(GreaterThan5));
        // Prints False (1/3 elements evaluate to true).
        GD.Print(new Godot.Collections.Array>int< { 4, 10, 4 }.All(GreaterThan5));
        // Prints False (0/3 elements evaluate to true).
        GD.Print(new Godot.Collections.Array>int< { 4, 4, 4 }.All(GreaterThan5));
        // Prints True (0/0 elements evaluate to true).
        GD.Print(new Godot.Collections.Array>int< { }.All(GreaterThan5));

        // Same as the first line above, but using a lambda function.
        GD.Print(new Godot.Collections.Array>int< { 6, 10, 6 }.All(element => element > 5)); // Prints True
    }

See also [any()](class_array.md#class_Array_method_any), [filter()](class_array.md#class_Array_method_filter), [map()](class_array.md#class_Array_method_map) and [reduce()](class_array.md#class_Array_method_reduce).

 **Note:** Unlike relying on the size of an array returned by [filter()](class_array.md#class_Array_method_filter), this method will return as early as possible to improve performance (especially with large arrays).

 **Note:** For an empty array, this method always returns `true`.

---

<span id="class_Array_method_any"></span>

[bool](class_bool.md#class_bool) **any** ( method: [Callable](class_callable.md#class_Callable) ) *const* [🔗](class_array.md#class_Array_method_any)

Calls the given [Callable](class_callable.md#class_Callable) on each element in the array and returns `true` if the [Callable](class_callable.md#class_Callable) returns `true` for *one or more* elements in the array. If the [Callable](class_callable.md#class_Callable) returns `false` for all elements in the array, this method returns `false`.

The `method` should take one [Variant](class_variant.md#class_Variant) parameter (the current array element) and return a [bool](class_bool.md#class_bool).

::

    func greater_than_5(number):
        return number > 5

    func _ready():
        print([6, 10, 6].any(greater_than_5)) # Prints true (3 elements evaluate to true).
        print([4, 10, 4].any(greater_than_5)) # Prints true (1 elements evaluate to true).
        print([4, 4, 4].any(greater_than_5))  # Prints false (0 elements evaluate to true).
        print([].any(greater_than_5))         # Prints false (0 elements evaluate to true).

        # Same as the first line above, but using a lambda function.
        print([6, 10, 6].any(func(number): return number > 5)) # Prints true

See also [all()](class_array.md#class_Array_method_all), [filter()](class_array.md#class_Array_method_filter), [map()](class_array.md#class_Array_method_map) and [reduce()](class_array.md#class_Array_method_reduce).

 **Note:** Unlike relying on the size of an array returned by [filter()](class_array.md#class_Array_method_filter), this method will return as early as possible to improve performance (especially with large arrays).

 **Note:** For an empty array, this method always returns `false`.

---

<span id="class_Array_method_append"></span>

void **append** ( value: [Variant](class_variant.md#class_Variant) ) [🔗](class_array.md#class_Array_method_append)

Appends `value` at the end of the array (alias of [push_back()](class_array.md#class_Array_method_push_back)).

---

<span id="class_Array_method_append_array"></span>

void **append_array** ( array: [Array](class_array.md#class_Array) ) [🔗](class_array.md#class_Array_method_append_array)

Appends another `array` at the end of this array.

::

    var numbers = [1, 2, 3]
    var extra = [4, 5, 6]
    numbers.append_array(extra)
    print(numbers) # Prints [1, 2, 3, 4, 5, 6]

---

<span id="class_Array_method_assign"></span>

void **assign** ( array: [Array](class_array.md#class_Array) ) [🔗](class_array.md#class_Array_method_assign)

Assigns elements of another `array` into the array. Resizes the array to match `array`. Performs type conversions if the array is typed.

---

<span id="class_Array_method_back"></span>

[Variant](class_variant.md#class_Variant) **back** ( ) *const* [🔗](class_array.md#class_Array_method_back)

Returns the last element of the array. If the array is empty, fails and returns `null`. See also [front()](class_array.md#class_Array_method_front).

 **Note:** Unlike with the `[]` operator (`array[-1]`), an error is generated without stopping project execution.

---

<span id="class_Array_method_bsearch"></span>

[int](class_int.md#class_int) **bsearch** ( value: [Variant](class_variant.md#class_Variant), before: [bool](class_bool.md#class_bool) = true ) *const* [🔗](class_array.md#class_Array_method_bsearch)

Returns the index of `value` in the sorted array. If it cannot be found, returns where `value` should be inserted to keep the array sorted. The algorithm used is binary search.

If `before` is `true` (as by default), the returned index comes before all existing elements equal to `value` in the array.

::

    var numbers = [2, 4, 8, 10]
    var idx = numbers.bsearch(7)

    numbers.insert(idx, 7)
    print(numbers) # Prints [2, 4, 7, 8, 10]

    var fruits = ["Apple", "Lemon", "Lemon", "Orange"]
    print(fruits.bsearch("Lemon", true))  # Prints 1, points at the first "Lemon".
    print(fruits.bsearch("Lemon", false)) # Prints 3, points at "Orange".

 **Note:** Calling [bsearch()](class_array.md#class_Array_method_bsearch) on an *unsorted* array will result in unexpected behavior. Use [sort()](class_array.md#class_Array_method_sort) before calling this method.

---

<span id="class_Array_method_bsearch_custom"></span>

[int](class_int.md#class_int) **bsearch_custom** ( value: [Variant](class_variant.md#class_Variant), func: [Callable](class_callable.md#class_Callable), before: [bool](class_bool.md#class_bool) = true ) *const* [🔗](class_array.md#class_Array_method_bsearch_custom)

Returns the index of `value` in the sorted array. If it cannot be found, returns where `value` should be inserted to keep the array sorted (using `func` for the comparisons). The algorithm used is binary search.

Similar to [sort_custom()](class_array.md#class_Array_method_sort_custom), `func` is called as many times as necessary, receiving one array element and `value` as arguments. The function should return `true` if the array element should be *behind* `value`, otherwise it should return `false`.

If `before` is `true` (as by default), the returned index comes before all existing elements equal to `value` in the array.

::

    func sort_by_amount(a, b):
        if a[1] < b[1]:
            return true
        return false

    func _ready():
        var my_items = [["Tomato", 2], ["Kiwi", 5], ["Rice", 9]]

        var apple = ["Apple", 5]
        # "Apple" is inserted before "Kiwi".
        my_items.insert(my_items.bsearch_custom(apple, sort_by_amount, true), apple)

        var banana = ["Banana", 5]
        # "Banana" is inserted after "Kiwi".
        my_items.insert(my_items.bsearch_custom(banana, sort_by_amount, false), banana)

        # Prints [["Tomato", 2], ["Apple", 5], ["Kiwi", 5], ["Banana", 5], ["Rice", 9]]
        print(my_items)

 **Note:** Calling [bsearch_custom()](class_array.md#class_Array_method_bsearch_custom) on an *unsorted* array will result in unexpected behavior. Use [sort_custom()](class_array.md#class_Array_method_sort_custom) with `func` before calling this method.

---

<span id="class_Array_method_clear"></span>

void **clear** ( ) [🔗](class_array.md#class_Array_method_clear)

Removes all elements from the array. This is equivalent to using [resize()](class_array.md#class_Array_method_resize) with a size of `0`.

---

<span id="class_Array_method_count"></span>

[int](class_int.md#class_int) **count** ( value: [Variant](class_variant.md#class_Variant) ) *const* [🔗](class_array.md#class_Array_method_count)

Returns the number of times an element is in the array.

To count how many elements in an array satisfy a condition, see [reduce()](class_array.md#class_Array_method_reduce).

---

<span id="class_Array_method_duplicate"></span>

[Array](class_array.md#class_Array) **duplicate** ( deep: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_array.md#class_Array_method_duplicate)

Returns a new copy of the array.

By default, a **shallow** copy is returned: all nested **Array**, [Dictionary](class_dictionary.md#class_Dictionary), and [Resource](class_resource.md#class_Resource) elements are shared with the original array. Modifying any of those in one array will also affect them in the other.

If `deep` is `true`, a **deep** copy is returned: all nested arrays and dictionaries are also duplicated (recursively). Any [Resource](class_resource.md#class_Resource) is still shared with the original array, though.

---

<span id="class_Array_method_duplicate_deep"></span>

[Array](class_array.md#class_Array) **duplicate_deep** ( deep_subresources_mode: [int](class_int.md#class_int) = 1 ) *const* [🔗](class_array.md#class_Array_method_duplicate_deep)

Duplicates this array, deeply, like [duplicate()](class_array.md#class_Array_method_duplicate) when passing `true`, with extra control over how subresources are handled.

 `deep_subresources_mode` must be one of the values from [DeepDuplicateMode](class_resource.md#enum_Resource_DeepDuplicateMode). By default, only internal resources will be duplicated (recursively).

---

<span id="class_Array_method_erase"></span>

void **erase** ( value: [Variant](class_variant.md#class_Variant) ) [🔗](class_array.md#class_Array_method_erase)

Finds and removes the first occurrence of `value` from the array. If `value` does not exist in the array, nothing happens. To remove an element by index, use [remove_at()](class_array.md#class_Array_method_remove_at) instead.

 **Note:** This method shifts every element's index after the removed `value` back, which may have a noticeable performance cost, especially on larger arrays.

 **Note:** Erasing elements while iterating over arrays is **not** supported and will result in unpredictable behavior.

---

<span id="class_Array_method_fill"></span>

void **fill** ( value: [Variant](class_variant.md#class_Variant) ) [🔗](class_array.md#class_Array_method_fill)

Assigns the given `value` to all elements in the array.

This method can often be combined with [resize()](class_array.md#class_Array_method_resize) to create an array with a given size and initialized elements:

.. tabs::

```
```

    var array = []
    array.resize(5)
    array.fill(2)
    print(array) # Prints [2, 2, 2, 2, 2]

```
```

    Godot.Collections.Array array = [];
    array.Resize(5);
    array.Fill(2);
    GD.Print(array); // Prints [2, 2, 2, 2, 2]

 **Note:** If `value` is a [Variant](class_variant.md#class_Variant) passed by reference ([Object](class_object.md#class_Object)-derived, **Array**, [Dictionary](class_dictionary.md#class_Dictionary), etc.), the array will be filled with references to the same `value`, which are not duplicates.

---

<span id="class_Array_method_filter"></span>

[Array](class_array.md#class_Array) **filter** ( method: [Callable](class_callable.md#class_Callable) ) *const* [🔗](class_array.md#class_Array_method_filter)

Calls the given [Callable](class_callable.md#class_Callable) on each element in the array and returns a new, filtered **Array**.

The `method` receives one of the array elements as an argument, and should return `true` to add the element to the filtered array, or `false` to exclude it.

::

    func is_even(number):
        return number % 2 == 0

    func _ready():
        print([1, 4, 5, 8].filter(is_even)) # Prints [4, 8]

        # Same as above, but using a lambda function.
        print([1, 4, 5, 8].filter(func(number): return number % 2 == 0))

See also [any()](class_array.md#class_Array_method_any), [all()](class_array.md#class_Array_method_all), [map()](class_array.md#class_Array_method_map) and [reduce()](class_array.md#class_Array_method_reduce).

---

<span id="class_Array_method_find"></span>

[int](class_int.md#class_int) **find** ( what: [Variant](class_variant.md#class_Variant), from: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_array.md#class_Array_method_find)

Returns the index of the **first** occurrence of `what` in this array, or `-1` if there are none. The search's start can be specified with `from`, continuing to the end of the array.

 **Note:** If you just want to know whether the array contains `what`, use [has()](class_array.md#class_Array_method_has) (`Contains` in C#). In GDScript, you may also use the `in` operator.

 **Note:** For performance reasons, the search is affected by `what`'s Variant.Type. For example, `7` ([int](class_int.md#class_int)) and `7.0` ([float](class_float.md#class_float)) are not considered equal for this method.

---

<span id="class_Array_method_find_custom"></span>

[int](class_int.md#class_int) **find_custom** ( method: [Callable](class_callable.md#class_Callable), from: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_array.md#class_Array_method_find_custom)

Returns the index of the **first** element in the array that causes `method` to return `true`, or `-1` if there are none. The search's start can be specified with `from`, continuing to the end of the array.

 `method` is a callable that takes an element of the array, and returns a [bool](class_bool.md#class_bool).

 **Note:** If you just want to know whether the array contains *anything* that satisfies `method`, use [any()](class_array.md#class_Array_method_any).

.. tabs::

```
```

    func is_even(number):
        return number % 2 == 0

    func _ready():
        print([1, 3, 4, 7].find_custom(is_even.bind())) # Prints 2

---

<span id="class_Array_method_front"></span>

[Variant](class_variant.md#class_Variant) **front** ( ) *const* [🔗](class_array.md#class_Array_method_front)

Returns the first element of the array. If the array is empty, fails and returns `null`. See also [back()](class_array.md#class_Array_method_back).

 **Note:** Unlike with the `[]` operator (`array[0]`), an error is generated without stopping project execution.

---

<span id="class_Array_method_get"></span>

[Variant](class_variant.md#class_Variant) **get** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_array.md#class_Array_method_get)

Returns the element at the given `index` in the array. If `index` is out-of-bounds or negative, this method fails and returns `null`.

This method is similar (but not identical) to the `[]` operator. Most notably, when this method fails, it doesn't pause project execution if run from the editor.

---

<span id="class_Array_method_get_typed_builtin"></span>

[int](class_int.md#class_int) **get_typed_builtin** ( ) *const* [🔗](class_array.md#class_Array_method_get_typed_builtin)

Returns the built-in [Variant](class_variant.md#class_Variant) type of the typed array as a Variant.Type constant. If the array is not typed, returns @GlobalScope.TYPE_NIL. See also [is_typed()](class_array.md#class_Array_method_is_typed).

---

<span id="class_Array_method_get_typed_class_name"></span>

[StringName](class_stringname.md#class_StringName) **get_typed_class_name** ( ) *const* [🔗](class_array.md#class_Array_method_get_typed_class_name)

Returns the **built-in** class name of the typed array, if the built-in [Variant](class_variant.md#class_Variant) type @GlobalScope.TYPE_OBJECT. Otherwise, returns an empty [StringName](class_stringname.md#class_StringName). See also [is_typed()](class_array.md#class_Array_method_is_typed) and [Object.get_class()](class_object.md#class_Object_method_get_class).

---

<span id="class_Array_method_get_typed_script"></span>

[Variant](class_variant.md#class_Variant) **get_typed_script** ( ) *const* [🔗](class_array.md#class_Array_method_get_typed_script)

Returns the [Script](class_script.md#class_Script) instance associated with this typed array, or `null` if it does not exist. See also [is_typed()](class_array.md#class_Array_method_is_typed).

---

<span id="class_Array_method_has"></span>

[bool](class_bool.md#class_bool) **has** ( value: [Variant](class_variant.md#class_Variant) ) *const* [🔗](class_array.md#class_Array_method_has)

Returns `true` if the array contains the given `value`.

.. tabs::

```
```

    print(["inside", 7].has("inside"))  # Prints true
    print(["inside", 7].has("outside")) # Prints false
    print(["inside", 7].has(7))         # Prints true
    print(["inside", 7].has("7"))       # Prints false

```
```

    Godot.Collections.Array arr = ["inside", 7];
    // By C# convention, this method is renamed to `Contains`.
    GD.Print(arr.Contains("inside"));  // Prints True
    GD.Print(arr.Contains("outside")); // Prints False
    GD.Print(arr.Contains(7));         // Prints True
    GD.Print(arr.Contains("7"));       // Prints False

In GDScript, this is equivalent to the `in` operator:

::

    if 4 in [2, 4, 6, 8]:
        print("4 is here!") # Will be printed.

 **Note:** For performance reasons, the search is affected by the `value`'s Variant.Type. For example, `7` ([int](class_int.md#class_int)) and `7.0` ([float](class_float.md#class_float)) are not considered equal for this method.

---

<span id="class_Array_method_hash"></span>

[int](class_int.md#class_int) **hash** ( ) *const* [🔗](class_array.md#class_Array_method_hash)

Returns a hashed 32-bit integer value representing the array and its contents.

 **Note:** Arrays with equal hash values are *not* guaranteed to be the same, as a result of hash collisions. On the contrary, arrays with different hash values are guaranteed to be different.

---

<span id="class_Array_method_insert"></span>

[int](class_int.md#class_int) **insert** ( position: [int](class_int.md#class_int), value: [Variant](class_variant.md#class_Variant) ) [🔗](class_array.md#class_Array_method_insert)

Inserts a new element (`value`) at a given index (`position`) in the array. `position` should be between `0` and the array's [size()](class_array.md#class_Array_method_size). If negative, `position` is considered relative to the end of the array.

Returns @GlobalScope.OK on success, or one of the other Error constants if this method fails.

 **Note:** Every element's index after `position` needs to be shifted forward, which may have a noticeable performance cost, especially on larger arrays.

---

<span id="class_Array_method_is_empty"></span>

[bool](class_bool.md#class_bool) **is_empty** ( ) *const* [🔗](class_array.md#class_Array_method_is_empty)

Returns `true` if the array is empty (`[]`). See also [size()](class_array.md#class_Array_method_size).

---

<span id="class_Array_method_is_read_only"></span>

[bool](class_bool.md#class_bool) **is_read_only** ( ) *const* [🔗](class_array.md#class_Array_method_is_read_only)

Returns `true` if the array is read-only. See [make_read_only()](class_array.md#class_Array_method_make_read_only).

In GDScript, arrays are automatically read-only if declared with the `const` keyword.

---

<span id="class_Array_method_is_same_typed"></span>

[bool](class_bool.md#class_bool) **is_same_typed** ( array: [Array](class_array.md#class_Array) ) *const* [🔗](class_array.md#class_Array_method_is_same_typed)

Returns `true` if this array is typed the same as the given `array`. See also [is_typed()](class_array.md#class_Array_method_is_typed).

---

<span id="class_Array_method_is_typed"></span>

[bool](class_bool.md#class_bool) **is_typed** ( ) *const* [🔗](class_array.md#class_Array_method_is_typed)

Returns `true` if the array is typed. Typed arrays can only contain elements of a specific type, as defined by the typed array constructor. The methods of a typed array are still expected to return a generic [Variant](class_variant.md#class_Variant).

In GDScript, it is possible to define a typed array with static typing:

::

    var numbers: Array[float] = [0.2, 4.2, -2.0]
    print(numbers.is_typed()) # Prints true

---

<span id="class_Array_method_make_read_only"></span>

void **make_read_only** ( ) [🔗](class_array.md#class_Array_method_make_read_only)

Makes the array read-only. The array's elements cannot be overridden with different values, and their order cannot change. Does not apply to nested elements, such as dictionaries.

In GDScript, arrays are automatically read-only if declared with the `const` keyword.

---

<span id="class_Array_method_map"></span>

[Array](class_array.md#class_Array) **map** ( method: [Callable](class_callable.md#class_Callable) ) *const* [🔗](class_array.md#class_Array_method_map)

Calls the given [Callable](class_callable.md#class_Callable) for each element in the array and returns a new array filled with values returned by the `method`.

The `method` should take one [Variant](class_variant.md#class_Variant) parameter (the current array element) and can return any [Variant](class_variant.md#class_Variant).

::

    func double(number):
        return number * 2

    func _ready():
        print([1, 2, 3].map(double)) # Prints [2, 4, 6]

        # Same as above, but using a lambda function.
        print([1, 2, 3].map(func(element): return element * 2))

See also [filter()](class_array.md#class_Array_method_filter), [reduce()](class_array.md#class_Array_method_reduce), [any()](class_array.md#class_Array_method_any) and [all()](class_array.md#class_Array_method_all).

---

<span id="class_Array_method_max"></span>

[Variant](class_variant.md#class_Variant) **max** ( ) *const* [🔗](class_array.md#class_Array_method_max)

Returns the maximum value contained in the array, if all elements can be compared. Otherwise, returns `null`. See also [min()](class_array.md#class_Array_method_min).

To find the maximum value using a custom comparator, you can use [reduce()](class_array.md#class_Array_method_reduce).

---

<span id="class_Array_method_min"></span>

[Variant](class_variant.md#class_Variant) **min** ( ) *const* [🔗](class_array.md#class_Array_method_min)

Returns the minimum value contained in the array, if all elements can be compared. Otherwise, returns `null`. See also [max()](class_array.md#class_Array_method_max).

---

<span id="class_Array_method_pick_random"></span>

[Variant](class_variant.md#class_Variant) **pick_random** ( ) *const* [🔗](class_array.md#class_Array_method_pick_random)

Returns a random element from the array. Generates an error and returns `null` if the array is empty.

.. tabs::

```
```

    # May print 1, 2, 3.25, or "Hi".
    print([1, 2, 3.25, "Hi"].pick_random())

```
```

    Godot.Collections.Array array = [1, 2, 3.25f, "Hi"];
    GD.Print(array.PickRandom()); // May print 1, 2, 3.25, or "Hi".

 **Note:** Like many similar functions in the engine (such as @GlobalScope.randi() or [shuffle()](class_array.md#class_Array_method_shuffle)), this method uses a common, global random seed. To get a predictable outcome from this method, see @GlobalScope.seed().

---

<span id="class_Array_method_pop_at"></span>

[Variant](class_variant.md#class_Variant) **pop_at** ( position: [int](class_int.md#class_int) ) [🔗](class_array.md#class_Array_method_pop_at)

Removes and returns the element of the array at index `position`. If negative, `position` is considered relative to the end of the array. Returns `null` if the array is empty. If `position` is out of bounds, an error message is also generated.

 **Note:** This method shifts every element's index after `position` back, which may have a noticeable performance cost, especially on larger arrays.

---

<span id="class_Array_method_pop_back"></span>

[Variant](class_variant.md#class_Variant) **pop_back** ( ) [🔗](class_array.md#class_Array_method_pop_back)

Removes and returns the last element of the array. Returns `null` if the array is empty, without generating an error. See also [pop_front()](class_array.md#class_Array_method_pop_front).

---

<span id="class_Array_method_pop_front"></span>

[Variant](class_variant.md#class_Variant) **pop_front** ( ) [🔗](class_array.md#class_Array_method_pop_front)

Removes and returns the first element of the array. Returns `null` if the array is empty, without generating an error. See also [pop_back()](class_array.md#class_Array_method_pop_back).

 **Note:** This method shifts every other element's index back, which may have a noticeable performance cost, especially on larger arrays.

---

<span id="class_Array_method_push_back"></span>

void **push_back** ( value: [Variant](class_variant.md#class_Variant) ) [🔗](class_array.md#class_Array_method_push_back)

Appends an element at the end of the array. See also [push_front()](class_array.md#class_Array_method_push_front).

---

<span id="class_Array_method_push_front"></span>

void **push_front** ( value: [Variant](class_variant.md#class_Variant) ) [🔗](class_array.md#class_Array_method_push_front)

Adds an element at the beginning of the array. See also [push_back()](class_array.md#class_Array_method_push_back).

 **Note:** This method shifts every other element's index forward, which may have a noticeable performance cost, especially on larger arrays.

---

<span id="class_Array_method_reduce"></span>

[Variant](class_variant.md#class_Variant) **reduce** ( method: [Callable](class_callable.md#class_Callable), accum: [Variant](class_variant.md#class_Variant) = null ) *const* [🔗](class_array.md#class_Array_method_reduce)

Calls the given [Callable](class_callable.md#class_Callable) for each element in array, accumulates the result in `accum`, then returns it.

The `method` takes two arguments: the current value of `accum` and the current array element. If `accum` is `null` (as by default), the iteration will start from the second element, with the first one used as initial value of `accum`.

::

    func sum(accum, number):
        return accum + number

    func _ready():
        print([1, 2, 3].reduce(sum, 0))  # Prints 6
        print([1, 2, 3].reduce(sum, 10)) # Prints 16

        # Same as above, but using a lambda function.
        print([1, 2, 3].reduce(func(accum, number): return accum + number, 10))

If [max()](class_array.md#class_Array_method_max) is not desirable, this method may also be used to implement a custom comparator:

::

    func _ready():
        var arr = [Vector2i(5, 0), Vector2i(3, 4), Vector2i(1, 2)]

        var longest_vec = arr.reduce(func(max, vec): return vec if is_length_greater(vec, max) else max)
        print(longest_vec) # Prints (3, 4)

    func is_length_greater(a, b):
        return a.length() > b.length()

This method can also be used to count how many elements in an array satisfy a certain condition, similar to [count()](class_array.md#class_Array_method_count):

::

    func is_even(number):
        return number % 2 == 0

    func _ready():
        var arr = [1, 2, 3, 4, 5]
        # If the current element is even, increment count, otherwise leave count the same.
        var even_count = arr.reduce(func(count, next): return count + 1 if is_even(next) else count, 0)
        print(even_count) # Prints 2

See also [map()](class_array.md#class_Array_method_map), [filter()](class_array.md#class_Array_method_filter), [any()](class_array.md#class_Array_method_any), and [all()](class_array.md#class_Array_method_all).

---

<span id="class_Array_method_remove_at"></span>

void **remove_at** ( position: [int](class_int.md#class_int) ) [🔗](class_array.md#class_Array_method_remove_at)

Removes the element from the array at the given index (`position`). If the index is out of bounds, this method fails. If the index is negative, `position` is considered relative to the end of the array.

If you need to return the removed element, use [pop_at()](class_array.md#class_Array_method_pop_at). To remove an element by value, use [erase()](class_array.md#class_Array_method_erase) instead.

 **Note:** This method shifts every element's index after `position` back, which may have a noticeable performance cost, especially on larger arrays.

---

<span id="class_Array_method_resize"></span>

[int](class_int.md#class_int) **resize** ( size: [int](class_int.md#class_int) ) [🔗](class_array.md#class_Array_method_resize)

Sets the array's number of elements to `size`. If `size` is smaller than the array's current size, the elements at the end are removed. If `size` is greater, new default elements (usually `null`) are added, depending on the array's type.

Returns @GlobalScope.OK on success, or one of the following Error constants if this method fails: @GlobalScope.ERR_LOCKED if the array is read-only, @GlobalScope.ERR_INVALID_PARAMETER if the size is negative, or @GlobalScope.ERR_OUT_OF_MEMORY if allocations fail. Use [size()](class_array.md#class_Array_method_size) to find the actual size of the array after resize.

 **Note:** Calling this method once and assigning the new values is faster than calling [append()](class_array.md#class_Array_method_append) for every new element.

---

<span id="class_Array_method_reverse"></span>

void **reverse** ( ) [🔗](class_array.md#class_Array_method_reverse)

Reverses the order of all elements in the array.

---

<span id="class_Array_method_rfind"></span>

[int](class_int.md#class_int) **rfind** ( what: [Variant](class_variant.md#class_Variant), from: [int](class_int.md#class_int) = -1 ) *const* [🔗](class_array.md#class_Array_method_rfind)

Returns the index of the **last** occurrence of `what` in this array, or `-1` if there are none. The search's start can be specified with `from`, continuing to the beginning of the array. This method is the reverse of [find()](class_array.md#class_Array_method_find).

---

<span id="class_Array_method_rfind_custom"></span>

[int](class_int.md#class_int) **rfind_custom** ( method: [Callable](class_callable.md#class_Callable), from: [int](class_int.md#class_int) = -1 ) *const* [🔗](class_array.md#class_Array_method_rfind_custom)

Returns the index of the **last** element of the array that causes `method` to return `true`, or `-1` if there are none. The search's start can be specified with `from`, continuing to the beginning of the array. This method is the reverse of [find_custom()](class_array.md#class_Array_method_find_custom).

---

<span id="class_Array_method_set"></span>

void **set** ( index: [int](class_int.md#class_int), value: [Variant](class_variant.md#class_Variant) ) [🔗](class_array.md#class_Array_method_set)

Sets the value of the element at the given `index` to the given `value`. This will not change the size of the array, it only changes the value at an index already in the array. This is the same as using the `[]` operator (`array[index] = value`).

---

<span id="class_Array_method_shuffle"></span>

void **shuffle** ( ) [🔗](class_array.md#class_Array_method_shuffle)

Shuffles all elements of the array in a random order.

 **Note:** Like many similar functions in the engine (such as @GlobalScope.randi() or [pick_random()](class_array.md#class_Array_method_pick_random)), this method uses a common, global random seed. To get a predictable outcome from this method, see @GlobalScope.seed().

---

<span id="class_Array_method_size"></span>

[int](class_int.md#class_int) **size** ( ) *const* [🔗](class_array.md#class_Array_method_size)

Returns the number of elements in the array. Empty arrays (`[]`) always return `0`. See also [is_empty()](class_array.md#class_Array_method_is_empty).

---

<span id="class_Array_method_slice"></span>

[Array](class_array.md#class_Array) **slice** ( begin: [int](class_int.md#class_int), end: [int](class_int.md#class_int) = 2147483647, step: [int](class_int.md#class_int) = 1, deep: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_array.md#class_Array_method_slice)

Returns a new **Array** containing this array's elements, from index `begin` (inclusive) to `end` (exclusive), every `step` elements.

If either `begin` or `end` are negative, their value is relative to the end of the array.

If `step` is negative, this method iterates through the array in reverse, returning a slice ordered backwards. For this to work, `begin` must be greater than `end`.

If `deep` is `true`, all nested **Array** and [Dictionary](class_dictionary.md#class_Dictionary) elements in the slice are duplicated from the original, recursively. See also [duplicate()](class_array.md#class_Array_method_duplicate).

::

    var letters = ["A", "B", "C", "D", "E", "F"]

    print(letters.slice(0, 2))  # Prints ["A", "B"]
    print(letters.slice(2, -2)) # Prints ["C", "D"]
    print(letters.slice(-2, 6)) # Prints ["E", "F"]

    print(letters.slice(0, 6, 2))  # Prints ["A", "C", "E"]
    print(letters.slice(4, 1, -1)) # Prints ["E", "D", "C"]

---

<span id="class_Array_method_sort"></span>

void **sort** ( ) [🔗](class_array.md#class_Array_method_sort)

Sorts the array in ascending order. The final order is dependent on the "less than" (`<`) comparison between elements.

.. tabs::

```
```

    var numbers = [10, 5, 2.5, 8]
    numbers.sort()
    print(numbers) # Prints [2.5, 5, 8, 10]

```
```

    Godot.Collections.Array numbers = [10, 5, 2.5, 8];
    numbers.Sort();
    GD.Print(numbers); // Prints [2.5, 5, 8, 10]

 **Note:** The sorting algorithm used is not stable. This means that equivalent elements (such as `2` and `2.0`) may have their order changed when calling [sort()](class_array.md#class_Array_method_sort).

---

<span id="class_Array_method_sort_custom"></span>

void **sort_custom** ( func: [Callable](class_callable.md#class_Callable) ) [🔗](class_array.md#class_Array_method_sort_custom)

Sorts the array using a custom [Callable](class_callable.md#class_Callable).

 `func` is called as many times as necessary, receiving two array elements as arguments. The function should return `true` if the first element should be moved *before* the second one, otherwise it should return `false`.

::

    func sort_ascending(a, b):
        if a[1] < b[1]:
            return true
        return false

    func _ready():
        var my_items = [["Tomato", 5], ["Apple", 9], ["Rice", 4]]
        my_items.sort_custom(sort_ascending)
        print(my_items) # Prints [["Rice", 4], ["Tomato", 5], ["Apple", 9]]

        # Sort descending, using a lambda function.
        my_items.sort_custom(func(a, b): return a[1] > b[1])
        print(my_items) # Prints [["Apple", 9], ["Tomato", 5], ["Rice", 4]]

It may also be necessary to use this method to sort strings by natural order, with [String.naturalnocasecmp_to()](class_string.md#class_String_method_naturalnocasecmp_to), as in the following example:

::

    var files = ["newfile1", "newfile2", "newfile10", "newfile11"]
    files.sort_custom(func(a, b): return a.naturalnocasecmp_to(b) < 0)
    print(files) # Prints ["newfile1", "newfile2", "newfile10", "newfile11"]

 **Note:** In C#, this method is not supported.

 **Note:** The sorting algorithm used is not stable. This means that values considered equal may have their order changed when calling this method.

 **Note:** You should not randomize the return value of `func`, as the heapsort algorithm expects a consistent result. Randomizing the return value will result in unexpected behavior.

---

### Operator Descriptions

<span id="class_Array_operator_neq_Array"></span>

[bool](class_bool.md#class_bool) **operator !=** ( right: [Array](class_array.md#class_Array) ) [🔗](class_array.md#class_Array_operator_neq_Array)

Returns `true` if the array's size or its elements are different than `right`'s.

---

<span id="class_Array_operator_sum_Array"></span>

[Array](class_array.md#class_Array) **operator +** ( right: [Array](class_array.md#class_Array) ) [🔗](class_array.md#class_Array_operator_sum_Array)

Appends the `right` array to the left operand, creating a new **Array**. This is also known as an array concatenation.

.. tabs::

```
```

    var array1 = ["One", 2]
    var array2 = [3, "Four"]
    print(array1 + array2) # Prints ["One", 2, 3, "Four"]

```
```

    // Note that concatenation is not possible with C#'s native Array type.
    Godot.Collections.Array array1 = ["One", 2];
    Godot.Collections.Array array2 = [3, "Four"];
    GD.Print(array1 + array2); // Prints ["One", 2, 3, "Four"]

 **Note:** For existing arrays, [append_array()](class_array.md#class_Array_method_append_array) is much more efficient than concatenation and assignment with the `+=` operator.

---

<span id="class_Array_operator_lt_Array"></span>

[bool](class_bool.md#class_bool) **operator <** ( right: [Array](class_array.md#class_Array) ) [🔗](class_array.md#class_Array_operator_lt_Array)

Compares the elements of both arrays in order, starting from index `0` and ending on the last index in common between both arrays. For each pair of elements, returns `true` if this array's element is less than `right`'s, `false` if this element is greater. Otherwise, continues to the next pair.

If all searched elements are equal, returns `true` if this array's size is less than `right`'s, otherwise returns `false`.

---

<span id="class_Array_operator_lte_Array"></span>

[bool](class_bool.md#class_bool) **operator <=** ( right: [Array](class_array.md#class_Array) ) [🔗](class_array.md#class_Array_operator_lte_Array)

Compares the elements of both arrays in order, starting from index `0` and ending on the last index in common between both arrays. For each pair of elements, returns `true` if this array's element is less than `right`'s, `false` if this element is greater. Otherwise, continues to the next pair.

If all searched elements are equal, returns `true` if this array's size is less or equal to `right`'s, otherwise returns `false`.

---

<span id="class_Array_operator_eq_Array"></span>

[bool](class_bool.md#class_bool) **operator ==** ( right: [Array](class_array.md#class_Array) ) [🔗](class_array.md#class_Array_operator_eq_Array)

Compares the left operand **Array** against the `right` **Array**. Returns `true` if the sizes and contents of the arrays are equal, `false` otherwise.

---

<span id="class_Array_operator_gt_Array"></span>

[bool](class_bool.md#class_bool) **operator >** ( right: [Array](class_array.md#class_Array) ) [🔗](class_array.md#class_Array_operator_gt_Array)

Compares the elements of both arrays in order, starting from index `0` and ending on the last index in common between both arrays. For each pair of elements, returns `true` if this array's element is greater than `right`'s, `false` if this element is less. Otherwise, continues to the next pair.

If all searched elements are equal, returns `true` if this array's size is greater than `right`'s, otherwise returns `false`.

---

<span id="class_Array_operator_gte_Array"></span>

[bool](class_bool.md#class_bool) **operator >=** ( right: [Array](class_array.md#class_Array) ) [🔗](class_array.md#class_Array_operator_gte_Array)

Compares the elements of both arrays in order, starting from index `0` and ending on the last index in common between both arrays. For each pair of elements, returns `true` if this array's element is greater than `right`'s, `false` if this element is less. Otherwise, continues to the next pair.

If all searched elements are equal, returns `true` if this array's size is greater or equal to `right`'s, otherwise returns `false`.

---

<span id="class_Array_operator_idx_int"></span>

[Variant](class_variant.md#class_Variant) **operator []** ( index: [int](class_int.md#class_int) ) [🔗](class_array.md#class_Array_operator_idx_int)

Returns the [Variant](class_variant.md#class_Variant) element at the specified `index`. Arrays start at index 0. If `index` is greater or equal to `0`, the element is fetched starting from the beginning of the array. If `index` is a negative value, the element is fetched starting from the end. Accessing an array out-of-bounds will cause a run-time error, pausing the project execution if run from the editor.
