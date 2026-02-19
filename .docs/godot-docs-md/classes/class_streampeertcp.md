<span id="class_StreamPeerTCP"></span>

## StreamPeerTCP

**Inherits:** [StreamPeerSocket](class_streampeersocket.md#class_StreamPeerSocket) **<** [StreamPeer](class_streampeer.md#class_StreamPeer) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A stream peer that handles TCP connections.

### Description

A stream peer that handles TCP connections. This object can be used to connect to TCP servers, or also is returned by a TCP server.

 **Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

### Methods


| Error | [bind](class_streampeertcp.md#class_StreamPeerTCP_method_bind) ( port: [int](class_int.md#class_int), host: [String](class_string.md#class_String) = "*" ) |
| --- | --- |
| Error | [connect_to_host](class_streampeertcp.md#class_StreamPeerTCP_method_connect_to_host) ( host: [String](class_string.md#class_String), port: [int](class_int.md#class_int) ) |
| [String](class_string.md#class_String) | [get_connected_host](class_streampeertcp.md#class_StreamPeerTCP_method_get_connected_host) ( ) const |
| [int](class_int.md#class_int) | [get_connected_port](class_streampeertcp.md#class_StreamPeerTCP_method_get_connected_port) ( ) const |
| [int](class_int.md#class_int) | [get_local_port](class_streampeertcp.md#class_StreamPeerTCP_method_get_local_port) ( ) const |
| void | [set_no_delay](class_streampeertcp.md#class_StreamPeerTCP_method_set_no_delay) ( enabled: [bool](class_bool.md#class_bool) ) |

---

### Method Descriptions

<span id="class_StreamPeerTCP_method_bind"></span>

Error **bind** ( port: [int](class_int.md#class_int), host: [String](class_string.md#class_String) = "*" ) [🔗](class_streampeertcp.md#class_StreamPeerTCP_method_bind)

Opens the TCP socket, and binds it to the specified local address.

This method is generally not needed, and only used to force the subsequent call to [connect_to_host()](class_streampeertcp.md#class_StreamPeerTCP_method_connect_to_host) to use the specified `host` and `port` as source address. This can be desired in some NAT punchthrough techniques, or when forcing the source network interface.

---

<span id="class_StreamPeerTCP_method_connect_to_host"></span>

Error **connect_to_host** ( host: [String](class_string.md#class_String), port: [int](class_int.md#class_int) ) [🔗](class_streampeertcp.md#class_StreamPeerTCP_method_connect_to_host)

Connects to the specified `host:port` pair. A hostname will be resolved if valid. Returns @GlobalScope.OK on success.

---

<span id="class_StreamPeerTCP_method_get_connected_host"></span>

[String](class_string.md#class_String) **get_connected_host** ( ) *const* [🔗](class_streampeertcp.md#class_StreamPeerTCP_method_get_connected_host)

Returns the IP of this peer.

---

<span id="class_StreamPeerTCP_method_get_connected_port"></span>

[int](class_int.md#class_int) **get_connected_port** ( ) *const* [🔗](class_streampeertcp.md#class_StreamPeerTCP_method_get_connected_port)

Returns the port of this peer.

---

<span id="class_StreamPeerTCP_method_get_local_port"></span>

[int](class_int.md#class_int) **get_local_port** ( ) *const* [🔗](class_streampeertcp.md#class_StreamPeerTCP_method_get_local_port)

Returns the local port to which this peer is bound.

---

<span id="class_StreamPeerTCP_method_set_no_delay"></span>

void **set_no_delay** ( enabled: [bool](class_bool.md#class_bool) ) [🔗](class_streampeertcp.md#class_StreamPeerTCP_method_set_no_delay)

If `enabled` is `true`, packets will be sent immediately. If `enabled` is `false` (the default), packet transfers will be delayed and combined using Nagle's algorithm.

 **Note:** It's recommended to leave this disabled for applications that send large packets or need to transfer a lot of data, as enabling this can decrease the total available bandwidth.
