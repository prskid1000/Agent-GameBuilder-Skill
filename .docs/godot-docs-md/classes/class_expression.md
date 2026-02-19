<span id="class_Expression"></span>

## Expression

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A class that stores an expression you can execute.

### Description

An expression can be made of any arithmetic operation, built-in math function call, method call of a passed instance, or built-in type construction call.

An example expression text using the built-in math functions could be `sqrt(pow(3, 2) + pow(4, 2))`.

In the following example we use a [LineEdit](class_lineedit.md#class_LineEdit) node to write our expression and show the result.

.. tabs::

```
```

    var expression = Expression.new()

    func _ready():
        $LineEdit.text_submitted.connect(self._on_text_submitted)

    func _on_text_submitted(command):
        var error = expression.parse(command)
        if error != OK:
            print(expression.get_error_text())
            return
        var result = expression.execute()
        if not expression.has_execute_failed():
            $LineEdit.text = str(result)

```
```

    private Expression _expression = new Expression();

    public override void _Ready()
    {
        GetNode<LineEdit>("LineEdit").TextSubmitted += OnTextEntered;
    }

    private void OnTextEntered(string command)
    {
        Error error = _expression.Parse(command);
        if (error != Error.Ok)
        {
            GD.Print(_expression.GetErrorText());
            return;
        }
        Variant result = _expression.Execute();
        if (!_expression.HasExecuteFailed())
        {
            GetNode<LineEdit>("LineEdit").Text = result.ToString();
        }
    }

### Tutorials

- [Evaluating Expressions](../tutorials/scripting/evaluating_expressions.md)

### Methods


| [Variant](class_variant.md#class_Variant) | [execute](class_expression.md#class_Expression_method_execute) ( inputs: [Array](class_array.md#class_Array) = [], base_instance: [Object](class_object.md#class_Object) = null, show_error: [bool](class_bool.md#class_bool) = true, const_calls_only: [bool](class_bool.md#class_bool) = false ) |
| --- | --- |
| [String](class_string.md#class_String) | [get_error_text](class_expression.md#class_Expression_method_get_error_text) ( ) const |
| [bool](class_bool.md#class_bool) | [has_execute_failed](class_expression.md#class_Expression_method_has_execute_failed) ( ) const |
| Error | [parse](class_expression.md#class_Expression_method_parse) ( expression: [String](class_string.md#class_String), input_names: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) = PackedStringArray() ) |

---

### Method Descriptions

<span id="class_Expression_method_execute"></span>

[Variant](class_variant.md#class_Variant) **execute** ( inputs: [Array](class_array.md#class_Array) = [], base_instance: [Object](class_object.md#class_Object) = null, show_error: [bool](class_bool.md#class_bool) = true, const_calls_only: [bool](class_bool.md#class_bool) = false ) [🔗](class_expression.md#class_Expression_method_execute)

Executes the expression that was previously parsed by [parse()](class_expression.md#class_Expression_method_parse) and returns the result. Before you use the returned object, you should check if the method failed by calling [has_execute_failed()](class_expression.md#class_Expression_method_has_execute_failed).

If you defined input variables in [parse()](class_expression.md#class_Expression_method_parse), you can specify their values in the inputs array, in the same order.

---

<span id="class_Expression_method_get_error_text"></span>

[String](class_string.md#class_String) **get_error_text** ( ) *const* [🔗](class_expression.md#class_Expression_method_get_error_text)

Returns the error text if [parse()](class_expression.md#class_Expression_method_parse) or [execute()](class_expression.md#class_Expression_method_execute) has failed.

---

<span id="class_Expression_method_has_execute_failed"></span>

[bool](class_bool.md#class_bool) **has_execute_failed** ( ) *const* [🔗](class_expression.md#class_Expression_method_has_execute_failed)

Returns `true` if [execute()](class_expression.md#class_Expression_method_execute) has failed.

---

<span id="class_Expression_method_parse"></span>

Error **parse** ( expression: [String](class_string.md#class_String), input_names: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) = PackedStringArray() ) [🔗](class_expression.md#class_Expression_method_parse)

Parses the expression and returns an Error code.

You can optionally specify names of variables that may appear in the expression with `input_names`, so that you can bind them when it gets executed.
