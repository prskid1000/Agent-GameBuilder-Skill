<span id="class_VisualShaderNodeReroute"></span>

## VisualShaderNodeReroute

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A node that allows rerouting a connection within the visual shader graph.

### Description

Automatically adapts its port type to the type of the incoming connection and ensures valid connections.

### Methods


| [PortType](class_visualshadernode.md#enum_VisualShaderNode_PortType) | [get_port_type](class_visualshadernodereroute.md#class_VisualShaderNodeReroute_method_get_port_type) ( ) const |
| --- | --- |

---

### Method Descriptions

<span id="class_VisualShaderNodeReroute_method_get_port_type"></span>

[PortType](class_visualshadernode.md#enum_VisualShaderNode_PortType) **get_port_type** ( ) *const* [🔗](class_visualshadernodereroute.md#class_VisualShaderNodeReroute_method_get_port_type)

Returns the port type of the reroute node.
