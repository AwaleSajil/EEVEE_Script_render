#!/usr/bin/python

import sys
import bpy

def looop(start_frame, start_frame, location):
    for step in range(start_frame, end_frame + 1):
        bpy.context.scene.frame_set(step)
        
        bpy.data.scenes["Scene"].render.filepath = location + '\V.png_%d.png' % step

        bpy.ops.render.render( write_still=True )



argv = sys.argv
list_of_arg = argv[argv.index("--") + 1:]  # get all args after "--"

list_of_arg = str(sys.argv)

location = str(list_of_arg[0])
start_frame = int(list_of_arg[1])
start_frame = int(list_of_arg[2])
looop(start_frame, start_frame, location)