<span id="class_LightmapProbe"></span>

## LightmapProbe

**Inherits:** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Represents a single manually placed probe for dynamic object lighting with [LightmapGI](class_lightmapgi.md#class_LightmapGI).

### Description

**LightmapProbe** represents the position of a single manually placed probe for dynamic object lighting with [LightmapGI](class_lightmapgi.md#class_LightmapGI). Lightmap probes affect the lighting of [GeometryInstance3D](class_geometryinstance3d.md#class_GeometryInstance3D)-derived nodes that have their [GeometryInstance3D.gi_mode](class_geometryinstance3d.md#class_GeometryInstance3D_property_gi_mode) set to [GeometryInstance3D.GI_MODE_DYNAMIC](class_geometryinstance3d.md#class_GeometryInstance3D_constant_GI_MODE_DYNAMIC).

Typically, [LightmapGI](class_lightmapgi.md#class_LightmapGI) probes are placed automatically by setting [LightmapGI.generate_probes_subdiv](class_lightmapgi.md#class_LightmapGI_property_generate_probes_subdiv) to a value other than [LightmapGI.GENERATE_PROBES_DISABLED](class_lightmapgi.md#class_LightmapGI_constant_GENERATE_PROBES_DISABLED). By creating **LightmapProbe** nodes before baking lightmaps, you can add more probes in specific areas for greater detail, or disable automatic generation and rely only on manually placed probes instead.

 **Note:** **LightmapProbe** nodes that are placed after baking lightmaps are ignored by dynamic objects. You must bake lightmaps again after creating or modifying **LightmapProbe** s for the probes to be effective.
