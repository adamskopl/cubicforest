import imp
import cubicCube


class CubesGroup:
    """
    Class defining model's group of cubes.

    Blender's equivalent: Group.
    """
    def __init__(self, name):
        # reload symbol table for Blender
        imp.reload(cubicCube)
        self.name = name
        # list of Cube elements
        self.cubes = list()

    def load_cubes(self, groupCubes):
        """
        Fill cubes list with objects from groupCubes list.
        """
        for groupCube in groupCubes:
            cube = cubicCube.Cube(groupCube.name)
            cube.set_pos(groupCube.location)
            cube.set_rot(groupCube.rotation_euler)
            cube.set_color(groupCube.data.materials[0].name)
            self.cubes.append(cube)

    def to_dict(self):
        groupDict = dict()
        cubesList = list()
        for c in self.cubes:
            cubeDict = c.to_dict()
            cubesList.append(cubeDict)

        groupDict["name"] = self.name
        groupDict["cubes"] = cubesList
        return groupDict
