<span id="class_EditorUndoRedoManager"></span>

## EditorUndoRedoManager

**Inherits:** [Object](class_object.md#class_Object)

Manages undo history of scenes opened in the editor.

### Description

**EditorUndoRedoManager** is a manager for [UndoRedo](class_undoredo.md#class_UndoRedo) objects associated with edited scenes. Each scene has its own undo history and **EditorUndoRedoManager** ensures that each action performed in the editor gets associated with a proper scene. For actions not related to scenes ([ProjectSettings](class_projectsettings.md#class_ProjectSettings) edits, external resources, etc.), a separate global history is used.

The usage is mostly the same as [UndoRedo](class_undoredo.md#class_UndoRedo). You create and commit actions and the manager automatically decides under-the-hood what scenes it belongs to. The scene is deduced based on the first operation in an action, using the object from the operation. The rules are as follows:

- If the object is a [Node](class_node.md#class_Node), use the currently edited scene;

- If the object is a built-in resource, use the scene from its path;

- If the object is external resource or anything else, use global history.

This guessing can sometimes yield false results, so you can provide a custom context object when creating an action.

 **EditorUndoRedoManager** is intended to be used by Godot editor plugins. You can obtain it using [EditorPlugin.get_undo_redo()](class_editorplugin.md#class_EditorPlugin_method_get_undo_redo). For non-editor uses or plugins that don't need to integrate with the editor's undo history, use [UndoRedo](class_undoredo.md#class_UndoRedo) instead.

The manager's API is mostly the same as in [UndoRedo](class_undoredo.md#class_UndoRedo), so you can refer to its documentation for more examples. The main difference is that **EditorUndoRedoManager** uses object + method name for actions, instead of [Callable](class_callable.md#class_Callable).

### Methods


| void | [add_do_method](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_add_do_method) ( object: [Object](class_object.md#class_Object), method: [StringName](class_stringname.md#class_StringName), ... ) vararg |
| --- | --- |
| void | [add_do_property](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_add_do_property) ( object: [Object](class_object.md#class_Object), property: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) |
| void | [add_do_reference](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_add_do_reference) ( object: [Object](class_object.md#class_Object) ) |
| void | [add_undo_method](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_add_undo_method) ( object: [Object](class_object.md#class_Object), method: [StringName](class_stringname.md#class_StringName), ... ) vararg |
| void | [add_undo_property](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_add_undo_property) ( object: [Object](class_object.md#class_Object), property: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) |
| void | [add_undo_reference](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_add_undo_reference) ( object: [Object](class_object.md#class_Object) ) |
| void | [clear_history](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_clear_history) ( id: [int](class_int.md#class_int) = -99, increase_version: [bool](class_bool.md#class_bool) = true ) |
| void | [commit_action](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_commit_action) ( execute: [bool](class_bool.md#class_bool) = true ) |
| void | [create_action](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_create_action) ( name: [String](class_string.md#class_String), merge_mode: [MergeMode](class_undoredo.md#enum_UndoRedo_MergeMode) = 0, custom_context: [Object](class_object.md#class_Object) = null, backward_undo_ops: [bool](class_bool.md#class_bool) = false, mark_unsaved: [bool](class_bool.md#class_bool) = true ) |
| void | [force_fixed_history](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_force_fixed_history) ( ) |
| [UndoRedo](class_undoredo.md#class_UndoRedo) | [get_history_undo_redo](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_get_history_undo_redo) ( id: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_object_history_id](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_get_object_history_id) ( object: [Object](class_object.md#class_Object) ) const |
| [bool](class_bool.md#class_bool) | [is_committing_action](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_is_committing_action) ( ) const |

---

### Signals

<span id="class_EditorUndoRedoManager_signal_history_changed"></span>

**history_changed** ( ) [🔗](class_editorundoredomanager.md#class_EditorUndoRedoManager_signal_history_changed)

Emitted when the list of actions in any history has changed, either when an action is committed or a history is cleared.

---

<span id="class_EditorUndoRedoManager_signal_version_changed"></span>

**version_changed** ( ) [🔗](class_editorundoredomanager.md#class_EditorUndoRedoManager_signal_version_changed)

Emitted when the version of any history has changed as a result of undo or redo call.

---

### Enumerations

<span id="enum_EditorUndoRedoManager_SpecialHistory"></span>

enum **SpecialHistory**: [🔗](class_editorundoredomanager.md#enum_EditorUndoRedoManager_SpecialHistory)

<span id="class_EditorUndoRedoManager_constant_GLOBAL_HISTORY"></span>

[SpecialHistory](class_editorundoredomanager.md#enum_EditorUndoRedoManager_SpecialHistory) **GLOBAL_HISTORY** = `0`

Global history not associated with any scene, but with external resources etc.

<span id="class_EditorUndoRedoManager_constant_REMOTE_HISTORY"></span>

[SpecialHistory](class_editorundoredomanager.md#enum_EditorUndoRedoManager_SpecialHistory) **REMOTE_HISTORY** = `-9`

History associated with remote inspector. Used when live editing a running project.

<span id="class_EditorUndoRedoManager_constant_INVALID_HISTORY"></span>

[SpecialHistory](class_editorundoredomanager.md#enum_EditorUndoRedoManager_SpecialHistory) **INVALID_HISTORY** = `-99`

Invalid "null" history. It's a special value, not associated with any object.

---

### Method Descriptions

<span id="class_EditorUndoRedoManager_method_add_do_method"></span>

void **add_do_method** ( object: [Object](class_object.md#class_Object), method: [StringName](class_stringname.md#class_StringName), ... ) *vararg* [🔗](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_add_do_method)

Register a method that will be called when the action is committed (i.e. the "do" action).

If this is the first operation, the `object` will be used to deduce target undo history.

---

<span id="class_EditorUndoRedoManager_method_add_do_property"></span>

void **add_do_property** ( object: [Object](class_object.md#class_Object), property: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) [🔗](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_add_do_property)

Register a property value change for "do".

If this is the first operation, the `object` will be used to deduce target undo history.

---

<span id="class_EditorUndoRedoManager_method_add_do_reference"></span>

void **add_do_reference** ( object: [Object](class_object.md#class_Object) ) [🔗](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_add_do_reference)

Register a reference for "do" that will be erased if the "do" history is lost. This is useful mostly for new nodes created for the "do" call. Do not use for resources.

---

<span id="class_EditorUndoRedoManager_method_add_undo_method"></span>

void **add_undo_method** ( object: [Object](class_object.md#class_Object), method: [StringName](class_stringname.md#class_StringName), ... ) *vararg* [🔗](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_add_undo_method)

Register a method that will be called when the action is undone (i.e. the "undo" action).

If this is the first operation, the `object` will be used to deduce target undo history.

---

<span id="class_EditorUndoRedoManager_method_add_undo_property"></span>

void **add_undo_property** ( object: [Object](class_object.md#class_Object), property: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) [🔗](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_add_undo_property)

Register a property value change for "undo".

If this is the first operation, the `object` will be used to deduce target undo history.

---

<span id="class_EditorUndoRedoManager_method_add_undo_reference"></span>

void **add_undo_reference** ( object: [Object](class_object.md#class_Object) ) [🔗](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_add_undo_reference)

Register a reference for "undo" that will be erased if the "undo" history is lost. This is useful mostly for nodes removed with the "do" call (not the "undo" call!).

---

<span id="class_EditorUndoRedoManager_method_clear_history"></span>

void **clear_history** ( id: [int](class_int.md#class_int) = -99, increase_version: [bool](class_bool.md#class_bool) = true ) [🔗](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_clear_history)

Clears the given undo history. You can clear history for a specific scene, global history, or for all histories at once (except [REMOTE_HISTORY](class_editorundoredomanager.md#class_EditorUndoRedoManager_constant_REMOTE_HISTORY)) if `id` is [INVALID_HISTORY](class_editorundoredomanager.md#class_EditorUndoRedoManager_constant_INVALID_HISTORY).

If `increase_version` is `true`, the undo history version will be increased, marking it as unsaved. Useful for operations that modify the scene, but don't support undo.

::

    var scene_root = EditorInterface.get_edited_scene_root()
    var undo_redo = EditorInterface.get_editor_undo_redo()
    undo_redo.clear_history(undo_redo.get_object_history_id(scene_root))

 **Note:** If you want to mark an edited scene as unsaved without clearing its history, use [EditorInterface.mark_scene_as_unsaved()](class_editorinterface.md#class_EditorInterface_method_mark_scene_as_unsaved) instead.

---

<span id="class_EditorUndoRedoManager_method_commit_action"></span>

void **commit_action** ( execute: [bool](class_bool.md#class_bool) = true ) [🔗](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_commit_action)

Commits the action. If `execute` is `true` (default), all "do" methods/properties are called/set when this function is called.

---

<span id="class_EditorUndoRedoManager_method_create_action"></span>

void **create_action** ( name: [String](class_string.md#class_String), merge_mode: [MergeMode](class_undoredo.md#enum_UndoRedo_MergeMode) = 0, custom_context: [Object](class_object.md#class_Object) = null, backward_undo_ops: [bool](class_bool.md#class_bool) = false, mark_unsaved: [bool](class_bool.md#class_bool) = true ) [🔗](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_create_action)

Create a new action. After this is called, do all your calls to [add_do_method()](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_add_do_method), [add_undo_method()](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_add_undo_method), [add_do_property()](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_add_do_property), and [add_undo_property()](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_add_undo_property), then commit the action with [commit_action()](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_commit_action).

The way actions are merged is dictated by the `merge_mode` argument.

If `custom_context` object is provided, it will be used for deducing target history (instead of using the first operation).

The way undo operation are ordered in actions is dictated by `backward_undo_ops`. When `backward_undo_ops` is `false` undo option are ordered in the same order they were added. Which means the first operation to be added will be the first to be undone.

If `mark_unsaved` is `false`, the action will not mark the history as unsaved. This is useful for example for actions that change a selection, or a setting that will be saved automatically. Otherwise, this should be left to `true` if the action requires saving by the user or if it can cause data loss when left unsaved.

---

<span id="class_EditorUndoRedoManager_method_force_fixed_history"></span>

void **force_fixed_history** ( ) [🔗](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_force_fixed_history)

Forces the next operation (e.g. [add_do_method()](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_add_do_method)) to use the action's history rather than guessing it from the object. This is sometimes needed when a history can't be correctly determined, like for a nested resource that doesn't have a path yet.

This method should only be used when absolutely necessary, otherwise it might cause invalid history state. For most of complex cases, the `custom_context` parameter of [create_action()](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_create_action) is sufficient.

---

<span id="class_EditorUndoRedoManager_method_get_history_undo_redo"></span>

[UndoRedo](class_undoredo.md#class_UndoRedo) **get_history_undo_redo** ( id: [int](class_int.md#class_int) ) *const* [🔗](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_get_history_undo_redo)

Returns the [UndoRedo](class_undoredo.md#class_UndoRedo) object associated with the given history `id`.

 `id` above `0` are mapped to the opened scene tabs (but it doesn't match their order). `id` of `0` or lower have special meaning (see [SpecialHistory](class_editorundoredomanager.md#enum_EditorUndoRedoManager_SpecialHistory)).

Best used with [get_object_history_id()](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_get_object_history_id). This method is only provided in case you need some more advanced methods of [UndoRedo](class_undoredo.md#class_UndoRedo) (but keep in mind that directly operating on the [UndoRedo](class_undoredo.md#class_UndoRedo) object might affect editor's stability).

---

<span id="class_EditorUndoRedoManager_method_get_object_history_id"></span>

[int](class_int.md#class_int) **get_object_history_id** ( object: [Object](class_object.md#class_Object) ) *const* [🔗](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_get_object_history_id)

Returns the history ID deduced from the given `object`. It can be used with [get_history_undo_redo()](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_get_history_undo_redo).

---

<span id="class_EditorUndoRedoManager_method_is_committing_action"></span>

[bool](class_bool.md#class_bool) **is_committing_action** ( ) *const* [🔗](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_is_committing_action)

Returns `true` if the **EditorUndoRedoManager** is currently committing the action, i.e. running its "do" method or property change (see [commit_action()](class_editorundoredomanager.md#class_EditorUndoRedoManager_method_commit_action)).
