<span id="class_SocketServer"></span>

## SocketServer

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [TCPServer](class_tcpserver.md#class_TCPServer), [UDSServer](class_udsserver.md#class_UDSServer)

An abstract class for servers based on sockets.

### Description

A socket server.

### Methods


| [bool](class_bool.md#class_bool) | [is_connection_available](class_socketserver.md#class_SocketServer_method_is_connection_available) ( ) const |
| --- | --- |
| [bool](class_bool.md#class_bool) | [is_listening](class_socketserver.md#class_SocketServer_method_is_listening) ( ) const |
| void | [stop](class_socketserver.md#class_SocketServer_method_stop) ( ) |
| [StreamPeerSocket](class_streampeersocket.md#class_StreamPeerSocket) | [take_socket_connection](class_socketserver.md#class_SocketServer_method_take_socket_connection) ( ) |

---

### Method Descriptions

<span id="class_SocketServer_method_is_connection_available"></span>

[bool](class_bool.md#class_bool) **is_connection_available** ( ) *const* [🔗](class_socketserver.md#class_SocketServer_method_is_connection_available)

Returns `true` if a connection is available for taking.

---

<span id="class_SocketServer_method_is_listening"></span>

[bool](class_bool.md#class_bool) **is_listening** ( ) *const* [🔗](class_socketserver.md#class_SocketServer_method_is_listening)

Returns `true` if the server is currently listening for connections.

---

<span id="class_SocketServer_method_stop"></span>

void **stop** ( ) [🔗](class_socketserver.md#class_SocketServer_method_stop)

Stops listening.

---

<span id="class_SocketServer_method_take_socket_connection"></span>

[StreamPeerSocket](class_streampeersocket.md#class_StreamPeerSocket) **take_socket_connection** ( ) [🔗](class_socketserver.md#class_SocketServer_method_take_socket_connection)

If a connection is available, returns a StreamPeerSocket with the connection.
