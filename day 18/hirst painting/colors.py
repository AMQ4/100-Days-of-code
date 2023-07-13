import colorgram

colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colorgram.extract('hirst colors.jpg', 50)]
