.. meta::
	:keywords: sound

<span id="class_AudioListener2D"></span>

## AudioListener2D

**Inherits:** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Overrides the location sounds are heard from.

### Description

Once added to the scene tree and enabled using [make_current()](class_audiolistener2d.md#class_AudioListener2D_method_make_current), this node will override the location sounds are heard from. Only one **AudioListener2D** can be current. Using [make_current()](class_audiolistener2d.md#class_AudioListener2D_method_make_current) will disable the previous **AudioListener2D**.

If there is no active **AudioListener2D** in the current [Viewport](class_viewport.md#class_Viewport), center of the screen will be used as a hearing point for the audio. **AudioListener2D** needs to be inside [SceneTree](class_scenetree.md#class_SceneTree) to function.

### Methods


| void | [clear_current](class_audiolistener2d.md#class_AudioListener2D_method_clear_current) ( ) |
| --- | --- |
| [bool](class_bool.md#class_bool) | [is_current](class_audiolistener2d.md#class_AudioListener2D_method_is_current) ( ) const |
| void | [make_current](class_audiolistener2d.md#class_AudioListener2D_method_make_current) ( ) |

---

### Method Descriptions

<span id="class_AudioListener2D_method_clear_current"></span>

void **clear_current** ( ) [🔗](class_audiolistener2d.md#class_AudioListener2D_method_clear_current)

Disables the **AudioListener2D**. If it's not set as current, this method will have no effect.

---

<span id="class_AudioListener2D_method_is_current"></span>

[bool](class_bool.md#class_bool) **is_current** ( ) *const* [🔗](class_audiolistener2d.md#class_AudioListener2D_method_is_current)

Returns `true` if this **AudioListener2D** is currently active.

---

<span id="class_AudioListener2D_method_make_current"></span>

void **make_current** ( ) [🔗](class_audiolistener2d.md#class_AudioListener2D_method_make_current)

Makes the **AudioListener2D** active, setting it as the hearing point for the sounds. If there is already another active **AudioListener2D**, it will be disabled.

This method will have no effect if the **AudioListener2D** is not added to [SceneTree](class_scenetree.md#class_SceneTree).
