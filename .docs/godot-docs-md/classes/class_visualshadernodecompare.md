<span id="class_VisualShaderNodeCompare"></span>

## VisualShaderNodeCompare

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A comparison function for common types within the visual shader graph.

### Description

Compares `a` and `b` of [type](class_visualshadernodecompare.md#class_VisualShaderNodeCompare_property_type) by [function](class_visualshadernodecompare.md#class_VisualShaderNodeCompare_property_function). Returns a boolean scalar. Translates to `if` instruction in shader code.

### Properties


| [Condition](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_Condition) | [condition](class_visualshadernodecompare.md#class_VisualShaderNodeCompare_property_condition) | `0` |
| --- | --- | --- |
| [Function](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_Function) | [function](class_visualshadernodecompare.md#class_VisualShaderNodeCompare_property_function) | `0` |
| [ComparisonType](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_ComparisonType) | [type](class_visualshadernodecompare.md#class_VisualShaderNodeCompare_property_type) | `0` |

---

### Enumerations

<span id="enum_VisualShaderNodeCompare_ComparisonType"></span>

enum **ComparisonType**: [🔗](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_ComparisonType)

<span id="class_VisualShaderNodeCompare_constant_CTYPE_SCALAR"></span>

[ComparisonType](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_ComparisonType) **CTYPE_SCALAR** = `0`

A floating-point scalar.

<span id="class_VisualShaderNodeCompare_constant_CTYPE_SCALAR_INT"></span>

[ComparisonType](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_ComparisonType) **CTYPE_SCALAR_INT** = `1`

An integer scalar.

<span id="class_VisualShaderNodeCompare_constant_CTYPE_SCALAR_UINT"></span>

[ComparisonType](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_ComparisonType) **CTYPE_SCALAR_UINT** = `2`

An unsigned integer scalar.

<span id="class_VisualShaderNodeCompare_constant_CTYPE_VECTOR_2D"></span>

[ComparisonType](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_ComparisonType) **CTYPE_VECTOR_2D** = `3`

A 2D vector type.

<span id="class_VisualShaderNodeCompare_constant_CTYPE_VECTOR_3D"></span>

[ComparisonType](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_ComparisonType) **CTYPE_VECTOR_3D** = `4`

A 3D vector type.

<span id="class_VisualShaderNodeCompare_constant_CTYPE_VECTOR_4D"></span>

[ComparisonType](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_ComparisonType) **CTYPE_VECTOR_4D** = `5`

A 4D vector type.

<span id="class_VisualShaderNodeCompare_constant_CTYPE_BOOLEAN"></span>

[ComparisonType](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_ComparisonType) **CTYPE_BOOLEAN** = `6`

A boolean type.

<span id="class_VisualShaderNodeCompare_constant_CTYPE_TRANSFORM"></span>

[ComparisonType](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_ComparisonType) **CTYPE_TRANSFORM** = `7`

A transform (`mat4`) type.

<span id="class_VisualShaderNodeCompare_constant_CTYPE_MAX"></span>

[ComparisonType](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_ComparisonType) **CTYPE_MAX** = `8`

Represents the size of the [ComparisonType](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_ComparisonType) enum.

---

<span id="enum_VisualShaderNodeCompare_Function"></span>

enum **Function**: [🔗](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_Function)

<span id="class_VisualShaderNodeCompare_constant_FUNC_EQUAL"></span>

[Function](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_Function) **FUNC_EQUAL** = `0`

Comparison for equality (`a == b`).

<span id="class_VisualShaderNodeCompare_constant_FUNC_NOT_EQUAL"></span>

[Function](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_Function) **FUNC_NOT_EQUAL** = `1`

Comparison for inequality (`a != b`).

<span id="class_VisualShaderNodeCompare_constant_FUNC_GREATER_THAN"></span>

[Function](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_Function) **FUNC_GREATER_THAN** = `2`

Comparison for greater than (`a > b`). Cannot be used if [type](class_visualshadernodecompare.md#class_VisualShaderNodeCompare_property_type) set to [CTYPE_BOOLEAN](class_visualshadernodecompare.md#class_VisualShaderNodeCompare_constant_CTYPE_BOOLEAN) or [CTYPE_TRANSFORM](class_visualshadernodecompare.md#class_VisualShaderNodeCompare_constant_CTYPE_TRANSFORM).

<span id="class_VisualShaderNodeCompare_constant_FUNC_GREATER_THAN_EQUAL"></span>

[Function](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_Function) **FUNC_GREATER_THAN_EQUAL** = `3`

Comparison for greater than or equal (`a >= b`). Cannot be used if [type](class_visualshadernodecompare.md#class_VisualShaderNodeCompare_property_type) set to [CTYPE_BOOLEAN](class_visualshadernodecompare.md#class_VisualShaderNodeCompare_constant_CTYPE_BOOLEAN) or [CTYPE_TRANSFORM](class_visualshadernodecompare.md#class_VisualShaderNodeCompare_constant_CTYPE_TRANSFORM).

<span id="class_VisualShaderNodeCompare_constant_FUNC_LESS_THAN"></span>

[Function](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_Function) **FUNC_LESS_THAN** = `4`

Comparison for less than (`a < b`). Cannot be used if [type](class_visualshadernodecompare.md#class_VisualShaderNodeCompare_property_type) set to [CTYPE_BOOLEAN](class_visualshadernodecompare.md#class_VisualShaderNodeCompare_constant_CTYPE_BOOLEAN) or [CTYPE_TRANSFORM](class_visualshadernodecompare.md#class_VisualShaderNodeCompare_constant_CTYPE_TRANSFORM).

<span id="class_VisualShaderNodeCompare_constant_FUNC_LESS_THAN_EQUAL"></span>

[Function](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_Function) **FUNC_LESS_THAN_EQUAL** = `5`

Comparison for less than or equal (`a <= b`). Cannot be used if [type](class_visualshadernodecompare.md#class_VisualShaderNodeCompare_property_type) set to [CTYPE_BOOLEAN](class_visualshadernodecompare.md#class_VisualShaderNodeCompare_constant_CTYPE_BOOLEAN) or [CTYPE_TRANSFORM](class_visualshadernodecompare.md#class_VisualShaderNodeCompare_constant_CTYPE_TRANSFORM).

<span id="class_VisualShaderNodeCompare_constant_FUNC_MAX"></span>

[Function](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_Function) **FUNC_MAX** = `6`

Represents the size of the [Function](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_Function) enum.

---

<span id="enum_VisualShaderNodeCompare_Condition"></span>

enum **Condition**: [🔗](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_Condition)

<span id="class_VisualShaderNodeCompare_constant_COND_ALL"></span>

[Condition](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_Condition) **COND_ALL** = `0`

The result will be `true` if all components in the vector satisfy the comparison condition.

<span id="class_VisualShaderNodeCompare_constant_COND_ANY"></span>

[Condition](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_Condition) **COND_ANY** = `1`

The result will be `true` if any component in the vector satisfies the comparison condition.

<span id="class_VisualShaderNodeCompare_constant_COND_MAX"></span>

[Condition](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_Condition) **COND_MAX** = `2`

Represents the size of the [Condition](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_Condition) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeCompare_property_condition"></span>

[Condition](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_Condition) **condition** = `0` [🔗](class_visualshadernodecompare.md#class_VisualShaderNodeCompare_property_condition)

- void **set_condition** ( value: [Condition](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_Condition) )
- [Condition](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_Condition) **get_condition** ( )

Extra condition which is applied if [type](class_visualshadernodecompare.md#class_VisualShaderNodeCompare_property_type) is set to [CTYPE_VECTOR_3D](class_visualshadernodecompare.md#class_VisualShaderNodeCompare_constant_CTYPE_VECTOR_3D).

---

<span id="class_VisualShaderNodeCompare_property_function"></span>

[Function](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_Function) **function** = `0` [🔗](class_visualshadernodecompare.md#class_VisualShaderNodeCompare_property_function)

- void **set_function** ( value: [Function](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_Function) )
- [Function](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_Function) **get_function** ( )

A comparison function.

---

<span id="class_VisualShaderNodeCompare_property_type"></span>

[ComparisonType](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_ComparisonType) **type** = `0` [🔗](class_visualshadernodecompare.md#class_VisualShaderNodeCompare_property_type)

- void **set_comparison_type** ( value: [ComparisonType](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_ComparisonType) )
- [ComparisonType](class_visualshadernodecompare.md#enum_VisualShaderNodeCompare_ComparisonType) **get_comparison_type** ( )

The type to be used in the comparison.
