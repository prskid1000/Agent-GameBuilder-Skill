<span id="class_RandomNumberGenerator"></span>

## RandomNumberGenerator

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Provides methods for generating pseudo-random numbers.

### Description

RandomNumberGenerator is a class for generating pseudo-random numbers. It currently uses PCG32.

 **Note:** The underlying algorithm is an implementation detail and should not be depended upon.

To generate a random float number (within a given range) based on a time-dependent seed:

::

    var rng = RandomNumberGenerator.new()
    func _ready():
        var my_random_number = rng.randf_range(-10.0, 10.0)

### Tutorials

- [Random number generation](../tutorials/math/random_number_generation.md)

### Properties


| [int](class_int.md#class_int) | [seed](class_randomnumbergenerator.md#class_RandomNumberGenerator_property_seed) | `0` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [state](class_randomnumbergenerator.md#class_RandomNumberGenerator_property_state) | `0` |

### Methods


| [int](class_int.md#class_int) | [rand_weighted](class_randomnumbergenerator.md#class_RandomNumberGenerator_method_rand_weighted) ( weights: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) ) |
| --- | --- |
| [float](class_float.md#class_float) | [randf](class_randomnumbergenerator.md#class_RandomNumberGenerator_method_randf) ( ) |
| [float](class_float.md#class_float) | [randf_range](class_randomnumbergenerator.md#class_RandomNumberGenerator_method_randf_range) ( from: [float](class_float.md#class_float), to: [float](class_float.md#class_float) ) |
| [float](class_float.md#class_float) | [randfn](class_randomnumbergenerator.md#class_RandomNumberGenerator_method_randfn) ( mean: [float](class_float.md#class_float) = 0.0, deviation: [float](class_float.md#class_float) = 1.0 ) |
| [int](class_int.md#class_int) | [randi](class_randomnumbergenerator.md#class_RandomNumberGenerator_method_randi) ( ) |
| [int](class_int.md#class_int) | [randi_range](class_randomnumbergenerator.md#class_RandomNumberGenerator_method_randi_range) ( from: [int](class_int.md#class_int), to: [int](class_int.md#class_int) ) |
| void | [randomize](class_randomnumbergenerator.md#class_RandomNumberGenerator_method_randomize) ( ) |

---

### Property Descriptions

<span id="class_RandomNumberGenerator_property_seed"></span>

[int](class_int.md#class_int) **seed** = `0` [🔗](class_randomnumbergenerator.md#class_RandomNumberGenerator_property_seed)

- void **set_seed** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_seed** ( )

Initializes the random number generator state based on the given seed value. A given seed will give a reproducible sequence of pseudo-random numbers.

 **Note:** The RNG does not have an avalanche effect, and can output similar random streams given similar seeds. Consider using a hash function to improve your seed quality if they're sourced externally.

 **Note:** Setting this property produces a side effect of changing the internal [state](class_randomnumbergenerator.md#class_RandomNumberGenerator_property_state), so make sure to initialize the seed *before* modifying the [state](class_randomnumbergenerator.md#class_RandomNumberGenerator_property_state):

 **Note:** The default value of this property is pseudo-random, and changes when calling [randomize()](class_randomnumbergenerator.md#class_RandomNumberGenerator_method_randomize). The `0` value documented here is a placeholder, and not the actual default seed.

::

    var rng = RandomNumberGenerator.new()
    rng.seed = hash("Godot")
    rng.state = 100 # Restore to some previously saved state.

---

<span id="class_RandomNumberGenerator_property_state"></span>

[int](class_int.md#class_int) **state** = `0` [🔗](class_randomnumbergenerator.md#class_RandomNumberGenerator_property_state)

- void **set_state** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_state** ( )

The current state of the random number generator. Save and restore this property to restore the generator to a previous state:

::

    var rng = RandomNumberGenerator.new()
    print(rng.randf())
    var saved_state = rng.state # Store current state.
    print(rng.randf()) # Advance internal state.
    rng.state = saved_state # Restore the state.
    print(rng.randf()) # Prints the same value as previously.

 **Note:** Do not set state to arbitrary values, since the random number generator requires the state to have certain qualities to behave properly. It should only be set to values that came from the state property itself. To initialize the random number generator with arbitrary input, use [seed](class_randomnumbergenerator.md#class_RandomNumberGenerator_property_seed) instead.

 **Note:** The default value of this property is pseudo-random, and changes when calling [randomize()](class_randomnumbergenerator.md#class_RandomNumberGenerator_method_randomize). The `0` value documented here is a placeholder, and not the actual default state.

---

### Method Descriptions

<span id="class_RandomNumberGenerator_method_rand_weighted"></span>

[int](class_int.md#class_int) **rand_weighted** ( weights: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) ) [🔗](class_randomnumbergenerator.md#class_RandomNumberGenerator_method_rand_weighted)

Returns a random index with non-uniform weights. Prints an error and returns `-1` if the array is empty.

.. tabs::

```
```

    var rng = RandomNumberGenerator.new()

    var my_array = ["one", "two", "three", "four"]
    var weights = PackedFloat32Array([0.5, 1, 1, 2])

    # Prints one of the four elements in `my_array`.
    # It is more likely to print "four", and less likely to print "one".
    print(my_array[rng.rand_weighted(weights)])

---

<span id="class_RandomNumberGenerator_method_randf"></span>

[float](class_float.md#class_float) **randf** ( ) [🔗](class_randomnumbergenerator.md#class_RandomNumberGenerator_method_randf)

Returns a pseudo-random float between `0.0` and `1.0` (inclusive).

---

<span id="class_RandomNumberGenerator_method_randf_range"></span>

[float](class_float.md#class_float) **randf_range** ( from: [float](class_float.md#class_float), to: [float](class_float.md#class_float) ) [🔗](class_randomnumbergenerator.md#class_RandomNumberGenerator_method_randf_range)

Returns a pseudo-random float between `from` and `to` (inclusive).

---

<span id="class_RandomNumberGenerator_method_randfn"></span>

[float](class_float.md#class_float) **randfn** ( mean: [float](class_float.md#class_float) = 0.0, deviation: [float](class_float.md#class_float) = 1.0 ) [🔗](class_randomnumbergenerator.md#class_RandomNumberGenerator_method_randfn)

Returns a normally-distributed, pseudo-random floating-point number from the specified `mean` and a standard `deviation`. This is also known as a Gaussian distribution.

 **Note:** This method uses the Box-Muller transform algorithm.

---

<span id="class_RandomNumberGenerator_method_randi"></span>

[int](class_int.md#class_int) **randi** ( ) [🔗](class_randomnumbergenerator.md#class_RandomNumberGenerator_method_randi)

Returns a pseudo-random 32-bit unsigned integer between `0` and `4294967295` (inclusive).

---

<span id="class_RandomNumberGenerator_method_randi_range"></span>

[int](class_int.md#class_int) **randi_range** ( from: [int](class_int.md#class_int), to: [int](class_int.md#class_int) ) [🔗](class_randomnumbergenerator.md#class_RandomNumberGenerator_method_randi_range)

Returns a pseudo-random 32-bit signed integer between `from` and `to` (inclusive).

---

<span id="class_RandomNumberGenerator_method_randomize"></span>

void **randomize** ( ) [🔗](class_randomnumbergenerator.md#class_RandomNumberGenerator_method_randomize)

Sets up a time-based seed for this **RandomNumberGenerator** instance. Unlike the @GlobalScope random number generation functions, different **RandomNumberGenerator** instances can use different seeds.
