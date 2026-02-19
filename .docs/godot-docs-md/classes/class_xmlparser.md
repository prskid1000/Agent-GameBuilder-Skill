<span id="class_XMLParser"></span>

## XMLParser

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Provides a low-level interface for creating parsers for XML files.

### Description

Provides a low-level interface for creating parsers for XML files. This class can serve as base to make custom XML parsers.

To parse XML, you must open a file with the [open()](class_xmlparser.md#class_XMLParser_method_open) method or a buffer with the [open_buffer()](class_xmlparser.md#class_XMLParser_method_open_buffer) method. Then, the [read()](class_xmlparser.md#class_XMLParser_method_read) method must be called to parse the next nodes. Most of the methods take into consideration the currently parsed node.

Here is an example of using **XMLParser** to parse an SVG file (which is based on XML), printing each element and its attributes as a dictionary:

.. tabs::

```
```

    var parser = XMLParser.new()
    parser.open("path/to/file.svg")
    while parser.read() != ERR_FILE_EOF:
        if parser.get_node_type() == XMLParser.NODE_ELEMENT:
            var node_name = parser.get_node_name()
            var attributes_dict = {}
            for idx in range(parser.get_attribute_count()):
                attributes_dict[parser.get_attribute_name(idx)] = parser.get_attribute_value(idx)
            print("The ", node_name, " element has the following attributes: ", attributes_dict)

```
```

    var parser = new XmlParser();
    parser.Open("path/to/file.svg");
    while (parser.Read() != Error.FileEof)
    {
        if (parser.GetNodeType() == XmlParser.NodeType.Element)
        {
            var nodeName = parser.GetNodeName();
            var attributesDict = new Godot.Collections.Dictionary();
            for (int idx = 0; idx < parser.GetAttributeCount(); idx++)
            {
                attributesDict[parser.GetAttributeName(idx)] = parser.GetAttributeValue(idx);
            }
            GD.Print($"The {nodeName} element has the following attributes: {attributesDict}");
        }
    }

### Methods


| [int](class_int.md#class_int) | [get_attribute_count](class_xmlparser.md#class_XMLParser_method_get_attribute_count) ( ) const |
| --- | --- |
| [String](class_string.md#class_String) | [get_attribute_name](class_xmlparser.md#class_XMLParser_method_get_attribute_name) ( idx: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_attribute_value](class_xmlparser.md#class_XMLParser_method_get_attribute_value) ( idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_current_line](class_xmlparser.md#class_XMLParser_method_get_current_line) ( ) const |
| [String](class_string.md#class_String) | [get_named_attribute_value](class_xmlparser.md#class_XMLParser_method_get_named_attribute_value) ( name: [String](class_string.md#class_String) ) const |
| [String](class_string.md#class_String) | [get_named_attribute_value_safe](class_xmlparser.md#class_XMLParser_method_get_named_attribute_value_safe) ( name: [String](class_string.md#class_String) ) const |
| [String](class_string.md#class_String) | [get_node_data](class_xmlparser.md#class_XMLParser_method_get_node_data) ( ) const |
| [String](class_string.md#class_String) | [get_node_name](class_xmlparser.md#class_XMLParser_method_get_node_name) ( ) const |
| [int](class_int.md#class_int) | [get_node_offset](class_xmlparser.md#class_XMLParser_method_get_node_offset) ( ) const |
| [NodeType](class_xmlparser.md#enum_XMLParser_NodeType) | [get_node_type](class_xmlparser.md#class_XMLParser_method_get_node_type) ( ) |
| [bool](class_bool.md#class_bool) | [has_attribute](class_xmlparser.md#class_XMLParser_method_has_attribute) ( name: [String](class_string.md#class_String) ) const |
| [bool](class_bool.md#class_bool) | [is_empty](class_xmlparser.md#class_XMLParser_method_is_empty) ( ) const |
| Error | [open](class_xmlparser.md#class_XMLParser_method_open) ( file: [String](class_string.md#class_String) ) |
| Error | [open_buffer](class_xmlparser.md#class_XMLParser_method_open_buffer) ( buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| Error | [read](class_xmlparser.md#class_XMLParser_method_read) ( ) |
| Error | [seek](class_xmlparser.md#class_XMLParser_method_seek) ( position: [int](class_int.md#class_int) ) |
| void | [skip_section](class_xmlparser.md#class_XMLParser_method_skip_section) ( ) |

---

### Enumerations

<span id="enum_XMLParser_NodeType"></span>

enum **NodeType**: [🔗](class_xmlparser.md#enum_XMLParser_NodeType)

<span id="class_XMLParser_constant_NODE_NONE"></span>

[NodeType](class_xmlparser.md#enum_XMLParser_NodeType) **NODE_NONE** = `0`

There's no node (no file or buffer opened).

<span id="class_XMLParser_constant_NODE_ELEMENT"></span>

[NodeType](class_xmlparser.md#enum_XMLParser_NodeType) **NODE_ELEMENT** = `1`

An element node type, also known as a tag, e.g. `<title>`.

<span id="class_XMLParser_constant_NODE_ELEMENT_END"></span>

[NodeType](class_xmlparser.md#enum_XMLParser_NodeType) **NODE_ELEMENT_END** = `2`

An end of element node type, e.g. `</title>`.

<span id="class_XMLParser_constant_NODE_TEXT"></span>

[NodeType](class_xmlparser.md#enum_XMLParser_NodeType) **NODE_TEXT** = `3`

A text node type, i.e. text that is not inside an element. This includes whitespace.

<span id="class_XMLParser_constant_NODE_COMMENT"></span>

[NodeType](class_xmlparser.md#enum_XMLParser_NodeType) **NODE_COMMENT** = `4`

A comment node type, e.g. `<!--A comment-->`.

<span id="class_XMLParser_constant_NODE_CDATA"></span>

[NodeType](class_xmlparser.md#enum_XMLParser_NodeType) **NODE_CDATA** = `5`

A node type for CDATA (Character Data) sections, e.g. `<![CDATA[CDATA section]]>`.

<span id="class_XMLParser_constant_NODE_UNKNOWN"></span>

[NodeType](class_xmlparser.md#enum_XMLParser_NodeType) **NODE_UNKNOWN** = `6`

An unknown node type.

---

### Method Descriptions

<span id="class_XMLParser_method_get_attribute_count"></span>

[int](class_int.md#class_int) **get_attribute_count** ( ) *const* [🔗](class_xmlparser.md#class_XMLParser_method_get_attribute_count)

Returns the number of attributes in the currently parsed element.

 **Note:** If this method is used while the currently parsed node is not [NODE_ELEMENT](class_xmlparser.md#class_XMLParser_constant_NODE_ELEMENT) or [NODE_ELEMENT_END](class_xmlparser.md#class_XMLParser_constant_NODE_ELEMENT_END), this count will not be updated and will still reflect the last element.

---

<span id="class_XMLParser_method_get_attribute_name"></span>

[String](class_string.md#class_String) **get_attribute_name** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_xmlparser.md#class_XMLParser_method_get_attribute_name)

Returns the name of an attribute of the currently parsed element, specified by the `idx` index.

---

<span id="class_XMLParser_method_get_attribute_value"></span>

[String](class_string.md#class_String) **get_attribute_value** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_xmlparser.md#class_XMLParser_method_get_attribute_value)

Returns the value of an attribute of the currently parsed element, specified by the `idx` index.

---

<span id="class_XMLParser_method_get_current_line"></span>

[int](class_int.md#class_int) **get_current_line** ( ) *const* [🔗](class_xmlparser.md#class_XMLParser_method_get_current_line)

Returns the current line in the parsed file, counting from 0.

---

<span id="class_XMLParser_method_get_named_attribute_value"></span>

[String](class_string.md#class_String) **get_named_attribute_value** ( name: [String](class_string.md#class_String) ) *const* [🔗](class_xmlparser.md#class_XMLParser_method_get_named_attribute_value)

Returns the value of an attribute of the currently parsed element, specified by its `name`. This method will raise an error if the element has no such attribute.

---

<span id="class_XMLParser_method_get_named_attribute_value_safe"></span>

[String](class_string.md#class_String) **get_named_attribute_value_safe** ( name: [String](class_string.md#class_String) ) *const* [🔗](class_xmlparser.md#class_XMLParser_method_get_named_attribute_value_safe)

Returns the value of an attribute of the currently parsed element, specified by its `name`. This method will return an empty string if the element has no such attribute.

---

<span id="class_XMLParser_method_get_node_data"></span>

[String](class_string.md#class_String) **get_node_data** ( ) *const* [🔗](class_xmlparser.md#class_XMLParser_method_get_node_data)

Returns the contents of a text node. This method will raise an error if the current parsed node is of any other type.

---

<span id="class_XMLParser_method_get_node_name"></span>

[String](class_string.md#class_String) **get_node_name** ( ) *const* [🔗](class_xmlparser.md#class_XMLParser_method_get_node_name)

Returns the name of a node. This method will raise an error if the currently parsed node is a text node.

 **Note:** The content of a [NODE_CDATA](class_xmlparser.md#class_XMLParser_constant_NODE_CDATA) node and the comment string of a [NODE_COMMENT](class_xmlparser.md#class_XMLParser_constant_NODE_COMMENT) node are also considered names.

---

<span id="class_XMLParser_method_get_node_offset"></span>

[int](class_int.md#class_int) **get_node_offset** ( ) *const* [🔗](class_xmlparser.md#class_XMLParser_method_get_node_offset)

Returns the byte offset of the currently parsed node since the beginning of the file or buffer. This is usually equivalent to the number of characters before the read position.

---

<span id="class_XMLParser_method_get_node_type"></span>

[NodeType](class_xmlparser.md#enum_XMLParser_NodeType) **get_node_type** ( ) [🔗](class_xmlparser.md#class_XMLParser_method_get_node_type)

Returns the type of the current node. Compare with [NodeType](class_xmlparser.md#enum_XMLParser_NodeType) constants.

---

<span id="class_XMLParser_method_has_attribute"></span>

[bool](class_bool.md#class_bool) **has_attribute** ( name: [String](class_string.md#class_String) ) *const* [🔗](class_xmlparser.md#class_XMLParser_method_has_attribute)

Returns `true` if the currently parsed element has an attribute with the `name`.

---

<span id="class_XMLParser_method_is_empty"></span>

[bool](class_bool.md#class_bool) **is_empty** ( ) *const* [🔗](class_xmlparser.md#class_XMLParser_method_is_empty)

Returns `true` if the currently parsed element is empty, e.g. `<element />`.

---

<span id="class_XMLParser_method_open"></span>

Error **open** ( file: [String](class_string.md#class_String) ) [🔗](class_xmlparser.md#class_XMLParser_method_open)

Opens an XML `file` for parsing. This method returns an error code.

---

<span id="class_XMLParser_method_open_buffer"></span>

Error **open_buffer** ( buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_xmlparser.md#class_XMLParser_method_open_buffer)

Opens an XML raw `buffer` for parsing. This method returns an error code.

---

<span id="class_XMLParser_method_read"></span>

Error **read** ( ) [🔗](class_xmlparser.md#class_XMLParser_method_read)

Parses the next node in the file. This method returns an error code.

---

<span id="class_XMLParser_method_seek"></span>

Error **seek** ( position: [int](class_int.md#class_int) ) [🔗](class_xmlparser.md#class_XMLParser_method_seek)

Moves the buffer cursor to a certain offset (since the beginning) and reads the next node there. This method returns an error code.

---

<span id="class_XMLParser_method_skip_section"></span>

void **skip_section** ( ) [🔗](class_xmlparser.md#class_XMLParser_method_skip_section)

Skips the current section. If the currently parsed node contains more inner nodes, they will be ignored and the cursor will go to the closing of the current element.
