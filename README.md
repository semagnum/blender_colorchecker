# Color Checker Calibrator
A Blender addon that can calibrate images to a range of colors
## How to Use
In the image editor's color checker panel, create the target colors that you need (you can name them for convenience) and click "Add Color" to add it to the list. 

Pick the correlating colors in the image (make sure the hues match!). Once you're satisfied, click "Generate Node" to create a hue correct node in your compositor.

### Generate a set of colors
If you want to want a set of colors to get you started, you can open up the Blender terminal and paste the following (a planned feature is to presets so you don't have to do this, but it will do for now):
```python
default_colors = [
    ("Red", (1.0, 0.0, 0.0)),
    ("Orange", (1.0, 0.5, 0.0)),
    ("Yellow", (1.0, 1.0, 0.0)),
    ("Green", (0.0, 1.0, 0.0)),
    ("Cyan", (0.0, 1.0, 1.0)),
    ("Blue", (0.0, 0.0, 1.0)),
    ("Purple", (0.5, 0.0, 1.0)),
    ("Magenta", (1.0, 0.0, 1.0))
]

for color_name, color_val in default_colors:
    new_color = C.scene.cc_colors.add()
    new_color.name = color_name
    new_color.target_color = color_val
    new_color.picked_color = color_val
```
