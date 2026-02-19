<span id="class_UDSServer"></span>

## UDSServer

**Inherits:** [SocketServer](class_socketserver.md#class_SocketServer) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A Unix Domain Socket (UDS) server.

### Description

A Unix Domain Socket (UDS) server. Listens to connections on a socket path and returns a [StreamPeerUDS](class_streampeeruds.md#class_StreamPeerUDS) when it gets an incoming connection. Unix Domain Sockets provide inter-process communication on the same machine using the filesystem namespace.

 **Note:** Unix Domain Sockets are only available on Unix-like systems (Linux, macOS, etc.) and are not supported on Windows.

### Methods


| Error | [listen](class_udsserver.md#class_UDSServer_method_listen) ( path: [String](class_string.md#class_String) ) |
| --- | --- |
| [StreamPeerUDS](class_streampeeruds.md#class_StreamPeerUDS) | [take_connection](class_udsserver.md#class_UDSServer_method_take_connection) ( ) |

---

### Method Descriptions

<span id="class_UDSServer_method_listen"></span>

Error **listen** ( path: [String](class_string.md#class_String) ) [🔗](class_udsserver.md#class_UDSServer_method_listen)

Listens on the socket at `path`. The socket file will be created at the specified path.

 **Note:** The socket file must not already exist at the specified path. You may need to remove any existing socket file before calling this method.

---

<span id="class_UDSServer_method_take_connection"></span>

[StreamPeerUDS](class_streampeeruds.md#class_StreamPeerUDS) **take_connection** ( ) [🔗](class_udsserver.md#class_UDSServer_method_take_connection)

If a connection is available, returns a StreamPeerUDS with the connection.
