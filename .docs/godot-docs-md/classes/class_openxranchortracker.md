<span id="class_OpenXRAnchorTracker"></span>

## OpenXRAnchorTracker

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialEntityTracker](class_openxrspatialentitytracker.md#class_OpenXRSpatialEntityTracker) **<** [XRPositionalTracker](class_xrpositionaltracker.md#class_XRPositionalTracker) **<** [XRTracker](class_xrtracker.md#class_XRTracker) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Positional tracker for our spatial entity anchor extension.

### Description

Positional tracker for our OpenXR spatial entity anchor extension, it tracks a user defined location in real space and maps it to our virtual space.

### Properties


| [String](class_string.md#class_String) | [uuid](class_openxranchortracker.md#class_OpenXRAnchorTracker_property_uuid) | `""` |
| --- | --- | --- |

### Methods


| [bool](class_bool.md#class_bool) | [has_uuid](class_openxranchortracker.md#class_OpenXRAnchorTracker_method_has_uuid) ( ) const |
| --- | --- |

---

### Signals

<span id="class_OpenXRAnchorTracker_signal_uuid_changed"></span>

**uuid_changed** ( ) [🔗](class_openxranchortracker.md#class_OpenXRAnchorTracker_signal_uuid_changed)

Emitted when the UUID for this anchor was changed.

---

### Property Descriptions

<span id="class_OpenXRAnchorTracker_property_uuid"></span>

[String](class_string.md#class_String) **uuid** = `""` [🔗](class_openxranchortracker.md#class_OpenXRAnchorTracker_property_uuid)

- void **set_uuid** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_uuid** ( )

The UUID provided for persistent anchors.

---

### Method Descriptions

<span id="class_OpenXRAnchorTracker_method_has_uuid"></span>

[bool](class_bool.md#class_bool) **has_uuid** ( ) *const* [🔗](class_openxranchortracker.md#class_OpenXRAnchorTracker_method_has_uuid)

Returns `true` if a non-zero UUID is set.
