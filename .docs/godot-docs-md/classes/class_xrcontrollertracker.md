<span id="class_XRControllerTracker"></span>

## XRControllerTracker

**Inherits:** [XRPositionalTracker](class_xrpositionaltracker.md#class_XRPositionalTracker) **<** [XRTracker](class_xrtracker.md#class_XRTracker) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A tracked controller.

### Description

An instance of this object represents a controller that is tracked.

As controllers are turned on and the [XRInterface](class_xrinterface.md#class_XRInterface) detects them, instances of this object are automatically added to this list of active tracking objects accessible through the [XRServer](class_xrserver.md#class_XRServer).

The [XRController3D](class_xrcontroller3d.md#class_XRController3D) consumes objects of this type and should be used in your project.

### Tutorials

- [XR documentation index](../tutorials/xr/index.md)

### Properties


| [TrackerType](class_xrserver.md#enum_XRServer_TrackerType) | type | `2` (overrides [XRTracker](class_xrtracker.md#class_XRTracker_property_type)) |
| --- | --- | --- |
