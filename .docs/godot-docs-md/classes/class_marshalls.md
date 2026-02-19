<span id="class_Marshalls"></span>

## Marshalls

**Inherits:** [Object](class_object.md#class_Object)

Data transformation (marshaling) and encoding helpers.

### Description

Provides data transformation and encoding utility functions.

### Methods


| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [base64_to_raw](class_marshalls.md#class_Marshalls_method_base64_to_raw) ( base64_str: [String](class_string.md#class_String) ) |
| --- | --- |
| [String](class_string.md#class_String) | [base64_to_utf8](class_marshalls.md#class_Marshalls_method_base64_to_utf8) ( base64_str: [String](class_string.md#class_String) ) |
| [Variant](class_variant.md#class_Variant) | [base64_to_variant](class_marshalls.md#class_Marshalls_method_base64_to_variant) ( base64_str: [String](class_string.md#class_String), allow_objects: [bool](class_bool.md#class_bool) = false ) |
| [String](class_string.md#class_String) | [raw_to_base64](class_marshalls.md#class_Marshalls_method_raw_to_base64) ( array: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| [String](class_string.md#class_String) | [utf8_to_base64](class_marshalls.md#class_Marshalls_method_utf8_to_base64) ( utf8_str: [String](class_string.md#class_String) ) |
| [String](class_string.md#class_String) | [variant_to_base64](class_marshalls.md#class_Marshalls_method_variant_to_base64) ( variant: [Variant](class_variant.md#class_Variant), full_objects: [bool](class_bool.md#class_bool) = false ) |

---

### Method Descriptions

<span id="class_Marshalls_method_base64_to_raw"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **base64_to_raw** ( base64_str: [String](class_string.md#class_String) ) [🔗](class_marshalls.md#class_Marshalls_method_base64_to_raw)

Returns a decoded [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) corresponding to the Base64-encoded string `base64_str`.

---

<span id="class_Marshalls_method_base64_to_utf8"></span>

[String](class_string.md#class_String) **base64_to_utf8** ( base64_str: [String](class_string.md#class_String) ) [🔗](class_marshalls.md#class_Marshalls_method_base64_to_utf8)

Returns a decoded string corresponding to the Base64-encoded string `base64_str`.

---

<span id="class_Marshalls_method_base64_to_variant"></span>

[Variant](class_variant.md#class_Variant) **base64_to_variant** ( base64_str: [String](class_string.md#class_String), allow_objects: [bool](class_bool.md#class_bool) = false ) [🔗](class_marshalls.md#class_Marshalls_method_base64_to_variant)

Returns a decoded [Variant](class_variant.md#class_Variant) corresponding to the Base64-encoded string `base64_str`. If `allow_objects` is `true`, decoding objects is allowed.

Internally, this uses the same decoding mechanism as the @GlobalScope.bytes_to_var() method.

 **Warning:** Deserialized objects can contain code which gets executed. Do not use this option if the serialized object comes from untrusted sources to avoid potential security threats such as remote code execution.

---

<span id="class_Marshalls_method_raw_to_base64"></span>

[String](class_string.md#class_String) **raw_to_base64** ( array: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_marshalls.md#class_Marshalls_method_raw_to_base64)

Returns a Base64-encoded string of a given [PackedByteArray](class_packedbytearray.md#class_PackedByteArray).

---

<span id="class_Marshalls_method_utf8_to_base64"></span>

[String](class_string.md#class_String) **utf8_to_base64** ( utf8_str: [String](class_string.md#class_String) ) [🔗](class_marshalls.md#class_Marshalls_method_utf8_to_base64)

Returns a Base64-encoded string of the UTF-8 string `utf8_str`.

---

<span id="class_Marshalls_method_variant_to_base64"></span>

[String](class_string.md#class_String) **variant_to_base64** ( variant: [Variant](class_variant.md#class_Variant), full_objects: [bool](class_bool.md#class_bool) = false ) [🔗](class_marshalls.md#class_Marshalls_method_variant_to_base64)

Returns a Base64-encoded string of the [Variant](class_variant.md#class_Variant) `variant`. If `full_objects` is `true`, encoding objects is allowed (and can potentially include code).

Internally, this uses the same encoding mechanism as the @GlobalScope.var_to_bytes() method.
