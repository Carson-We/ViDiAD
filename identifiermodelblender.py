import bpy

# Clear the default objects in the scene
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Create the identifier geometry
bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(0, 0, 0))

# Scale the identifier cube
cube = bpy.context.object
cube.scale = (0.2, 0.2, 0.2)  # Adjust the size to be moderate

# Set the material
material = bpy.data.materials.new(name="Identifier Material")
material.diffuse_color = (1, 0, 0)  # Set an obvious color like red
cube.data.materials.append(material)

# Render the scene
bpy.ops.render.render(write_still=True)
