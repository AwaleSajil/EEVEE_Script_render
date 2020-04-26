import sys
import bpy

def looop(start_frame, end_frame, location):
    print('Came in looop')
    for step in range(start_frame, end_frame + 1):
        bpy.context.scene.frame_set(step)
        
        bpy.data.scenes["Scene"].render.filepath = location + '/V.png_%d.png' % step

        bpy.ops.render.render( write_still=True )



argv = sys.argv
list_of_arg = argv[argv.index("--") + 1:]  # get all args after "--"

list_of_arg = list(sys.argv)

print(list_of_arg )
location = str(list_of_arg[-1])
print('location: ' , location )
end_frame = int(list_of_arg[-2])
print('end_frame  : ' , end_frame )
start_frame = int(list_of_arg[-3])
print('start_frame   : ' , start_frame )


looop(start_frame, end_frame, location)