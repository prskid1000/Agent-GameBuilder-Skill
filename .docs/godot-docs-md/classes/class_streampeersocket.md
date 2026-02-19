<span id="class_StreamPeerSocket"></span>

## StreamPeerSocket

**Inherits:** [StreamPeer](class_streampeer.md#class_StreamPeer) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [StreamPeerTCP](class_streampeertcp.md#class_StreamPeerTCP), [StreamPeerUDS](class_streampeeruds.md#class_StreamPeerUDS)

Abstract base class for interacting with socket streams.

### Description

StreamPeerSocket is an abstract base class that defines common behavior for socket-based streams.

### Methods


| void | [disconnect_from_host](class_streampeersocket.md#class_StreamPeerSocket_method_disconnect_from_host) ( ) |
| --- | --- |
| [Status](class_streampeersocket.md#enum_StreamPeerSocket_Status) | [get_status](class_streampeersocket.md#class_StreamPeerSocket_method_get_status) ( ) const |
| Error | [poll](class_streampeersocket.md#class_StreamPeerSocket_method_poll) ( ) |

---

### Enumerations

<span id="enum_StreamPeerSocket_Status"></span>

enum **Status**: [🔗](class_streampeersocket.md#enum_StreamPeerSocket_Status)

<span id="class_StreamPeerSocket_constant_STATUS_NONE"></span>

[Status](class_streampeersocket.md#enum_StreamPeerSocket_Status) **STATUS_NONE** = `0`

The initial status of the **StreamPeerSocket**. This is also the status after disconnecting.

<span id="class_StreamPeerSocket_constant_STATUS_CONNECTING"></span>

[Status](class_streampeersocket.md#enum_StreamPeerSocket_Status) **STATUS_CONNECTING** = `1`

A status representing a **StreamPeerSocket** that is connecting to a host.

<span id="class_StreamPeerSocket_constant_STATUS_CONNECTED"></span>

[Status](class_streampeersocket.md#enum_StreamPeerSocket_Status) **STATUS_CONNECTED** = `2`

A status representing a **StreamPeerSocket** that is connected to a host.

<span id="class_StreamPeerSocket_constant_STATUS_ERROR"></span>

[Status](class_streampeersocket.md#enum_StreamPeerSocket_Status) **STATUS_ERROR** = `3`

A status representing a **StreamPeerSocket** in error state.

---

### Method Descriptions

<span id="class_StreamPeerSocket_method_disconnect_from_host"></span>

void **disconnect_from_host** ( ) [🔗](class_streampeersocket.md#class_StreamPeerSocket_method_disconnect_from_host)

Disconnects from host.

---

<span id="class_StreamPeerSocket_method_get_status"></span>

[Status](class_streampeersocket.md#enum_StreamPeerSocket_Status) **get_status** ( ) *const* [🔗](class_streampeersocket.md#class_StreamPeerSocket_method_get_status)

Returns the status of the connection.

---

<span id="class_StreamPeerSocket_method_poll"></span>

Error **poll** ( ) [🔗](class_streampeersocket.md#class_StreamPeerSocket_method_poll)

Polls the socket, updating its state. See [get_status()](class_streampeersocket.md#class_StreamPeerSocket_method_get_status).
