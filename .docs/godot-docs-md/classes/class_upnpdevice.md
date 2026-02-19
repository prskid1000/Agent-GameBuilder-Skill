<span id="class_UPNPDevice"></span>

## UPNPDevice

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Universal Plug and Play (UPnP) device.

### Description

Universal Plug and Play (UPnP) device. See [UPNP](class_upnp.md#class_UPNP) for UPnP discovery and utility functions. Provides low-level access to UPNP control commands. Allows to manage port mappings (port forwarding) and to query network information of the device (like local and external IP address and status). Note that methods on this class are synchronous and block the calling thread.

### Properties


| [String](class_string.md#class_String) | [description_url](class_upnpdevice.md#class_UPNPDevice_property_description_url) | `""` |
| --- | --- | --- |
| [String](class_string.md#class_String) | [igd_control_url](class_upnpdevice.md#class_UPNPDevice_property_igd_control_url) | `""` |
| [String](class_string.md#class_String) | [igd_our_addr](class_upnpdevice.md#class_UPNPDevice_property_igd_our_addr) | `""` |
| [String](class_string.md#class_String) | [igd_service_type](class_upnpdevice.md#class_UPNPDevice_property_igd_service_type) | `""` |
| [IGDStatus](class_upnpdevice.md#enum_UPNPDevice_IGDStatus) | [igd_status](class_upnpdevice.md#class_UPNPDevice_property_igd_status) | `9` |
| [String](class_string.md#class_String) | [service_type](class_upnpdevice.md#class_UPNPDevice_property_service_type) | `""` |

### Methods


| [int](class_int.md#class_int) | [add_port_mapping](class_upnpdevice.md#class_UPNPDevice_method_add_port_mapping) ( port: [int](class_int.md#class_int), port_internal: [int](class_int.md#class_int) = 0, desc: [String](class_string.md#class_String) = "", proto: [String](class_string.md#class_String) = "UDP", duration: [int](class_int.md#class_int) = 0 ) const |
| --- | --- |
| [int](class_int.md#class_int) | [delete_port_mapping](class_upnpdevice.md#class_UPNPDevice_method_delete_port_mapping) ( port: [int](class_int.md#class_int), proto: [String](class_string.md#class_String) = "UDP" ) const |
| [bool](class_bool.md#class_bool) | [is_valid_gateway](class_upnpdevice.md#class_UPNPDevice_method_is_valid_gateway) ( ) const |
| [String](class_string.md#class_String) | [query_external_address](class_upnpdevice.md#class_UPNPDevice_method_query_external_address) ( ) const |

---

### Enumerations

<span id="enum_UPNPDevice_IGDStatus"></span>

enum **IGDStatus**: [🔗](class_upnpdevice.md#enum_UPNPDevice_IGDStatus)

<span id="class_UPNPDevice_constant_IGD_STATUS_OK"></span>

[IGDStatus](class_upnpdevice.md#enum_UPNPDevice_IGDStatus) **IGD_STATUS_OK** = `0`

OK.

<span id="class_UPNPDevice_constant_IGD_STATUS_HTTP_ERROR"></span>

[IGDStatus](class_upnpdevice.md#enum_UPNPDevice_IGDStatus) **IGD_STATUS_HTTP_ERROR** = `1`

HTTP error.

<span id="class_UPNPDevice_constant_IGD_STATUS_HTTP_EMPTY"></span>

[IGDStatus](class_upnpdevice.md#enum_UPNPDevice_IGDStatus) **IGD_STATUS_HTTP_EMPTY** = `2`

Empty HTTP response.

<span id="class_UPNPDevice_constant_IGD_STATUS_NO_URLS"></span>

[IGDStatus](class_upnpdevice.md#enum_UPNPDevice_IGDStatus) **IGD_STATUS_NO_URLS** = `3`

**Deprecated:** This value is no longer used.

Returned response contained no URLs.

<span id="class_UPNPDevice_constant_IGD_STATUS_NO_IGD"></span>

[IGDStatus](class_upnpdevice.md#enum_UPNPDevice_IGDStatus) **IGD_STATUS_NO_IGD** = `4`

Not a valid IGD.

<span id="class_UPNPDevice_constant_IGD_STATUS_DISCONNECTED"></span>

[IGDStatus](class_upnpdevice.md#enum_UPNPDevice_IGDStatus) **IGD_STATUS_DISCONNECTED** = `5`

Disconnected.

<span id="class_UPNPDevice_constant_IGD_STATUS_UNKNOWN_DEVICE"></span>

[IGDStatus](class_upnpdevice.md#enum_UPNPDevice_IGDStatus) **IGD_STATUS_UNKNOWN_DEVICE** = `6`

Unknown device.

<span id="class_UPNPDevice_constant_IGD_STATUS_INVALID_CONTROL"></span>

[IGDStatus](class_upnpdevice.md#enum_UPNPDevice_IGDStatus) **IGD_STATUS_INVALID_CONTROL** = `7`

Invalid control.

<span id="class_UPNPDevice_constant_IGD_STATUS_MALLOC_ERROR"></span>

[IGDStatus](class_upnpdevice.md#enum_UPNPDevice_IGDStatus) **IGD_STATUS_MALLOC_ERROR** = `8`

**Deprecated:** This value is no longer used.

Memory allocation error.

<span id="class_UPNPDevice_constant_IGD_STATUS_UNKNOWN_ERROR"></span>

[IGDStatus](class_upnpdevice.md#enum_UPNPDevice_IGDStatus) **IGD_STATUS_UNKNOWN_ERROR** = `9`

Unknown error.

---

### Property Descriptions

<span id="class_UPNPDevice_property_description_url"></span>

[String](class_string.md#class_String) **description_url** = `""` [🔗](class_upnpdevice.md#class_UPNPDevice_property_description_url)

- void **set_description_url** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_description_url** ( )

URL to the device description.

---

<span id="class_UPNPDevice_property_igd_control_url"></span>

[String](class_string.md#class_String) **igd_control_url** = `""` [🔗](class_upnpdevice.md#class_UPNPDevice_property_igd_control_url)

- void **set_igd_control_url** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_igd_control_url** ( )

IDG control URL.

---

<span id="class_UPNPDevice_property_igd_our_addr"></span>

[String](class_string.md#class_String) **igd_our_addr** = `""` [🔗](class_upnpdevice.md#class_UPNPDevice_property_igd_our_addr)

- void **set_igd_our_addr** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_igd_our_addr** ( )

Address of the local machine in the network connecting it to this **UPNPDevice**.

---

<span id="class_UPNPDevice_property_igd_service_type"></span>

[String](class_string.md#class_String) **igd_service_type** = `""` [🔗](class_upnpdevice.md#class_UPNPDevice_property_igd_service_type)

- void **set_igd_service_type** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_igd_service_type** ( )

IGD service type.

---

<span id="class_UPNPDevice_property_igd_status"></span>

[IGDStatus](class_upnpdevice.md#enum_UPNPDevice_IGDStatus) **igd_status** = `9` [🔗](class_upnpdevice.md#class_UPNPDevice_property_igd_status)

- void **set_igd_status** ( value: [IGDStatus](class_upnpdevice.md#enum_UPNPDevice_IGDStatus) )
- [IGDStatus](class_upnpdevice.md#enum_UPNPDevice_IGDStatus) **get_igd_status** ( )

IGD status.

---

<span id="class_UPNPDevice_property_service_type"></span>

[String](class_string.md#class_String) **service_type** = `""` [🔗](class_upnpdevice.md#class_UPNPDevice_property_service_type)

- void **set_service_type** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_service_type** ( )

Service type.

---

### Method Descriptions

<span id="class_UPNPDevice_method_add_port_mapping"></span>

[int](class_int.md#class_int) **add_port_mapping** ( port: [int](class_int.md#class_int), port_internal: [int](class_int.md#class_int) = 0, desc: [String](class_string.md#class_String) = "", proto: [String](class_string.md#class_String) = "UDP", duration: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_upnpdevice.md#class_UPNPDevice_method_add_port_mapping)

Adds a port mapping to forward the given external port on this **UPNPDevice** for the given protocol to the local machine. See [UPNP.add_port_mapping()](class_upnp.md#class_UPNP_method_add_port_mapping).

---

<span id="class_UPNPDevice_method_delete_port_mapping"></span>

[int](class_int.md#class_int) **delete_port_mapping** ( port: [int](class_int.md#class_int), proto: [String](class_string.md#class_String) = "UDP" ) *const* [🔗](class_upnpdevice.md#class_UPNPDevice_method_delete_port_mapping)

Deletes the port mapping identified by the given port and protocol combination on this device. See [UPNP.delete_port_mapping()](class_upnp.md#class_UPNP_method_delete_port_mapping).

---

<span id="class_UPNPDevice_method_is_valid_gateway"></span>

[bool](class_bool.md#class_bool) **is_valid_gateway** ( ) *const* [🔗](class_upnpdevice.md#class_UPNPDevice_method_is_valid_gateway)

Returns `true` if this is a valid IGD (InternetGatewayDevice) which potentially supports port forwarding.

---

<span id="class_UPNPDevice_method_query_external_address"></span>

[String](class_string.md#class_String) **query_external_address** ( ) *const* [🔗](class_upnpdevice.md#class_UPNPDevice_method_query_external_address)

Returns the external IP address of this **UPNPDevice** or an empty string.
