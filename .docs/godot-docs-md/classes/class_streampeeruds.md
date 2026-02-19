<span id="class_StreamPeerUDS"></span>

## StreamPeerUDS

**Inherits:** [StreamPeerSocket](class_streampeersocket.md#class_StreamPeerSocket) **<** [StreamPeer](class_streampeer.md#class_StreamPeer) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A stream peer that handles UNIX Domain Socket (UDS) connections.

### Description

A stream peer that handles UNIX Domain Socket (UDS) connections. This object can be used to connect to UDS servers, or also is returned by a UDS server. Unix Domain Sockets provide inter-process communication on the same machine using the filesystem namespace.

 **Note:** UNIX Domain Sockets are only available on UNIX-like systems (Linux, macOS, etc.) and are not supported on Windows.

### Methods


| Error | [bind](class_streampeeruds.md#class_StreamPeerUDS_method_bind) ( path: [String](class_string.md#class_String) ) |
| --- | --- |
| Error | [connect_to_host](class_streampeeruds.md#class_StreamPeerUDS_method_connect_to_host) ( path: [String](class_string.md#class_String) ) |
| [String](class_string.md#class_String) | [get_connected_path](class_streampeeruds.md#class_StreamPeerUDS_method_get_connected_path) ( ) const |

---

### Method Descriptions

<span id="class_StreamPeerUDS_method_bind"></span>

Error **bind** ( path: [String](class_string.md#class_String) ) [🔗](class_streampeeruds.md#class_StreamPeerUDS_method_bind)

Opens the UDS socket, and binds it to the specified socket path.

This method is generally not needed, and only used to force the subsequent call to [connect_to_host()](class_streampeeruds.md#class_StreamPeerUDS_method_connect_to_host) to use the specified `path` as the source address.

---

<span id="class_StreamPeerUDS_method_connect_to_host"></span>

Error **connect_to_host** ( path: [String](class_string.md#class_String) ) [🔗](class_streampeeruds.md#class_StreamPeerUDS_method_connect_to_host)

Connects to the specified UNIX Domain Socket path. Returns @GlobalScope.OK on success.

---

<span id="class_StreamPeerUDS_method_get_connected_path"></span>

[String](class_string.md#class_String) **get_connected_path** ( ) *const* [🔗](class_streampeeruds.md#class_StreamPeerUDS_method_get_connected_path)

Returns the socket path of this peer.
