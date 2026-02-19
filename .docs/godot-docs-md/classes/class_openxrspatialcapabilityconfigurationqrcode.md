<span id="class_OpenXRSpatialCapabilityConfigurationQrCode"></span>

## OpenXRSpatialCapabilityConfigurationQrCode

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialCapabilityConfigurationBaseHeader](class_openxrspatialcapabilityconfigurationbaseheader.md#class_OpenXRSpatialCapabilityConfigurationBaseHeader) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Configuration header for micro QR code markers.

### Description

Configuration header for micro QR code markers. Pass this to [OpenXRSpatialEntityExtension.create_spatial_context()](class_openxrspatialentityextension.md#class_OpenXRSpatialEntityExtension_method_create_spatial_context) to create a spatial context that can detect micro QR code markers.

### Methods


| [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) | [get_enabled_components](class_openxrspatialcapabilityconfigurationqrcode.md#class_OpenXRSpatialCapabilityConfigurationQrCode_method_get_enabled_components) ( ) const |
| --- | --- |

---

### Method Descriptions

<span id="class_OpenXRSpatialCapabilityConfigurationQrCode_method_get_enabled_components"></span>

[PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) **get_enabled_components** ( ) *const* [🔗](class_openxrspatialcapabilityconfigurationqrcode.md#class_OpenXRSpatialCapabilityConfigurationQrCode_method_get_enabled_components)

Returns the components enabled by this configuration.

 **Note:** Only valid after this configuration was used to create a spatial context.
