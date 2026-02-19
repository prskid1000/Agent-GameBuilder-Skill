.. meta::
	:keywords: background, sky

<span id="class_WorldEnvironment"></span>

## WorldEnvironment

**Inherits:** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Default environment properties for the entire scene (post-processing effects, lighting and background settings).

### Description

The **WorldEnvironment** node is used to configure the default [Environment](class_environment.md#class_Environment) for the scene.

The parameters defined in the **WorldEnvironment** can be overridden by an [Environment](class_environment.md#class_Environment) node set on the current [Camera3D](class_camera3d.md#class_Camera3D). Additionally, only one **WorldEnvironment** may be instantiated in a given scene at a time.

The **WorldEnvironment** allows the user to specify default lighting parameters (e.g. ambient lighting), various post-processing effects (e.g. SSAO, DOF, Tonemapping), and how to draw the background (e.g. solid color, skybox). Usually, these are added in order to improve the realism/color balance of the scene.

### Tutorials

- [Environment and post-processing](../tutorials/3d/environment_and_post_processing.md)

- 3D Material Testers Demo

- Third Person Shooter (TPS) Demo

### Properties


| [CameraAttributes](class_cameraattributes.md#class_CameraAttributes) | [camera_attributes](class_worldenvironment.md#class_WorldEnvironment_property_camera_attributes) |
| --- | --- |
| [Compositor](class_compositor.md#class_Compositor) | [compositor](class_worldenvironment.md#class_WorldEnvironment_property_compositor) |
| [Environment](class_environment.md#class_Environment) | [environment](class_worldenvironment.md#class_WorldEnvironment_property_environment) |

---

### Property Descriptions

<span id="class_WorldEnvironment_property_camera_attributes"></span>

[CameraAttributes](class_cameraattributes.md#class_CameraAttributes) **camera_attributes** [🔗](class_worldenvironment.md#class_WorldEnvironment_property_camera_attributes)

- void **set_camera_attributes** ( value: [CameraAttributes](class_cameraattributes.md#class_CameraAttributes) )
- [CameraAttributes](class_cameraattributes.md#class_CameraAttributes) **get_camera_attributes** ( )

The default [CameraAttributes](class_cameraattributes.md#class_CameraAttributes) resource to use if none set on the [Camera3D](class_camera3d.md#class_Camera3D).

---

<span id="class_WorldEnvironment_property_compositor"></span>

[Compositor](class_compositor.md#class_Compositor) **compositor** [🔗](class_worldenvironment.md#class_WorldEnvironment_property_compositor)

- void **set_compositor** ( value: [Compositor](class_compositor.md#class_Compositor) )
- [Compositor](class_compositor.md#class_Compositor) **get_compositor** ( )

The default [Compositor](class_compositor.md#class_Compositor) resource to use if none set on the [Camera3D](class_camera3d.md#class_Camera3D).

---

<span id="class_WorldEnvironment_property_environment"></span>

[Environment](class_environment.md#class_Environment) **environment** [🔗](class_worldenvironment.md#class_WorldEnvironment_property_environment)

- void **set_environment** ( value: [Environment](class_environment.md#class_Environment) )
- [Environment](class_environment.md#class_Environment) **get_environment** ( )

The [Environment](class_environment.md#class_Environment) resource used by this **WorldEnvironment**, defining the default properties.
