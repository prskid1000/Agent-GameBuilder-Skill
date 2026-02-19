<span id="class_OpenXRSpatialCapabilityConfigurationAprilTag"></span>

## OpenXRSpatialCapabilityConfigurationAprilTag

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialCapabilityConfigurationBaseHeader](class_openxrspatialcapabilityconfigurationbaseheader.md#class_OpenXRSpatialCapabilityConfigurationBaseHeader) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Configuration header for April tag markers.

### Description

Configuration header for April tag markers. Pass this to [OpenXRSpatialEntityExtension.create_spatial_context()](class_openxrspatialentityextension.md#class_OpenXRSpatialEntityExtension_method_create_spatial_context) to create a spatial context that can detect April tags.

### Properties


| [AprilTagDict](class_openxrspatialcapabilityconfigurationapriltag.md#enum_OpenXRSpatialCapabilityConfigurationAprilTag_AprilTagDict) | [april_dict](class_openxrspatialcapabilityconfigurationapriltag.md#class_OpenXRSpatialCapabilityConfigurationAprilTag_property_april_dict) | `4` |
| --- | --- | --- |

### Methods


| [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) | [get_enabled_components](class_openxrspatialcapabilityconfigurationapriltag.md#class_OpenXRSpatialCapabilityConfigurationAprilTag_method_get_enabled_components) ( ) const |
| --- | --- |

---

### Enumerations

<span id="enum_OpenXRSpatialCapabilityConfigurationAprilTag_AprilTagDict"></span>

enum **AprilTagDict**: [🔗](class_openxrspatialcapabilityconfigurationapriltag.md#enum_OpenXRSpatialCapabilityConfigurationAprilTag_AprilTagDict)

<span id="class_OpenXRSpatialCapabilityConfigurationAprilTag_constant_APRIL_TAG_DICT_16H5"></span>

[AprilTagDict](class_openxrspatialcapabilityconfigurationapriltag.md#enum_OpenXRSpatialCapabilityConfigurationAprilTag_AprilTagDict) **APRIL_TAG_DICT_16H5** = `1`

4 by 4 bits, minimum Hamming distance between any two codes = 5, 30 codes.

<span id="class_OpenXRSpatialCapabilityConfigurationAprilTag_constant_APRIL_TAG_DICT_25H9"></span>

[AprilTagDict](class_openxrspatialcapabilityconfigurationapriltag.md#enum_OpenXRSpatialCapabilityConfigurationAprilTag_AprilTagDict) **APRIL_TAG_DICT_25H9** = `2`

5 by 5 bits, minimum Hamming distance between any two codes = 9, 35 codes.

<span id="class_OpenXRSpatialCapabilityConfigurationAprilTag_constant_APRIL_TAG_DICT_36H10"></span>

[AprilTagDict](class_openxrspatialcapabilityconfigurationapriltag.md#enum_OpenXRSpatialCapabilityConfigurationAprilTag_AprilTagDict) **APRIL_TAG_DICT_36H10** = `3`

6 by 6 bits, minimum Hamming distance between any two codes = 10, 2320 codes.

<span id="class_OpenXRSpatialCapabilityConfigurationAprilTag_constant_APRIL_TAG_DICT_36H11"></span>

[AprilTagDict](class_openxrspatialcapabilityconfigurationapriltag.md#enum_OpenXRSpatialCapabilityConfigurationAprilTag_AprilTagDict) **APRIL_TAG_DICT_36H11** = `4`

6 by 6 bits, minimum Hamming distance between any two codes = 11, 587 codes.

---

### Property Descriptions

<span id="class_OpenXRSpatialCapabilityConfigurationAprilTag_property_april_dict"></span>

[AprilTagDict](class_openxrspatialcapabilityconfigurationapriltag.md#enum_OpenXRSpatialCapabilityConfigurationAprilTag_AprilTagDict) **april_dict** = `4` [🔗](class_openxrspatialcapabilityconfigurationapriltag.md#class_OpenXRSpatialCapabilityConfigurationAprilTag_property_april_dict)

- void **set_april_dict** ( value: [AprilTagDict](class_openxrspatialcapabilityconfigurationapriltag.md#enum_OpenXRSpatialCapabilityConfigurationAprilTag_AprilTagDict) )
- [AprilTagDict](class_openxrspatialcapabilityconfigurationapriltag.md#enum_OpenXRSpatialCapabilityConfigurationAprilTag_AprilTagDict) **get_april_dict** ( )

Dictionary to use to decode April tags.

 **Note:** Must be set before using this configuration to create a spatial context.

---

### Method Descriptions

<span id="class_OpenXRSpatialCapabilityConfigurationAprilTag_method_get_enabled_components"></span>

[PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) **get_enabled_components** ( ) *const* [🔗](class_openxrspatialcapabilityconfigurationapriltag.md#class_OpenXRSpatialCapabilityConfigurationAprilTag_method_get_enabled_components)

Returns the components enabled by this configuration.

 **Note:** Only valid after this configuration was used to create a spatial context.
