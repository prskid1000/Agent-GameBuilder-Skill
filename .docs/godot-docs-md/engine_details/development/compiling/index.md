<span id="doc_compiling_index"></span>

## Building from source

.. highlight:: shell

Godot prides itself on being very easy to build, by C++ project standards.
[Godot uses the SCons build system](../../../about/faq.md#doc_faq_why_scons), and after the initial
setup compiling the engine for your current platform should be as easy as running:

::

    scons

But you will probably need to use at least some of the available options to configure
the build to match your specific needs, be it a custom engine fork, a lightweight build
stripped of extra modules, or an executable targeting engine development.

The articles below should help you navigate configuration options available, as well as
prerequisites required to compile Godot exactly the way you need.

.. rubric:: Basics of building Godot
   :heading-level: 2

Let's start with basics, and learn how to get Godot's source code, and then which options
to use to compile it regardless of your target platform.

- [Getting Source](getting_source.md)
- [Introduction To The Buildsystem](introduction_to_the_buildsystem.md)
.. rubric:: Building for target platforms
   :heading-level: 2

Below you can find instructions for compiling the engine for your specific target platform.
Note that Godot supports cross-compilation, which means you can compile it for a target platform
that doesn't match your current platform (say, target Linux while being on Windows). The guides
will try their best to cover all possible situations.

- [Compiling For Windows](compiling_for_windows.md)
- [Compiling For Linuxbsd](compiling_for_linuxbsd.md)
- [Compiling For Macos](compiling_for_macos.md)
- [Compiling For Android](compiling_for_android.md)
- [Compiling For Ios](compiling_for_ios.md)
- [Compiling For Visionos](compiling_for_visionos.md)
- [Compiling For Web](compiling_for_web.md)
- [Cross Compiling For Ios On Linux](cross-compiling_for_ios_on_linux.md)
.. rubric:: Other compilation targets and options
   :heading-level: 2

Some additional universal compilation options require further setup. Namely, while Godot
does have C#/.NET support as a part of its main codebase, it does not get compiled by
default to reduce the executable size for users who don't need C# for their projects.

Articles below explain how to configure the buildsystem for cases like this, and also
cover some optimization techniques.

- [Compiling With Dotnet](compiling_with_dotnet.md)
- [Compiling With Script Encryption Key](compiling_with_script_encryption_key.md)
- [Optimizing For Size](optimizing_for_size.md)
