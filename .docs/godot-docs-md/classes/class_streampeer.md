<span id="class_StreamPeer"></span>

## StreamPeer

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [StreamPeerBuffer](class_streampeerbuffer.md#class_StreamPeerBuffer), [StreamPeerExtension](class_streampeerextension.md#class_StreamPeerExtension), [StreamPeerGZIP](class_streampeergzip.md#class_StreamPeerGZIP), [StreamPeerSocket](class_streampeersocket.md#class_StreamPeerSocket), [StreamPeerTLS](class_streampeertls.md#class_StreamPeerTLS)

Abstract base class for interacting with streams.

### Description

StreamPeer is an abstract base class mostly used for stream-based protocols (such as TCP). It provides an API for sending and receiving data through streams as raw data or strings.

 **Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

### Properties


| [bool](class_bool.md#class_bool) | [big_endian](class_streampeer.md#class_StreamPeer_property_big_endian) | `false` |
| --- | --- | --- |

### Methods


| [int](class_int.md#class_int) | [get_8](class_streampeer.md#class_StreamPeer_method_get_8) ( ) |
| --- | --- |
| [int](class_int.md#class_int) | [get_16](class_streampeer.md#class_StreamPeer_method_get_16) ( ) |
| [int](class_int.md#class_int) | [get_32](class_streampeer.md#class_StreamPeer_method_get_32) ( ) |
| [int](class_int.md#class_int) | [get_64](class_streampeer.md#class_StreamPeer_method_get_64) ( ) |
| [int](class_int.md#class_int) | [get_available_bytes](class_streampeer.md#class_StreamPeer_method_get_available_bytes) ( ) const |
| [Array](class_array.md#class_Array) | [get_data](class_streampeer.md#class_StreamPeer_method_get_data) ( bytes: [int](class_int.md#class_int) ) |
| [float](class_float.md#class_float) | [get_double](class_streampeer.md#class_StreamPeer_method_get_double) ( ) |
| [float](class_float.md#class_float) | [get_float](class_streampeer.md#class_StreamPeer_method_get_float) ( ) |
| [float](class_float.md#class_float) | [get_half](class_streampeer.md#class_StreamPeer_method_get_half) ( ) |
| [Array](class_array.md#class_Array) | [get_partial_data](class_streampeer.md#class_StreamPeer_method_get_partial_data) ( bytes: [int](class_int.md#class_int) ) |
| [String](class_string.md#class_String) | [get_string](class_streampeer.md#class_StreamPeer_method_get_string) ( bytes: [int](class_int.md#class_int) = -1 ) |
| [int](class_int.md#class_int) | [get_u8](class_streampeer.md#class_StreamPeer_method_get_u8) ( ) |
| [int](class_int.md#class_int) | [get_u16](class_streampeer.md#class_StreamPeer_method_get_u16) ( ) |
| [int](class_int.md#class_int) | [get_u32](class_streampeer.md#class_StreamPeer_method_get_u32) ( ) |
| [int](class_int.md#class_int) | [get_u64](class_streampeer.md#class_StreamPeer_method_get_u64) ( ) |
| [String](class_string.md#class_String) | [get_utf8_string](class_streampeer.md#class_StreamPeer_method_get_utf8_string) ( bytes: [int](class_int.md#class_int) = -1 ) |
| [Variant](class_variant.md#class_Variant) | [get_var](class_streampeer.md#class_StreamPeer_method_get_var) ( allow_objects: [bool](class_bool.md#class_bool) = false ) |
| void | [put_8](class_streampeer.md#class_StreamPeer_method_put_8) ( value: [int](class_int.md#class_int) ) |
| void | [put_16](class_streampeer.md#class_StreamPeer_method_put_16) ( value: [int](class_int.md#class_int) ) |
| void | [put_32](class_streampeer.md#class_StreamPeer_method_put_32) ( value: [int](class_int.md#class_int) ) |
| void | [put_64](class_streampeer.md#class_StreamPeer_method_put_64) ( value: [int](class_int.md#class_int) ) |
| Error | [put_data](class_streampeer.md#class_StreamPeer_method_put_data) ( data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| void | [put_double](class_streampeer.md#class_StreamPeer_method_put_double) ( value: [float](class_float.md#class_float) ) |
| void | [put_float](class_streampeer.md#class_StreamPeer_method_put_float) ( value: [float](class_float.md#class_float) ) |
| void | [put_half](class_streampeer.md#class_StreamPeer_method_put_half) ( value: [float](class_float.md#class_float) ) |
| [Array](class_array.md#class_Array) | [put_partial_data](class_streampeer.md#class_StreamPeer_method_put_partial_data) ( data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| void | [put_string](class_streampeer.md#class_StreamPeer_method_put_string) ( value: [String](class_string.md#class_String) ) |
| void | [put_u8](class_streampeer.md#class_StreamPeer_method_put_u8) ( value: [int](class_int.md#class_int) ) |
| void | [put_u16](class_streampeer.md#class_StreamPeer_method_put_u16) ( value: [int](class_int.md#class_int) ) |
| void | [put_u32](class_streampeer.md#class_StreamPeer_method_put_u32) ( value: [int](class_int.md#class_int) ) |
| void | [put_u64](class_streampeer.md#class_StreamPeer_method_put_u64) ( value: [int](class_int.md#class_int) ) |
| void | [put_utf8_string](class_streampeer.md#class_StreamPeer_method_put_utf8_string) ( value: [String](class_string.md#class_String) ) |
| void | [put_var](class_streampeer.md#class_StreamPeer_method_put_var) ( value: [Variant](class_variant.md#class_Variant), full_objects: [bool](class_bool.md#class_bool) = false ) |

---

### Property Descriptions

<span id="class_StreamPeer_property_big_endian"></span>

[bool](class_bool.md#class_bool) **big_endian** = `false` [🔗](class_streampeer.md#class_StreamPeer_property_big_endian)

- void **set_big_endian** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_big_endian_enabled** ( )

If `true`, this **StreamPeer** will using big-endian format for encoding and decoding.

---

### Method Descriptions

<span id="class_StreamPeer_method_get_8"></span>

[int](class_int.md#class_int) **get_8** ( ) [🔗](class_streampeer.md#class_StreamPeer_method_get_8)

Gets a signed byte from the stream.

---

<span id="class_StreamPeer_method_get_16"></span>

[int](class_int.md#class_int) **get_16** ( ) [🔗](class_streampeer.md#class_StreamPeer_method_get_16)

Gets a signed 16-bit value from the stream.

---

<span id="class_StreamPeer_method_get_32"></span>

[int](class_int.md#class_int) **get_32** ( ) [🔗](class_streampeer.md#class_StreamPeer_method_get_32)

Gets a signed 32-bit value from the stream.

---

<span id="class_StreamPeer_method_get_64"></span>

[int](class_int.md#class_int) **get_64** ( ) [🔗](class_streampeer.md#class_StreamPeer_method_get_64)

Gets a signed 64-bit value from the stream.

---

<span id="class_StreamPeer_method_get_available_bytes"></span>

[int](class_int.md#class_int) **get_available_bytes** ( ) *const* [🔗](class_streampeer.md#class_StreamPeer_method_get_available_bytes)

Returns the number of bytes this **StreamPeer** has available.

---

<span id="class_StreamPeer_method_get_data"></span>

[Array](class_array.md#class_Array) **get_data** ( bytes: [int](class_int.md#class_int) ) [🔗](class_streampeer.md#class_StreamPeer_method_get_data)

Returns a chunk data with the received bytes, as an [Array](class_array.md#class_Array) containing two elements: an Error constant and a [PackedByteArray](class_packedbytearray.md#class_PackedByteArray). `bytes` is the number of bytes to be received. If not enough bytes are available, the function will block until the desired amount is received.

---

<span id="class_StreamPeer_method_get_double"></span>

[float](class_float.md#class_float) **get_double** ( ) [🔗](class_streampeer.md#class_StreamPeer_method_get_double)

Gets a double-precision float from the stream.

---

<span id="class_StreamPeer_method_get_float"></span>

[float](class_float.md#class_float) **get_float** ( ) [🔗](class_streampeer.md#class_StreamPeer_method_get_float)

Gets a single-precision float from the stream.

---

<span id="class_StreamPeer_method_get_half"></span>

[float](class_float.md#class_float) **get_half** ( ) [🔗](class_streampeer.md#class_StreamPeer_method_get_half)

Gets a half-precision float from the stream.

---

<span id="class_StreamPeer_method_get_partial_data"></span>

[Array](class_array.md#class_Array) **get_partial_data** ( bytes: [int](class_int.md#class_int) ) [🔗](class_streampeer.md#class_StreamPeer_method_get_partial_data)

Returns a chunk data with the received bytes, as an [Array](class_array.md#class_Array) containing two elements: an Error constant and a [PackedByteArray](class_packedbytearray.md#class_PackedByteArray). `bytes` is the number of bytes to be received. If not enough bytes are available, the function will return how many were actually received.

---

<span id="class_StreamPeer_method_get_string"></span>

[String](class_string.md#class_String) **get_string** ( bytes: [int](class_int.md#class_int) = -1 ) [🔗](class_streampeer.md#class_StreamPeer_method_get_string)

Gets an ASCII string with byte-length `bytes` from the stream. If `bytes` is negative (default) the length will be read from the stream using the reverse process of [put_string()](class_streampeer.md#class_StreamPeer_method_put_string).

---

<span id="class_StreamPeer_method_get_u8"></span>

[int](class_int.md#class_int) **get_u8** ( ) [🔗](class_streampeer.md#class_StreamPeer_method_get_u8)

Gets an unsigned byte from the stream.

---

<span id="class_StreamPeer_method_get_u16"></span>

[int](class_int.md#class_int) **get_u16** ( ) [🔗](class_streampeer.md#class_StreamPeer_method_get_u16)

Gets an unsigned 16-bit value from the stream.

---

<span id="class_StreamPeer_method_get_u32"></span>

[int](class_int.md#class_int) **get_u32** ( ) [🔗](class_streampeer.md#class_StreamPeer_method_get_u32)

Gets an unsigned 32-bit value from the stream.

---

<span id="class_StreamPeer_method_get_u64"></span>

[int](class_int.md#class_int) **get_u64** ( ) [🔗](class_streampeer.md#class_StreamPeer_method_get_u64)

Gets an unsigned 64-bit value from the stream.

---

<span id="class_StreamPeer_method_get_utf8_string"></span>

[String](class_string.md#class_String) **get_utf8_string** ( bytes: [int](class_int.md#class_int) = -1 ) [🔗](class_streampeer.md#class_StreamPeer_method_get_utf8_string)

Gets a UTF-8 string with byte-length `bytes` from the stream (this decodes the string sent as UTF-8). If `bytes` is negative (default) the length will be read from the stream using the reverse process of [put_utf8_string()](class_streampeer.md#class_StreamPeer_method_put_utf8_string).

---

<span id="class_StreamPeer_method_get_var"></span>

[Variant](class_variant.md#class_Variant) **get_var** ( allow_objects: [bool](class_bool.md#class_bool) = false ) [🔗](class_streampeer.md#class_StreamPeer_method_get_var)

Gets a Variant from the stream. If `allow_objects` is `true`, decoding objects is allowed.

Internally, this uses the same decoding mechanism as the @GlobalScope.bytes_to_var() method.

 **Warning:** Deserialized objects can contain code which gets executed. Do not use this option if the serialized object comes from untrusted sources to avoid potential security threats such as remote code execution.

---

<span id="class_StreamPeer_method_put_8"></span>

void **put_8** ( value: [int](class_int.md#class_int) ) [🔗](class_streampeer.md#class_StreamPeer_method_put_8)

Puts a signed byte into the stream.

---

<span id="class_StreamPeer_method_put_16"></span>

void **put_16** ( value: [int](class_int.md#class_int) ) [🔗](class_streampeer.md#class_StreamPeer_method_put_16)

Puts a signed 16-bit value into the stream.

---

<span id="class_StreamPeer_method_put_32"></span>

void **put_32** ( value: [int](class_int.md#class_int) ) [🔗](class_streampeer.md#class_StreamPeer_method_put_32)

Puts a signed 32-bit value into the stream.

---

<span id="class_StreamPeer_method_put_64"></span>

void **put_64** ( value: [int](class_int.md#class_int) ) [🔗](class_streampeer.md#class_StreamPeer_method_put_64)

Puts a signed 64-bit value into the stream.

---

<span id="class_StreamPeer_method_put_data"></span>

Error **put_data** ( data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_streampeer.md#class_StreamPeer_method_put_data)

Sends a chunk of data through the connection, blocking if necessary until the data is done sending. This function returns an Error code.

---

<span id="class_StreamPeer_method_put_double"></span>

void **put_double** ( value: [float](class_float.md#class_float) ) [🔗](class_streampeer.md#class_StreamPeer_method_put_double)

Puts a double-precision float into the stream.

---

<span id="class_StreamPeer_method_put_float"></span>

void **put_float** ( value: [float](class_float.md#class_float) ) [🔗](class_streampeer.md#class_StreamPeer_method_put_float)

Puts a single-precision float into the stream.

---

<span id="class_StreamPeer_method_put_half"></span>

void **put_half** ( value: [float](class_float.md#class_float) ) [🔗](class_streampeer.md#class_StreamPeer_method_put_half)

Puts a half-precision float into the stream.

---

<span id="class_StreamPeer_method_put_partial_data"></span>

[Array](class_array.md#class_Array) **put_partial_data** ( data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_streampeer.md#class_StreamPeer_method_put_partial_data)

Sends a chunk of data through the connection. If all the data could not be sent at once, only part of it will. This function returns two values, an Error code and an integer, describing how much data was actually sent.

---

<span id="class_StreamPeer_method_put_string"></span>

void **put_string** ( value: [String](class_string.md#class_String) ) [🔗](class_streampeer.md#class_StreamPeer_method_put_string)

Puts a zero-terminated ASCII string into the stream prepended by a 32-bit unsigned integer representing its size.

 **Note:** To put an ASCII string without prepending its size, you can use [put_data()](class_streampeer.md#class_StreamPeer_method_put_data):

.. tabs::

```
```

    put_data("Hello world".to_ascii_buffer())

```
```

    PutData("Hello World".ToAsciiBuffer());

---

<span id="class_StreamPeer_method_put_u8"></span>

void **put_u8** ( value: [int](class_int.md#class_int) ) [🔗](class_streampeer.md#class_StreamPeer_method_put_u8)

Puts an unsigned byte into the stream.

---

<span id="class_StreamPeer_method_put_u16"></span>

void **put_u16** ( value: [int](class_int.md#class_int) ) [🔗](class_streampeer.md#class_StreamPeer_method_put_u16)

Puts an unsigned 16-bit value into the stream.

---

<span id="class_StreamPeer_method_put_u32"></span>

void **put_u32** ( value: [int](class_int.md#class_int) ) [🔗](class_streampeer.md#class_StreamPeer_method_put_u32)

Puts an unsigned 32-bit value into the stream.

---

<span id="class_StreamPeer_method_put_u64"></span>

void **put_u64** ( value: [int](class_int.md#class_int) ) [🔗](class_streampeer.md#class_StreamPeer_method_put_u64)

Puts an unsigned 64-bit value into the stream.

---

<span id="class_StreamPeer_method_put_utf8_string"></span>

void **put_utf8_string** ( value: [String](class_string.md#class_String) ) [🔗](class_streampeer.md#class_StreamPeer_method_put_utf8_string)

Puts a zero-terminated UTF-8 string into the stream prepended by a 32 bits unsigned integer representing its size.

 **Note:** To put a UTF-8 string without prepending its size, you can use [put_data()](class_streampeer.md#class_StreamPeer_method_put_data):

.. tabs::

```
```

    put_data("Hello world".to_utf8_buffer())

```
```

    PutData("Hello World".ToUtf8Buffer());

---

<span id="class_StreamPeer_method_put_var"></span>

void **put_var** ( value: [Variant](class_variant.md#class_Variant), full_objects: [bool](class_bool.md#class_bool) = false ) [🔗](class_streampeer.md#class_StreamPeer_method_put_var)

Puts a Variant into the stream. If `full_objects` is `true` encoding objects is allowed (and can potentially include code).

Internally, this uses the same encoding mechanism as the @GlobalScope.var_to_bytes() method.
