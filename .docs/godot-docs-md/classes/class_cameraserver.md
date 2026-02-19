<span id="class_CameraServer"></span>

## CameraServer

**Inherits:** [Object](class_object.md#class_Object)

Server keeping track of different cameras accessible in Godot.

### Description

The **CameraServer** keeps track of different cameras accessible in Godot. These are external cameras such as webcams or the cameras on your phone.

It is notably used to provide AR modules with a video feed from the camera.

 **Note:** This class is currently only implemented on Linux, Android, macOS, and iOS. On other platforms no [CameraFeed](class_camerafeed.md#class_CameraFeed) s will be available. To get a [CameraFeed](class_camerafeed.md#class_CameraFeed) on iOS, the camera plugin from godot-ios-plugins is required.

### Properties


| [bool](class_bool.md#class_bool) | [monitoring_feeds](class_cameraserver.md#class_CameraServer_property_monitoring_feeds) | `false` |
| --- | --- | --- |

### Methods


| void | [add_feed](class_cameraserver.md#class_CameraServer_method_add_feed) ( feed: [CameraFeed](class_camerafeed.md#class_CameraFeed) ) |
| --- | --- |
| [Array](class_array.md#class_Array)\[[CameraFeed](class_camerafeed.md#class_CameraFeed)\] | [feeds](class_cameraserver.md#class_CameraServer_method_feeds) ( ) |
| [CameraFeed](class_camerafeed.md#class_CameraFeed) | [get_feed](class_cameraserver.md#class_CameraServer_method_get_feed) ( index: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [get_feed_count](class_cameraserver.md#class_CameraServer_method_get_feed_count) ( ) |
| void | [remove_feed](class_cameraserver.md#class_CameraServer_method_remove_feed) ( feed: [CameraFeed](class_camerafeed.md#class_CameraFeed) ) |

---

### Signals

<span id="class_CameraServer_signal_camera_feed_added"></span>

**camera_feed_added** ( id: [int](class_int.md#class_int) ) [🔗](class_cameraserver.md#class_CameraServer_signal_camera_feed_added)

Emitted when a [CameraFeed](class_camerafeed.md#class_CameraFeed) is added (e.g. a webcam is plugged in).

---

<span id="class_CameraServer_signal_camera_feed_removed"></span>

**camera_feed_removed** ( id: [int](class_int.md#class_int) ) [🔗](class_cameraserver.md#class_CameraServer_signal_camera_feed_removed)

Emitted when a [CameraFeed](class_camerafeed.md#class_CameraFeed) is removed (e.g. a webcam is unplugged).

---

<span id="class_CameraServer_signal_camera_feeds_updated"></span>

**camera_feeds_updated** ( ) [🔗](class_cameraserver.md#class_CameraServer_signal_camera_feeds_updated)

Emitted when camera feeds are updated.

---

### Enumerations

<span id="enum_CameraServer_FeedImage"></span>

enum **FeedImage**: [🔗](class_cameraserver.md#enum_CameraServer_FeedImage)

<span id="class_CameraServer_constant_FEED_RGBA_IMAGE"></span>

[FeedImage](class_cameraserver.md#enum_CameraServer_FeedImage) **FEED_RGBA_IMAGE** = `0`

The RGBA camera image.

<span id="class_CameraServer_constant_FEED_YCBCR_IMAGE"></span>

[FeedImage](class_cameraserver.md#enum_CameraServer_FeedImage) **FEED_YCBCR_IMAGE** = `0`

The YCbCr camera image.

<span id="class_CameraServer_constant_FEED_Y_IMAGE"></span>

[FeedImage](class_cameraserver.md#enum_CameraServer_FeedImage) **FEED_Y_IMAGE** = `0`

The Y component camera image.

<span id="class_CameraServer_constant_FEED_CBCR_IMAGE"></span>

[FeedImage](class_cameraserver.md#enum_CameraServer_FeedImage) **FEED_CBCR_IMAGE** = `1`

The CbCr component camera image.

---

### Property Descriptions

<span id="class_CameraServer_property_monitoring_feeds"></span>

[bool](class_bool.md#class_bool) **monitoring_feeds** = `false` [🔗](class_cameraserver.md#class_CameraServer_property_monitoring_feeds)

- void **set_monitoring_feeds** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_monitoring_feeds** ( )

If `true`, the server is actively monitoring available camera feeds.

This has a performance cost, so only set it to `true` when you're actively accessing the camera.

 **Note:** After setting it to `true`, you can receive updated camera feeds through the [camera_feeds_updated](class_cameraserver.md#class_CameraServer_signal_camera_feeds_updated) signal.

.. tabs::

```
```

    func _ready():
        CameraServer.camera_feeds_updated.connect(_on_camera_feeds_updated)
        CameraServer.monitoring_feeds = true

    func _on_camera_feeds_updated():
        var feeds = CameraServer.feeds()

```
```

    public override void _Ready()
    {
        CameraServer.CameraFeedsUpdated += OnCameraFeedsUpdated;
        CameraServer.MonitoringFeeds = true;
    }

    void OnCameraFeedsUpdated()
    {
        var feeds = CameraServer.Feeds();
    }

---

### Method Descriptions

<span id="class_CameraServer_method_add_feed"></span>

void **add_feed** ( feed: [CameraFeed](class_camerafeed.md#class_CameraFeed) ) [🔗](class_cameraserver.md#class_CameraServer_method_add_feed)

Adds the camera `feed` to the camera server.

---

<span id="class_CameraServer_method_feeds"></span>

[Array](class_array.md#class_Array)\[[CameraFeed](class_camerafeed.md#class_CameraFeed)\] **feeds** ( ) [🔗](class_cameraserver.md#class_CameraServer_method_feeds)

Returns an array of [CameraFeed](class_camerafeed.md#class_CameraFeed) s.

---

<span id="class_CameraServer_method_get_feed"></span>

[CameraFeed](class_camerafeed.md#class_CameraFeed) **get_feed** ( index: [int](class_int.md#class_int) ) [🔗](class_cameraserver.md#class_CameraServer_method_get_feed)

Returns the [CameraFeed](class_camerafeed.md#class_CameraFeed) corresponding to the camera with the given `index`.

---

<span id="class_CameraServer_method_get_feed_count"></span>

[int](class_int.md#class_int) **get_feed_count** ( ) [🔗](class_cameraserver.md#class_CameraServer_method_get_feed_count)

Returns the number of [CameraFeed](class_camerafeed.md#class_CameraFeed) s registered.

---

<span id="class_CameraServer_method_remove_feed"></span>

void **remove_feed** ( feed: [CameraFeed](class_camerafeed.md#class_CameraFeed) ) [🔗](class_cameraserver.md#class_CameraServer_method_remove_feed)

Removes the specified camera `feed`.
