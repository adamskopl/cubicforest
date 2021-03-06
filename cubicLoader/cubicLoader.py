import imp
import simplejson
import bpy
import configparser
import cubicModel
import os

"""
Load and run this script in the Blender Console
e.g.:

import sys
sys.path.append.path("/path_to_cubicLoader_folder")
import cubicLoader
cubicLoader.run("cubicModel", frameStart, frameEnd)

requirements:
https://github.com/simplejson/simplejson
"""


class ModelLoader:
    """
    Class loading groups and their objects(cubes) from a default scene
    into a Model class.
    """
    def __init__(self, modelName):
        self.modelName = modelName

    def load_model(self):
        """
        Fill Model class with data from a default scene.
        """
        self.model = cubicModel.Model(self.modelName)
        self.model.load_groups()

    def print_model(self, fStart, fEnd):
        """
        For frames in range of fStart and fEnd, print names of model's
        groups and their cubes (name+position).
        """

        print("model: ", self.modelName)
        scene = bpy.data.scenes[0]

        for frameNum in range(fStart, fEnd+1):
            scene.frame_set(frameNum)
            print("FRAME: ", frameNum)
            for mGroup in self.model.groups:
                print("---- GROUP: ", mGroup.name)
                for gCube in mGroup.cubes:
                    print(gCube.name, "  ", gCube.pos)
            print("------------------------------------")

    def save_model(self, fStart, fEnd):
        """
        x
        """
        currentDir = os.path.dirname(os.path.abspath(__file__))
        config = configparser.ConfigParser()
        config.read(currentDir + "/config.ini")
        modelDict = self.model.to_dict(fStart, fEnd)
        jsonData = simplejson.dumps(modelDict)
        fd = open(config['Paths']['writePath'] + '/' +
                  self.modelName + ".json", "w")
        fd.write(jsonData)
        fd.close


def run(modelName, fStart=1, fEnd=1):
    """
    Function for Blender Console. Invokes ModelLoader's loadModel()
    function.
    """
    # reload symbol table for Blender
    imp.reload(cubicModel)

    m = ModelLoader(modelName)
    m.load_model()
    m.save_model(fStart, fEnd)
