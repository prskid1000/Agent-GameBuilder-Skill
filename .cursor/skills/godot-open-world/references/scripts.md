# All Scripts — Full Source + Line-by-Line Comments

Based on `.examples/godot-craft/scripts/`. All scripts are exact source from the example.

---

## face.gd

```gdscript
class_name Face
# Static utility class — no extends, never instantiated.
# Provides the 6 face directions as Vector3i for use in block meshing and neighbor lookups.

enum Type {
    FORWARD,  # -Z (Godot's "forward" is -Z in 3D)
    BACK,     # +Z
    LEFT,     # -X
    RIGHT,    # +X
    UP,       # +Y
    DOWN,     # -Y
    COUNT,    # total number of face types (6); used for iteration
}

# Maps each Face.Type to its Vector3i direction
static var _VECTORS = [
    Vector3i.BACK,      # FORWARD (-Z in Godot = Vector3i(0,0,-1))
    Vector3i.FORWARD,   # BACK    (+Z)
    Vector3i.LEFT,      # LEFT    (-X)
    Vector3i.RIGHT,     # RIGHT   (+X)
    Vector3i.UP,        # UP      (+Y)
    Vector3i.DOWN       # DOWN    (-Y)
]

static func get_vector(face: Type) -> Vector3i:
    return _VECTORS[face]
```

---

## block.gd

```gdscript
class_name Block
# Static utility class — all methods and data are static.
# Defines block types, their vertex data, texture coordinates, transparency,
# light emission, and face exposure rules.

enum Type {
    GRASS,       # 0 — top=grass, sides=grass-side, bottom=dirt
    DIRT,        # 1
    STONE,       # 2
    WATER,       # 3 — transparent
    LOG,         # 4 — top/bottom=log-top, sides=log-side
    LEAVES,      # 5
    SAND,        # 6
    BUSH,        # 7 — sprite (cross shape, no collision)
    POPPY,       # 8 — sprite
    DANDELION,   # 9 — sprite
    DAISY,       # 10 — sprite
    CORNFLOWER,  # 11 — sprite
    MARIGOLD,    # 12 — sprite
    LAVENDER,    # 13 — sprite
    RED_TORCH,   # 14 — sprite + OmniLight3D
    YELLOW_TORCH,# 15 — sprite + OmniLight3D
    GREEN_TORCH, # 16 — sprite + OmniLight3D
    BLUE_TORCH,  # 17 — sprite + OmniLight3D
    CYAN_TORCH,  # 18 — sprite + OmniLight3D
    MAGENTA_TORCH,# 19 — sprite + OmniLight3D
    WHITE_TORCH, # 20 — sprite + OmniLight3D
    PLANKS,      # 21
    GLASS,       # 22 — transparent
    COUNT,       # 23 — sentinel: total non-EMPTY block types
    EMPTY,       # 24 — air / no block
}

static var _INDICES = PackedInt32Array([0, 1, 2, 0, 2, 3])
# Two triangles per face quad: (0,1,2) and (0,2,3)

static var _TORCH_LIGHT_STRENGTH = Vector3(5, 0.02, 1.0)
# x=omni_range, y=omni_attenuation, z=light_energy

# Cube face vertices — 6 faces × 4 vertices, in face order (FORWARD,BACK,LEFT,RIGHT,UP,DOWN)
# Each Vector3 is a corner of the unit cube [0..1]^3
static var _VERTICES = PackedVector3Array([
    # FORWARD face (+Z)
    Vector3(0,1,1), Vector3(1,1,1), Vector3(1,0,1), Vector3(0,0,1),
    # BACK face (-Z)
    Vector3(1,1,0), Vector3(0,1,0), Vector3(0,0,0), Vector3(1,0,0),
    # LEFT face (-X)
    Vector3(0,1,0), Vector3(0,1,1), Vector3(0,0,1), Vector3(0,0,0),
    # RIGHT face (+X)
    Vector3(1,1,1), Vector3(1,1,0), Vector3(1,0,0), Vector3(1,0,1),
    # UP face (+Y)
    Vector3(0,1,0), Vector3(1,1,0), Vector3(1,1,1), Vector3(0,1,1),
    # DOWN face (-Y)
    Vector3(0,0,1), Vector3(1,0,1), Vector3(1,0,0), Vector3(0,0,0)
])

# UV within each face tile (same for all cube faces)
static var _TEXCOORDS = PackedVector2Array([
    # 6 faces × 4 vertices: same pattern but mirrored for back/left
    Vector2(0,0), Vector2(1,0), Vector2(1,1), Vector2(0,1),  # FORWARD
    Vector2(1,0), Vector2(0,0), Vector2(0,1), Vector2(1,1),  # BACK
    Vector2(0,0), Vector2(1,0), Vector2(1,1), Vector2(0,1),  # LEFT
    Vector2(0,0), Vector2(1,0), Vector2(1,1), Vector2(0,1),  # RIGHT
    Vector2(0,0), Vector2(1,0), Vector2(1,1), Vector2(0,1),  # UP
    Vector2(0,0), Vector2(1,0), Vector2(1,1), Vector2(0,1),  # DOWN
])

# Cross-sprite vertices — 4 "faces" × 4 verts (two diagonals, both sides)
static var _SPRITE_VERTICES = PackedVector3Array([
    Vector3(0,1,1), Vector3(1,1,0), Vector3(1,0,0), Vector3(0,0,1),
    Vector3(1,1,0), Vector3(0,1,1), Vector3(0,0,1), Vector3(1,0,0),
    Vector3(1,1,1), Vector3(0,1,0), Vector3(0,0,0), Vector3(1,0,1),
    Vector3(0,1,0), Vector3(1,1,1), Vector3(1,0,1), Vector3(0,0,0),
])

static var _SPRITE_TEXCOORDS = PackedVector2Array([
    Vector2(0,0), Vector2(1,0), Vector2(1,1), Vector2(0,1),
    Vector2(0,0), Vector2(1,0), Vector2(1,1), Vector2(0,1),
    Vector2(1,0), Vector2(0,0), Vector2(0,1), Vector2(1,1),
    Vector2(0,0), Vector2(1,0), Vector2(1,1), Vector2(0,1),
])

static var _SPRITE_NORMALS = PackedVector3Array([
    Vector3(0,1,0), Vector3(0,1,0), Vector3(0,1,0), Vector3(0,1,0),
])

static func get_indices() -> PackedInt32Array:
    return _INDICES

static func get_vertex(_type: Type, face: Face.Type, index: int) -> Vector3:
    if is_sprite(_type):
        return _SPRITE_VERTICES[face * 4 + index]
    return _VERTICES[face * 4 + index]

static func get_texcoord2(_type: Type, face: Face.Type, index: int) -> Vector2:
    # UV2 = per-vertex in-tile UV (used in shader to sample within tile)
    if is_sprite(_type):
        return _SPRITE_TEXCOORDS[face * 4 + index]
    return _TEXCOORDS[face * 4 + index]

static func get_normal(_type: Type, face: Face.Type) -> Vector3i:
    if is_sprite(_type):
        return _SPRITE_NORMALS[face]
    return Face.get_vector(face)

static func get_texcoord(type: Type, face: Face.Type) -> Vector2:
    # Returns the spritesheet TILE coordinate (column, row) for this block+face.
    # The shader uses UV (tile coord) + UV2 (in-tile UV) to sample the Texture2DArray.
    match type:
        Type.GRASS:
            match face:
                Face.Type.UP:   return Vector2(0, 0)   # grass top
                Face.Type.DOWN: return Vector2(1, 0)   # dirt bottom
                _:              return Vector2(2, 0)   # grass side
        Type.DIRT:        return Vector2(1, 0)
        Type.STONE:       return Vector2(3, 0)
        Type.WATER:       return Vector2(4, 0)
        Type.LOG:
            match face:
                Face.Type.UP, Face.Type.DOWN: return Vector2(5, 0)  # log end
                _:                             return Vector2(6, 0)  # log bark
        Type.LEAVES:      return Vector2(7, 0)
        Type.SAND:        return Vector2(8, 0)
        Type.BUSH:        return Vector2(9, 0)
        Type.POPPY:       return Vector2(10, 0)
        Type.DANDELION:   return Vector2(11, 0)
        Type.DAISY:       return Vector2(12, 0)
        Type.CORNFLOWER:  return Vector2(13, 0)
        Type.MARIGOLD:    return Vector2(14, 0)
        Type.LAVENDER:    return Vector2(15, 0)
        Type.YELLOW_TORCH: return Vector2(0, 1)
        Type.RED_TORCH:    return Vector2(1, 1)
        Type.BLUE_TORCH:   return Vector2(2, 1)
        Type.GREEN_TORCH:  return Vector2(3, 1)
        Type.CYAN_TORCH:   return Vector2(4, 1)
        Type.MAGENTA_TORCH:return Vector2(5, 1)
        Type.WHITE_TORCH:  return Vector2(6, 1)
        Type.PLANKS:       return Vector2(7, 1)
        Type.GLASS:        return Vector2(8, 1)
    return Vector2.ZERO

static func is_transparent(type: Type) -> bool:
    match type:
        Type.WATER, Type.GLASS: return true
    return false

static func is_sprite(type: Type) -> bool:
    # Cross-sprite blocks have no cube geometry; rendered as two crossing quads
    match type:
        Type.BUSH, Type.POPPY, Type.DANDELION, Type.DAISY,
        Type.CORNFLOWER, Type.MARIGOLD, Type.LAVENDER,
        Type.YELLOW_TORCH, Type.RED_TORCH, Type.BLUE_TORCH,
        Type.GREEN_TORCH, Type.CYAN_TORCH, Type.MAGENTA_TORCH,
        Type.WHITE_TORCH:
            return true
    return false

static func is_light(type: Type) -> bool:
    match type:
        Type.YELLOW_TORCH, Type.RED_TORCH, Type.BLUE_TORCH,
        Type.GREEN_TORCH, Type.CYAN_TORCH, Type.MAGENTA_TORCH,
        Type.WHITE_TORCH:
            return true
    return false

static func get_light_color(type: Type) -> Color:
    match type:
        Type.YELLOW_TORCH:  return Color(1.0, 1.0, 0.0)
        Type.RED_TORCH:     return Color(1.0, 0.0, 0.0)
        Type.BLUE_TORCH:    return Color(0.0, 0.0, 1.0)
        Type.GREEN_TORCH:   return Color(0.0, 1.0, 0.0)
        Type.CYAN_TORCH:    return Color(0.0, 1.0, 1.0)
        Type.MAGENTA_TORCH: return Color(1.0, 0.0, 1.0)
        Type.WHITE_TORCH:   return Color(1.0, 1.0, 1.0)
    return Color()

static func get_light_strength(type: Type) -> Vector3:
    # Returns Vector3(omni_range, omni_attenuation, light_energy)
    if is_light(type):
        return _TORCH_LIGHT_STRENGTH   # Vector3(5, 0.02, 1.0)
    return Vector3.ZERO

static func is_exposed(lhs: Type, rhs: Type) -> bool:
    # Should the lhs face adjacent to rhs be rendered?
    assert(lhs != Type.EMPTY)
    assert(!is_sprite(lhs))
    if rhs == Type.EMPTY or is_sprite(rhs):
        return true   # air or sprite neighbor = always draw this face
    if not is_transparent(lhs) and is_transparent(rhs):
        return true   # opaque next to transparent = draw (see through water)
    return false      # same-type or opaque-opaque = culled
```

---

## resources.gd

```gdscript
extends Node
# Autoload: GDCraftResources
# Runs before any scene. Slices spritesheet.png into a Texture2DArray and
# creates the three ShaderMaterials shared by all chunk MeshInstance3D nodes.

const SPRITESHEET = preload("res://resources/spritesheet.png")
const OPAQUE_SHADER = preload("res://resources/opaque.gdshader")
const TRANSPARENT_SHADER = preload("res://resources/transparent.gdshader")
const SPRITE_SHADER = preload("res://resources/sprite.gdshader")
const SIZE = 16  # tile size in pixels

var opaque_material: ShaderMaterial = null
var transparent_material: ShaderMaterial = null
var sprite_material: ShaderMaterial = null

func _ready() -> void:
    var spritesheet = _create_spritesheet()
    # Create one ShaderMaterial per mesh type; all share the same Texture2DArray
    opaque_material = ShaderMaterial.new()
    opaque_material.shader = OPAQUE_SHADER
    opaque_material.set_shader_parameter("spritesheet", spritesheet)
    opaque_material.render_priority = 0

    transparent_material = ShaderMaterial.new()
    transparent_material.shader = TRANSPARENT_SHADER
    transparent_material.set_shader_parameter("spritesheet", spritesheet)
    transparent_material.render_priority = 1  # render after opaque

    sprite_material = ShaderMaterial.new()
    sprite_material.shader = SPRITE_SHADER
    sprite_material.set_shader_parameter("spritesheet", spritesheet)
    sprite_material.render_priority = 0

func _create_spritesheet() -> Texture2DArray:
    var image = SPRITESHEET.get_image()
    if image.is_compressed():
        image.decompress()
    var columns = image.get_width() / SIZE    # number of tile columns
    var rows = image.get_height() / SIZE      # number of tile rows
    var images = []
    for y in range(rows):
        for x in range(columns):
            # Extract each SIZE×SIZE tile as a separate Image layer
            var layer = Image.create_empty(SIZE, SIZE, true, image.get_format())
            for i in range(SIZE):
                for j in range(SIZE):
                    var color = image.get_pixel(x * SIZE + i, y * SIZE + j)
                    layer.set_pixel(i, j, color)
            layer.generate_mipmaps()
            images.append(layer)
    var texture_array = Texture2DArray.new()
    texture_array.create_from_images(images)
    return texture_array
```

---

## generator.gd

```gdscript
class_name Generator
extends Node

enum Type {
    NOISE,      # Default: heightmap terrain with trees and foliage
    SUPERFLAT,  # Flat 5-layer world (stone×3, dirt, grass)
    DEBUG,      # Single block at (0,0,0) for testing mesh
}

@export var type = Type.NOISE
@export var generator_seed = 1337

var _base_generator := FastNoiseLite.new()
    # Low-frequency (0.01) simplex — controls broad terrain height
var _overlay_generator := FastNoiseLite.new()
    # Higher-frequency (0.1) simplex — adds local variation
var _foliage_generator := FastNoiseLite.new()
    # Spatially coherent noise for foliage placement decisions
var _tree_generator := FastNoiseLite.new()
    # Determines tree heights and placement fine-grain randomness

func _init() -> void:
    _base_generator.seed = generator_seed * 13
    _base_generator.noise_type = FastNoiseLite.TYPE_SIMPLEX
    _base_generator.frequency = 0.01
    _overlay_generator.seed = generator_seed * 79
    _overlay_generator.noise_type = FastNoiseLite.TYPE_SIMPLEX
    _overlay_generator.frequency = 0.1
    _foliage_generator.seed = generator_seed * 53
    _foliage_generator.noise_type = FastNoiseLite.TYPE_SIMPLEX
    _foliage_generator.frequency = 0.05
    _tree_generator.seed = generator_seed * 139
    _tree_generator.noise_type = FastNoiseLite.TYPE_SIMPLEX
    _tree_generator.frequency = 0.05

func generate(index: Vector3i) -> Dictionary[Vector3i, Block.Type]:
    var blocks: Dictionary[Vector3i, Block.Type] = {}
    match type:
        Type.NOISE:      _noise(index, blocks)
        Type.SUPERFLAT:  _superflat(index, blocks)
        Type.DEBUG:      _debug(index, blocks)
    assert(not blocks.is_empty())
    return blocks

func _noise(index: Vector3i, blocks: Dictionary[Vector3i, Block.Type]) -> void:
    var sea_level = 10
    var start_y = index.y * Chunk.HEIGHT  # vertical offset for this chunk row
    for x in range(0, Chunk.WIDTH):
        for z in range(0, Chunk.WIDTH):
            var block_x = index.x * Chunk.WIDTH + x  # world X
            var block_z = index.z * Chunk.WIDTH + z  # world Z
            # Height from noise: [0..1] → non-linear power curve → integer height
            var base_noise = (_base_generator.get_noise_2d(block_x, block_z) + 1.0) * 0.5
            var overlay_noise = (_overlay_generator.get_noise_2d(block_x, block_z) + 1.0) * 0.5
            var noise = int(pow(base_noise * 5, 1.25) * 5 + overlay_noise * 2)
            var end_y = min(start_y + Chunk.HEIGHT, max(noise, sea_level))
            for y in range(start_y, end_y):
                var block_index = Vector3i(x, y - start_y, z)
                assert(Chunk.in_bounds(block_index))
                if y > noise:
                    blocks[block_index] = Block.Type.WATER       # below sea, above terrain
                elif (noise >= sea_level - 1 and noise < sea_level + overlay_noise * 2) \
                    or (y > noise - 2 and noise <= sea_level):
                    blocks[block_index] = Block.Type.SAND        # beach / underwater surface
                elif y > 20 + overlay_noise * 2:
                    blocks[block_index] = Block.Type.STONE       # high altitude = stone
                elif y == noise - 1:
                    blocks[block_index] = Block.Type.GRASS       # surface layer
                    # Decide: tree (rare) or foliage (common)
                    var foliage_noise = _foliage_generator.get_noise_2d(block_x, block_z)
                    var foliage_value = int(foliage_noise * 13793) % 100
                    if foliage_value < 2 and _tree_in_bounds(x, z):
                        _tree(blocks, x, noise - start_y, z)
                    else:
                        _foliage(blocks, block_index + Vector3i.UP, foliage_value)
                elif y > noise - 4:
                    blocks[block_index] = Block.Type.DIRT        # shallow sub-surface
                else:
                    blocks[block_index] = Block.Type.STONE       # deep = stone

func _tree(blocks: Dictionary[Vector3i, Block.Type], x: int, y: int, z: int) -> void:
    # Tree height: 4–8 blocks (noise-derived)
    var height = int((_tree_generator.get_noise_2d(x, z) + 1.0) * 2.0) + 4
    for i in range(height):
        var index = Vector3i(x, y + i, z)
        if Chunk.in_bounds(index):
            blocks[index] = Block.Type.LOG
    # Leaves: sphere of radius 3 (manhattan) centered at top of trunk - 2
    for lx in range(-2, 3):
        for ly in range(-2, 3):
            for lz in range(-2, 3):
                if abs(lx) + abs(ly) + abs(lz) > 3:
                    continue
                var index = Vector3i(x + lx, y + height - 2 + ly, z + lz)
                if Chunk.in_bounds(index) and index not in blocks:
                    blocks[index] = Block.Type.LEAVES

func _foliage(blocks: Dictionary[Vector3i, Block.Type], index: Vector3i, value: int) -> void:
    # value is in [0,100); different ranges map to different plants
    if value > 10 and value < 50:   blocks[index] = Block.Type.BUSH
    elif value > 50 and value < 53: blocks[index] = Block.Type.POPPY
    elif value > 56 and value < 59: blocks[index] = Block.Type.DANDELION
    elif value > 62 and value < 65: blocks[index] = Block.Type.DAISY
    elif value > 68 and value < 71: blocks[index] = Block.Type.CORNFLOWER
    elif value > 74 and value < 77: blocks[index] = Block.Type.MARIGOLD
    elif value > 80 and value < 83: blocks[index] = Block.Type.LAVENDER

func _tree_in_bounds(x: int, z: int) -> bool:
    # Keep trees at least 2 blocks from chunk edge (leaves would overflow)
    return x > 1 and z > 1 and x < Chunk.SIZE.x - 2 and z < Chunk.SIZE.z - 2

func _superflat(_index: Vector3i, _blocks: Dictionary[Vector3i, Block.Type]) -> void:
    if _index.y != 0:
        return
    for x in range(Chunk.WIDTH):
        for y in range(Chunk.WIDTH):
            _blocks[Vector3i(x, 0, y)] = Block.Type.STONE
            _blocks[Vector3i(x, 1, y)] = Block.Type.STONE
            _blocks[Vector3i(x, 2, y)] = Block.Type.STONE
            _blocks[Vector3i(x, 3, y)] = Block.Type.DIRT
            _blocks[Vector3i(x, 4, y)] = Block.Type.GRASS

func _debug(_index: Vector3i, _blocks: Dictionary[Vector3i, Block.Type]) -> void:
    _blocks[Vector3i(0, 0, 0)] = Block.Type.GRASS
```

---

## database.gd

```gdscript
class_name Database
extends Node
# Handles all SQLite persistence using the godot-sqlite GDExtension.
# Thread-safe: all queries use a Mutex (chunk generation runs on WorkerThreadPool).

@export var path = "user://gdcraft.sqlite"
var _database: SQLite = null
var _mutex = Mutex.new()

func _init() -> void:
    _database = SQLite.new()
    _database.path = path
    _database.verbosity_level = SQLite.VerbosityLevel.NORMAL
    if not _database.open_db():
        push_error("Failed to open database: " + path)

    # Table: blocks — stores only player-edited blocks (not all procedural ones)
    # Primary key on all 6 coordinates (chunk + local block position)
    _database.query("""
        CREATE TABLE IF NOT EXISTS blocks (
            chunk_x INTEGER NOT NULL, chunk_y INTEGER NOT NULL, chunk_z INTEGER NOT NULL,
            block_x INTEGER NOT NULL, block_y INTEGER NOT NULL, block_z INTEGER NOT NULL,
            type INTEGER NOT NULL,
            PRIMARY KEY (chunk_x, chunk_y, chunk_z, block_x, block_y, block_z)
        );
    """)
    _database.query("""
        CREATE INDEX IF NOT EXISTS blocks_index ON blocks (chunk_x, chunk_y, chunk_z);
    """)

    # Table: players — position and rotation per player ID
    _database.query("""
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY,
            position_x INTEGER NOT NULL, position_y INTEGER NOT NULL, position_z INTEGER NOT NULL,
            rotation_x INTEGER NOT NULL, rotation_y INTEGER NOT NULL, rotation_z INTEGER NOT NULL
        );
    """)
    _database.query("CREATE INDEX IF NOT EXISTS players_index ON players (id);")

    # Table: sky — persists time_of_day so day cycle continues after restart
    _database.query("""
        CREATE TABLE IF NOT EXISTS sky (
            id INTEGER PRIMARY KEY,
            time_of_day INTEGER NOT NULL
        );
    """)
    _database.query("CREATE INDEX IF NOT EXISTS sky_index ON sky (id);")

func _notification(what: int) -> void:
    if what == NOTIFICATION_PREDELETE:
        _mutex.lock()
        _database.close_db()
        _database = null
        _mutex.unlock()

func set_block(chunk: Vector3i, block: Vector3i, type: Block.Type) -> void:
    _mutex.lock()
    if _database == null: _mutex.unlock(); return
    if type == Block.Type.EMPTY:
        # DELETE row when block is removed
        _database.query_with_bindings("""
            DELETE FROM blocks
            WHERE chunk_x=? AND chunk_y=? AND chunk_z=?
              AND block_x=? AND block_y=? AND block_z=?;
        """, [chunk.x, chunk.y, chunk.z, block.x, block.y, block.z])
    else:
        # UPSERT: insert or update if this block position already has a record
        _database.query_with_bindings("""
            INSERT INTO blocks
            (chunk_x, chunk_y, chunk_z, block_x, block_y, block_z, type)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(chunk_x, chunk_y, chunk_z, block_x, block_y, block_z)
            DO UPDATE SET type = excluded.type;
        """, [chunk.x, chunk.y, chunk.z, block.x, block.y, block.z, type])
    _mutex.unlock()

func get_blocks(chunk: Vector3i) -> Array:
    # Called from worker thread — must be mutex-protected
    _mutex.lock()
    if _database == null: _mutex.unlock(); return []
    _database.query_with_bindings("""
        SELECT block_x, block_y, block_z, type FROM blocks
        WHERE chunk_x=? AND chunk_y=? AND chunk_z=?;
    """, [chunk.x, chunk.y, chunk.z])
    var result = _database.query_result.duplicate(true)
    _mutex.unlock()
    return result

func save_player(player: Player, id: int) -> void:
    _mutex.lock()
    if _database == null: _mutex.unlock(); return
    _database.query_with_bindings("""
        INSERT INTO players
        (position_x, position_y, position_z, rotation_x, rotation_y, rotation_z, id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(id) DO UPDATE SET
            position_x = excluded.position_x, position_y = excluded.position_y,
            position_z = excluded.position_z, rotation_x = excluded.rotation_x,
            rotation_y = excluded.rotation_y, rotation_z = excluded.rotation_z;
    """, [player.position.x, player.position.y, player.position.z,
          player.rotation.x, player.rotation.y, player.rotation.z, id])
    _mutex.unlock()

func load_player(player: Player, id: int) -> void:
    _mutex.lock()
    if _database == null: _mutex.unlock(); return
    _database.query_with_bindings(
        "SELECT position_x, position_y, position_z, rotation_x, rotation_y, rotation_z FROM players WHERE id = ?;",
        [id])
    var result = _database.query_result
    if not result.is_empty():
        result = result[0]
        player.position = Vector3(result.position_x, result.position_y, result.position_z)
        player.rotation = Vector3(result.rotation_x, result.rotation_y, result.rotation_z)
    _mutex.unlock()

func save_sky(sky: GDCraftSky) -> void:
    _mutex.lock()
    if _database == null: _mutex.unlock(); return
    _database.query_with_bindings("""
        INSERT INTO sky (time_of_day, id) VALUES (?, ?)
        ON CONFLICT(id) DO UPDATE SET time_of_day = excluded.time_of_day;
    """, [sky.time_of_day, 0])
    _mutex.unlock()

func load_sky(sky: GDCraftSky) -> void:
    _mutex.lock()
    if _database == null: _mutex.unlock(); return
    _database.query_with_bindings("SELECT time_of_day FROM sky WHERE id = ?;", [0])
    var result = _database.query_result
    if not result.is_empty():
        sky.time_of_day = result[0].time_of_day
    _mutex.unlock()
```

---

## chunk.gd

```gdscript
class_name Chunk
extends StaticBody3D
# Represents one 10×128×10 chunk of the world.
# Lifecycle: NONE → GENERATING → GENERATED → MESHING → MESHED.
# Generation and meshing run on WorkerThreadPool threads.

const WIDTH = 10
const HEIGHT = 128
const SIZE = Vector3i(WIDTH, HEIGHT, WIDTH)

enum Flag {
    NONE       = 0,
    GENERATING = 0b00000001,  # currently running _generate on worker thread
    GENERATED  = 0b00000010,  # _generate finished; block data is valid
    EXPOSED    = 0b00000100,  # _expose() has been run; _exposed_blocks is valid
    MESHING    = 0b00001000,  # currently running _mesh on worker thread
    MESHED     = 0b00010000,  # mesh is built and added to scene
    WORKING    = GENERATING | MESHING,  # mask: is any async task running?
}

enum MeshType {
    OPAQUE,       # solid blocks
    TRANSPARENT,  # water, glass
    SPRITE,       # cross-shaped plants and torches
    COUNT,
}

var _world = null         # reference to World node
var _index: Vector3i      # chunk grid index (not world position)
var _flags = Flag.NONE
var _all_blocks: Dictionary[Vector3i, Block.Type] = {}     # all solid blocks in chunk
var _exposed_blocks: Dictionary[Vector3i, bool] = {}       # subset: blocks with visible faces
var _lights: Dictionary[Vector3i, OmniLight3D] = {}        # torch lights by block index

func _init(world, index: Vector3i) -> void:
    _world = world
    _index = index

# --- Flag helpers ---
func set_flag(flag: Flag) -> void:   _flags = (_flags | flag) as Flag
func clear_flag(flag: Flag) -> void: _flags = (_flags & ~flag) as Flag
func has_flag(flag: Flag) -> bool:   return _flags & flag

static func in_bounds(index: Vector3i) -> bool:
    return index.x >= 0 and index.x < SIZE.x \
        and index.y >= 0 and index.y < SIZE.y \
        and index.z >= 0 and index.z < SIZE.z

func get_block(index: Vector3i) -> Block.Type:
    assert(in_bounds(index))
    return _all_blocks.get(index, Block.Type.EMPTY)

func _get_local_position(index: Vector3i) -> Vector3i:
    # Wrap index into [0, SIZE) using modular arithmetic
    return (index % SIZE + SIZE) % SIZE

func _get_block(index: Vector3i, face: Vector3i) -> Block.Type:
    # Get block at (index + face), crossing into neighbor chunk if needed
    index += face
    if in_bounds(index):
        return get_block(index)
    assert(face.y != -1)     # should never query below chunk floor
    if face.y == 1:
        return Block.Type.EMPTY   # above chunk top = air
    var neighbor_chunk_index = _index + face
    var neighbor_chunk = _world.get_chunk(neighbor_chunk_index)
    assert(neighbor_chunk.has_flag(Flag.GENERATED))
    var neighbor_index = _get_local_position(index)
    return neighbor_chunk.get_block(neighbor_index)

func _expose_neighbor(index: Vector3i, face: Vector3i) -> void:
    # Mark the neighbor chunk's block adjacent to this chunk as exposed
    assert(in_bounds(index))
    index += face
    assert(not in_bounds(index))
    if face.y != 0: return   # only horizontal neighbors
    var neighbor_chunk = _world.get_chunk(_index + face)
    assert(not neighbor_chunk.has_flag(Flag.WORKING))
    assert(neighbor_chunk.has_flag(Flag.GENERATED))
    var neighbor_index = _get_local_position(index)
    if neighbor_chunk.get_block(neighbor_index) != Block.Type.EMPTY:
        neighbor_chunk._exposed_blocks[neighbor_index] = false

func _exposed(index: Vector3i) -> bool:
    # Is this block's geometry visible (has at least one exposed face)?
    assert(in_bounds(index))
    var block = _all_blocks.get(index, Block.Type.EMPTY)
    if block == Block.Type.EMPTY: return false
    if Block.is_sprite(block): return true   # sprites always drawn
    for face in range(Face.Type.COUNT):
        if _skip_face(index, face): continue
        var vector = Face.get_vector(face)
        var neighbor_block = _get_block(index, vector)
        if Block.is_exposed(block, neighbor_block):
            _exposed_blocks[index] = false
            return true
    return false

func set_block(index: Vector3i, type: Block.Type) -> void:
    # Called on main thread after player places/breaks a block
    assert(has_flag(Flag.GENERATED) and has_flag(Flag.EXPOSED) and has_flag(Flag.MESHED))
    assert(not has_flag(Flag.WORKING))
    assert(in_bounds(index))
    if type == Block.Type.EMPTY:
        _all_blocks.erase(index)
    else:
        _all_blocks[index] = type
    # Update exposure for this block and all 6 neighbors
    if _exposed(index): _exposed_blocks[index] = false
    else: _exposed_blocks.erase(index)
    for face in range(Face.Type.COUNT):
        var vector = Face.get_vector(face)
        var neighbor_index = index + vector
        if not in_bounds(neighbor_index):
            _expose_neighbor(index, vector)
            continue
        _exposed_blocks.erase(neighbor_index)
        if _exposed(neighbor_index):
            _exposed_blocks[neighbor_index] = false
    set_light(index, type)
    clear_flag(Chunk.Flag.MESHED)   # triggers remesh in World._remesh()

func set_light(index: Vector3i, type: Block.Type) -> void:
    # Add/remove OmniLight3D for torch blocks
    var light = _lights.get(index, null)
    if light: remove_child(light); _lights.erase(index)
    if not Block.is_light(type): return
    light = OmniLight3D.new()
    light.light_color = Block.get_light_color(type)
    light.position = Vector3(_index * SIZE + index) + Vector3.ONE / 2
    var strength = Block.get_light_strength(type)
    light.omni_range = strength.x
    light.omni_attenuation = strength.y
    light.light_energy = strength.z
    add_child.call_deferred(light)
    _lights[index] = light

func generate() -> void:
    # Kick off async terrain generation
    assert(not has_flag(Flag.GENERATED) and not has_flag(Flag.WORKING))
    set_flag(Flag.GENERATING)
    var task_id = WorkerThreadPool.add_task(_generate)
    _world.add_task_id(task_id)

func mesh(async: bool, force = false) -> void:
    # Build mesh. If async=true, runs on worker thread.
    assert(has_flag(Flag.GENERATED) and not has_flag(Flag.WORKING))
    if force and has_flag(Flag.MESHED): clear_flag(Flag.MESHED)
    assert(not has_flag(Flag.MESHED))
    # Remove old mesh children (keep OmniLight3D nodes)
    for child in get_children():
        if child is OmniLight3D: continue
        remove_child(child); child.queue_free()
    set_flag(Flag.MESHING)
    if not async: _mesh(); return
    var task_id = WorkerThreadPool.add_task(_mesh)
    _world.add_task_id(task_id)

func _generate() -> void:
    # Worker thread: call generator, then apply saved player edits from DB
    _all_blocks = _world.generator.generate(_index)
    var blocks = _world.database.get_blocks(_index)  # player-edited blocks
    for block in blocks:
        assert(block.type != Block.Type.EMPTY)
        var index = Vector3i(block.block_x, block.block_y, block.block_z)
        assert(in_bounds(index))
        _all_blocks[index] = block.type
        set_light(index, block.type)
    _end_generate.call_deferred(WorkerThreadPool.get_caller_task_id())

func _mesh() -> void:
    # Worker thread: build ArrayMesh geometry for all three mesh types
    if not has_flag(Flag.EXPOSED): _expose()
    var _meshes = []
    for _type in range(MeshType.COUNT):
        _meshes.append(_create_mesh_arrays())
    for index in _exposed_blocks:
        var block = _all_blocks.get(index, Block.Type.EMPTY)
        assert(block != Block.Type.EMPTY)
        if Block.is_sprite(block):
            for face in range(4):   # 4 cross-faces for sprites
                _emit_face(_meshes[MeshType.SPRITE], index, block, face)
            continue
        for face in range(Face.Type.COUNT):
            if _skip_face(index, face): continue
            var vector = Face.get_vector(face)
            var neighbor_block = _get_block(index, vector)
            if not Block.is_exposed(block, neighbor_block): continue
            if not Block.is_transparent(block):
                _emit_face(_meshes[MeshType.OPAQUE], index, block, face)
            else:
                _emit_face(_meshes[MeshType.TRANSPARENT], index, block, face)
    for type in range(MeshType.COUNT):
        var mesh_instance = _create_mesh_instance(_meshes[type], type)
        if not mesh_instance: continue
        if type == MeshType.SPRITE: mesh_instance.cast_shadow = false
        add_child.call_deferred(mesh_instance)
    var collision_shape = _create_collision_shape(_meshes[MeshType.OPAQUE])
    add_child.call_deferred(collision_shape)
    _end_mesh.call_deferred(WorkerThreadPool.get_caller_task_id())

func _end_generate(task_id: int) -> void:
    clear_flag(Flag.GENERATING); set_flag(Flag.GENERATED)
    assert(not has_flag(Flag.MESHING) and not has_flag(Flag.MESHED))
    assert(task_id > 0)
    _world.remove_task_id(task_id)

func _end_mesh(task_id: int) -> void:
    assert(not has_flag(Flag.GENERATING) and has_flag(Flag.GENERATED))
    clear_flag(Flag.MESHING); set_flag(Flag.MESHED)
    if task_id > 0: _world.remove_task_id(task_id)

func _expose() -> void:
    # Build _exposed_blocks: mark each block that has at least one visible face
    assert(has_flag(Flag.GENERATED) and not has_flag(Flag.EXPOSED) and not has_flag(Flag.MESHED))
    assert(_exposed_blocks.is_empty())
    for index in _all_blocks:
        if _exposed(index): _exposed_blocks[index] = false
    set_flag(Flag.EXPOSED)

func _emit_face(arrays: Array, index: Vector3i, type: Block.Type, face: Face.Type) -> void:
    var start_index = arrays[Mesh.ARRAY_VERTEX].size()
    var location = Vector3(_index * SIZE + index)  # world-space block origin
    for i in range(4):
        arrays[Mesh.ARRAY_VERTEX].append(location + Block.get_vertex(type, face, i))
        arrays[Mesh.ARRAY_NORMAL].append(Block.get_normal(type, face))
        arrays[Mesh.ARRAY_TEX_UV].append(Block.get_texcoord(type, face))   # tile coord
        arrays[Mesh.ARRAY_TEX_UV2].append(Block.get_texcoord2(type, face, i)) # in-tile UV
    for i in Block.get_indices():
        arrays[Mesh.ARRAY_INDEX].append(start_index + i)

func _skip_face(index: Vector3i, face: Face.Type):
    # Skip the bottom face of blocks at Y=0 in the bottom chunk row (never visible)
    return index.y == 0 and _index.y == 0 and face == Face.Type.DOWN

func _create_mesh_arrays() -> Array:
    var arrays = []; arrays.resize(Mesh.ARRAY_MAX)
    arrays[Mesh.ARRAY_VERTEX] = PackedVector3Array([])
    arrays[Mesh.ARRAY_NORMAL] = PackedVector3Array([])
    arrays[Mesh.ARRAY_TEX_UV] = PackedVector2Array([])
    arrays[Mesh.ARRAY_TEX_UV2] = PackedVector2Array([])
    arrays[Mesh.ARRAY_INDEX] = PackedInt32Array([])
    return arrays

func _create_mesh_instance(arrays: Array, type: MeshType) -> MeshInstance3D:
    if arrays[Mesh.ARRAY_VERTEX].is_empty(): return null
    var array_mesh = ArrayMesh.new()
    array_mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, arrays)
    var mesh_instance = MeshInstance3D.new()
    mesh_instance.mesh = array_mesh
    match type:
        MeshType.OPAQUE:      mesh_instance.material_override = GDCraftResources.opaque_material
        MeshType.TRANSPARENT: mesh_instance.material_override = GDCraftResources.transparent_material
        MeshType.SPRITE:      mesh_instance.material_override = GDCraftResources.sprite_material
    return mesh_instance

func _create_collision_shape(arrays: Array) -> CollisionShape3D:
    # Build ConcavePolygonShape3D from opaque mesh triangles only
    var vertices = PackedVector3Array()
    for i in range(0, arrays[Mesh.ARRAY_VERTEX].size(), 4):
        for j in Block.get_indices():
            vertices.append(arrays[Mesh.ARRAY_VERTEX][i + j])
    var shape = ConcavePolygonShape3D.new()
    shape.set_faces(vertices)
    var collision_shape = CollisionShape3D.new()
    collision_shape.shape = shape
    return collision_shape
```

---

## player.gd

```gdscript
class_name Player
extends CharacterBody3D

signal switch_block(type: Block.Type)   # emitted when player scrolls block selection
signal set_block(index: Vector3i, type: Block.Type)  # emitted on LMB/RMB

@export var walk_speed = 10.0
@export var sprint_speed = 100.0
@export var rotate_speed = 0.001   # radians per pixel of mouse movement

@onready var _head = $Head                  # rotates up/down (pitch)
@onready var _raycast = $Head/RayCast3D     # detects block face player is looking at
@onready var _raycast_block = $RayCastBlock # wireframe preview of targeted block

var _raycast_break_position: Vector3i   # block to break (inside the targeted block)
var _raycast_place_position: Vector3i   # block to place (one step in front of face normal)
var _block_type = Block.Type.GRASS      # currently selected block for placement

func _init() -> void:
    position.y = 30   # spawn above terrain; world will have generated below by then

func _ready() -> void:
    _switch_block(0)   # emit switch_block for initial HUD display

func _switch_block(delta: int) -> void:
    var count = Block.Type.COUNT   # wraps around, skips EMPTY
    _block_type = (_block_type + delta + count) as Block.Type
    _block_type = (_block_type % count) as Block.Type
    switch_block.emit(_block_type)

func _notification(what: int) -> void:
    # Release mouse capture when window loses focus
    if what == NOTIFICATION_WM_WINDOW_FOCUS_OUT \
    or what == NOTIFICATION_APPLICATION_FOCUS_OUT:
        Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)

func _input(event: InputEvent) -> void:
    if Input.get_mouse_mode() == Input.MOUSE_MODE_CAPTURED:
        if event is InputEventMouseMotion:
            rotate_y(-event.relative.x * rotate_speed)       # yaw (horizontal look)
            _head.rotate_x(-event.relative.y * rotate_speed) # pitch (vertical look)
    if event is InputEventMouseButton:
        Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)
        if _raycast.is_colliding():
            if event.is_action_pressed(&"place"):
                set_block.emit(_raycast_place_position, _block_type)
            elif event.is_action_pressed(&"break"):
                set_block.emit(_raycast_break_position, Block.Type.EMPTY)
        if event.pressed:
            if event.button_index == MOUSE_BUTTON_WHEEL_DOWN:
                _switch_block(-event.factor)
            elif event.button_index == MOUSE_BUTTON_WHEEL_UP:
                _switch_block(event.factor)
    elif event.is_action_pressed(&"unfocus"):
        Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)

func _physics_process(_delta) -> void:
    if Input.get_mouse_mode() == Input.MOUSE_MODE_CAPTURED:
        var direction = Vector3.ZERO
        var up = Vector3.ZERO
        var speed = walk_speed
        if Input.is_action_pressed(&"right"):   direction.x += 1
        if Input.is_action_pressed(&"left"):    direction.x -= 1
        if Input.is_action_pressed(&"back"):    direction.z += 1
        if Input.is_action_pressed(&"forward"): direction.z -= 1
        if Input.is_action_pressed(&"jump"):    up.y += 1
        if Input.is_action_pressed(&"crouch"):  up.y -= 1
        if Input.is_action_pressed(&"sprint"):  speed = sprint_speed
        direction = direction.normalized()
        direction = (_head.global_transform.basis * direction).normalized()  # relative to camera
        direction = (direction + up).normalized()
        velocity = direction * speed
        move_and_slide()
    # Update block highlight wireframe
    _raycast_block.visible = _raycast.is_colliding()
    if not _raycast.is_colliding(): return
    var ray_position = _raycast.get_collision_point()
    var ray_normal = _raycast.get_collision_normal()
    var block_position = Vector3i((ray_position - ray_normal / 2).floor())
    _raycast_block.global_position = Vector3(block_position) + Vector3(0.5, 0.5, 0.5)
    _raycast_break_position = block_position
    _raycast_place_position = Vector3i((ray_position + ray_normal / 2).floor())
```

---

## sky.gd

```gdscript
class_name GDCraftSky
extends Node
# Day/night cycle with 4 phases: sunrise → day → sunset → night.
# Controls DirectionalLight3D energy, shadow, and ProceduralSkyMaterial colors.

@export var sunrise_length = 30.0
@export var day_length = 60.0
@export var sunset_length = 30.0
@export var night_length = 60.0
@export var speed = 1.0   # time multiplier

# Sky colors for each phase (top of sky dome and horizon)
@export var night_sky_top: Color     = Color(0.02, 0.02, 0.1)
@export var night_sky_horizon: Color = Color(0.05, 0.05, 0.2)
@export var sunrise_sky_top: Color   = Color(0.5, 0.2, 0.1)
@export var sunrise_sky_horizon: Color = Color(1.0, 0.5, 0.2)
@export var day_sky_top: Color       = Color(0.5, 0.7, 1.0)
@export var day_sky_horizon: Color   = Color(0.8, 0.9, 1.0)
@export var sunset_sky_top: Color    = Color(0.5, 0.2, 0.1)
@export var sunset_sky_horizon: Color = Color(1.0, 0.5, 0.2)
@export var night_ambient: Color     = Color(0.05, 0.05, 0.1)
@export var day_ambient: Color       = Color(1, 1, 1)

@onready var _sun = $Sun                        # DirectionalLight3D
@onready var _world_environment = $WorldEnvironment
@onready var _environment = _world_environment.environment
@onready var _sky = _environment.sky
@onready var _sky_material = _sky.sky_material  # ProceduralSkyMaterial

var _sunrise_end: float
var _day_end: float
var _sunset_end: float
var _night_end: float
var _total_length: float
var time_of_day: float   # 0.0–1.0; persisted to DB

func _init() -> void:
    _total_length = sunrise_length + day_length + sunset_length + night_length
    _sunrise_end = sunrise_length / _total_length
    _day_end = _sunrise_end + day_length / _total_length
    _sunset_end = _day_end + sunset_length / _total_length
    _night_end = 1.0
    # Start at middle of day
    time_of_day = _sunrise_end + (_day_end - _sunrise_end) / 2.0

func _process(delta: float) -> void:
    time_of_day += delta * speed / _total_length
    time_of_day = fmod(time_of_day, 1.0)   # wrap at 1.0

    # Sun angle: full rotation over one day, offset so noon = overhead
    var sun_angle = time_of_day * TAU + PI / 2
    var sin_angle = sin(sun_angle - PI)     # positive when sun is above horizon
    _sun.rotation.x = sun_angle
    _sun.light_energy = clamp(sin_angle, 0.0, 1.0)
    _sun.shadow_enabled = sin_angle > 0.0

    # Lerp colors across the 4 phases
    var top_color: Color; var horizon_color: Color; var ambient_color: Color; var t: float
    if time_of_day < _sunrise_end:
        t = time_of_day / _sunrise_end
        top_color = night_sky_top.lerp(sunrise_sky_top, t)
        horizon_color = night_sky_horizon.lerp(sunrise_sky_horizon, t)
        ambient_color = night_ambient.lerp(day_ambient, t)
    elif time_of_day < _day_end:
        t = (time_of_day - _sunrise_end) / (_day_end - _sunrise_end)
        top_color = sunrise_sky_top.lerp(day_sky_top, t)
        horizon_color = sunrise_sky_horizon.lerp(day_sky_horizon, t)
        ambient_color = day_ambient
    elif time_of_day < _sunset_end:
        t = (time_of_day - _day_end) / (_sunset_end - _day_end)
        top_color = day_sky_top.lerp(sunset_sky_top, t)
        horizon_color = day_sky_horizon.lerp(sunset_sky_horizon, t)
        ambient_color = day_ambient.lerp(night_ambient, t)
    else:
        t = (time_of_day - _sunset_end) / (_night_end - _sunset_end)
        top_color = sunset_sky_top.lerp(night_sky_top, t)
        horizon_color = sunset_sky_horizon.lerp(night_sky_horizon, t)
        ambient_color = night_ambient

    _environment.ambient_light_color = ambient_color
    _environment.ambient_light_energy = clamp(_sun.light_energy, 0.1, 1.0)
    _sky_material.sky_top_color = top_color
    _sky_material.sky_horizon_color = horizon_color
    _sky_material.ground_bottom_color = horizon_color
    _sky_material.ground_horizon_color = horizon_color
```

---

## hud.gd

```gdscript
extends Node
# HUD: stats overlay (F3) + current block texture and name display.
# Receives switch_block signal from Player (wired in world.tscn).

@onready var _stats = $Stats
@onready var _fps_label = $Stats/FPS
@onready var _process_label = $Stats/Process
@onready var _physics_process_label = $Stats/PhysicsProcess
@onready var _static_memory_used_label = $Stats/StaticMemoryUsed
@onready var _video_memory_used_label = $Stats/VideoMemoryUsed
@onready var _draw_calls_label = $Stats/DrawCalls
@onready var _primitives_label = $Stats/Primitives
@onready var _block_texture: TextureRect = $BlockH/BlockV/Texture
@onready var _block_label: Label = $BlockH/BlockV/Label

func _input(event: InputEvent) -> void:
    if event is InputEventKey:
        if event.is_action_pressed(&"debug"):
            _stats.visible = not _stats.visible

func _process(_delta: float) -> void:
    _fps_label.text = "FPS: " + str(Performance.get_monitor(Performance.Monitor.TIME_FPS))
    _process_label.text = "Process: " + str(Performance.get_monitor(Performance.Monitor.TIME_PROCESS) * 1000) + " ms"
    _physics_process_label.text = "Physics Process: " + str(Performance.get_monitor(Performance.Monitor.TIME_PHYSICS_PROCESS) * 1000) + " ms"
    _static_memory_used_label.text = "Static Memory Used: " + str(int(Performance.get_monitor(Performance.Monitor.MEMORY_STATIC) / 1024 / 1024)) + " mb"
    _video_memory_used_label.text = "Video Memory Used: " + str(int(Performance.get_monitor(Performance.Monitor.RENDER_VIDEO_MEM_USED) / 1024 / 1024)) + " mb"
    _draw_calls_label.text = "Draw Calls: " + str(int(Performance.get_monitor(Performance.Monitor.RENDER_TOTAL_DRAW_CALLS_IN_FRAME)))
    _primitives_label.text = "Primitives: " + str(int(Performance.get_monitor(Performance.Monitor.RENDER_TOTAL_PRIMITIVES_IN_FRAME)))

func _on_player_switch_block(type: Block.Type) -> void:
    # Crop the correct 16×16 tile from the spritesheet for the current block
    var size = GDCraftResources.SIZE
    var texcoord = Block.get_texcoord(type, Face.Type.FORWARD) * size
    _block_texture.texture.region = Rect2(texcoord.x, texcoord.y, size, size)
    # Format block name: "RED_TORCH" → "Red Torch"
    var text: String = Block.Type.keys()[type].replace("_", " ")
    var strings: PackedStringArray = text.split(" ")
    for i in range(strings.size()):
        strings[i] = strings[i].capitalize()
    _block_label.text = " ".join(strings)
```

---

## world.gd

```gdscript
class_name World
extends Node
# Top-level orchestrator. Manages chunk lifecycle (generate, mesh, unload).
# Connects player signals to chunk set_block and HUD switch_block.

@export var load_radius = 10    # chunks generated in this radius around player
@export var unload_radius = 12  # chunks kept alive up to this radius
@export var player_id = 0       # DB player ID (supports multiple players in future)
@export var max_workers = 8     # max concurrent WorkerThreadPool tasks

@onready var _player = $Player
@onready var _sky = $Sky
@onready var generator = $Generator
@onready var database = $Database

var _chunks: Dictionary[Vector3i, Chunk] = {}
var _generate_chunks: Array[Vector3i] = []   # relative offsets to generate
var _mesh_chunks: Array[Vector3i] = []       # relative offsets to mesh (one smaller)
var _player_chunk_index = Vector3i.ZERO      # current chunk the player is in
var _task_ids: Dictionary[int, bool] = {}    # active worker task IDs

func _ready() -> void:
    var mesh_radius = load_radius - 1
    for x in range(-load_radius, load_radius + 1):
        for y in range(-load_radius, load_radius + 1):
            _generate_chunks.append(Vector3i(x, 0, y))
    for x in range(-mesh_radius, mesh_radius + 1):
        for y in range(-mesh_radius, mesh_radius + 1):
            _mesh_chunks.append(Vector3i(x, 0, y))
    _mesh_chunks.sort_custom(_sort)   # mesh closest chunks first (visible sooner)
    database.load_player(_player, player_id)
    database.load_sky(_sky)

func _notification(what: int) -> void:
    if what == NOTIFICATION_PREDELETE:
        for task_id in _task_ids:
            WorkerThreadPool.wait_for_task_completion(task_id)  # drain threads safely
        database.save_player(_player, player_id)
        database.save_sky(_sky)

func _in_bounds(index: Vector3i) -> bool:
    assert(index.y == 0)
    index -= _player_chunk_index
    return index.x >= -unload_radius and index.x <= unload_radius \
        and index.z >= -unload_radius and index.z <= unload_radius

func _sort(lhs: Vector3i, rhs: Vector3i) -> bool:
    return lhs.length() < rhs.length()  # sort by distance from origin (player)

func add_task_id(task_id: int) -> void:
    assert(_task_ids.size() < max_workers)
    _task_ids[task_id] = false

func remove_task_id(task_id: int) -> void:
    assert(_task_ids.has(task_id))
    _task_ids.erase(task_id)

func get_chunk(index: Vector3i) -> Chunk:
    assert(index.y == 0)
    return _chunks.get(index, null)

func _process(_delta: float) -> void:
    _player_chunk_index = Vector3i(_player.position) / Chunk.WIDTH
    _player_chunk_index.y = 0
    var _workers = _task_ids.size()
    _generate()
    if _workers == _task_ids.size():   # only mesh if no new generate tasks started
        _mesh()
    _unload()

func _generate() -> void:
    for index in _generate_chunks:
        if _task_ids.size() >= max_workers: return
        index += _player_chunk_index
        var chunk = _chunks.get(index, null)
        if not chunk:
            chunk = Chunk.new(self, index)
            add_child(chunk)
            _chunks[index] = chunk
        if chunk.has_flag(Chunk.Flag.GENERATING): continue
        elif not chunk.has_flag(Chunk.Flag.GENERATED):
            assert(not chunk.has_flag(Chunk.Flag.MESHED))
            chunk.generate()

func _mesh():
    for index in _mesh_chunks:
        if _task_ids.size() >= max_workers: return
        index += _player_chunk_index
        var chunk = _chunks.get(index, null)
        assert(chunk)
        assert(not chunk.has_flag(Chunk.Flag.GENERATING))
        assert(chunk.has_flag(Chunk.Flag.GENERATED))
        if chunk.has_flag(Chunk.Flag.MESHING): continue
        elif not chunk.has_flag(Chunk.Flag.MESHED):
            chunk.mesh(true)

func _unload() -> void:
    for index in _chunks.keys():
        var chunk = _chunks[index]
        if chunk.has_flag(Chunk.Flag.WORKING): continue   # don't kill working chunks
        if _in_bounds(index): continue
        # Don't free a chunk if a neighbor is still meshing (it might reference this chunk)
        var free = true
        for face in range(Face.Type.COUNT):
            if face == Face.Type.UP or face == Face.Type.DOWN: continue
            var neighbor_chunk = get_chunk(index + Face.get_vector(face))
            if not neighbor_chunk: continue
            if neighbor_chunk.has_flag(Chunk.Flag.MESHING): free = false; break
        if not free: continue
        _chunks.erase(index)
        remove_child(chunk)
        WorkerThreadPool.add_task(func(): chunk.free())   # free on worker to avoid stall

func _remesh(index: Vector3i) -> void:
    var chunk = get_chunk(index)
    if not chunk: return
    if chunk.has_flag(Chunk.Flag.WORKING) or not chunk.has_flag(Chunk.Flag.MESHED): return
    chunk.mesh(false, true)   # sync remesh (force=true clears MESHED flag)
    assert(not chunk.has_flag(Chunk.Flag.MESHED))

func _on_player_set_block(index: Vector3i, type: Block.Type) -> void:
    # Convert global block index to chunk + local index
    var chunk_index = Vector3i((Vector3(index) / Vector3(Chunk.SIZE)).floor())
    var block_index = index - chunk_index * Chunk.SIZE
    var chunk = get_chunk(chunk_index)
    if not chunk: return
    if chunk.has_flag(Chunk.Flag.WORKING) or not chunk.has_flag(Chunk.Flag.MESHED): return
    # All 4 horizontal neighbors must be GENERATED before modifying (face culling needs them)
    for face in range(Face.Type.COUNT):
        if face == Face.Type.UP or face == Face.Type.DOWN: continue
        var neighbor_chunk = get_chunk(chunk_index + Face.get_vector(face))
        if not neighbor_chunk.has_flag(Chunk.Flag.GENERATED): return
    chunk.set_block(block_index, type)
    chunk.mesh(false)   # synchronous remesh of this chunk
    # Remesh adjacent chunks if block was on a chunk boundary
    if block_index.x == 0:
        _remesh(chunk_index - Vector3i(1, 0, 0))
    elif block_index.x == Chunk.SIZE.x - 1:
        _remesh(chunk_index + Vector3i(1, 0, 0))
    if block_index.z == 0:
        _remesh(chunk_index - Vector3i(0, 0, 1))
    elif block_index.z == Chunk.SIZE.z - 1:
        _remesh(chunk_index + Vector3i(0, 0, 1))
    database.set_block(chunk_index, block_index, type)
```

---

## Shaders

### spritesheet.gdshaderinc

```glsl
uniform sampler2DArray spritesheet : filter_nearest;

vec4 get_color(vec2 uv, vec2 tile) {
    // uv = in-tile UV (UV2), tile = tile grid position (UV)
    float layer = tile.y * float(textureSize(spritesheet, 0).x / 16) + tile.x;
    return texture(spritesheet, vec3(uv, layer));
}
```

### opaque.gdshader

```glsl
shader_type spatial;
render_mode cull_back;

#include "spritesheet.gdshaderinc"

void fragment() {
    vec4 color = get_color(UV2, UV);
    if (color.a < 0.5) discard;   // alpha cutout for leaves/glass edges
    ALBEDO = color.rgb;
}
```

### transparent.gdshader

```glsl
shader_type spatial;
render_mode blend_mix, cull_back, depth_draw_always;

#include "spritesheet.gdshaderinc"

void fragment() {
    vec4 color = get_color(UV2, UV);
    ALBEDO = color.rgb;
    ALPHA = color.a;
}
```

### sprite.gdshader

```glsl
shader_type spatial;
render_mode cull_disabled, unshaded;

#include "spritesheet.gdshaderinc"

void fragment() {
    vec4 color = get_color(UV2, UV);
    if (color.a < 0.5) discard;
    ALBEDO = color.rgb;
}
```
