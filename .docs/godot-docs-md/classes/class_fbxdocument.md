<span id="class_FBXDocument"></span>

## FBXDocument

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [GLTFDocument](class_gltfdocument.md#class_GLTFDocument) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Handles FBX documents.

### Description

The FBXDocument handles FBX documents. It provides methods to append data from buffers or files, generate scenes, and register/unregister document extensions.

When exporting FBX from Blender, use the "FBX Units Scale" option. The "FBX Units Scale" option sets the correct scale factor and avoids manual adjustments when re-importing into Blender, such as through glTF export.
