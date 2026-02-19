<span id="class_int"></span>

## int

A built-in type for integers.

### Description

Signed 64-bit integer type. This means that it can take values from `-2^63` to `2^63 - 1`, i.e. from `-9223372036854775808` to `9223372036854775807`. When it exceeds these bounds, it will wrap around.

 **int** s can be automatically converted to [float](class_float.md#class_float) s when necessary, for example when passing them as arguments in functions. The [float](class_float.md#class_float) will be as close to the original integer as possible.

Likewise, [float](class_float.md#class_float) s can be automatically converted into **int** s. This will truncate the [float](class_float.md#class_float), discarding anything after the floating-point.

 **Note:** In a boolean context, an **int** will evaluate to `false` if it equals `0`, and to `true` otherwise.

.. tabs::

```
```

    var x: int = 1 # x is 1
    x = 4.2 # x is 4, because 4.2 gets truncated
    var max_int = 9223372036854775807 # Biggest value an int can store
    max_int += 1 # max_int is -9223372036854775808, because it wrapped around

```
```

    int x = 1; // x is 1
    x = (int)4.2; // x is 4, because 4.2 gets truncated
    // We use long below, because GDScript's int is 64-bit while C#'s int is 32-bit.
    long maxLong = 9223372036854775807; // Biggest value a long can store
    maxLong++; // maxLong is now -9223372036854775808, because it wrapped around.

    // Alternatively with C#'s 32-bit int type, which has a smaller maximum value.
    int maxInt = 2147483647; // Biggest value an int can store
    maxInt++; // maxInt is now -2147483648, because it wrapped around

You can use the `0b` literal for binary representation, the `0x` literal for hexadecimal representation, and the `_` symbol to separate long numbers and improve readability.

.. tabs::

```
```

    var x = 0b1001 # x is 9
    var y = 0xF5 # y is 245
    var z = 10_000_000 # z is 10000000

```
```

    int x = 0b1001; // x is 9
    int y = 0xF5; // y is 245
    int z = 10_000_000; // z is 10000000

### Constructors


| [int](class_int.md#class_int) | [int](class_int.md#class_int_constructor_int) ( ) |
| --- | --- |
| [int](class_int.md#class_int) | [int](class_int.md#class_int_constructor_int) ( from: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [int](class_int.md#class_int_constructor_int) ( from: [String](class_string.md#class_String) ) |
| [int](class_int.md#class_int) | [int](class_int.md#class_int_constructor_int) ( from: [bool](class_bool.md#class_bool) ) |
| [int](class_int.md#class_int) | [int](class_int.md#class_int_constructor_int) ( from: [float](class_float.md#class_float) ) |

### Operators


| [bool](class_bool.md#class_bool) | [operator !=](class_int.md#class_int_operator_neq_float) ( right: [float](class_float.md#class_float) ) |
| --- | --- |
| [bool](class_bool.md#class_bool) | [operator !=](class_int.md#class_int_operator_neq_int) ( right: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [operator %](class_int.md#class_int_operator_mod_int) ( right: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [operator &](class_int.md#class_int_operator_bwand_int) ( right: [int](class_int.md#class_int) ) |
| [Color](class_color.md#class_Color) | [operator *](class_int.md#class_int_operator_mul_Color) ( right: [Color](class_color.md#class_Color) ) |
| [Quaternion](class_quaternion.md#class_Quaternion) | [operator *](class_int.md#class_int_operator_mul_Quaternion) ( right: [Quaternion](class_quaternion.md#class_Quaternion) ) |
| [Vector2](class_vector2.md#class_Vector2) | [operator *](class_int.md#class_int_operator_mul_Vector2) ( right: [Vector2](class_vector2.md#class_Vector2) ) |
| [Vector2i](class_vector2i.md#class_Vector2i) | [operator *](class_int.md#class_int_operator_mul_Vector2i) ( right: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| [Vector3](class_vector3.md#class_Vector3) | [operator *](class_int.md#class_int_operator_mul_Vector3) ( right: [Vector3](class_vector3.md#class_Vector3) ) |
| [Vector3i](class_vector3i.md#class_Vector3i) | [operator *](class_int.md#class_int_operator_mul_Vector3i) ( right: [Vector3i](class_vector3i.md#class_Vector3i) ) |
| [Vector4](class_vector4.md#class_Vector4) | [operator *](class_int.md#class_int_operator_mul_Vector4) ( right: [Vector4](class_vector4.md#class_Vector4) ) |
| [Vector4i](class_vector4i.md#class_Vector4i) | [operator *](class_int.md#class_int_operator_mul_Vector4i) ( right: [Vector4i](class_vector4i.md#class_Vector4i) ) |
| [float](class_float.md#class_float) | [operator *](class_int.md#class_int_operator_mul_float) ( right: [float](class_float.md#class_float) ) |
| [int](class_int.md#class_int) | [operator *](class_int.md#class_int_operator_mul_int) ( right: [int](class_int.md#class_int) ) |
| [float](class_float.md#class_float) | [operator **](class_int.md#class_int_operator_pow_float) ( right: [float](class_float.md#class_float) ) |
| [int](class_int.md#class_int) | [operator **](class_int.md#class_int_operator_pow_int) ( right: [int](class_int.md#class_int) ) |
| [float](class_float.md#class_float) | [operator +](class_int.md#class_int_operator_sum_float) ( right: [float](class_float.md#class_float) ) |
| [int](class_int.md#class_int) | [operator +](class_int.md#class_int_operator_sum_int) ( right: [int](class_int.md#class_int) ) |
| [float](class_float.md#class_float) | [operator -](class_int.md#class_int_operator_dif_float) ( right: [float](class_float.md#class_float) ) |
| [int](class_int.md#class_int) | [operator -](class_int.md#class_int_operator_dif_int) ( right: [int](class_int.md#class_int) ) |
| [float](class_float.md#class_float) | [operator /](class_int.md#class_int_operator_div_float) ( right: [float](class_float.md#class_float) ) |
| [int](class_int.md#class_int) | [operator /](class_int.md#class_int_operator_div_int) ( right: [int](class_int.md#class_int) ) |
| [bool](class_bool.md#class_bool) | operator \ ( right: [float](class_float.md#class_float) ) |
| [bool](class_bool.md#class_bool) | operator \ ( right: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | operator \ ( right: [int](class_int.md#class_int) ) |
| [bool](class_bool.md#class_bool) | operator \ ( right: [float](class_float.md#class_float) ) |
| [bool](class_bool.md#class_bool) | operator \ ( right: [int](class_int.md#class_int) ) |
| [bool](class_bool.md#class_bool) | [operator ==](class_int.md#class_int_operator_eq_float) ( right: [float](class_float.md#class_float) ) |
| [bool](class_bool.md#class_bool) | [operator ==](class_int.md#class_int_operator_eq_int) ( right: [int](class_int.md#class_int) ) |
| [bool](class_bool.md#class_bool) | [operator >](class_int.md#class_int_operator_gt_float) ( right: [float](class_float.md#class_float) ) |
| [bool](class_bool.md#class_bool) | [operator >](class_int.md#class_int_operator_gt_int) ( right: [int](class_int.md#class_int) ) |
| [bool](class_bool.md#class_bool) | [operator >=](class_int.md#class_int_operator_gte_float) ( right: [float](class_float.md#class_float) ) |
| [bool](class_bool.md#class_bool) | [operator >=](class_int.md#class_int_operator_gte_int) ( right: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [operator >>](class_int.md#class_int_operator_bwsr_int) ( right: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [operator ^](class_int.md#class_int_operator_bwxor_int) ( right: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [operator unary+](class_int.md#class_int_operator_unplus) ( ) |
| [int](class_int.md#class_int) | [operator unary-](class_int.md#class_int_operator_unminus) ( ) |
| [int](class_int.md#class_int) | :ref:`operator | <class_int_operator_bwor_int>` ( right: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [operator ~](class_int.md#class_int_operator_bwnot) ( ) |

---

### Constructor Descriptions

<span id="class_int_constructor_int"></span>

[int](class_int.md#class_int) **int** ( ) [🔗](class_int.md#class_int_constructor_int)

Constructs an **int** set to `0`.

---

[int](class_int.md#class_int) **int** ( from: [int](class_int.md#class_int) )

Constructs an **int** as a copy of the given **int**.

---

[int](class_int.md#class_int) **int** ( from: [String](class_string.md#class_String) )

Constructs a new **int** from a [String](class_string.md#class_String), following the same rules as [String.to_int()](class_string.md#class_String_method_to_int).

---

[int](class_int.md#class_int) **int** ( from: [bool](class_bool.md#class_bool) )

Constructs a new **int** from a [bool](class_bool.md#class_bool). `true` is converted to `1` and `false` is converted to `0`.

---

[int](class_int.md#class_int) **int** ( from: [float](class_float.md#class_float) )

Constructs a new **int** from a [float](class_float.md#class_float). This will truncate the [float](class_float.md#class_float), discarding anything after the floating point.

---

### Operator Descriptions

<span id="class_int_operator_neq_float"></span>

[bool](class_bool.md#class_bool) **operator !=** ( right: [float](class_float.md#class_float) ) [🔗](class_int.md#class_int_operator_neq_float)

Returns `true` if the **int** is not equivalent to the [float](class_float.md#class_float).

---

<span id="class_int_operator_neq_int"></span>

[bool](class_bool.md#class_bool) **operator !=** ( right: [int](class_int.md#class_int) ) [🔗](class_int.md#class_int_operator_neq_int)

Returns `true` if the **int** s are not equal.

---

<span id="class_int_operator_mod_int"></span>

[int](class_int.md#class_int) **operator %** ( right: [int](class_int.md#class_int) ) [🔗](class_int.md#class_int_operator_mod_int)

Returns the remainder after dividing two **int** s. Uses truncated division, which returns a negative number if the dividend is negative. If this is not desired, consider using @GlobalScope.posmod().

::

    print(6 % 2) # Prints 0
    print(11 % 4) # Prints 3
    print(-5 % 3) # Prints -2

---

<span id="class_int_operator_bwand_int"></span>

[int](class_int.md#class_int) **operator &** ( right: [int](class_int.md#class_int) ) [🔗](class_int.md#class_int_operator_bwand_int)

Performs the bitwise `AND` operation.

::

    print(0b1100 & 0b1010) # Prints 8 (binary 1000)

This is useful for retrieving binary flags from a variable.

::

    var flags = 0b101
    # Check if the first or second bit are enabled.
    if flags & 0b011:
        do_stuff() # This line will run.

---

<span id="class_int_operator_mul_Color"></span>

[Color](class_color.md#class_Color) **operator *** ( right: [Color](class_color.md#class_Color) ) [🔗](class_int.md#class_int_operator_mul_Color)

Multiplies each component of the [Color](class_color.md#class_Color) by the **int**.

---

<span id="class_int_operator_mul_Quaternion"></span>

[Quaternion](class_quaternion.md#class_Quaternion) **operator *** ( right: [Quaternion](class_quaternion.md#class_Quaternion) ) [🔗](class_int.md#class_int_operator_mul_Quaternion)

Multiplies each component of the [Quaternion](class_quaternion.md#class_Quaternion) by the **int**. This operation is not meaningful on its own, but it can be used as a part of a larger expression.

---

<span id="class_int_operator_mul_Vector2"></span>

[Vector2](class_vector2.md#class_Vector2) **operator *** ( right: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_int.md#class_int_operator_mul_Vector2)

Multiplies each component of the [Vector2](class_vector2.md#class_Vector2) by the **int**.

::

    print(2 * Vector2(1, 4)) # Prints (2, 8)

---

<span id="class_int_operator_mul_Vector2i"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **operator *** ( right: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_int.md#class_int_operator_mul_Vector2i)

Multiplies each component of the [Vector2i](class_vector2i.md#class_Vector2i) by the **int**.

---

<span id="class_int_operator_mul_Vector3"></span>

[Vector3](class_vector3.md#class_Vector3) **operator *** ( right: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_int.md#class_int_operator_mul_Vector3)

Multiplies each component of the [Vector3](class_vector3.md#class_Vector3) by the **int**.

---

<span id="class_int_operator_mul_Vector3i"></span>

[Vector3i](class_vector3i.md#class_Vector3i) **operator *** ( right: [Vector3i](class_vector3i.md#class_Vector3i) ) [🔗](class_int.md#class_int_operator_mul_Vector3i)

Multiplies each component of the [Vector3i](class_vector3i.md#class_Vector3i) by the **int**.

---

<span id="class_int_operator_mul_Vector4"></span>

[Vector4](class_vector4.md#class_Vector4) **operator *** ( right: [Vector4](class_vector4.md#class_Vector4) ) [🔗](class_int.md#class_int_operator_mul_Vector4)

Multiplies each component of the [Vector4](class_vector4.md#class_Vector4) by the **int**.

---

<span id="class_int_operator_mul_Vector4i"></span>

[Vector4i](class_vector4i.md#class_Vector4i) **operator *** ( right: [Vector4i](class_vector4i.md#class_Vector4i) ) [🔗](class_int.md#class_int_operator_mul_Vector4i)

Multiplies each component of the [Vector4i](class_vector4i.md#class_Vector4i) by the **int**.

---

<span id="class_int_operator_mul_float"></span>

[float](class_float.md#class_float) **operator *** ( right: [float](class_float.md#class_float) ) [🔗](class_int.md#class_int_operator_mul_float)

Multiplies the [float](class_float.md#class_float) by the **int**. The result is a [float](class_float.md#class_float).

---

<span id="class_int_operator_mul_int"></span>

[int](class_int.md#class_int) **operator *** ( right: [int](class_int.md#class_int) ) [🔗](class_int.md#class_int_operator_mul_int)

Multiplies the two **int** s.

---

<span id="class_int_operator_pow_float"></span>

[float](class_float.md#class_float) **operator **** ( right: [float](class_float.md#class_float) ) [🔗](class_int.md#class_int_operator_pow_float)

Raises an **int** to a power of a [float](class_float.md#class_float). The result is a [float](class_float.md#class_float).

::

    print(2 ** 0.5) # Prints 1.4142135623731

---

<span id="class_int_operator_pow_int"></span>

[int](class_int.md#class_int) **operator **** ( right: [int](class_int.md#class_int) ) [🔗](class_int.md#class_int_operator_pow_int)

Raises the left **int** to a power of the right **int**.

::

    print(3 ** 4) # Prints 81

---

<span id="class_int_operator_sum_float"></span>

[float](class_float.md#class_float) **operator +** ( right: [float](class_float.md#class_float) ) [🔗](class_int.md#class_int_operator_sum_float)

Adds the **int** and the [float](class_float.md#class_float). The result is a [float](class_float.md#class_float).

---

<span id="class_int_operator_sum_int"></span>

[int](class_int.md#class_int) **operator +** ( right: [int](class_int.md#class_int) ) [🔗](class_int.md#class_int_operator_sum_int)

Adds the two **int** s.

---

<span id="class_int_operator_dif_float"></span>

[float](class_float.md#class_float) **operator -** ( right: [float](class_float.md#class_float) ) [🔗](class_int.md#class_int_operator_dif_float)

Subtracts the [float](class_float.md#class_float) from the **int**. The result is a [float](class_float.md#class_float).

---

<span id="class_int_operator_dif_int"></span>

[int](class_int.md#class_int) **operator -** ( right: [int](class_int.md#class_int) ) [🔗](class_int.md#class_int_operator_dif_int)

Subtracts the two **int** s.

---

<span id="class_int_operator_div_float"></span>

[float](class_float.md#class_float) **operator /** ( right: [float](class_float.md#class_float) ) [🔗](class_int.md#class_int_operator_div_float)

Divides the **int** by the [float](class_float.md#class_float). The result is a [float](class_float.md#class_float).

::

    print(10 / 3.0) # Prints 3.33333333333333

---

<span id="class_int_operator_div_int"></span>

[int](class_int.md#class_int) **operator /** ( right: [int](class_int.md#class_int) ) [🔗](class_int.md#class_int_operator_div_int)

Divides the two **int** s. The result is an **int**. This will truncate the [float](class_float.md#class_float), discarding anything after the floating point.

::

    print(6 / 2) # Prints 3
    print(5 / 3) # Prints 1

---

<span id="class_int_operator_lt_float"></span>

[bool](class_bool.md#class_bool) **operator <** ( right: [float](class_float.md#class_float) ) [🔗](class_int.md#class_int_operator_lt_float)

Returns `true` if the **int** is less than the [float](class_float.md#class_float).

---

<span id="class_int_operator_lt_int"></span>

[bool](class_bool.md#class_bool) **operator <** ( right: [int](class_int.md#class_int) ) [🔗](class_int.md#class_int_operator_lt_int)

Returns `true` if the left **int** is less than the right **int**.

---

<span id="class_int_operator_bwsl_int"></span>

[int](class_int.md#class_int) **operator <<** ( right: [int](class_int.md#class_int) ) [🔗](class_int.md#class_int_operator_bwsl_int)

Performs the bitwise shift left operation. Effectively the same as multiplying by a power of 2.

::

    print(0b1010 << 1) # Prints 20 (binary 10100)
    print(0b1010 << 3) # Prints 80 (binary 1010000)

---

<span id="class_int_operator_lte_float"></span>

[bool](class_bool.md#class_bool) **operator <=** ( right: [float](class_float.md#class_float) ) [🔗](class_int.md#class_int_operator_lte_float)

Returns `true` if the **int** is less than or equal to the [float](class_float.md#class_float).

---

<span id="class_int_operator_lte_int"></span>

[bool](class_bool.md#class_bool) **operator <=** ( right: [int](class_int.md#class_int) ) [🔗](class_int.md#class_int_operator_lte_int)

Returns `true` if the left **int** is less than or equal to the right **int**.

---

<span id="class_int_operator_eq_float"></span>

[bool](class_bool.md#class_bool) **operator ==** ( right: [float](class_float.md#class_float) ) [🔗](class_int.md#class_int_operator_eq_float)

Returns `true` if the **int** is equal to the [float](class_float.md#class_float).

---

<span id="class_int_operator_eq_int"></span>

[bool](class_bool.md#class_bool) **operator ==** ( right: [int](class_int.md#class_int) ) [🔗](class_int.md#class_int_operator_eq_int)

Returns `true` if the two **int** s are equal.

---

<span id="class_int_operator_gt_float"></span>

[bool](class_bool.md#class_bool) **operator >** ( right: [float](class_float.md#class_float) ) [🔗](class_int.md#class_int_operator_gt_float)

Returns `true` if the **int** is greater than the [float](class_float.md#class_float).

---

<span id="class_int_operator_gt_int"></span>

[bool](class_bool.md#class_bool) **operator >** ( right: [int](class_int.md#class_int) ) [🔗](class_int.md#class_int_operator_gt_int)

Returns `true` if the left **int** is greater than the right **int**.

---

<span id="class_int_operator_gte_float"></span>

[bool](class_bool.md#class_bool) **operator >=** ( right: [float](class_float.md#class_float) ) [🔗](class_int.md#class_int_operator_gte_float)

Returns `true` if the **int** is greater than or equal to the [float](class_float.md#class_float).

---

<span id="class_int_operator_gte_int"></span>

[bool](class_bool.md#class_bool) **operator >=** ( right: [int](class_int.md#class_int) ) [🔗](class_int.md#class_int_operator_gte_int)

Returns `true` if the left **int** is greater than or equal to the right **int**.

---

<span id="class_int_operator_bwsr_int"></span>

[int](class_int.md#class_int) **operator >>** ( right: [int](class_int.md#class_int) ) [🔗](class_int.md#class_int_operator_bwsr_int)

Performs the bitwise shift right operation. Effectively the same as dividing by a power of 2.

::

    print(0b1010 >> 1) # Prints 5 (binary 101)
    print(0b1010 >> 2) # Prints 2 (binary 10)

---

<span id="class_int_operator_bwxor_int"></span>

[int](class_int.md#class_int) **operator ^** ( right: [int](class_int.md#class_int) ) [🔗](class_int.md#class_int_operator_bwxor_int)

Performs the bitwise `XOR` operation.

::

    print(0b1100 ^ 0b1010) # Prints 6 (binary 110)

---

<span id="class_int_operator_unplus"></span>

[int](class_int.md#class_int) **operator unary+** ( ) [🔗](class_int.md#class_int_operator_unplus)

Returns the same value as if the `+` was not there. Unary `+` does nothing, but sometimes it can make your code more readable.

---

<span id="class_int_operator_unminus"></span>

[int](class_int.md#class_int) **operator unary-** ( ) [🔗](class_int.md#class_int_operator_unminus)

Returns the negated value of the **int**. If positive, turns the number negative. If negative, turns the number positive. If zero, does nothing.

---

<span id="class_int_operator_bwor_int"></span>

[int](class_int.md#class_int) **operator |** ( right: [int](class_int.md#class_int) ) [🔗](class_int.md#class_int_operator_bwor_int)

Performs the bitwise `OR` operation.

::

    print(0b1100 | 0b1010) # Prints 14 (binary 1110)

This is useful for storing binary flags in a variable.

::

    var flags = 0
    flags |= 0b101 # Turn the first and third bits on.

---

<span id="class_int_operator_bwnot"></span>

[int](class_int.md#class_int) **operator ~** ( ) [🔗](class_int.md#class_int_operator_bwnot)

Performs the bitwise `NOT` operation on the **int**. Due to 2's complement, it's effectively equal to `-(int + 1)`.

::

    print(~4) # Prints -5
    print(~(-7)) # Prints 6
