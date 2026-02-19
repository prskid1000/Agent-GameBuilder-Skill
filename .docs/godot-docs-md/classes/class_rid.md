<span id="class_RID"></span>

## RID

A handle for a [Resource](class_resource.md#class_Resource)'s unique identifier.

### Description

The RID [Variant](class_variant.md#class_Variant) type is used to access a low-level resource by its unique ID. RIDs are opaque, which means they do not grant access to the resource by themselves. They are used by the low-level server classes, such as [DisplayServer](class_displayserver.md#class_DisplayServer), [RenderingServer](class_renderingserver.md#class_RenderingServer), [TextServer](class_textserver.md#class_TextServer), etc.

A low-level resource may correspond to a high-level [Resource](class_resource.md#class_Resource), such as [Texture](class_texture.md#class_Texture) or [Mesh](class_mesh.md#class_Mesh).

 **Note:** RIDs are only useful during the current session. It won't correspond to a similar resource if sent over a network, or loaded from a file at a later time.

 **Note:** In a boolean context, an RID will evaluate to `false` if it has the invalid ID `0`. Otherwise, an RID will always evaluate to `true`. This is equivalent to calling [is_valid()](class_rid.md#class_RID_method_is_valid).

> **Note:** There are notable differences when using this API with C#. See :ref:`doc_c_sharp_differences` for more information.

### Constructors


| [RID](class_rid.md#class_RID) | [RID](class_rid.md#class_RID_constructor_RID) ( ) |
| --- | --- |
| [RID](class_rid.md#class_RID) | [RID](class_rid.md#class_RID_constructor_RID) ( from: [RID](class_rid.md#class_RID) ) |

### Methods


| [int](class_int.md#class_int) | [get_id](class_rid.md#class_RID_method_get_id) ( ) const |
| --- | --- |
| [bool](class_bool.md#class_bool) | [is_valid](class_rid.md#class_RID_method_is_valid) ( ) const |

### Operators


| [bool](class_bool.md#class_bool) | [operator !=](class_rid.md#class_RID_operator_neq_RID) ( right: [RID](class_rid.md#class_RID) ) |
| --- | --- |
| [bool](class_bool.md#class_bool) | operator \ ( right: [RID](class_rid.md#class_RID) ) |
| [bool](class_bool.md#class_bool) | operator \ ( right: [RID](class_rid.md#class_RID) ) |
| [bool](class_bool.md#class_bool) | [operator ==](class_rid.md#class_RID_operator_eq_RID) ( right: [RID](class_rid.md#class_RID) ) |
| [bool](class_bool.md#class_bool) | [operator >](class_rid.md#class_RID_operator_gt_RID) ( right: [RID](class_rid.md#class_RID) ) |
| [bool](class_bool.md#class_bool) | [operator >=](class_rid.md#class_RID_operator_gte_RID) ( right: [RID](class_rid.md#class_RID) ) |

---

### Constructor Descriptions

<span id="class_RID_constructor_RID"></span>

[RID](class_rid.md#class_RID) **RID** ( ) [🔗](class_rid.md#class_RID_constructor_RID)

Constructs an empty **RID** with the invalid ID `0`.

---

[RID](class_rid.md#class_RID) **RID** ( from: [RID](class_rid.md#class_RID) )

Constructs an **RID** as a copy of the given **RID**.

---

### Method Descriptions

<span id="class_RID_method_get_id"></span>

[int](class_int.md#class_int) **get_id** ( ) *const* [🔗](class_rid.md#class_RID_method_get_id)

Returns the ID of the referenced low-level resource.

---

<span id="class_RID_method_is_valid"></span>

[bool](class_bool.md#class_bool) **is_valid** ( ) *const* [🔗](class_rid.md#class_RID_method_is_valid)

Returns `true` if the **RID** is not `0`.

---

### Operator Descriptions

<span id="class_RID_operator_neq_RID"></span>

[bool](class_bool.md#class_bool) **operator !=** ( right: [RID](class_rid.md#class_RID) ) [🔗](class_rid.md#class_RID_operator_neq_RID)

Returns `true` if the **RID** s are not equal.

---

<span id="class_RID_operator_lt_RID"></span>

[bool](class_bool.md#class_bool) **operator <** ( right: [RID](class_rid.md#class_RID) ) [🔗](class_rid.md#class_RID_operator_lt_RID)

Returns `true` if the **RID**'s ID is less than `right`'s ID.

---

<span id="class_RID_operator_lte_RID"></span>

[bool](class_bool.md#class_bool) **operator <=** ( right: [RID](class_rid.md#class_RID) ) [🔗](class_rid.md#class_RID_operator_lte_RID)

Returns `true` if the **RID**'s ID is less than or equal to `right`'s ID.

---

<span id="class_RID_operator_eq_RID"></span>

[bool](class_bool.md#class_bool) **operator ==** ( right: [RID](class_rid.md#class_RID) ) [🔗](class_rid.md#class_RID_operator_eq_RID)

Returns `true` if both **RID** s are equal, which means they both refer to the same low-level resource.

---

<span id="class_RID_operator_gt_RID"></span>

[bool](class_bool.md#class_bool) **operator >** ( right: [RID](class_rid.md#class_RID) ) [🔗](class_rid.md#class_RID_operator_gt_RID)

Returns `true` if the **RID**'s ID is greater than `right`'s ID.

---

<span id="class_RID_operator_gte_RID"></span>

[bool](class_bool.md#class_bool) **operator >=** ( right: [RID](class_rid.md#class_RID) ) [🔗](class_rid.md#class_RID_operator_gte_RID)

Returns `true` if the **RID**'s ID is greater than or equal to `right`'s ID.
