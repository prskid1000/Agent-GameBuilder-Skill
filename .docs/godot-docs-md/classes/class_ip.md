.. meta::
	:keywords: dns

<span id="class_IP"></span>

## IP

**Inherits:** [Object](class_object.md#class_Object)

Internet protocol (IP) support functions such as DNS resolution.

### Description

IP contains support functions for the Internet Protocol (IP). TCP/IP support is in different classes (see [StreamPeerTCP](class_streampeertcp.md#class_StreamPeerTCP) and [TCPServer](class_tcpserver.md#class_TCPServer)). IP provides DNS hostname resolution support, both blocking and threaded.

### Methods


| void | [clear_cache](class_ip.md#class_IP_method_clear_cache) ( hostname: [String](class_string.md#class_String) = "" ) |
| --- | --- |
| void | [erase_resolve_item](class_ip.md#class_IP_method_erase_resolve_item) ( id: [int](class_int.md#class_int) ) |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_local_addresses](class_ip.md#class_IP_method_get_local_addresses) ( ) const |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [get_local_interfaces](class_ip.md#class_IP_method_get_local_interfaces) ( ) const |
| [String](class_string.md#class_String) | [get_resolve_item_address](class_ip.md#class_IP_method_get_resolve_item_address) ( id: [int](class_int.md#class_int) ) const |
| [Array](class_array.md#class_Array) | [get_resolve_item_addresses](class_ip.md#class_IP_method_get_resolve_item_addresses) ( id: [int](class_int.md#class_int) ) const |
| [ResolverStatus](class_ip.md#enum_IP_ResolverStatus) | [get_resolve_item_status](class_ip.md#class_IP_method_get_resolve_item_status) ( id: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [resolve_hostname](class_ip.md#class_IP_method_resolve_hostname) ( host: [String](class_string.md#class_String), ip_type: [Type](class_ip.md#enum_IP_Type) = 3 ) |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [resolve_hostname_addresses](class_ip.md#class_IP_method_resolve_hostname_addresses) ( host: [String](class_string.md#class_String), ip_type: [Type](class_ip.md#enum_IP_Type) = 3 ) |
| [int](class_int.md#class_int) | [resolve_hostname_queue_item](class_ip.md#class_IP_method_resolve_hostname_queue_item) ( host: [String](class_string.md#class_String), ip_type: [Type](class_ip.md#enum_IP_Type) = 3 ) |

---

### Enumerations

<span id="enum_IP_ResolverStatus"></span>

enum **ResolverStatus**: [🔗](class_ip.md#enum_IP_ResolverStatus)

<span id="class_IP_constant_RESOLVER_STATUS_NONE"></span>

[ResolverStatus](class_ip.md#enum_IP_ResolverStatus) **RESOLVER_STATUS_NONE** = `0`

DNS hostname resolver status: No status.

<span id="class_IP_constant_RESOLVER_STATUS_WAITING"></span>

[ResolverStatus](class_ip.md#enum_IP_ResolverStatus) **RESOLVER_STATUS_WAITING** = `1`

DNS hostname resolver status: Waiting.

<span id="class_IP_constant_RESOLVER_STATUS_DONE"></span>

[ResolverStatus](class_ip.md#enum_IP_ResolverStatus) **RESOLVER_STATUS_DONE** = `2`

DNS hostname resolver status: Done.

<span id="class_IP_constant_RESOLVER_STATUS_ERROR"></span>

[ResolverStatus](class_ip.md#enum_IP_ResolverStatus) **RESOLVER_STATUS_ERROR** = `3`

DNS hostname resolver status: Error.

---

<span id="enum_IP_Type"></span>

enum **Type**: [🔗](class_ip.md#enum_IP_Type)

<span id="class_IP_constant_TYPE_NONE"></span>

[Type](class_ip.md#enum_IP_Type) **TYPE_NONE** = `0`

Address type: None.

<span id="class_IP_constant_TYPE_IPV4"></span>

[Type](class_ip.md#enum_IP_Type) **TYPE_IPV4** = `1`

Address type: Internet protocol version 4 (IPv4).

<span id="class_IP_constant_TYPE_IPV6"></span>

[Type](class_ip.md#enum_IP_Type) **TYPE_IPV6** = `2`

Address type: Internet protocol version 6 (IPv6).

<span id="class_IP_constant_TYPE_ANY"></span>

[Type](class_ip.md#enum_IP_Type) **TYPE_ANY** = `3`

Address type: Any.

---

### Constants

<span id="class_IP_constant_RESOLVER_MAX_QUERIES"></span>

**RESOLVER_MAX_QUERIES** = `256` [🔗](class_ip.md#class_IP_constant_RESOLVER_MAX_QUERIES)

Maximum number of concurrent DNS resolver queries allowed, [RESOLVER_INVALID_ID](class_ip.md#class_IP_constant_RESOLVER_INVALID_ID) is returned if exceeded.

<span id="class_IP_constant_RESOLVER_INVALID_ID"></span>

**RESOLVER_INVALID_ID** = `-1` [🔗](class_ip.md#class_IP_constant_RESOLVER_INVALID_ID)

Invalid ID constant. Returned if [RESOLVER_MAX_QUERIES](class_ip.md#class_IP_constant_RESOLVER_MAX_QUERIES) is exceeded.

---

### Method Descriptions

<span id="class_IP_method_clear_cache"></span>

void **clear_cache** ( hostname: [String](class_string.md#class_String) = "" ) [🔗](class_ip.md#class_IP_method_clear_cache)

Removes all of a `hostname`'s cached references. If no `hostname` is given, all cached IP addresses are removed.

---

<span id="class_IP_method_erase_resolve_item"></span>

void **erase_resolve_item** ( id: [int](class_int.md#class_int) ) [🔗](class_ip.md#class_IP_method_erase_resolve_item)

Removes a given item `id` from the queue. This should be used to free a queue after it has completed to enable more queries to happen.

---

<span id="class_IP_method_get_local_addresses"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_local_addresses** ( ) *const* [🔗](class_ip.md#class_IP_method_get_local_addresses)

Returns all the user's current IPv4 and IPv6 addresses as an array.

---

<span id="class_IP_method_get_local_interfaces"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **get_local_interfaces** ( ) *const* [🔗](class_ip.md#class_IP_method_get_local_interfaces)

Returns all network adapters as an array.

Each adapter is a dictionary of the form:

::

    {
        "index": "1", # Interface index.
        "name": "eth0", # Interface name.
        "friendly": "Ethernet One", # A friendly name (might be empty).
        "addresses": ["192.168.1.101"], # An array of IP addresses associated to this interface.
    }

---

<span id="class_IP_method_get_resolve_item_address"></span>

[String](class_string.md#class_String) **get_resolve_item_address** ( id: [int](class_int.md#class_int) ) *const* [🔗](class_ip.md#class_IP_method_get_resolve_item_address)

Returns a queued hostname's IP address, given its queue `id`. Returns an empty string on error or if resolution hasn't happened yet (see [get_resolve_item_status()](class_ip.md#class_IP_method_get_resolve_item_status)).

---

<span id="class_IP_method_get_resolve_item_addresses"></span>

[Array](class_array.md#class_Array) **get_resolve_item_addresses** ( id: [int](class_int.md#class_int) ) *const* [🔗](class_ip.md#class_IP_method_get_resolve_item_addresses)

Returns resolved addresses, or an empty array if an error happened or resolution didn't happen yet (see [get_resolve_item_status()](class_ip.md#class_IP_method_get_resolve_item_status)).

---

<span id="class_IP_method_get_resolve_item_status"></span>

[ResolverStatus](class_ip.md#enum_IP_ResolverStatus) **get_resolve_item_status** ( id: [int](class_int.md#class_int) ) *const* [🔗](class_ip.md#class_IP_method_get_resolve_item_status)

Returns a queued hostname's status as a [ResolverStatus](class_ip.md#enum_IP_ResolverStatus) constant, given its queue `id`.

---

<span id="class_IP_method_resolve_hostname"></span>

[String](class_string.md#class_String) **resolve_hostname** ( host: [String](class_string.md#class_String), ip_type: [Type](class_ip.md#enum_IP_Type) = 3 ) [🔗](class_ip.md#class_IP_method_resolve_hostname)

Returns a given hostname's IPv4 or IPv6 address when resolved (blocking-type method). The address type returned depends on the [Type](class_ip.md#enum_IP_Type) constant given as `ip_type`.

---

<span id="class_IP_method_resolve_hostname_addresses"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **resolve_hostname_addresses** ( host: [String](class_string.md#class_String), ip_type: [Type](class_ip.md#enum_IP_Type) = 3 ) [🔗](class_ip.md#class_IP_method_resolve_hostname_addresses)

Resolves a given hostname in a blocking way. Addresses are returned as an [Array](class_array.md#class_Array) of IPv4 or IPv6 addresses depending on `ip_type`.

---

<span id="class_IP_method_resolve_hostname_queue_item"></span>

[int](class_int.md#class_int) **resolve_hostname_queue_item** ( host: [String](class_string.md#class_String), ip_type: [Type](class_ip.md#enum_IP_Type) = 3 ) [🔗](class_ip.md#class_IP_method_resolve_hostname_queue_item)

Creates a queue item to resolve a hostname to an IPv4 or IPv6 address depending on the [Type](class_ip.md#enum_IP_Type) constant given as `ip_type`. Returns the queue ID if successful, or [RESOLVER_INVALID_ID](class_ip.md#class_IP_constant_RESOLVER_INVALID_ID) on error.
