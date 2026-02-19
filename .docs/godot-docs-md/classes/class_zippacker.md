<span id="class_ZIPPacker"></span>

## ZIPPacker

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Allows the creation of ZIP files.

### Description

This class implements a writer that allows storing the multiple blobs in a ZIP archive. See also [ZIPReader](class_zipreader.md#class_ZIPReader) and [PCKPacker](class_pckpacker.md#class_PCKPacker).

::

    # Create a ZIP archive with a single file at its root.
    func write_zip_file():
        var writer = ZIPPacker.new()
        var err = writer.open("user://archive.zip")
        if err != OK:
            return err
        writer.start_file("hello.txt")
        writer.write_file("Hello World".to_utf8_buffer())
        writer.close_file()

        writer.close()
        return OK

### Properties


| [int](class_int.md#class_int) | [compression_level](class_zippacker.md#class_ZIPPacker_property_compression_level) | `-1` |
| --- | --- | --- |

### Methods


| Error | [add_directory](class_zippacker.md#class_ZIPPacker_method_add_directory) ( path: [String](class_string.md#class_String), permissions: | bitfield | \[[UnixPermissionFlags](class_fileaccess.md#enum_FileAccess_UnixPermissionFlags)\] = 493, modified_time: [int](class_int.md#class_int) = 0 ) |
| --- | --- | --- | --- |
| Error | [close](class_zippacker.md#class_ZIPPacker_method_close) ( ) |
| Error | [close_file](class_zippacker.md#class_ZIPPacker_method_close_file) ( ) |
| Error | [open](class_zippacker.md#class_ZIPPacker_method_open) ( path: [String](class_string.md#class_String), append: [ZipAppend](class_zippacker.md#enum_ZIPPacker_ZipAppend) = 0 ) |
| Error | [start_file](class_zippacker.md#class_ZIPPacker_method_start_file) ( path: [String](class_string.md#class_String), permissions: | bitfield | \[[UnixPermissionFlags](class_fileaccess.md#enum_FileAccess_UnixPermissionFlags)\] = 420, modified_time: [int](class_int.md#class_int) = 0 ) |
| Error | [write_file](class_zippacker.md#class_ZIPPacker_method_write_file) ( data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |

---

### Enumerations

<span id="enum_ZIPPacker_ZipAppend"></span>

enum **ZipAppend**: [🔗](class_zippacker.md#enum_ZIPPacker_ZipAppend)

<span id="class_ZIPPacker_constant_APPEND_CREATE"></span>

[ZipAppend](class_zippacker.md#enum_ZIPPacker_ZipAppend) **APPEND_CREATE** = `0`

Create a new zip archive at the given path.

<span id="class_ZIPPacker_constant_APPEND_CREATEAFTER"></span>

[ZipAppend](class_zippacker.md#enum_ZIPPacker_ZipAppend) **APPEND_CREATEAFTER** = `1`

Append a new zip archive to the end of the already existing file at the given path.

<span id="class_ZIPPacker_constant_APPEND_ADDINZIP"></span>

[ZipAppend](class_zippacker.md#enum_ZIPPacker_ZipAppend) **APPEND_ADDINZIP** = `2`

Add new files to the existing zip archive at the given path.

---

<span id="enum_ZIPPacker_CompressionLevel"></span>

enum **CompressionLevel**: [🔗](class_zippacker.md#enum_ZIPPacker_CompressionLevel)

<span id="class_ZIPPacker_constant_COMPRESSION_DEFAULT"></span>

[CompressionLevel](class_zippacker.md#enum_ZIPPacker_CompressionLevel) **COMPRESSION_DEFAULT** = `-1`

Start a file with the default Deflate compression level (`6`). This is a good compromise between speed and file size.

<span id="class_ZIPPacker_constant_COMPRESSION_NONE"></span>

[CompressionLevel](class_zippacker.md#enum_ZIPPacker_CompressionLevel) **COMPRESSION_NONE** = `0`

Start a file with no compression. This is also known as the "Store" compression mode and is the fastest method of packing files inside a ZIP archive. Consider using this mode for files that are already compressed (such as JPEG, PNG, MP3, or Ogg Vorbis files).

<span id="class_ZIPPacker_constant_COMPRESSION_FAST"></span>

[CompressionLevel](class_zippacker.md#enum_ZIPPacker_CompressionLevel) **COMPRESSION_FAST** = `1`

Start a file with the fastest Deflate compression level (`1`). This is fast to compress, but results in larger file sizes than [COMPRESSION_DEFAULT](class_zippacker.md#class_ZIPPacker_constant_COMPRESSION_DEFAULT). Decompression speed is generally unaffected by the chosen compression level.

<span id="class_ZIPPacker_constant_COMPRESSION_BEST"></span>

[CompressionLevel](class_zippacker.md#enum_ZIPPacker_CompressionLevel) **COMPRESSION_BEST** = `9`

Start a file with the best Deflate compression level (`9`). This is slow to compress, but results in smaller file sizes than [COMPRESSION_DEFAULT](class_zippacker.md#class_ZIPPacker_constant_COMPRESSION_DEFAULT). Decompression speed is generally unaffected by the chosen compression level.

---

### Property Descriptions

<span id="class_ZIPPacker_property_compression_level"></span>

[int](class_int.md#class_int) **compression_level** = `-1` [🔗](class_zippacker.md#class_ZIPPacker_property_compression_level)

- void **set_compression_level** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_compression_level** ( )

The compression level used when [start_file()](class_zippacker.md#class_ZIPPacker_method_start_file) is called. Use [CompressionLevel](class_zippacker.md#enum_ZIPPacker_CompressionLevel) as a reference.

---

### Method Descriptions

<span id="class_ZIPPacker_method_add_directory"></span>

Error **add_directory** ( path: [String](class_string.md#class_String), permissions: *BitField*\[[UnixPermissionFlags](class_fileaccess.md#enum_FileAccess_UnixPermissionFlags)\] = 493, modified_time: [int](class_int.md#class_int) = 0 ) [🔗](class_zippacker.md#class_ZIPPacker_method_add_directory)

Adds directory to the archive. If `modified_time` is set to `0`, current system time is used.

 **Note:** Directories are automatically created when [start_file()](class_zippacker.md#class_ZIPPacker_method_start_file) is called, use this function before adding files to create directories with custom permissions and modification time.

---

<span id="class_ZIPPacker_method_close"></span>

Error **close** ( ) [🔗](class_zippacker.md#class_ZIPPacker_method_close)

Closes the underlying resources used by this instance.

---

<span id="class_ZIPPacker_method_close_file"></span>

Error **close_file** ( ) [🔗](class_zippacker.md#class_ZIPPacker_method_close_file)

Stops writing to a file within the archive.

It will fail if there is no open file.

---

<span id="class_ZIPPacker_method_open"></span>

Error **open** ( path: [String](class_string.md#class_String), append: [ZipAppend](class_zippacker.md#enum_ZIPPacker_ZipAppend) = 0 ) [🔗](class_zippacker.md#class_ZIPPacker_method_open)

Opens a zip file for writing at the given path using the specified write mode.

This must be called before everything else.

---

<span id="class_ZIPPacker_method_start_file"></span>

Error **start_file** ( path: [String](class_string.md#class_String), permissions: *BitField*\[[UnixPermissionFlags](class_fileaccess.md#enum_FileAccess_UnixPermissionFlags)\] = 420, modified_time: [int](class_int.md#class_int) = 0 ) [🔗](class_zippacker.md#class_ZIPPacker_method_start_file)

Starts writing to a file within the archive. Only one file can be written at the same time. If `modified_time` is set to `0`, current system time is used.

Must be called after [open()](class_zippacker.md#class_ZIPPacker_method_open).

---

<span id="class_ZIPPacker_method_write_file"></span>

Error **write_file** ( data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_zippacker.md#class_ZIPPacker_method_write_file)

Write the given `data` to the file.

Needs to be called after [start_file()](class_zippacker.md#class_ZIPPacker_method_start_file).
