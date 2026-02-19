<span id="class_StreamPeerGZIP"></span>

## StreamPeerGZIP

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [StreamPeer](class_streampeer.md#class_StreamPeer) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A stream peer that handles GZIP and deflate compression/decompression.

### Description

This class allows to compress or decompress data using GZIP/deflate in a streaming fashion. This is particularly useful when compressing or decompressing files that have to be sent through the network without needing to allocate them all in memory.

After starting the stream via [start_compression()](class_streampeergzip.md#class_StreamPeerGZIP_method_start_compression) (or [start_decompression()](class_streampeergzip.md#class_StreamPeerGZIP_method_start_decompression)), calling [StreamPeer.put_partial_data()](class_streampeer.md#class_StreamPeer_method_put_partial_data) on this stream will compress (or decompress) the data, writing it to the internal buffer. Calling [StreamPeer.get_available_bytes()](class_streampeer.md#class_StreamPeer_method_get_available_bytes) will return the pending bytes in the internal buffer, and [StreamPeer.get_partial_data()](class_streampeer.md#class_StreamPeer_method_get_partial_data) will retrieve the compressed (or decompressed) bytes from it. When the stream is over, you must call [finish()](class_streampeergzip.md#class_StreamPeerGZIP_method_finish) to ensure the internal buffer is properly flushed (make sure to call [StreamPeer.get_available_bytes()](class_streampeer.md#class_StreamPeer_method_get_available_bytes) on last time to check if more data needs to be read after that).

### Methods


| void | [clear](class_streampeergzip.md#class_StreamPeerGZIP_method_clear) ( ) |
| --- | --- |
| Error | [finish](class_streampeergzip.md#class_StreamPeerGZIP_method_finish) ( ) |
| Error | [start_compression](class_streampeergzip.md#class_StreamPeerGZIP_method_start_compression) ( use_deflate: [bool](class_bool.md#class_bool) = false, buffer_size: [int](class_int.md#class_int) = 65535 ) |
| Error | [start_decompression](class_streampeergzip.md#class_StreamPeerGZIP_method_start_decompression) ( use_deflate: [bool](class_bool.md#class_bool) = false, buffer_size: [int](class_int.md#class_int) = 65535 ) |

---

### Method Descriptions

<span id="class_StreamPeerGZIP_method_clear"></span>

void **clear** ( ) [🔗](class_streampeergzip.md#class_StreamPeerGZIP_method_clear)

Clears this stream, resetting the internal state.

---

<span id="class_StreamPeerGZIP_method_finish"></span>

Error **finish** ( ) [🔗](class_streampeergzip.md#class_StreamPeerGZIP_method_finish)

Finalizes the stream, compressing any buffered chunk left.

You must call it only when you are compressing.

---

<span id="class_StreamPeerGZIP_method_start_compression"></span>

Error **start_compression** ( use_deflate: [bool](class_bool.md#class_bool) = false, buffer_size: [int](class_int.md#class_int) = 65535 ) [🔗](class_streampeergzip.md#class_StreamPeerGZIP_method_start_compression)

Start the stream in compression mode with the given `buffer_size`, if `use_deflate` is `true` uses deflate instead of GZIP.

---

<span id="class_StreamPeerGZIP_method_start_decompression"></span>

Error **start_decompression** ( use_deflate: [bool](class_bool.md#class_bool) = false, buffer_size: [int](class_int.md#class_int) = 65535 ) [🔗](class_streampeergzip.md#class_StreamPeerGZIP_method_start_decompression)

Start the stream in decompression mode with the given `buffer_size`, if `use_deflate` is `true` uses deflate instead of GZIP.
