<span id="class_JavaScriptBridge"></span>

## JavaScriptBridge

**Inherits:** [Object](class_object.md#class_Object)

Singleton that connects the engine with the browser's JavaScript context in Web export.

### Description

The JavaScriptBridge singleton is implemented only in the Web export. It's used to access the browser's JavaScript context. This allows interaction with embedding pages or calling third-party JavaScript APIs.

 **Note:** This singleton can be disabled at build-time to improve security. By default, the JavaScriptBridge singleton is enabled. Official export templates also have the JavaScriptBridge singleton enabled. See [Compiling for the Web](../engine_details/development/compiling/compiling_for_web.md) in the documentation for more information.

### Tutorials

- [The JavaScriptBridge singleton](../tutorials/platform/web/javascript_bridge.md)

### Methods


| [JavaScriptObject](class_javascriptobject.md#class_JavaScriptObject) | [create_callback](class_javascriptbridge.md#class_JavaScriptBridge_method_create_callback) ( callable: [Callable](class_callable.md#class_Callable) ) |
| --- | --- |
| [Variant](class_variant.md#class_Variant) | [create_object](class_javascriptbridge.md#class_JavaScriptBridge_method_create_object) ( object: [String](class_string.md#class_String), ... ) vararg |
| void | [download_buffer](class_javascriptbridge.md#class_JavaScriptBridge_method_download_buffer) ( buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), name: [String](class_string.md#class_String), mime: [String](class_string.md#class_String) = "application/octet-stream" ) |
| [Variant](class_variant.md#class_Variant) | [eval](class_javascriptbridge.md#class_JavaScriptBridge_method_eval) ( code: [String](class_string.md#class_String), use_global_execution_context: [bool](class_bool.md#class_bool) = false ) |
| void | [force_fs_sync](class_javascriptbridge.md#class_JavaScriptBridge_method_force_fs_sync) ( ) |
| [JavaScriptObject](class_javascriptobject.md#class_JavaScriptObject) | [get_interface](class_javascriptbridge.md#class_JavaScriptBridge_method_get_interface) ( interface: [String](class_string.md#class_String) ) |
| [bool](class_bool.md#class_bool) | [is_js_buffer](class_javascriptbridge.md#class_JavaScriptBridge_method_is_js_buffer) ( javascript_object: [JavaScriptObject](class_javascriptobject.md#class_JavaScriptObject) ) |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [js_buffer_to_packed_byte_array](class_javascriptbridge.md#class_JavaScriptBridge_method_js_buffer_to_packed_byte_array) ( javascript_buffer: [JavaScriptObject](class_javascriptobject.md#class_JavaScriptObject) ) |
| [bool](class_bool.md#class_bool) | [pwa_needs_update](class_javascriptbridge.md#class_JavaScriptBridge_method_pwa_needs_update) ( ) const |
| Error | [pwa_update](class_javascriptbridge.md#class_JavaScriptBridge_method_pwa_update) ( ) |

---

### Signals

<span id="class_JavaScriptBridge_signal_pwa_update_available"></span>

**pwa_update_available** ( ) [🔗](class_javascriptbridge.md#class_JavaScriptBridge_signal_pwa_update_available)

Emitted when an update for this progressive web app has been detected but is waiting to be activated because a previous version is active. See [pwa_update()](class_javascriptbridge.md#class_JavaScriptBridge_method_pwa_update) to force the update to take place immediately.

---

### Method Descriptions

<span id="class_JavaScriptBridge_method_create_callback"></span>

[JavaScriptObject](class_javascriptobject.md#class_JavaScriptObject) **create_callback** ( callable: [Callable](class_callable.md#class_Callable) ) [🔗](class_javascriptbridge.md#class_JavaScriptBridge_method_create_callback)

Creates a reference to a [Callable](class_callable.md#class_Callable) that can be used as a callback by JavaScript. The reference must be kept until the callback happens, or it won't be called at all. See [JavaScriptObject](class_javascriptobject.md#class_JavaScriptObject) for usage.

 **Note:** The callback function must take exactly one [Array](class_array.md#class_Array) argument, which is going to be the JavaScript arguments object converted to an array.

---

<span id="class_JavaScriptBridge_method_create_object"></span>

[Variant](class_variant.md#class_Variant) **create_object** ( object: [String](class_string.md#class_String), ... ) *vararg* [🔗](class_javascriptbridge.md#class_JavaScriptBridge_method_create_object)

Creates a new JavaScript object using the `new` constructor. The `object` must a valid property of the JavaScript `window`. See [JavaScriptObject](class_javascriptobject.md#class_JavaScriptObject) for usage.

---

<span id="class_JavaScriptBridge_method_download_buffer"></span>

void **download_buffer** ( buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), name: [String](class_string.md#class_String), mime: [String](class_string.md#class_String) = "application/octet-stream" ) [🔗](class_javascriptbridge.md#class_JavaScriptBridge_method_download_buffer)

Prompts the user to download a file containing the specified `buffer`. The file will have the given `name` and `mime` type.

 **Note:** The browser may override the MIME type provided based on the file `name`'s extension.

 **Note:** Browsers might block the download if [download_buffer()](class_javascriptbridge.md#class_JavaScriptBridge_method_download_buffer) is not being called from a user interaction (e.g. button click).

 **Note:** Browsers might ask the user for permission or block the download if multiple download requests are made in a quick succession.

---

<span id="class_JavaScriptBridge_method_eval"></span>

[Variant](class_variant.md#class_Variant) **eval** ( code: [String](class_string.md#class_String), use_global_execution_context: [bool](class_bool.md#class_bool) = false ) [🔗](class_javascriptbridge.md#class_JavaScriptBridge_method_eval)

Execute the string `code` as JavaScript code within the browser window. This is a call to the actual global JavaScript function `eval()`.

If `use_global_execution_context` is `true`, the code will be evaluated in the global execution context. Otherwise, it is evaluated in the execution context of a function within the engine's runtime environment.

---

<span id="class_JavaScriptBridge_method_force_fs_sync"></span>

void **force_fs_sync** ( ) [🔗](class_javascriptbridge.md#class_JavaScriptBridge_method_force_fs_sync)

Force synchronization of the persistent file system (when enabled).

 **Note:** This is only useful for modules or extensions that can't use [FileAccess](class_fileaccess.md#class_FileAccess) to write files.

---

<span id="class_JavaScriptBridge_method_get_interface"></span>

[JavaScriptObject](class_javascriptobject.md#class_JavaScriptObject) **get_interface** ( interface: [String](class_string.md#class_String) ) [🔗](class_javascriptbridge.md#class_JavaScriptBridge_method_get_interface)

Returns an interface to a JavaScript object that can be used by scripts. The `interface` must be a valid property of the JavaScript `window`. The callback must accept a single [Array](class_array.md#class_Array) argument, which will contain the JavaScript `arguments`. See [JavaScriptObject](class_javascriptobject.md#class_JavaScriptObject) for usage.

---

<span id="class_JavaScriptBridge_method_is_js_buffer"></span>

[bool](class_bool.md#class_bool) **is_js_buffer** ( javascript_object: [JavaScriptObject](class_javascriptobject.md#class_JavaScriptObject) ) [🔗](class_javascriptbridge.md#class_JavaScriptBridge_method_is_js_buffer)

Returns `true` if the given `javascript_object` is of type [code]ArrayBuffer[/code], [code]DataView[/code], or one of the many typed array objects.

---

<span id="class_JavaScriptBridge_method_js_buffer_to_packed_byte_array"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **js_buffer_to_packed_byte_array** ( javascript_buffer: [JavaScriptObject](class_javascriptobject.md#class_JavaScriptObject) ) [🔗](class_javascriptbridge.md#class_JavaScriptBridge_method_js_buffer_to_packed_byte_array)

Returns a copy of `javascript_buffer`'s contents as a [PackedByteArray](class_packedbytearray.md#class_PackedByteArray). See also [is_js_buffer()](class_javascriptbridge.md#class_JavaScriptBridge_method_is_js_buffer).

---

<span id="class_JavaScriptBridge_method_pwa_needs_update"></span>

[bool](class_bool.md#class_bool) **pwa_needs_update** ( ) *const* [🔗](class_javascriptbridge.md#class_JavaScriptBridge_method_pwa_needs_update)

Returns `true` if a new version of the progressive web app is waiting to be activated.

 **Note:** Only relevant when exported as a Progressive Web App.

---

<span id="class_JavaScriptBridge_method_pwa_update"></span>

Error **pwa_update** ( ) [🔗](class_javascriptbridge.md#class_JavaScriptBridge_method_pwa_update)

Performs the live update of the progressive web app. Forcing the new version to be installed and the page to be reloaded.

 **Note:** Your application will be **reloaded in all browser tabs**.

 **Note:** Only relevant when exported as a Progressive Web App and [pwa_needs_update()](class_javascriptbridge.md#class_JavaScriptBridge_method_pwa_needs_update) returns `true`.
