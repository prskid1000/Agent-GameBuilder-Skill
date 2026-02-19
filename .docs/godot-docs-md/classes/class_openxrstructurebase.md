<span id="class_OpenXRStructureBase"></span>

## OpenXRStructureBase

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [OpenXRSpatialContextPersistenceConfig](class_openxrspatialcontextpersistenceconfig.md#class_OpenXRSpatialContextPersistenceConfig)

Object for storing OpenXR structure data.

### Description

Object for storing OpenXR structure data that is passed when calling into OpenXR APIs.

### Properties


| [OpenXRStructureBase](class_openxrstructurebase.md#class_OpenXRStructureBase) | [next](class_openxrstructurebase.md#class_OpenXRStructureBase_property_next) |
| --- | --- |

### Methods


| [int](class_int.md#class_int) | [_get_header](class_openxrstructurebase.md#class_OpenXRStructureBase_private_method__get_header) ( next: [int](class_int.md#class_int) ) virtual |
| --- | --- |
| [int](class_int.md#class_int) | [get_structure_type](class_openxrstructurebase.md#class_OpenXRStructureBase_method_get_structure_type) ( ) |

---

### Property Descriptions

<span id="class_OpenXRStructureBase_property_next"></span>

[OpenXRStructureBase](class_openxrstructurebase.md#class_OpenXRStructureBase) **next** [🔗](class_openxrstructurebase.md#class_OpenXRStructureBase_property_next)

- void **set_next** ( value: [OpenXRStructureBase](class_openxrstructurebase.md#class_OpenXRStructureBase) )
- [OpenXRStructureBase](class_openxrstructurebase.md#class_OpenXRStructureBase) **get_next** ( )

Setting another structure object here chains these structures together to extend the API functionality. Consult the OpenXR documentation for which structures can be used with a given API call.

---

### Method Descriptions

<span id="class_OpenXRStructureBase_private_method__get_header"></span>

[int](class_int.md#class_int) **_get_header** ( next: [int](class_int.md#class_int) ) *virtual* [🔗](class_openxrstructurebase.md#class_OpenXRStructureBase_private_method__get_header)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_OpenXRStructureBase_method_get_structure_type"></span>

[int](class_int.md#class_int) **get_structure_type** ( ) [🔗](class_openxrstructurebase.md#class_OpenXRStructureBase_method_get_structure_type)

Returns the structure type (OpenXR `XrStructureType`) used for this structure.
