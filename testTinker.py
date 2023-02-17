import mouse
import time as t

# get the position of mouse
t.sleep(2)

# In [12]: mouse.get_position()
# Out[12]: (714, 488)

# presses but doesn't release
# mouse.hold('left')
mouse.move(190, 340)
print(mouse.get_position())
# mouse.click(button='left')
# mouse.hold('left')
mouse.press(button='left')
# mouse.click(button='left')
# mouse.drag(190, 340, 1000, 10, duration=1)
# mouse.move(190, 340)
# mouse.hold(button='left')
# mouse.move(350, 480)
# mouse.release(button='left')
# mouse.press(button='right')
# mouse.move(1000, 340)

mouse.drag(370, 330, 20, 340, duration=1)

# mouse.release(button='left')
# print(mouse.is_pressed(button='left'))
# # i = 0
# while mouse.is_pressed(button='left'):
#     print("eNTRO")
# # drag from (0, 0) to (100, 100) relatively with a duration of 0.1s
#     mouse.drag(328, 417, 10, 417, duration=1)
#     # i += 1


