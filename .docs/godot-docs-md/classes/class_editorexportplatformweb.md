<span id="class_EditorExportPlatformWeb"></span>

## EditorExportPlatformWeb

**Inherits:** [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Exporter for the Web.

### Description

The Web exporter customizes how a web build is handled. In the editor's "Export" window, it is created when adding a new "Web" preset.

 **Note:** Godot on Web is rendered inside a `<canvas>` tag. Normally, the canvas cannot be positioned or resized manually, but otherwise acts as the main [Window](class_window.md#class_Window) of the application.

### Tutorials

- [Exporting for the Web](../tutorials/export/exporting_for_web.md)

- [Web documentation index](../tutorials/platform/web/index.md)

### Properties


| [String](class_string.md#class_String) | custom_template/debug |
| --- | --- |
| [String](class_string.md#class_String) | custom_template/release |
| [int](class_int.md#class_int) | html/canvas_resize_policy |
| [String](class_string.md#class_String) | html/custom_html_shell |
| [bool](class_bool.md#class_bool) | html/experimental_virtual_keyboard |
| [bool](class_bool.md#class_bool) | html/export_icon |
| [bool](class_bool.md#class_bool) | html/focus_canvas_on_start |
| [String](class_string.md#class_String) | html/head_include |
| [Color](class_color.md#class_Color) | progressive_web_app/background_color |
| [int](class_int.md#class_int) | progressive_web_app/display |
| [bool](class_bool.md#class_bool) | progressive_web_app/enabled |
| [bool](class_bool.md#class_bool) | progressive_web_app/ensure_cross_origin_isolation_headers |
| [String](class_string.md#class_String) | progressive_web_app/icon_144x144 |
| [String](class_string.md#class_String) | progressive_web_app/icon_180x180 |
| [String](class_string.md#class_String) | progressive_web_app/icon_512x512 |
| [String](class_string.md#class_String) | progressive_web_app/offline_page |
| [int](class_int.md#class_int) | progressive_web_app/orientation |
| [int](class_int.md#class_int) | threads/emscripten_pool_size |
| [int](class_int.md#class_int) | threads/godot_pool_size |
| [bool](class_bool.md#class_bool) | variant/extensions_support |
| [bool](class_bool.md#class_bool) | variant/thread_support |
| [bool](class_bool.md#class_bool) | vram_texture_compression/for_desktop |
| [bool](class_bool.md#class_bool) | vram_texture_compression/for_mobile |

---

### Property Descriptions

.. _class_EditorExportPlatformWeb_property_custom_template/debug:

[String](class_string.md#class_String) **custom_template/debug** 🔗

File path to the custom export template used for debug builds. If left empty, the default template is used.

---

.. _class_EditorExportPlatformWeb_property_custom_template/release:

[String](class_string.md#class_String) **custom_template/release** 🔗

File path to the custom export template used for release builds. If left empty, the default template is used.

---

.. _class_EditorExportPlatformWeb_property_html/canvas_resize_policy:

[int](class_int.md#class_int) **html/canvas_resize_policy** 🔗

Determines how the canvas should be resized by Godot.

- **None:** The canvas is not automatically resized.

- **Project:** The size of the canvas is dependent on the [ProjectSettings](class_projectsettings.md#class_ProjectSettings).

- **Adaptive:** The canvas is automatically resized to fit as much of the web page as possible.

---

.. _class_EditorExportPlatformWeb_property_html/custom_html_shell:

[String](class_string.md#class_String) **html/custom_html_shell** 🔗

The custom HTML page that wraps the exported web build. If left empty, the default HTML shell is used.

For more information, see the [Customizing HTML5 Shell](../tutorials/platform/web/customizing_html5_shell.md) tutorial.

---

.. _class_EditorExportPlatformWeb_property_html/experimental_virtual_keyboard:

[bool](class_bool.md#class_bool) **html/experimental_virtual_keyboard** 🔗

**Experimental:** This property may be changed or removed in future versions.

If `true`, embeds support for a virtual keyboard into the web page, which is shown when necessary on touchscreen devices.

---

.. _class_EditorExportPlatformWeb_property_html/export_icon:

[bool](class_bool.md#class_bool) **html/export_icon** 🔗

If `true`, the project icon will be used as the favicon for this application's web page.

---

.. _class_EditorExportPlatformWeb_property_html/focus_canvas_on_start:

[bool](class_bool.md#class_bool) **html/focus_canvas_on_start** 🔗

If `true`, the canvas will be focused as soon as the application is loaded, if the browser window is already in focus.

---

.. _class_EditorExportPlatformWeb_property_html/head_include:

[String](class_string.md#class_String) **html/head_include** 🔗

Additional HTML tags to include inside the `<head>`, such as `<meta>` tags.

 **Note:** You do not need to add a `<title>` tag, as it is automatically included based on the project's name.

---

.. _class_EditorExportPlatformWeb_property_progressive_web_app/background_color:

[Color](class_color.md#class_Color) **progressive_web_app/background_color** 🔗

The background color used behind the web application.

---

.. _class_EditorExportPlatformWeb_property_progressive_web_app/display:

[int](class_int.md#class_int) **progressive_web_app/display** 🔗

The display mode to use for this progressive web application. Different browsers and platforms may not behave the same.

- **Fullscreen:** Displays the app in fullscreen and hides all of the browser's UI elements.

- **Standalone:** Displays the app in a separate window and hides all of the browser's UI elements.

- **Minimal UI:** Displays the app in a separate window and only shows the browser's UI elements for navigation.

- **Browser:** Displays the app as a normal web page.

---

.. _class_EditorExportPlatformWeb_property_progressive_web_app/enabled:

[bool](class_bool.md#class_bool) **progressive_web_app/enabled** 🔗

If `true`, turns this web build into a progressive web application (PWA).

---

.. _class_EditorExportPlatformWeb_property_progressive_web_app/ensure_cross_origin_isolation_headers:

[bool](class_bool.md#class_bool) **progressive_web_app/ensure_cross_origin_isolation_headers** 🔗

When enabled, the progressive web app will make sure that each request has cross-origin isolation headers (COEP/COOP).

This can simplify the setup to serve the exported game.

---

.. _class_EditorExportPlatformWeb_property_progressive_web_app/icon_144x144:

[String](class_string.md#class_String) **progressive_web_app/icon_144x144** 🔗

File path to the smallest icon for this web application. If not defined, defaults to the project icon.

 **Note:** If the icon is not 144×144, it will be automatically resized for the final build.

---

.. _class_EditorExportPlatformWeb_property_progressive_web_app/icon_180x180:

[String](class_string.md#class_String) **progressive_web_app/icon_180x180** 🔗

File path to the small icon for this web application. If not defined, defaults to the project icon.

 **Note:** If the icon is not 180×180, it will be automatically resized for the final build.

---

.. _class_EditorExportPlatformWeb_property_progressive_web_app/icon_512x512:

[String](class_string.md#class_String) **progressive_web_app/icon_512x512** 🔗

File path to the largest icon for this web application. If not defined, defaults to the project icon.

 **Note:** If the icon is not 512×512, it will be automatically resized for the final build.

---

.. _class_EditorExportPlatformWeb_property_progressive_web_app/offline_page:

[String](class_string.md#class_String) **progressive_web_app/offline_page** 🔗

The page to display, should the server hosting the page not be available. This page is saved in the client's machine.

---

.. _class_EditorExportPlatformWeb_property_progressive_web_app/orientation:

[int](class_int.md#class_int) **progressive_web_app/orientation** 🔗

The orientation to use when the web application is run through a mobile device.

- **Any:** No orientation is forced.

- **Landscape:** Forces a horizontal layout (wider than it is taller).

- **Portrait:** Forces a vertical layout (taller than it is wider).

---

.. _class_EditorExportPlatformWeb_property_threads/emscripten_pool_size:

[int](class_int.md#class_int) **threads/emscripten_pool_size** 🔗

The number of threads that emscripten will allocate at startup. A smaller value will allocate fewer threads and consume fewer system resources, but you may run the risk of running out of threads in the pool and needing to allocate more threads at run time which may cause a deadlock.

 **Note:** Some browsers have a hard cap on the number of threads that can be allocated, so it is best to be cautious and keep this number low.

---

.. _class_EditorExportPlatformWeb_property_threads/godot_pool_size:

[int](class_int.md#class_int) **threads/godot_pool_size** 🔗

Override for the default size of the [WorkerThreadPool](class_workerthreadpool.md#class_WorkerThreadPool). This setting is used when ProjectSettings.threading/worker_pool/max_threads size is set to `-1` (which it is by default). This size must be smaller than threads/emscripten_pool_size otherwise deadlocks may occur.

When using threads, this size needs to be large enough to accommodate features that rely on having a dedicated thread like ProjectSettings.physics/2d/run_on_separate_thread or ProjectSettings.rendering/driver/threads/thread_model. In general, it is best to ensure that this is at least `4` and is at least `2` or `3` less than threads/emscripten_pool_size.

---

.. _class_EditorExportPlatformWeb_property_variant/extensions_support:

[bool](class_bool.md#class_bool) **variant/extensions_support** 🔗

If `true` enables [GDExtension](class_gdextension.md#class_GDExtension) support for this web build.

---

.. _class_EditorExportPlatformWeb_property_variant/thread_support:

[bool](class_bool.md#class_bool) **variant/thread_support** 🔗

If `true`, the exported game will support threads. It requires a "cross-origin isolated" website, which may be difficult to set up and is limited for security reasons (such as not being able to communicate with third-party websites).

If `false`, the exported game will not support threads. As a result, it is more prone to performance and audio issues, but will only require to be run on an HTTPS website.

---

.. _class_EditorExportPlatformWeb_property_vram_texture_compression/for_desktop:

[bool](class_bool.md#class_bool) **vram_texture_compression/for_desktop** 🔗

If `true`, allows textures to be optimized for desktop through the S3TC/BPTC algorithm.

---

.. _class_EditorExportPlatformWeb_property_vram_texture_compression/for_mobile:

[bool](class_bool.md#class_bool) **vram_texture_compression/for_mobile** 🔗

If `true` allows textures to be optimized for mobile through the ETC2/ASTC algorithm.
