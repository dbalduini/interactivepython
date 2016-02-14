import simplegui

frame_size = [200, 200]
image_size = [380, 287]

def draw(canvas):
    src_center = [220, 100]
    src_size = [100, 100]
    
    canvas.draw_image(image, 
                      src_center,
                      src_size,
                      [frame_size[0] / 2, frame_size[1] / 2],
                      frame_size)

frame = simplegui.create_frame("test", frame_size[0], frame_size[1])
frame.set_draw_handler(draw)
image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/alphatest.png")

frame.start()