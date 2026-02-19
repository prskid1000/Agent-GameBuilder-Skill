<span id="class_AnimationNode"></span>

## AnimationNode

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [AnimationNodeExtension](class_animationnodeextension.md#class_AnimationNodeExtension), [AnimationNodeOutput](class_animationnodeoutput.md#class_AnimationNodeOutput), [AnimationNodeSync](class_animationnodesync.md#class_AnimationNodeSync), [AnimationNodeTimeScale](class_animationnodetimescale.md#class_AnimationNodeTimeScale), [AnimationNodeTimeSeek](class_animationnodetimeseek.md#class_AnimationNodeTimeSeek), [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode)

Base class for [AnimationTree](class_animationtree.md#class_AnimationTree) nodes. Not related to scene nodes.

### Description

Base resource for [AnimationTree](class_animationtree.md#class_AnimationTree) nodes. In general, it's not used directly, but you can create custom ones with custom blending formulas.

Inherit this when creating animation nodes mainly for use in [AnimationNodeBlendTree](class_animationnodeblendtree.md#class_AnimationNodeBlendTree), otherwise [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) should be used instead.

You can access the time information as read-only parameter which is processed and stored in the previous frame for all nodes except [AnimationNodeOutput](class_animationnodeoutput.md#class_AnimationNodeOutput).

 **Note:** If multiple inputs exist in the **AnimationNode**, which time information takes precedence depends on the type of **AnimationNode**.

::

    var current_length = $AnimationTree["parameters/AnimationNodeName/current_length"]
    var current_position = $AnimationTree["parameters/AnimationNodeName/current_position"]
    var current_delta = $AnimationTree["parameters/AnimationNodeName/current_delta"]

### Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)

### Properties


| [bool](class_bool.md#class_bool) | [filter_enabled](class_animationnode.md#class_AnimationNode_property_filter_enabled) |
| --- | --- |

### Methods


| [String](class_string.md#class_String) | [_get_caption](class_animationnode.md#class_AnimationNode_private_method__get_caption) ( ) | virtual | const |
| --- | --- | --- | --- |
| [AnimationNode](class_animationnode.md#class_AnimationNode) | [_get_child_by_name](class_animationnode.md#class_AnimationNode_private_method__get_child_by_name) ( name: [StringName](class_stringname.md#class_StringName) ) | virtual | const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [_get_child_nodes](class_animationnode.md#class_AnimationNode_private_method__get_child_nodes) ( ) | virtual | const |
| [Variant](class_variant.md#class_Variant) | [_get_parameter_default_value](class_animationnode.md#class_AnimationNode_private_method__get_parameter_default_value) ( parameter: [StringName](class_stringname.md#class_StringName) ) | virtual | const |
| [Array](class_array.md#class_Array) | [_get_parameter_list](class_animationnode.md#class_AnimationNode_private_method__get_parameter_list) ( ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_has_filter](class_animationnode.md#class_AnimationNode_private_method__has_filter) ( ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_is_parameter_read_only](class_animationnode.md#class_AnimationNode_private_method__is_parameter_read_only) ( parameter: [StringName](class_stringname.md#class_StringName) ) | virtual | const |
| [float](class_float.md#class_float) | [_process](class_animationnode.md#class_AnimationNode_private_method__process) ( time: [float](class_float.md#class_float), seek: [bool](class_bool.md#class_bool), is_external_seeking: [bool](class_bool.md#class_bool), test_only: [bool](class_bool.md#class_bool) ) virtual |
| [bool](class_bool.md#class_bool) | [add_input](class_animationnode.md#class_AnimationNode_method_add_input) ( name: [String](class_string.md#class_String) ) |
| void | [blend_animation](class_animationnode.md#class_AnimationNode_method_blend_animation) ( animation: [StringName](class_stringname.md#class_StringName), time: [float](class_float.md#class_float), delta: [float](class_float.md#class_float), seeked: [bool](class_bool.md#class_bool), is_external_seeking: [bool](class_bool.md#class_bool), blend: [float](class_float.md#class_float), looped_flag: [LoopedFlag](class_animation.md#enum_Animation_LoopedFlag) = 0 ) |
| [float](class_float.md#class_float) | [blend_input](class_animationnode.md#class_AnimationNode_method_blend_input) ( input_index: [int](class_int.md#class_int), time: [float](class_float.md#class_float), seek: [bool](class_bool.md#class_bool), is_external_seeking: [bool](class_bool.md#class_bool), blend: [float](class_float.md#class_float), filter: [FilterAction](class_animationnode.md#enum_AnimationNode_FilterAction) = 0, sync: [bool](class_bool.md#class_bool) = true, test_only: [bool](class_bool.md#class_bool) = false ) |
| [float](class_float.md#class_float) | [blend_node](class_animationnode.md#class_AnimationNode_method_blend_node) ( name: [StringName](class_stringname.md#class_StringName), node: [AnimationNode](class_animationnode.md#class_AnimationNode), time: [float](class_float.md#class_float), seek: [bool](class_bool.md#class_bool), is_external_seeking: [bool](class_bool.md#class_bool), blend: [float](class_float.md#class_float), filter: [FilterAction](class_animationnode.md#enum_AnimationNode_FilterAction) = 0, sync: [bool](class_bool.md#class_bool) = true, test_only: [bool](class_bool.md#class_bool) = false ) |
| [int](class_int.md#class_int) | [find_input](class_animationnode.md#class_AnimationNode_method_find_input) ( name: [String](class_string.md#class_String) ) const |
| [int](class_int.md#class_int) | [get_input_count](class_animationnode.md#class_AnimationNode_method_get_input_count) ( ) const |
| [String](class_string.md#class_String) | [get_input_name](class_animationnode.md#class_AnimationNode_method_get_input_name) ( input: [int](class_int.md#class_int) ) const |
| [Variant](class_variant.md#class_Variant) | [get_parameter](class_animationnode.md#class_AnimationNode_method_get_parameter) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| [int](class_int.md#class_int) | [get_processing_animation_tree_instance_id](class_animationnode.md#class_AnimationNode_method_get_processing_animation_tree_instance_id) ( ) const |
| [bool](class_bool.md#class_bool) | [is_path_filtered](class_animationnode.md#class_AnimationNode_method_is_path_filtered) ( path: [NodePath](class_nodepath.md#class_NodePath) ) const |
| [bool](class_bool.md#class_bool) | [is_process_testing](class_animationnode.md#class_AnimationNode_method_is_process_testing) ( ) const |
| void | [remove_input](class_animationnode.md#class_AnimationNode_method_remove_input) ( index: [int](class_int.md#class_int) ) |
| void | [set_filter_path](class_animationnode.md#class_AnimationNode_method_set_filter_path) ( path: [NodePath](class_nodepath.md#class_NodePath), enable: [bool](class_bool.md#class_bool) ) |
| [bool](class_bool.md#class_bool) | [set_input_name](class_animationnode.md#class_AnimationNode_method_set_input_name) ( input: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) |
| void | [set_parameter](class_animationnode.md#class_AnimationNode_method_set_parameter) ( name: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) |

---

### Signals

<span id="class_AnimationNode_signal_animation_node_removed"></span>

**animation_node_removed** ( object_id: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) [🔗](class_animationnode.md#class_AnimationNode_signal_animation_node_removed)

Emitted by nodes that inherit from this class and that have an internal tree when one of their animation nodes removes. The animation nodes that emit this signal are [AnimationNodeBlendSpace1D](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D), [AnimationNodeBlendSpace2D](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D), [AnimationNodeStateMachine](class_animationnodestatemachine.md#class_AnimationNodeStateMachine), and [AnimationNodeBlendTree](class_animationnodeblendtree.md#class_AnimationNodeBlendTree).

---

<span id="class_AnimationNode_signal_animation_node_renamed"></span>

**animation_node_renamed** ( object_id: [int](class_int.md#class_int), old_name: [String](class_string.md#class_String), new_name: [String](class_string.md#class_String) ) [🔗](class_animationnode.md#class_AnimationNode_signal_animation_node_renamed)

Emitted by nodes that inherit from this class and that have an internal tree when one of their animation node names changes. The animation nodes that emit this signal are [AnimationNodeBlendSpace1D](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D), [AnimationNodeBlendSpace2D](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D), [AnimationNodeStateMachine](class_animationnodestatemachine.md#class_AnimationNodeStateMachine), and [AnimationNodeBlendTree](class_animationnodeblendtree.md#class_AnimationNodeBlendTree).

---

<span id="class_AnimationNode_signal_tree_changed"></span>

**tree_changed** ( ) [🔗](class_animationnode.md#class_AnimationNode_signal_tree_changed)

Emitted by nodes that inherit from this class and that have an internal tree when one of their animation nodes changes. The animation nodes that emit this signal are [AnimationNodeBlendSpace1D](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D), [AnimationNodeBlendSpace2D](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D), [AnimationNodeStateMachine](class_animationnodestatemachine.md#class_AnimationNodeStateMachine), [AnimationNodeBlendTree](class_animationnodeblendtree.md#class_AnimationNodeBlendTree) and [AnimationNodeTransition](class_animationnodetransition.md#class_AnimationNodeTransition).

---

### Enumerations

<span id="enum_AnimationNode_FilterAction"></span>

enum **FilterAction**: [🔗](class_animationnode.md#enum_AnimationNode_FilterAction)

<span id="class_AnimationNode_constant_FILTER_IGNORE"></span>

[FilterAction](class_animationnode.md#enum_AnimationNode_FilterAction) **FILTER_IGNORE** = `0`

Do not use filtering.

<span id="class_AnimationNode_constant_FILTER_PASS"></span>

[FilterAction](class_animationnode.md#enum_AnimationNode_FilterAction) **FILTER_PASS** = `1`

Paths matching the filter will be allowed to pass.

<span id="class_AnimationNode_constant_FILTER_STOP"></span>

[FilterAction](class_animationnode.md#enum_AnimationNode_FilterAction) **FILTER_STOP** = `2`

Paths matching the filter will be discarded.

<span id="class_AnimationNode_constant_FILTER_BLEND"></span>

[FilterAction](class_animationnode.md#enum_AnimationNode_FilterAction) **FILTER_BLEND** = `3`

Paths matching the filter will be blended (by the blend value).

---

### Property Descriptions

<span id="class_AnimationNode_property_filter_enabled"></span>

[bool](class_bool.md#class_bool) **filter_enabled** [🔗](class_animationnode.md#class_AnimationNode_property_filter_enabled)

- void **set_filter_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_filter_enabled** ( )

If `true`, filtering is enabled.

---

### Method Descriptions

<span id="class_AnimationNode_private_method__get_caption"></span>

[String](class_string.md#class_String) **_get_caption** ( ) *virtual* *const* [🔗](class_animationnode.md#class_AnimationNode_private_method__get_caption)

When inheriting from [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode), implement this virtual method to override the text caption for this animation node.

---

<span id="class_AnimationNode_private_method__get_child_by_name"></span>

[AnimationNode](class_animationnode.md#class_AnimationNode) **_get_child_by_name** ( name: [StringName](class_stringname.md#class_StringName) ) *virtual* *const* [🔗](class_animationnode.md#class_AnimationNode_private_method__get_child_by_name)

When inheriting from [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode), implement this virtual method to return a child animation node by its `name`.

---

<span id="class_AnimationNode_private_method__get_child_nodes"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **_get_child_nodes** ( ) *virtual* *const* [🔗](class_animationnode.md#class_AnimationNode_private_method__get_child_nodes)

When inheriting from [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode), implement this virtual method to return all child animation nodes in order as a `name: node` dictionary.

---

<span id="class_AnimationNode_private_method__get_parameter_default_value"></span>

[Variant](class_variant.md#class_Variant) **_get_parameter_default_value** ( parameter: [StringName](class_stringname.md#class_StringName) ) *virtual* *const* [🔗](class_animationnode.md#class_AnimationNode_private_method__get_parameter_default_value)

When inheriting from [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode), implement this virtual method to return the default value of a `parameter`. Parameters are custom local memory used for your animation nodes, given a resource can be reused in multiple trees.

---

<span id="class_AnimationNode_private_method__get_parameter_list"></span>

[Array](class_array.md#class_Array) **_get_parameter_list** ( ) *virtual* *const* [🔗](class_animationnode.md#class_AnimationNode_private_method__get_parameter_list)

When inheriting from [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode), implement this virtual method to return a list of the properties on this animation node. Parameters are custom local memory used for your animation nodes, given a resource can be reused in multiple trees. Format is similar to [Object.get_property_list()](class_object.md#class_Object_method_get_property_list).

---

<span id="class_AnimationNode_private_method__has_filter"></span>

[bool](class_bool.md#class_bool) **_has_filter** ( ) *virtual* *const* [🔗](class_animationnode.md#class_AnimationNode_private_method__has_filter)

When inheriting from [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode), implement this virtual method to return whether the blend tree editor should display filter editing on this animation node.

---

<span id="class_AnimationNode_private_method__is_parameter_read_only"></span>

[bool](class_bool.md#class_bool) **_is_parameter_read_only** ( parameter: [StringName](class_stringname.md#class_StringName) ) *virtual* *const* [🔗](class_animationnode.md#class_AnimationNode_private_method__is_parameter_read_only)

When inheriting from [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode), implement this virtual method to return whether the `parameter` is read-only. Parameters are custom local memory used for your animation nodes, given a resource can be reused in multiple trees.

---

<span id="class_AnimationNode_private_method__process"></span>

[float](class_float.md#class_float) **_process** ( time: [float](class_float.md#class_float), seek: [bool](class_bool.md#class_bool), is_external_seeking: [bool](class_bool.md#class_bool), test_only: [bool](class_bool.md#class_bool) ) *virtual* [🔗](class_animationnode.md#class_AnimationNode_private_method__process)

**Deprecated:** Currently this is mostly useless as there is a lack of many APIs to extend AnimationNode by GDScript. It is planned that a more flexible API using structures will be provided in the future.

When inheriting from [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode), implement this virtual method to run some code when this animation node is processed. The `time` parameter is a relative delta, unless `seek` is `true`, in which case it is absolute.

Here, call the [blend_input()](class_animationnode.md#class_AnimationNode_method_blend_input), [blend_node()](class_animationnode.md#class_AnimationNode_method_blend_node) or [blend_animation()](class_animationnode.md#class_AnimationNode_method_blend_animation) functions. You can also use [get_parameter()](class_animationnode.md#class_AnimationNode_method_get_parameter) and [set_parameter()](class_animationnode.md#class_AnimationNode_method_set_parameter) to modify local memory.

This function should return the delta.

---

<span id="class_AnimationNode_method_add_input"></span>

[bool](class_bool.md#class_bool) **add_input** ( name: [String](class_string.md#class_String) ) [🔗](class_animationnode.md#class_AnimationNode_method_add_input)

Adds an input to the animation node. This is only useful for animation nodes created for use in an [AnimationNodeBlendTree](class_animationnodeblendtree.md#class_AnimationNodeBlendTree). If the addition fails, returns `false`.

---

<span id="class_AnimationNode_method_blend_animation"></span>

void **blend_animation** ( animation: [StringName](class_stringname.md#class_StringName), time: [float](class_float.md#class_float), delta: [float](class_float.md#class_float), seeked: [bool](class_bool.md#class_bool), is_external_seeking: [bool](class_bool.md#class_bool), blend: [float](class_float.md#class_float), looped_flag: [LoopedFlag](class_animation.md#enum_Animation_LoopedFlag) = 0 ) [🔗](class_animationnode.md#class_AnimationNode_method_blend_animation)

Blends an animation by `blend` amount (name must be valid in the linked [AnimationPlayer](class_animationplayer.md#class_AnimationPlayer)). A `time` and `delta` may be passed, as well as whether `seeked` happened.

A `looped_flag` is used by internal processing immediately after the loop.

---

<span id="class_AnimationNode_method_blend_input"></span>

[float](class_float.md#class_float) **blend_input** ( input_index: [int](class_int.md#class_int), time: [float](class_float.md#class_float), seek: [bool](class_bool.md#class_bool), is_external_seeking: [bool](class_bool.md#class_bool), blend: [float](class_float.md#class_float), filter: [FilterAction](class_animationnode.md#enum_AnimationNode_FilterAction) = 0, sync: [bool](class_bool.md#class_bool) = true, test_only: [bool](class_bool.md#class_bool) = false ) [🔗](class_animationnode.md#class_AnimationNode_method_blend_input)

Blends an input. This is only useful for animation nodes created for an [AnimationNodeBlendTree](class_animationnodeblendtree.md#class_AnimationNodeBlendTree). The `time` parameter is a relative delta, unless `seek` is `true`, in which case it is absolute. A filter mode may be optionally passed.

---

<span id="class_AnimationNode_method_blend_node"></span>

[float](class_float.md#class_float) **blend_node** ( name: [StringName](class_stringname.md#class_StringName), node: [AnimationNode](class_animationnode.md#class_AnimationNode), time: [float](class_float.md#class_float), seek: [bool](class_bool.md#class_bool), is_external_seeking: [bool](class_bool.md#class_bool), blend: [float](class_float.md#class_float), filter: [FilterAction](class_animationnode.md#enum_AnimationNode_FilterAction) = 0, sync: [bool](class_bool.md#class_bool) = true, test_only: [bool](class_bool.md#class_bool) = false ) [🔗](class_animationnode.md#class_AnimationNode_method_blend_node)

Blend another animation node (in case this animation node contains child animation nodes). This function is only useful if you inherit from [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) instead, otherwise editors will not display your animation node for addition.

---

<span id="class_AnimationNode_method_find_input"></span>

[int](class_int.md#class_int) **find_input** ( name: [String](class_string.md#class_String) ) *const* [🔗](class_animationnode.md#class_AnimationNode_method_find_input)

Returns the input index which corresponds to `name`. If not found, returns `-1`.

---

<span id="class_AnimationNode_method_get_input_count"></span>

[int](class_int.md#class_int) **get_input_count** ( ) *const* [🔗](class_animationnode.md#class_AnimationNode_method_get_input_count)

Amount of inputs in this animation node, only useful for animation nodes that go into [AnimationNodeBlendTree](class_animationnodeblendtree.md#class_AnimationNodeBlendTree).

---

<span id="class_AnimationNode_method_get_input_name"></span>

[String](class_string.md#class_String) **get_input_name** ( input: [int](class_int.md#class_int) ) *const* [🔗](class_animationnode.md#class_AnimationNode_method_get_input_name)

Gets the name of an input by index.

---

<span id="class_AnimationNode_method_get_parameter"></span>

[Variant](class_variant.md#class_Variant) **get_parameter** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_animationnode.md#class_AnimationNode_method_get_parameter)

Gets the value of a parameter. Parameters are custom local memory used for your animation nodes, given a resource can be reused in multiple trees.

---

<span id="class_AnimationNode_method_get_processing_animation_tree_instance_id"></span>

[int](class_int.md#class_int) **get_processing_animation_tree_instance_id** ( ) *const* [🔗](class_animationnode.md#class_AnimationNode_method_get_processing_animation_tree_instance_id)

Returns the object id of the [AnimationTree](class_animationtree.md#class_AnimationTree) that owns this node.

 **Note:** This method should only be called from within the [AnimationNodeExtension._process_animation_node()](class_animationnodeextension.md#class_AnimationNodeExtension_private_method__process_animation_node) method, and will return an invalid id otherwise.

---

<span id="class_AnimationNode_method_is_path_filtered"></span>

[bool](class_bool.md#class_bool) **is_path_filtered** ( path: [NodePath](class_nodepath.md#class_NodePath) ) *const* [🔗](class_animationnode.md#class_AnimationNode_method_is_path_filtered)

Returns `true` if the given path is filtered.

---

<span id="class_AnimationNode_method_is_process_testing"></span>

[bool](class_bool.md#class_bool) **is_process_testing** ( ) *const* [🔗](class_animationnode.md#class_AnimationNode_method_is_process_testing)

Returns `true` if this animation node is being processed in test-only mode.

---

<span id="class_AnimationNode_method_remove_input"></span>

void **remove_input** ( index: [int](class_int.md#class_int) ) [🔗](class_animationnode.md#class_AnimationNode_method_remove_input)

Removes an input, call this only when inactive.

---

<span id="class_AnimationNode_method_set_filter_path"></span>

void **set_filter_path** ( path: [NodePath](class_nodepath.md#class_NodePath), enable: [bool](class_bool.md#class_bool) ) [🔗](class_animationnode.md#class_AnimationNode_method_set_filter_path)

Adds or removes a path for the filter.

---

<span id="class_AnimationNode_method_set_input_name"></span>

[bool](class_bool.md#class_bool) **set_input_name** ( input: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) [🔗](class_animationnode.md#class_AnimationNode_method_set_input_name)

Sets the name of the input at the given `input` index. If the setting fails, returns `false`.

---

<span id="class_AnimationNode_method_set_parameter"></span>

void **set_parameter** ( name: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) [🔗](class_animationnode.md#class_AnimationNode_method_set_parameter)

Sets a custom parameter. These are used as local memory, because resources can be reused across the tree or scenes.
