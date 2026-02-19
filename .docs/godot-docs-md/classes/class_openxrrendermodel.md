<span id="class_OpenXRRenderModel"></span>

## OpenXRRenderModel

**Inherits:** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

This node will display an OpenXR render model.

### Description

This node will display an OpenXR render model by accessing the associated GLTF and processes all animation data (if supported by the XR runtime).

Render models were introduced to allow showing the correct model for the controller (or other device) the user has in hand, since the OpenXR action map does not provide information about the hardware used by the user. Note that while the controller (or device) can be somewhat inferred by the bound action map profile, this is a dangerous approach as the user may be using hardware not known at time of development and OpenXR will simply simulate an available interaction profile.

### Properties


| [RID](class_rid.md#class_RID) | [render_model](class_openxrrendermodel.md#class_OpenXRRenderModel_property_render_model) | `RID()` |
| --- | --- | --- |

### Methods


| [String](class_string.md#class_String) | [get_top_level_path](class_openxrrendermodel.md#class_OpenXRRenderModel_method_get_top_level_path) ( ) const |
| --- | --- |

---

### Signals

<span id="class_OpenXRRenderModel_signal_render_model_top_level_path_changed"></span>

**render_model_top_level_path_changed** ( ) [🔗](class_openxrrendermodel.md#class_OpenXRRenderModel_signal_render_model_top_level_path_changed)

Emitted when the top level path of this render model has changed.

---

### Property Descriptions

<span id="class_OpenXRRenderModel_property_render_model"></span>

[RID](class_rid.md#class_RID) **render_model** = `RID()` [🔗](class_openxrrendermodel.md#class_OpenXRRenderModel_property_render_model)

- void **set_render_model** ( value: [RID](class_rid.md#class_RID) )
- [RID](class_rid.md#class_RID) **get_render_model** ( )

The render model RID for the render model to load, as returned by [OpenXRRenderModelExtension.render_model_create()](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_render_model_create) or [OpenXRRenderModelExtension.render_model_get_all()](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_render_model_get_all).

---

### Method Descriptions

<span id="class_OpenXRRenderModel_method_get_top_level_path"></span>

[String](class_string.md#class_String) **get_top_level_path** ( ) *const* [🔗](class_openxrrendermodel.md#class_OpenXRRenderModel_method_get_top_level_path)

Returns the top level path related to this render model.
