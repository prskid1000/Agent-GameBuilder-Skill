<span id="class_OpenXRSpatialCapabilityConfigurationBaseHeader"></span>

## OpenXRSpatialCapabilityConfigurationBaseHeader

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [OpenXRSpatialCapabilityConfigurationAnchor](class_openxrspatialcapabilityconfigurationanchor.md#class_OpenXRSpatialCapabilityConfigurationAnchor), [OpenXRSpatialCapabilityConfigurationAprilTag](class_openxrspatialcapabilityconfigurationapriltag.md#class_OpenXRSpatialCapabilityConfigurationAprilTag), [OpenXRSpatialCapabilityConfigurationAruco](class_openxrspatialcapabilityconfigurationaruco.md#class_OpenXRSpatialCapabilityConfigurationAruco), [OpenXRSpatialCapabilityConfigurationMicroQrCode](class_openxrspatialcapabilityconfigurationmicroqrcode.md#class_OpenXRSpatialCapabilityConfigurationMicroQrCode), [OpenXRSpatialCapabilityConfigurationPlaneTracking](class_openxrspatialcapabilityconfigurationplanetracking.md#class_OpenXRSpatialCapabilityConfigurationPlaneTracking), [OpenXRSpatialCapabilityConfigurationQrCode](class_openxrspatialcapabilityconfigurationqrcode.md#class_OpenXRSpatialCapabilityConfigurationQrCode)

Wrapper base class for OpenXR Spatial Capability Configuration headers.

### Description

Wrapper base class for OpenXR Spatial Capability Configuration headers. This class needs to be implemented for each capability configuration structure usable within OpenXR's spatial entities system.

### Methods


| [int](class_int.md#class_int) | [_get_configuration](class_openxrspatialcapabilityconfigurationbaseheader.md#class_OpenXRSpatialCapabilityConfigurationBaseHeader_private_method__get_configuration) ( ) virtual |
| --- | --- |
| [bool](class_bool.md#class_bool) | [_has_valid_configuration](class_openxrspatialcapabilityconfigurationbaseheader.md#class_OpenXRSpatialCapabilityConfigurationBaseHeader_private_method__has_valid_configuration) ( ) | virtual | const |
| [bool](class_bool.md#class_bool) | [has_valid_configuration](class_openxrspatialcapabilityconfigurationbaseheader.md#class_OpenXRSpatialCapabilityConfigurationBaseHeader_method_has_valid_configuration) ( ) const |

---

### Method Descriptions

<span id="class_OpenXRSpatialCapabilityConfigurationBaseHeader_private_method__get_configuration"></span>

[int](class_int.md#class_int) **_get_configuration** ( ) *virtual* [🔗](class_openxrspatialcapabilityconfigurationbaseheader.md#class_OpenXRSpatialCapabilityConfigurationBaseHeader_private_method__get_configuration)

Return a pointer (encoded as an `int64_t`) to a struct holding the spatial capability configuration data. The memory for this struct should remain accessible as long as this object remains instantiated.

---

<span id="class_OpenXRSpatialCapabilityConfigurationBaseHeader_private_method__has_valid_configuration"></span>

[bool](class_bool.md#class_bool) **_has_valid_configuration** ( ) *virtual* *const* [🔗](class_openxrspatialcapabilityconfigurationbaseheader.md#class_OpenXRSpatialCapabilityConfigurationBaseHeader_private_method__has_valid_configuration)

Return `true` if this object contains a valid configuration that can be retrieved when calling [_get_configuration()](class_openxrspatialcapabilityconfigurationbaseheader.md#class_OpenXRSpatialCapabilityConfigurationBaseHeader_private_method__get_configuration).

---

<span id="class_OpenXRSpatialCapabilityConfigurationBaseHeader_method_has_valid_configuration"></span>

[bool](class_bool.md#class_bool) **has_valid_configuration** ( ) *const* [🔗](class_openxrspatialcapabilityconfigurationbaseheader.md#class_OpenXRSpatialCapabilityConfigurationBaseHeader_method_has_valid_configuration)

Returns `true` if this object contains a valid configuration that can be used when calling [OpenXRSpatialEntityExtension.create_spatial_context()](class_openxrspatialentityextension.md#class_OpenXRSpatialEntityExtension_method_create_spatial_context).
