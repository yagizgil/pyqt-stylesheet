class CheckBox():

    def __init__(self, text, data):
        self.text = text
        self.data = data

        self.write()

    def write(self):
        f = open("a", "w")
        f.write(self.text + " {")

        if self.data.me["color"] != "":
            f.write("\n   color: {};".format(self.data.me["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.me["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.me["outline"]))

        if self.data.me["width_value"] != 0 and self.data.me["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.me["width_value"], self.data.me["width_type"]))

        if self.data.me["height_value"] != 0 and self.data.me["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.me["height_value"], self.data.me["height_type"]))

        if self.data.me["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.me["font_family"]))

        if self.data.me["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.me["font_size"]))

        if self.data.me["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.me["font_weight"]))

        if self.data.me["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.me["font_style"]))

        if self.data.me["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.me["line_height"]))

        if self.data.me["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.me["text_align"]))

        if self.data.me["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.me["text_decoration"]))

        if self.data.me["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.me["text_transform"]))

        if self.data.me["background"] != "":
            f.write("\n   background: {};".format(self.data.me["background"]))

        if self.data.me["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.me["background_image"]))

        if self.data.me["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.me["background_color"]))

        if self.data.me["border"] != "":
            f.write("\n   border: {};".format(self.data.me["border"]))

        if self.data.me["border_width_value"] != 0 and self.data.me["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.me["border_width_value"], self.data.me["border_width_type"]))

        if self.data.me["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.me["border_style"]))

        if self.data.me["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.me["border_color"]))

        if self.data.me["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.me["border_top"]))

        if self.data.me["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.me["border_right"]))

        if self.data.me["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.me["border_bottom"]))

        if self.data.me["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.me["border_left"]))

        if self.data.me["border_radius"] != 0 and self.data.me["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.me["border_radius"]))

        if self.data.me["padding_top_value"] != 0 and self.data.me["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.me["padding_top_value"], self.data.me["padding_top_type"]))

        if self.data.me["padding_right_value"] != 0 and self.data.me["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.me["padding_right_value"], self.data.me["padding_right_type"]))

        if self.data.me["padding_bottom_value"] != 0 and self.data.me["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.me["padding_bottom_value"], self.data.me["padding_bottom_type"]))

        if self.data.me["padding_left_value"] != 0 and self.data.me["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.me["padding_left_value"], self.data.me["padding_left_type"]))


        if self.data.me["margin_top_value"] != 0 and self.data.me["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.me["margin_top_value"], self.data.me["margin_top_type"]))

        if self.data.me["margin_right_value"] != 0 and self.data.me["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.me["margin_right_value"], self.data.me["margin_right_type"]))

        if self.data.me["margin_bottom_value"] != 0 and self.data.me["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.me["margin_bottom_value"], self.data.me["margin_bottom_type"]))

        if self.data.me["margin_left_value"] != 0 and self.data.me["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.me["margin_left_value"], self.data.me["margin_left_type"]))

        f.write("\n}")



        f.write("\n")




        f.write(self.text + ":hover {")

        if self.data.hover["color"] != "":
            f.write("\n   color: {};".format(self.data.hover["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.hover["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.hover["outline"]))

        if self.data.hover["width_value"] != 0 and self.data.hover["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.hover["width_value"], self.data.hover["width_type"]))

        if self.data.hover["height_value"] != 0 and self.data.hover["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.hover["height_value"], self.data.hover["height_type"]))

        if self.data.hover["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.hover["font_family"]))

        if self.data.hover["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.hover["font_size"]))

        if self.data.hover["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.hover["font_weight"]))

        if self.data.hover["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.hover["font_style"]))

        if self.data.hover["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.hover["line_height"]))

        if self.data.hover["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.hover["text_align"]))

        if self.data.hover["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.hover["text_decoration"]))

        if self.data.hover["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.hover["text_transform"]))

        if self.data.hover["background"] != "":
            f.write("\n   background: {};".format(self.data.hover["background"]))

        if self.data.hover["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.hover["background_image"]))

        if self.data.hover["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.hover["background_color"]))

        if self.data.hover["border"] != "":
            f.write("\n   border: {};".format(self.data.hover["border"]))

        if self.data.hover["border_width_value"] != 0 and self.data.hover["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.hover["border_width_value"], self.data.hover["border_width_type"]))

        if self.data.hover["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.hover["border_style"]))

        if self.data.hover["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.hover["border_color"]))

        if self.data.hover["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.hover["border_top"]))

        if self.data.hover["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.hover["border_right"]))

        if self.data.hover["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.hover["border_bottom"]))

        if self.data.hover["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.hover["border_left"]))

        if self.data.hover["border_radius"] != 0 and self.data.hover["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.hover["border_radius"]))

        if self.data.hover["padding_top_value"] != 0 and self.data.hover["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.hover["padding_top_value"], self.data.hover["padding_top_type"]))

        if self.data.hover["padding_right_value"] != 0 and self.data.hover["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.hover["padding_right_value"], self.data.hover["padding_right_type"]))

        if self.data.hover["padding_bottom_value"] != 0 and self.data.hover["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.hover["padding_bottom_value"], self.data.hover["padding_bottom_type"]))

        if self.data.hover["padding_left_value"] != 0 and self.data.hover["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.hover["padding_left_value"], self.data.hover["padding_left_type"]))


        if self.data.hover["margin_top_value"] != 0 and self.data.hover["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.hover["margin_top_value"], self.data.hover["margin_top_type"]))

        if self.data.hover["margin_right_value"] != 0 and self.data.hover["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.hover["margin_right_value"], self.data.hover["margin_right_type"]))

        if self.data.hover["margin_bottom_value"] != 0 and self.data.hover["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.hover["margin_bottom_value"], self.data.hover["margin_bottom_type"]))

        if self.data.hover["margin_left_value"] != 0 and self.data.hover["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.hover["margin_left_value"], self.data.hover["margin_left_type"]))


        f.write("\n}")



        f.write("\n")




        f.write(self.text + "::pressed {")

        if self.data.pressed["color"] != "":
            f.write("\n   color: {};".format(self.data.pressed["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.pressed["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.pressed["outline"]))

        if self.data.pressed["width_value"] != 0 and self.data.pressed["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.pressed["width_value"], self.data.pressed["width_type"]))

        if self.data.pressed["height_value"] != 0 and self.data.pressed["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.pressed["height_value"], self.data.pressed["height_type"]))

        if self.data.pressed["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.pressed["font_family"]))

        if self.data.pressed["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.pressed["font_size"]))

        if self.data.pressed["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.pressed["font_weight"]))

        if self.data.pressed["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.pressed["font_style"]))

        if self.data.pressed["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.pressed["line_height"]))

        if self.data.pressed["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.pressed["text_align"]))

        if self.data.pressed["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.pressed["text_decoration"]))

        if self.data.pressed["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.pressed["text_transform"]))

        if self.data.pressed["background"] != "":
            f.write("\n   background: {};".format(self.data.pressed["background"]))

        if self.data.pressed["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.pressed["background_image"]))

        if self.data.pressed["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.pressed["background_color"]))

        if self.data.pressed["border"] != "":
            f.write("\n   border: {};".format(self.data.pressed["border"]))

        if self.data.pressed["border_width_value"] != 0 and self.data.pressed["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.pressed["border_width_value"], self.data.pressed["border_width_type"]))

        if self.data.pressed["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.pressed["border_style"]))

        if self.data.pressed["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.pressed["border_color"]))

        if self.data.pressed["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.pressed["border_top"]))

        if self.data.pressed["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.pressed["border_right"]))

        if self.data.pressed["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.pressed["border_bottom"]))

        if self.data.pressed["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.pressed["border_left"]))

        if self.data.pressed["border_radius"] != 0 and self.data.pressed["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.pressed["border_radius"]))

        if self.data.pressed["padding_top_value"] != 0 and self.data.pressed["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.pressed["padding_top_value"], self.data.pressed["padding_top_type"]))

        if self.data.pressed["padding_right_value"] != 0 and self.data.pressed["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.pressed["padding_right_value"], self.data.pressed["padding_right_type"]))

        if self.data.pressed["padding_bottom_value"] != 0 and self.data.pressed["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.pressed["padding_bottom_value"], self.data.pressed["padding_bottom_type"]))

        if self.data.pressed["padding_left_value"] != 0 and self.data.pressed["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.pressed["padding_left_value"], self.data.pressed["padding_left_type"]))


        if self.data.pressed["margin_top_value"] != 0 and self.data.pressed["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.pressed["margin_top_value"], self.data.pressed["margin_top_type"]))

        if self.data.pressed["margin_right_value"] != 0 and self.data.pressed["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.pressed["margin_right_value"], self.data.pressed["margin_right_type"]))

        if self.data.pressed["margin_bottom_value"] != 0 and self.data.pressed["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.pressed["margin_bottom_value"], self.data.pressed["margin_bottom_type"]))

        if self.data.pressed["margin_left_value"] != 0 and self.data.pressed["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.pressed["margin_left_value"], self.data.pressed["margin_left_type"]))

        f.write("\n}")








        f.write("\n")






        f.write(self.text + "::checked {")

        if self.data.checked["color"] != "":
            f.write("\n   color: {};".format(self.data.checked["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.checked["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.checked["outline"]))

        if self.data.checked["width_value"] != 0 and self.data.checked["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.checked["width_value"], self.data.checked["width_type"]))

        if self.data.checked["height_value"] != 0 and self.data.checked["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.checked["height_value"], self.data.checked["height_type"]))

        if self.data.checked["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.checked["font_family"]))

        if self.data.checked["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.checked["font_size"]))

        if self.data.checked["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.checked["font_weight"]))

        if self.data.checked["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.checked["font_style"]))

        if self.data.checked["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.checked["line_height"]))

        if self.data.checked["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.checked["text_align"]))

        if self.data.checked["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.checked["text_decoration"]))

        if self.data.checked["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.checked["text_transform"]))

        if self.data.checked["background"] != "":
            f.write("\n   background: {};".format(self.data.checked["background"]))

        if self.data.checked["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.checked["background_image"]))

        if self.data.checked["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.checked["background_color"]))

        if self.data.checked["border"] != "":
            f.write("\n   border: {};".format(self.data.checked["border"]))

        if self.data.checked["border_width_value"] != 0 and self.data.checked["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.checked["border_width_value"], self.data.checked["border_width_type"]))

        if self.data.checked["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.checked["border_style"]))

        if self.data.checked["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.checked["border_color"]))

        if self.data.checked["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.checked["border_top"]))

        if self.data.checked["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.checked["border_right"]))

        if self.data.checked["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.checked["border_bottom"]))

        if self.data.checked["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.checked["border_left"]))

        if self.data.checked["border_radius"] != 0 and self.data.checked["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.checked["border_radius"]))

        if self.data.checked["padding_top_value"] != 0 and self.data.checked["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.checked["padding_top_value"], self.data.checked["padding_top_type"]))

        if self.data.checked["padding_right_value"] != 0 and self.data.checked["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.checked["padding_right_value"], self.data.checked["padding_right_type"]))

        if self.data.checked["padding_bottom_value"] != 0 and self.data.checked["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.checked["padding_bottom_value"], self.data.checked["padding_bottom_type"]))

        if self.data.checked["padding_left_value"] != 0 and self.data.checked["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.checked["padding_left_value"], self.data.checked["padding_left_type"]))


        if self.data.checked["margin_top_value"] != 0 and self.data.checked["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.checked["margin_top_value"], self.data.checked["margin_top_type"]))

        if self.data.checked["margin_right_value"] != 0 and self.data.checked["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.checked["margin_right_value"], self.data.checked["margin_right_type"]))

        if self.data.checked["margin_bottom_value"] != 0 and self.data.checked["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.checked["margin_bottom_value"], self.data.checked["margin_bottom_type"]))

        if self.data.checked["margin_left_value"] != 0 and self.data.checked["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.checked["margin_left_value"], self.data.checked["margin_left_type"]))

        f.write("\n}")




        f.write("\n")






        f.write(self.text + "::unchecked {")

        if self.data.unchecked["color"] != "":
            f.write("\n   color: {};".format(self.data.unchecked["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.unchecked["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.unchecked["outline"]))

        if self.data.unchecked["width_value"] != 0 and self.data.unchecked["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.unchecked["width_value"], self.data.unchecked["width_type"]))

        if self.data.unchecked["height_value"] != 0 and self.data.unchecked["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.unchecked["height_value"], self.data.unchecked["height_type"]))

        if self.data.unchecked["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.unchecked["font_family"]))

        if self.data.unchecked["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.unchecked["font_size"]))

        if self.data.unchecked["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.unchecked["font_weight"]))

        if self.data.unchecked["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.unchecked["font_style"]))

        if self.data.unchecked["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.unchecked["line_height"]))

        if self.data.unchecked["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.unchecked["text_align"]))

        if self.data.unchecked["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.unchecked["text_decoration"]))

        if self.data.unchecked["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.unchecked["text_transform"]))

        if self.data.unchecked["background"] != "":
            f.write("\n   background: {};".format(self.data.unchecked["background"]))

        if self.data.unchecked["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.unchecked["background_image"]))

        if self.data.unchecked["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.unchecked["background_color"]))

        if self.data.unchecked["border"] != "":
            f.write("\n   border: {};".format(self.data.unchecked["border"]))

        if self.data.unchecked["border_width_value"] != 0 and self.data.unchecked["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.unchecked["border_width_value"], self.data.unchecked["border_width_type"]))

        if self.data.unchecked["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.unchecked["border_style"]))

        if self.data.unchecked["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.unchecked["border_color"]))

        if self.data.unchecked["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.unchecked["border_top"]))

        if self.data.unchecked["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.unchecked["border_right"]))

        if self.data.unchecked["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.unchecked["border_bottom"]))

        if self.data.unchecked["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.unchecked["border_left"]))

        if self.data.unchecked["border_radius"] != 0 and self.data.unchecked["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.unchecked["border_radius"]))

        if self.data.unchecked["padding_top_value"] != 0 and self.data.unchecked["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.unchecked["padding_top_value"], self.data.unchecked["padding_top_type"]))

        if self.data.unchecked["padding_right_value"] != 0 and self.data.unchecked["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.unchecked["padding_right_value"], self.data.unchecked["padding_right_type"]))

        if self.data.unchecked["padding_bottom_value"] != 0 and self.data.unchecked["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.unchecked["padding_bottom_value"], self.data.unchecked["padding_bottom_type"]))

        if self.data.unchecked["padding_left_value"] != 0 and self.data.unchecked["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.unchecked["padding_left_value"], self.data.unchecked["padding_left_type"]))


        if self.data.unchecked["margin_top_value"] != 0 and self.data.unchecked["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.unchecked["margin_top_value"], self.data.unchecked["margin_top_type"]))

        if self.data.unchecked["margin_right_value"] != 0 and self.data.unchecked["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.unchecked["margin_right_value"], self.data.unchecked["margin_right_type"]))

        if self.data.unchecked["margin_bottom_value"] != 0 and self.data.unchecked["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.unchecked["margin_bottom_value"], self.data.unchecked["margin_bottom_type"]))

        if self.data.unchecked["margin_left_value"] != 0 and self.data.unchecked["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.unchecked["margin_left_value"], self.data.unchecked["margin_left_type"]))

        f.write("\n}")






        f.write("\n")




        f.write(self.text + "::checked:hover {")

        if self.data.checked_hover["color"] != "":
            f.write("\n   color: {};".format(self.data.checked_hover["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.checked_hover["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.checked_hover["outline"]))

        if self.data.checked_hover["width_value"] != 0 and self.data.checked_hover["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.checked_hover["width_value"], self.data.checked_hover["width_type"]))

        if self.data.checked_hover["height_value"] != 0 and self.data.checked_hover["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.checked_hover["height_value"], self.data.checked_hover["height_type"]))

        if self.data.checked_hover["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.checked_hover["font_family"]))

        if self.data.checked_hover["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.checked_hover["font_size"]))

        if self.data.checked_hover["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.checked_hover["font_weight"]))

        if self.data.checked_hover["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.checked_hover["font_style"]))

        if self.data.checked_hover["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.checked_hover["line_height"]))

        if self.data.checked_hover["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.checked_hover["text_align"]))

        if self.data.checked_hover["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.checked_hover["text_decoration"]))

        if self.data.checked_hover["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.checked_hover["text_transform"]))

        if self.data.checked_hover["background"] != "":
            f.write("\n   background: {};".format(self.data.checked_hover["background"]))

        if self.data.checked_hover["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.checked_hover["background_image"]))

        if self.data.checked_hover["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.checked_hover["background_color"]))

        if self.data.checked_hover["border"] != "":
            f.write("\n   border: {};".format(self.data.checked_hover["border"]))

        if self.data.checked_hover["border_width_value"] != 0 and self.data.checked_hover["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.checked_hover["border_width_value"], self.data.checked_hover["border_width_type"]))

        if self.data.checked_hover["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.checked_hover["border_style"]))

        if self.data.checked_hover["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.checked_hover["border_color"]))

        if self.data.checked_hover["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.checked_hover["border_top"]))

        if self.data.checked_hover["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.checked_hover["border_right"]))

        if self.data.checked_hover["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.checked_hover["border_bottom"]))

        if self.data.checked_hover["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.checked_hover["border_left"]))

        if self.data.checked_hover["border_radius"] != 0 and self.data.checked_hover["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.checked_hover["border_radius"]))

        if self.data.checked_hover["padding_top_value"] != 0 and self.data.checked_hover["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.checked_hover["padding_top_value"], self.data.checked_hover["padding_top_type"]))

        if self.data.checked_hover["padding_right_value"] != 0 and self.data.checked_hover["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.checked_hover["padding_right_value"], self.data.checked_hover["padding_right_type"]))

        if self.data.checked_hover["padding_bottom_value"] != 0 and self.data.checked_hover["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.checked_hover["padding_bottom_value"], self.data.checked_hover["padding_bottom_type"]))

        if self.data.checked_hover["padding_left_value"] != 0 and self.data.checked_hover["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.checked_hover["padding_left_value"], self.data.checked_hover["padding_left_type"]))


        if self.data.checked_hover["margin_top_value"] != 0 and self.data.checked_hover["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.checked_hover["margin_top_value"], self.data.checked_hover["margin_top_type"]))

        if self.data.checked_hover["margin_right_value"] != 0 and self.data.checked_hover["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.checked_hover["margin_right_value"], self.data.checked_hover["margin_right_type"]))

        if self.data.checked_hover["margin_bottom_value"] != 0 and self.data.checked_hover["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.checked_hover["margin_bottom_value"], self.data.checked_hover["margin_bottom_type"]))

        if self.data.checked_hover["margin_left_value"] != 0 and self.data.checked_hover["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.checked_hover["margin_left_value"], self.data.checked_hover["margin_left_type"]))

        f.write("\n}")



        f.write("\n")




        f.write(self.text + "::unchecked:hover {")

        if self.data.unchecked_hover["color"] != "":
            f.write("\n   color: {};".format(self.data.unchecked_hover["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.unchecked_hover["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.unchecked_hover["outline"]))

        if self.data.unchecked_hover["width_value"] != 0 and self.data.unchecked_hover["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.unchecked_hover["width_value"], self.data.unchecked_hover["width_type"]))

        if self.data.unchecked_hover["height_value"] != 0 and self.data.unchecked_hover["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.unchecked_hover["height_value"], self.data.unchecked_hover["height_type"]))

        if self.data.unchecked_hover["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.unchecked_hover["font_family"]))

        if self.data.unchecked_hover["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.unchecked_hover["font_size"]))

        if self.data.unchecked_hover["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.unchecked_hover["font_weight"]))

        if self.data.unchecked_hover["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.unchecked_hover["font_style"]))

        if self.data.unchecked_hover["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.unchecked_hover["line_height"]))

        if self.data.unchecked_hover["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.unchecked_hover["text_align"]))

        if self.data.unchecked_hover["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.unchecked_hover["text_decoration"]))

        if self.data.unchecked_hover["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.unchecked_hover["text_transform"]))

        if self.data.unchecked_hover["background"] != "":
            f.write("\n   background: {};".format(self.data.unchecked_hover["background"]))

        if self.data.unchecked_hover["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.unchecked_hover["background_image"]))

        if self.data.unchecked_hover["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.unchecked_hover["background_color"]))

        if self.data.unchecked_hover["border"] != "":
            f.write("\n   border: {};".format(self.data.unchecked_hover["border"]))

        if self.data.unchecked_hover["border_width_value"] != 0 and self.data.unchecked_hover["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.unchecked_hover["border_width_value"], self.data.unchecked_hover["border_width_type"]))

        if self.data.unchecked_hover["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.unchecked_hover["border_style"]))

        if self.data.unchecked_hover["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.unchecked_hover["border_color"]))

        if self.data.unchecked_hover["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.unchecked_hover["border_top"]))

        if self.data.unchecked_hover["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.unchecked_hover["border_right"]))

        if self.data.unchecked_hover["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.unchecked_hover["border_bottom"]))

        if self.data.unchecked_hover["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.unchecked_hover["border_left"]))

        if self.data.unchecked_hover["border_radius"] != 0 and self.data.unchecked_hover["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.unchecked_hover["border_radius"]))

        if self.data.unchecked_hover["padding_top_value"] != 0 and self.data.unchecked_hover["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.unchecked_hover["padding_top_value"], self.data.unchecked_hover["padding_top_type"]))

        if self.data.unchecked_hover["padding_right_value"] != 0 and self.data.unchecked_hover["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.unchecked_hover["padding_right_value"], self.data.unchecked_hover["padding_right_type"]))

        if self.data.unchecked_hover["padding_bottom_value"] != 0 and self.data.unchecked_hover["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.unchecked_hover["padding_bottom_value"], self.data.unchecked_hover["padding_bottom_type"]))

        if self.data.unchecked_hover["padding_left_value"] != 0 and self.data.unchecked_hover["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.unchecked_hover["padding_left_value"], self.data.unchecked_hover["padding_left_type"]))


        if self.data.unchecked_hover["margin_top_value"] != 0 and self.data.unchecked_hover["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.unchecked_hover["margin_top_value"], self.data.unchecked_hover["margin_top_type"]))

        if self.data.unchecked_hover["margin_right_value"] != 0 and self.data.unchecked_hover["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.unchecked_hover["margin_right_value"], self.data.unchecked_hover["margin_right_type"]))

        if self.data.unchecked_hover["margin_bottom_value"] != 0 and self.data.unchecked_hover["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.unchecked_hover["margin_bottom_value"], self.data.unchecked_hover["margin_bottom_type"]))

        if self.data.unchecked_hover["margin_left_value"] != 0 and self.data.unchecked_hover["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.unchecked_hover["margin_left_value"], self.data.unchecked_hover["margin_left_type"]))

        f.write("\n}")








        f.write("\n")






        f.write(self.text + "::indicator {")

        if self.data.indicator["color"] != "":
            f.write("\n   color: {};".format(self.data.indicator["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.indicator["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.indicator["outline"]))

        if self.data.indicator["width_value"] != 0 and self.data.indicator["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.indicator["width_value"], self.data.indicator["width_type"]))

        if self.data.indicator["height_value"] != 0 and self.data.indicator["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.indicator["height_value"], self.data.indicator["height_type"]))

        if self.data.indicator["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.indicator["font_family"]))

        if self.data.indicator["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.indicator["font_size"]))

        if self.data.indicator["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.indicator["font_weight"]))

        if self.data.indicator["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.indicator["font_style"]))

        if self.data.indicator["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.indicator["line_height"]))

        if self.data.indicator["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.indicator["text_align"]))

        if self.data.indicator["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.indicator["text_decoration"]))

        if self.data.indicator["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.indicator["text_transform"]))

        if self.data.indicator["background"] != "":
            f.write("\n   background: {};".format(self.data.indicator["background"]))

        if self.data.indicator["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.indicator["background_image"]))

        if self.data.indicator["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.indicator["background_color"]))

        if self.data.indicator["border"] != "":
            f.write("\n   border: {};".format(self.data.indicator["border"]))

        if self.data.indicator["border_width_value"] != 0 and self.data.indicator["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.indicator["border_width_value"], self.data.indicator["border_width_type"]))

        if self.data.indicator["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.indicator["border_style"]))

        if self.data.indicator["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.indicator["border_color"]))

        if self.data.indicator["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.indicator["border_top"]))

        if self.data.indicator["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.indicator["border_right"]))

        if self.data.indicator["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.indicator["border_bottom"]))

        if self.data.indicator["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.indicator["border_left"]))

        if self.data.indicator["border_radius"] != 0 and self.data.indicator["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.indicator["border_radius"]))

        if self.data.indicator["padding_top_value"] != 0 and self.data.indicator["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator["padding_top_value"], self.data.indicator["padding_top_type"]))

        if self.data.indicator["padding_right_value"] != 0 and self.data.indicator["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.indicator["padding_right_value"], self.data.indicator["padding_right_type"]))

        if self.data.indicator["padding_bottom_value"] != 0 and self.data.indicator["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.indicator["padding_bottom_value"], self.data.indicator["padding_bottom_type"]))

        if self.data.indicator["padding_left_value"] != 0 and self.data.indicator["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.indicator["padding_left_value"], self.data.indicator["padding_left_type"]))


        if self.data.indicator["margin_top_value"] != 0 and self.data.indicator["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator["margin_top_value"], self.data.indicator["margin_top_type"]))

        if self.data.indicator["margin_right_value"] != 0 and self.data.indicator["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.indicator["margin_right_value"], self.data.indicator["margin_right_type"]))

        if self.data.indicator["margin_bottom_value"] != 0 and self.data.indicator["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.indicator["margin_bottom_value"], self.data.indicator["margin_bottom_type"]))

        if self.data.indicator["margin_left_value"] != 0 and self.data.indicator["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.indicator["margin_left_value"], self.data.indicator["margin_left_type"]))

        f.write("\n}")








        f.write("\n")






        f.write(self.text + "::indicator:checked {")

        if self.data.indicator_checked["color"] != "":
            f.write("\n   color: {};".format(self.data.indicator_checked["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.indicator_checked["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.indicator_checked["outline"]))

        if self.data.indicator_checked["width_value"] != 0 and self.data.indicator_checked["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.indicator_checked["width_value"], self.data.indicator_checked["width_type"]))

        if self.data.indicator_checked["height_value"] != 0 and self.data.indicator_checked["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.indicator_checked["height_value"], self.data.indicator_checked["height_type"]))

        if self.data.indicator_checked["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.indicator_checked["font_family"]))

        if self.data.indicator_checked["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.indicator_checked["font_size"]))

        if self.data.indicator_checked["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.indicator_checked["font_weight"]))

        if self.data.indicator_checked["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.indicator_checked["font_style"]))

        if self.data.indicator_checked["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.indicator_checked["line_height"]))

        if self.data.indicator_checked["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.indicator_checked["text_align"]))

        if self.data.indicator_checked["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.indicator_checked["text_decoration"]))

        if self.data.indicator_checked["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.indicator_checked["text_transform"]))

        if self.data.indicator_checked["background"] != "":
            f.write("\n   background: {};".format(self.data.indicator_checked["background"]))

        if self.data.indicator_checked["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.indicator_checked["background_image"]))

        if self.data.indicator_checked["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.indicator_checked["background_color"]))

        if self.data.indicator_checked["border"] != "":
            f.write("\n   border: {};".format(self.data.indicator_checked["border"]))

        if self.data.indicator_checked["border_width_value"] != 0 and self.data.indicator_checked["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.indicator_checked["border_width_value"], self.data.indicator_checked["border_width_type"]))

        if self.data.indicator_checked["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.indicator_checked["border_style"]))

        if self.data.indicator_checked["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.indicator_checked["border_color"]))

        if self.data.indicator_checked["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.indicator_checked["border_top"]))

        if self.data.indicator_checked["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.indicator_checked["border_right"]))

        if self.data.indicator_checked["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.indicator_checked["border_bottom"]))

        if self.data.indicator_checked["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.indicator_checked["border_left"]))

        if self.data.indicator_checked["border_radius"] != 0 and self.data.indicator_checked["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.indicator_checked["border_radius"]))

        if self.data.indicator_checked["padding_top_value"] != 0 and self.data.indicator_checked["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_checked["padding_top_value"], self.data.indicator_checked["padding_top_type"]))

        if self.data.indicator_checked["padding_right_value"] != 0 and self.data.indicator_checked["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.indicator_checked["padding_right_value"], self.data.indicator_checked["padding_right_type"]))

        if self.data.indicator_checked["padding_bottom_value"] != 0 and self.data.indicator_checked["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.indicator_checked["padding_bottom_value"], self.data.indicator_checked["padding_bottom_type"]))

        if self.data.indicator_checked["padding_left_value"] != 0 and self.data.indicator_checked["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.indicator_checked["padding_left_value"], self.data.indicator_checked["padding_left_type"]))


        if self.data.indicator_checked["margin_top_value"] != 0 and self.data.indicator_checked["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_checked["margin_top_value"], self.data.indicator_checked["margin_top_type"]))

        if self.data.indicator_checked["margin_right_value"] != 0 and self.data.indicator_checked["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.indicator_checked["margin_right_value"], self.data.indicator_checked["margin_right_type"]))

        if self.data.indicator_checked["margin_bottom_value"] != 0 and self.data.indicator_checked["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.indicator_checked["margin_bottom_value"], self.data.indicator_checked["margin_bottom_type"]))

        if self.data.indicator_checked["margin_left_value"] != 0 and self.data.indicator_checked["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.indicator_checked["margin_left_value"], self.data.indicator_checked["margin_left_type"]))

        f.write("\n}")







        f.write("\n")






        f.write(self.text + "::indicator:checked:hover {")

        if self.data.indicator_checked_hover["color"] != "":
            f.write("\n   color: {};".format(self.data.indicator_checked_hover["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.indicator_checked_hover["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.indicator_checked_hover["outline"]))

        if self.data.indicator_checked_hover["width_value"] != 0 and self.data.indicator_checked_hover["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.indicator_checked_hover["width_value"], self.data.indicator_checked_hover["width_type"]))

        if self.data.indicator_checked_hover["height_value"] != 0 and self.data.indicator_checked_hover["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.indicator_checked_hover["height_value"], self.data.indicator_checked_hover["height_type"]))

        if self.data.indicator_checked_hover["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.indicator_checked_hover["font_family"]))

        if self.data.indicator_checked_hover["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.indicator_checked_hover["font_size"]))

        if self.data.indicator_checked_hover["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.indicator_checked_hover["font_weight"]))

        if self.data.indicator_checked_hover["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.indicator_checked_hover["font_style"]))

        if self.data.indicator_checked_hover["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.indicator_checked_hover["line_height"]))

        if self.data.indicator_checked_hover["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.indicator_checked_hover["text_align"]))

        if self.data.indicator_checked_hover["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.indicator_checked_hover["text_decoration"]))

        if self.data.indicator_checked_hover["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.indicator_checked_hover["text_transform"]))

        if self.data.indicator_checked_hover["background"] != "":
            f.write("\n   background: {};".format(self.data.indicator_checked_hover["background"]))

        if self.data.indicator_checked_hover["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.indicator_checked_hover["background_image"]))

        if self.data.indicator_checked_hover["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.indicator_checked_hover["background_color"]))

        if self.data.indicator_checked_hover["border"] != "":
            f.write("\n   border: {};".format(self.data.indicator_checked_hover["border"]))

        if self.data.indicator_checked_hover["border_width_value"] != 0 and self.data.indicator_checked_hover["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.indicator_checked_hover["border_width_value"], self.data.indicator_checked_hover["border_width_type"]))

        if self.data.indicator_checked_hover["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.indicator_checked_hover["border_style"]))

        if self.data.indicator_checked_hover["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.indicator_checked_hover["border_color"]))

        if self.data.indicator_checked_hover["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.indicator_checked_hover["border_top"]))

        if self.data.indicator_checked_hover["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.indicator_checked_hover["border_right"]))

        if self.data.indicator_checked_hover["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.indicator_checked_hover["border_bottom"]))

        if self.data.indicator_checked_hover["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.indicator_checked_hover["border_left"]))

        if self.data.indicator_checked_hover["border_radius"] != 0 and self.data.indicator_checked_hover["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.indicator_checked_hover["border_radius"]))

        if self.data.indicator_checked_hover["padding_top_value"] != 0 and self.data.indicator_checked_hover["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_checked_hover["padding_top_value"], self.data.indicator_checked_hover["padding_top_type"]))

        if self.data.indicator_checked_hover["padding_right_value"] != 0 and self.data.indicator_checked_hover["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.indicator_checked_hover["padding_right_value"], self.data.indicator_checked_hover["padding_right_type"]))

        if self.data.indicator_checked_hover["padding_bottom_value"] != 0 and self.data.indicator_checked_hover["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.indicator_checked_hover["padding_bottom_value"], self.data.indicator_checked_hover["padding_bottom_type"]))

        if self.data.indicator_checked_hover["padding_left_value"] != 0 and self.data.indicator_checked_hover["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.indicator_checked_hover["padding_left_value"], self.data.indicator_checked_hover["padding_left_type"]))


        if self.data.indicator_checked_hover["margin_top_value"] != 0 and self.data.indicator_checked_hover["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_checked_hover["margin_top_value"], self.data.indicator_checked_hover["margin_top_type"]))

        if self.data.indicator_checked_hover["margin_right_value"] != 0 and self.data.indicator_checked_hover["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.indicator_checked_hover["margin_right_value"], self.data.indicator_checked_hover["margin_right_type"]))

        if self.data.indicator_checked_hover["margin_bottom_value"] != 0 and self.data.indicator_checked_hover["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.indicator_checked_hover["margin_bottom_value"], self.data.indicator_checked_hover["margin_bottom_type"]))

        if self.data.indicator_checked_hover["margin_left_value"] != 0 and self.data.indicator_checked_hover["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.indicator_checked_hover["margin_left_value"], self.data.indicator_checked_hover["margin_left_type"]))

        f.write("\n}")





        f.write("\n")






        f.write(self.text + "::indicator:checked:pressed {")

        if self.data.indicator_checked_pressed["color"] != "":
            f.write("\n   color: {};".format(self.data.indicator_checked_pressed["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.indicator_checked_pressed["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.indicator_checked_pressed["outline"]))

        if self.data.indicator_checked_pressed["width_value"] != 0 and self.data.indicator_checked_pressed["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.indicator_checked_pressed["width_value"], self.data.indicator_checked_pressed["width_type"]))

        if self.data.indicator_checked_pressed["height_value"] != 0 and self.data.indicator_checked_pressed["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.indicator_checked_pressed["height_value"], self.data.indicator_checked_pressed["height_type"]))

        if self.data.indicator_checked_pressed["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.indicator_checked_pressed["font_family"]))

        if self.data.indicator_checked_pressed["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.indicator_checked_pressed["font_size"]))

        if self.data.indicator_checked_pressed["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.indicator_checked_pressed["font_weight"]))

        if self.data.indicator_checked_pressed["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.indicator_checked_pressed["font_style"]))

        if self.data.indicator_checked_pressed["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.indicator_checked_pressed["line_height"]))

        if self.data.indicator_checked_pressed["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.indicator_checked_pressed["text_align"]))

        if self.data.indicator_checked_pressed["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.indicator_checked_pressed["text_decoration"]))

        if self.data.indicator_checked_pressed["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.indicator_checked_pressed["text_transform"]))

        if self.data.indicator_checked_pressed["background"] != "":
            f.write("\n   background: {};".format(self.data.indicator_checked_pressed["background"]))

        if self.data.indicator_checked_pressed["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.indicator_checked_pressed["background_image"]))

        if self.data.indicator_checked_pressed["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.indicator_checked_pressed["background_color"]))

        if self.data.indicator_checked_pressed["border"] != "":
            f.write("\n   border: {};".format(self.data.indicator_checked_pressed["border"]))

        if self.data.indicator_checked_pressed["border_width_value"] != 0 and self.data.indicator_checked_pressed["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.indicator_checked_pressed["border_width_value"], self.data.indicator_checked_pressed["border_width_type"]))

        if self.data.indicator_checked_pressed["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.indicator_checked_pressed["border_style"]))

        if self.data.indicator_checked_pressed["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.indicator_checked_pressed["border_color"]))

        if self.data.indicator_checked_pressed["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.indicator_checked_pressed["border_top"]))

        if self.data.indicator_checked_pressed["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.indicator_checked_pressed["border_right"]))

        if self.data.indicator_checked_pressed["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.indicator_checked_pressed["border_bottom"]))

        if self.data.indicator_checked_pressed["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.indicator_checked_pressed["border_left"]))

        if self.data.indicator_checked_pressed["border_radius"] != 0 and self.data.indicator_checked_pressed["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.indicator_checked_pressed["border_radius"]))

        if self.data.indicator_checked_pressed["padding_top_value"] != 0 and self.data.indicator_checked_pressed["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_checked_pressed["padding_top_value"], self.data.indicator_checked_pressed["padding_top_type"]))

        if self.data.indicator_checked_pressed["padding_right_value"] != 0 and self.data.indicator_checked_pressed["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.indicator_checked_pressed["padding_right_value"], self.data.indicator_checked_pressed["padding_right_type"]))

        if self.data.indicator_checked_pressed["padding_bottom_value"] != 0 and self.data.indicator_checked_pressed["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.indicator_checked_pressed["padding_bottom_value"], self.data.indicator_checked_pressed["padding_bottom_type"]))

        if self.data.indicator_checked_pressed["padding_left_value"] != 0 and self.data.indicator_checked_pressed["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.indicator_checked_pressed["padding_left_value"], self.data.indicator_checked_pressed["padding_left_type"]))


        if self.data.indicator_checked_pressed["margin_top_value"] != 0 and self.data.indicator_checked_pressed["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_checked_pressed["margin_top_value"], self.data.indicator_checked_pressed["margin_top_type"]))

        if self.data.indicator_checked_pressed["margin_right_value"] != 0 and self.data.indicator_checked_pressed["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.indicator_checked_pressed["margin_right_value"], self.data.indicator_checked_pressed["margin_right_type"]))

        if self.data.indicator_checked_pressed["margin_bottom_value"] != 0 and self.data.indicator_checked_pressed["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.indicator_checked_pressed["margin_bottom_value"], self.data.indicator_checked_pressed["margin_bottom_type"]))

        if self.data.indicator_checked_pressed["margin_left_value"] != 0 and self.data.indicator_checked_pressed["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.indicator_checked_pressed["margin_left_value"], self.data.indicator_checked_pressed["margin_left_type"]))

        f.write("\n}")










        f.write("\n")






        f.write(self.text + "::indicator:unchecked {")

        if self.data.indicator_unchecked["color"] != "":
            f.write("\n   color: {};".format(self.data.indicator_unchecked["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.indicator_unchecked["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.indicator_unchecked["outline"]))

        if self.data.indicator_unchecked["width_value"] != 0 and self.data.indicator_unchecked["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.indicator_unchecked["width_value"], self.data.indicator_unchecked["width_type"]))

        if self.data.indicator_unchecked["height_value"] != 0 and self.data.indicator_unchecked["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.indicator_unchecked["height_value"], self.data.indicator_unchecked["height_type"]))

        if self.data.indicator_unchecked["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.indicator_unchecked["font_family"]))

        if self.data.indicator_unchecked["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.indicator_unchecked["font_size"]))

        if self.data.indicator_unchecked["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.indicator_unchecked["font_weight"]))

        if self.data.indicator_unchecked["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.indicator_unchecked["font_style"]))

        if self.data.indicator_unchecked["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.indicator_unchecked["line_height"]))

        if self.data.indicator_unchecked["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.indicator_unchecked["text_align"]))

        if self.data.indicator_unchecked["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.indicator_unchecked["text_decoration"]))

        if self.data.indicator_unchecked["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.indicator_unchecked["text_transform"]))

        if self.data.indicator_unchecked["background"] != "":
            f.write("\n   background: {};".format(self.data.indicator_unchecked["background"]))

        if self.data.indicator_unchecked["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.indicator_unchecked["background_image"]))

        if self.data.indicator_unchecked["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.indicator_unchecked["background_color"]))

        if self.data.indicator_unchecked["border"] != "":
            f.write("\n   border: {};".format(self.data.indicator_unchecked["border"]))

        if self.data.indicator_unchecked["border_width_value"] != 0 and self.data.indicator_unchecked["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.indicator_unchecked["border_width_value"], self.data.indicator_unchecked["border_width_type"]))

        if self.data.indicator_unchecked["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.indicator_unchecked["border_style"]))

        if self.data.indicator_unchecked["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.indicator_unchecked["border_color"]))

        if self.data.indicator_unchecked["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.indicator_unchecked["border_top"]))

        if self.data.indicator_unchecked["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.indicator_unchecked["border_right"]))

        if self.data.indicator_unchecked["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.indicator_unchecked["border_bottom"]))

        if self.data.indicator_unchecked["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.indicator_unchecked["border_left"]))

        if self.data.indicator_unchecked["border_radius"] != 0 and self.data.indicator_unchecked["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.indicator_unchecked["border_radius"]))

        if self.data.indicator_unchecked["padding_top_value"] != 0 and self.data.indicator_unchecked["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_unchecked["padding_top_value"], self.data.indicator_unchecked["padding_top_type"]))

        if self.data.indicator_unchecked["padding_right_value"] != 0 and self.data.indicator_unchecked["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.indicator_unchecked["padding_right_value"], self.data.indicator_unchecked["padding_right_type"]))

        if self.data.indicator_unchecked["padding_bottom_value"] != 0 and self.data.indicator_unchecked["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.indicator_unchecked["padding_bottom_value"], self.data.indicator_unchecked["padding_bottom_type"]))

        if self.data.indicator_unchecked["padding_left_value"] != 0 and self.data.indicator_unchecked["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.indicator_unchecked["padding_left_value"], self.data.indicator_unchecked["padding_left_type"]))


        if self.data.indicator_unchecked["margin_top_value"] != 0 and self.data.indicator_unchecked["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_unchecked["margin_top_value"], self.data.indicator_unchecked["margin_top_type"]))

        if self.data.indicator_unchecked["margin_right_value"] != 0 and self.data.indicator_unchecked["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.indicator_unchecked["margin_right_value"], self.data.indicator_unchecked["margin_right_type"]))

        if self.data.indicator_unchecked["margin_bottom_value"] != 0 and self.data.indicator_unchecked["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.indicator_unchecked["margin_bottom_value"], self.data.indicator_unchecked["margin_bottom_type"]))

        if self.data.indicator_unchecked["margin_left_value"] != 0 and self.data.indicator_unchecked["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.indicator_unchecked["margin_left_value"], self.data.indicator_unchecked["margin_left_type"]))

        f.write("\n}")







        f.write("\n")






        f.write(self.text + "::indicator:unchecked:hover {")

        if self.data.indicator_unchecked_hover["color"] != "":
            f.write("\n   color: {};".format(self.data.indicator_unchecked_hover["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.indicator_unchecked_hover["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.indicator_unchecked_hover["outline"]))

        if self.data.indicator_unchecked_hover["width_value"] != 0 and self.data.indicator_unchecked_hover["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.indicator_unchecked_hover["width_value"], self.data.indicator_unchecked_hover["width_type"]))

        if self.data.indicator_unchecked_hover["height_value"] != 0 and self.data.indicator_unchecked_hover["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.indicator_unchecked_hover["height_value"], self.data.indicator_unchecked_hover["height_type"]))

        if self.data.indicator_unchecked_hover["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.indicator_unchecked_hover["font_family"]))

        if self.data.indicator_unchecked_hover["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.indicator_unchecked_hover["font_size"]))

        if self.data.indicator_unchecked_hover["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.indicator_unchecked_hover["font_weight"]))

        if self.data.indicator_unchecked_hover["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.indicator_unchecked_hover["font_style"]))

        if self.data.indicator_unchecked_hover["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.indicator_unchecked_hover["line_height"]))

        if self.data.indicator_unchecked_hover["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.indicator_unchecked_hover["text_align"]))

        if self.data.indicator_unchecked_hover["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.indicator_unchecked_hover["text_decoration"]))

        if self.data.indicator_unchecked_hover["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.indicator_unchecked_hover["text_transform"]))

        if self.data.indicator_unchecked_hover["background"] != "":
            f.write("\n   background: {};".format(self.data.indicator_unchecked_hover["background"]))

        if self.data.indicator_unchecked_hover["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.indicator_unchecked_hover["background_image"]))

        if self.data.indicator_unchecked_hover["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.indicator_unchecked_hover["background_color"]))

        if self.data.indicator_unchecked_hover["border"] != "":
            f.write("\n   border: {};".format(self.data.indicator_unchecked_hover["border"]))

        if self.data.indicator_unchecked_hover["border_width_value"] != 0 and self.data.indicator_unchecked_hover["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.indicator_unchecked_hover["border_width_value"], self.data.indicator_unchecked_hover["border_width_type"]))

        if self.data.indicator_unchecked_hover["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.indicator_unchecked_hover["border_style"]))

        if self.data.indicator_unchecked_hover["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.indicator_unchecked_hover["border_color"]))

        if self.data.indicator_unchecked_hover["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.indicator_unchecked_hover["border_top"]))

        if self.data.indicator_unchecked_hover["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.indicator_unchecked_hover["border_right"]))

        if self.data.indicator_unchecked_hover["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.indicator_unchecked_hover["border_bottom"]))

        if self.data.indicator_unchecked_hover["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.indicator_unchecked_hover["border_left"]))

        if self.data.indicator_unchecked_hover["border_radius"] != 0 and self.data.indicator_unchecked_hover["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.indicator_unchecked_hover["border_radius"]))

        if self.data.indicator_unchecked_hover["padding_top_value"] != 0 and self.data.indicator_unchecked_hover["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_unchecked_hover["padding_top_value"], self.data.indicator_unchecked_hover["padding_top_type"]))

        if self.data.indicator_unchecked_hover["padding_right_value"] != 0 and self.data.indicator_unchecked_hover["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.indicator_unchecked_hover["padding_right_value"], self.data.indicator_unchecked_hover["padding_right_type"]))

        if self.data.indicator_unchecked_hover["padding_bottom_value"] != 0 and self.data.indicator_unchecked_hover["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.indicator_unchecked_hover["padding_bottom_value"], self.data.indicator_unchecked_hover["padding_bottom_type"]))

        if self.data.indicator_unchecked_hover["padding_left_value"] != 0 and self.data.indicator_unchecked_hover["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.indicator_unchecked_hover["padding_left_value"], self.data.indicator_unchecked_hover["padding_left_type"]))


        if self.data.indicator_unchecked_hover["margin_top_value"] != 0 and self.data.indicator_unchecked_hover["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_unchecked_hover["margin_top_value"], self.data.indicator_unchecked_hover["margin_top_type"]))

        if self.data.indicator_unchecked_hover["margin_right_value"] != 0 and self.data.indicator_unchecked_hover["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.indicator_unchecked_hover["margin_right_value"], self.data.indicator_unchecked_hover["margin_right_type"]))

        if self.data.indicator_unchecked_hover["margin_bottom_value"] != 0 and self.data.indicator_unchecked_hover["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.indicator_unchecked_hover["margin_bottom_value"], self.data.indicator_unchecked_hover["margin_bottom_type"]))

        if self.data.indicator_unchecked_hover["margin_left_value"] != 0 and self.data.indicator_unchecked_hover["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.indicator_unchecked_hover["margin_left_value"], self.data.indicator_unchecked_hover["margin_left_type"]))

        f.write("\n}")





        f.write("\n")






        f.write(self.text + "::indicator:unchecked:pressed {")

        if self.data.indicator_unchecked_pressed["color"] != "":
            f.write("\n   color: {};".format(self.data.indicator_unchecked_pressed["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.indicator_unchecked_pressed["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.indicator_unchecked_pressed["outline"]))

        if self.data.indicator_unchecked_pressed["width_value"] != 0 and self.data.indicator_unchecked_pressed["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.indicator_unchecked_pressed["width_value"], self.data.indicator_unchecked_pressed["width_type"]))

        if self.data.indicator_unchecked_pressed["height_value"] != 0 and self.data.indicator_unchecked_pressed["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.indicator_unchecked_pressed["height_value"], self.data.indicator_unchecked_pressed["height_type"]))

        if self.data.indicator_unchecked_pressed["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.indicator_unchecked_pressed["font_family"]))

        if self.data.indicator_unchecked_pressed["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.indicator_unchecked_pressed["font_size"]))

        if self.data.indicator_unchecked_pressed["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.indicator_unchecked_pressed["font_weight"]))

        if self.data.indicator_unchecked_pressed["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.indicator_unchecked_pressed["font_style"]))

        if self.data.indicator_unchecked_pressed["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.indicator_unchecked_pressed["line_height"]))

        if self.data.indicator_unchecked_pressed["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.indicator_unchecked_pressed["text_align"]))

        if self.data.indicator_unchecked_pressed["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.indicator_unchecked_pressed["text_decoration"]))

        if self.data.indicator_unchecked_pressed["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.indicator_unchecked_pressed["text_transform"]))

        if self.data.indicator_unchecked_pressed["background"] != "":
            f.write("\n   background: {};".format(self.data.indicator_unchecked_pressed["background"]))

        if self.data.indicator_unchecked_pressed["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.indicator_unchecked_pressed["background_image"]))

        if self.data.indicator_unchecked_pressed["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.indicator_unchecked_pressed["background_color"]))

        if self.data.indicator_unchecked_pressed["border"] != "":
            f.write("\n   border: {};".format(self.data.indicator_unchecked_pressed["border"]))

        if self.data.indicator_unchecked_pressed["border_width_value"] != 0 and self.data.indicator_unchecked_pressed["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.indicator_unchecked_pressed["border_width_value"], self.data.indicator_unchecked_pressed["border_width_type"]))

        if self.data.indicator_unchecked_pressed["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.indicator_unchecked_pressed["border_style"]))

        if self.data.indicator_unchecked_pressed["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.indicator_unchecked_pressed["border_color"]))

        if self.data.indicator_unchecked_pressed["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.indicator_unchecked_pressed["border_top"]))

        if self.data.indicator_unchecked_pressed["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.indicator_unchecked_pressed["border_right"]))

        if self.data.indicator_unchecked_pressed["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.indicator_unchecked_pressed["border_bottom"]))

        if self.data.indicator_unchecked_pressed["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.indicator_unchecked_pressed["border_left"]))

        if self.data.indicator_unchecked_pressed["border_radius"] != 0 and self.data.indicator_unchecked_pressed["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.indicator_unchecked_pressed["border_radius"]))

        if self.data.indicator_unchecked_pressed["padding_top_value"] != 0 and self.data.indicator_unchecked_pressed["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_unchecked_pressed["padding_top_value"], self.data.indicator_unchecked_pressed["padding_top_type"]))

        if self.data.indicator_unchecked_pressed["padding_right_value"] != 0 and self.data.indicator_unchecked_pressed["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.indicator_unchecked_pressed["padding_right_value"], self.data.indicator_unchecked_pressed["padding_right_type"]))

        if self.data.indicator_unchecked_pressed["padding_bottom_value"] != 0 and self.data.indicator_unchecked_pressed["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.indicator_unchecked_pressed["padding_bottom_value"], self.data.indicator_unchecked_pressed["padding_bottom_type"]))

        if self.data.indicator_unchecked_pressed["padding_left_value"] != 0 and self.data.indicator_unchecked_pressed["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.indicator_unchecked_pressed["padding_left_value"], self.data.indicator_unchecked_pressed["padding_left_type"]))


        if self.data.indicator_unchecked_pressed["margin_top_value"] != 0 and self.data.indicator_unchecked_pressed["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_unchecked_pressed["margin_top_value"], self.data.indicator_unchecked_pressed["margin_top_type"]))

        if self.data.indicator_unchecked_pressed["margin_right_value"] != 0 and self.data.indicator_unchecked_pressed["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.indicator_unchecked_pressed["margin_right_value"], self.data.indicator_unchecked_pressed["margin_right_type"]))

        if self.data.indicator_unchecked_pressed["margin_bottom_value"] != 0 and self.data.indicator_unchecked_pressed["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.indicator_unchecked_pressed["margin_bottom_value"], self.data.indicator_unchecked_pressed["margin_bottom_type"]))

        if self.data.indicator_unchecked_pressed["margin_left_value"] != 0 and self.data.indicator_unchecked_pressed["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.indicator_unchecked_pressed["margin_left_value"], self.data.indicator_unchecked_pressed["margin_left_type"]))

        f.write("\n}")





        f.write("\n")




        f.write(self.text + "::indicator:indeterminate:hover {")

        if self.data.indicator_indeterminate_hover["color"] != "":
            f.write("\n   color: {};".format(self.data.indicator_indeterminate_hover["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.indicator_indeterminate_hover["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.indicator_indeterminate_hover["outline"]))

        if self.data.indicator_indeterminate_hover["width_value"] != 0 and self.data.indicator_indeterminate_hover["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.indicator_indeterminate_hover["width_value"], self.data.indicator_indeterminate_hover["width_type"]))

        if self.data.indicator_indeterminate_hover["height_value"] != 0 and self.data.indicator_indeterminate_hover["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.indicator_indeterminate_hover["height_value"], self.data.indicator_indeterminate_hover["height_type"]))

        if self.data.indicator_indeterminate_hover["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.indicator_indeterminate_hover["font_family"]))

        if self.data.indicator_indeterminate_hover["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.indicator_indeterminate_hover["font_size"]))

        if self.data.indicator_indeterminate_hover["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.indicator_indeterminate_hover["font_weight"]))

        if self.data.indicator_indeterminate_hover["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.indicator_indeterminate_hover["font_style"]))

        if self.data.indicator_indeterminate_hover["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.indicator_indeterminate_hover["line_height"]))

        if self.data.indicator_indeterminate_hover["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.indicator_indeterminate_hover["text_align"]))

        if self.data.indicator_indeterminate_hover["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.indicator_indeterminate_hover["text_decoration"]))

        if self.data.indicator_indeterminate_hover["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.indicator_indeterminate_hover["text_transform"]))

        if self.data.indicator_indeterminate_hover["background"] != "":
            f.write("\n   background: {};".format(self.data.indicator_indeterminate_hover["background"]))

        if self.data.indicator_indeterminate_hover["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.indicator_indeterminate_hover["background_image"]))

        if self.data.indicator_indeterminate_hover["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.indicator_indeterminate_hover["background_color"]))

        if self.data.indicator_indeterminate_hover["border"] != "":
            f.write("\n   border: {};".format(self.data.indicator_indeterminate_hover["border"]))

        if self.data.indicator_indeterminate_hover["border_width_value"] != 0 and self.data.indicator_indeterminate_hover["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.indicator_indeterminate_hover["border_width_value"], self.data.indicator_indeterminate_hover["border_width_type"]))

        if self.data.indicator_indeterminate_hover["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.indicator_indeterminate_hover["border_style"]))

        if self.data.indicator_indeterminate_hover["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.indicator_indeterminate_hover["border_color"]))

        if self.data.indicator_indeterminate_hover["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.indicator_indeterminate_hover["border_top"]))

        if self.data.indicator_indeterminate_hover["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.indicator_indeterminate_hover["border_right"]))

        if self.data.indicator_indeterminate_hover["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.indicator_indeterminate_hover["border_bottom"]))

        if self.data.indicator_indeterminate_hover["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.indicator_indeterminate_hover["border_left"]))

        if self.data.indicator_indeterminate_hover["border_radius"] != 0 and self.data.indicator_indeterminate_hover["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.indicator_indeterminate_hover["border_radius"]))

        if self.data.indicator_indeterminate_hover["padding_top_value"] != 0 and self.data.indicator_indeterminate_hover["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_indeterminate_hover["padding_top_value"], self.data.indicator_indeterminate_hover["padding_top_type"]))

        if self.data.indicator_indeterminate_hover["padding_right_value"] != 0 and self.data.indicator_indeterminate_hover["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.indicator_indeterminate_hover["padding_right_value"], self.data.indicator_indeterminate_hover["padding_right_type"]))

        if self.data.indicator_indeterminate_hover["padding_bottom_value"] != 0 and self.data.indicator_indeterminate_hover["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.indicator_indeterminate_hover["padding_bottom_value"], self.data.indicator_indeterminate_hover["padding_bottom_type"]))

        if self.data.indicator_indeterminate_hover["padding_left_value"] != 0 and self.data.indicator_indeterminate_hover["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.indicator_indeterminate_hover["padding_left_value"], self.data.indicator_indeterminate_hover["padding_left_type"]))


        if self.data.indicator_indeterminate_hover["margin_top_value"] != 0 and self.data.indicator_indeterminate_hover["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_indeterminate_hover["margin_top_value"], self.data.indicator_indeterminate_hover["margin_top_type"]))

        if self.data.indicator_indeterminate_hover["margin_right_value"] != 0 and self.data.indicator_indeterminate_hover["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.indicator_indeterminate_hover["margin_right_value"], self.data.indicator_indeterminate_hover["margin_right_type"]))

        if self.data.indicator_indeterminate_hover["margin_bottom_value"] != 0 and self.data.indicator_indeterminate_hover["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.indicator_indeterminate_hover["margin_bottom_value"], self.data.indicator_indeterminate_hover["margin_bottom_type"]))

        if self.data.indicator_indeterminate_hover["margin_left_value"] != 0 and self.data.indicator_indeterminate_hover["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.indicator_indeterminate_hover["margin_left_value"], self.data.indicator_indeterminate_hover["margin_left_type"]))

        f.write("\n}")







        f.write("\n")




        f.write(self.text + "::indicator:indeterminate:pressed {")

        if self.data.indicator_indeterminate_pressed["color"] != "":
            f.write("\n   color: {};".format(self.data.indicator_indeterminate_pressed["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.indicator_indeterminate_pressed["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.indicator_indeterminate_pressed["outline"]))

        if self.data.indicator_indeterminate_pressed["width_value"] != 0 and self.data.indicator_indeterminate_pressed["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.indicator_indeterminate_pressed["width_value"], self.data.indicator_indeterminate_pressed["width_type"]))

        if self.data.indicator_indeterminate_pressed["height_value"] != 0 and self.data.indicator_indeterminate_pressed["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.indicator_indeterminate_pressed["height_value"], self.data.indicator_indeterminate_pressed["height_type"]))

        if self.data.indicator_indeterminate_pressed["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.indicator_indeterminate_pressed["font_family"]))

        if self.data.indicator_indeterminate_pressed["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.indicator_indeterminate_pressed["font_size"]))

        if self.data.indicator_indeterminate_pressed["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.indicator_indeterminate_pressed["font_weight"]))

        if self.data.indicator_indeterminate_pressed["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.indicator_indeterminate_pressed["font_style"]))

        if self.data.indicator_indeterminate_pressed["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.indicator_indeterminate_pressed["line_height"]))

        if self.data.indicator_indeterminate_pressed["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.indicator_indeterminate_pressed["text_align"]))

        if self.data.indicator_indeterminate_pressed["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.indicator_indeterminate_pressed["text_decoration"]))

        if self.data.indicator_indeterminate_pressed["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.indicator_indeterminate_pressed["text_transform"]))

        if self.data.indicator_indeterminate_pressed["background"] != "":
            f.write("\n   background: {};".format(self.data.indicator_indeterminate_pressed["background"]))

        if self.data.indicator_indeterminate_pressed["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.indicator_indeterminate_pressed["background_image"]))

        if self.data.indicator_indeterminate_pressed["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.indicator_indeterminate_pressed["background_color"]))

        if self.data.indicator_indeterminate_pressed["border"] != "":
            f.write("\n   border: {};".format(self.data.indicator_indeterminate_pressed["border"]))

        if self.data.indicator_indeterminate_pressed["border_width_value"] != 0 and self.data.indicator_indeterminate_pressed["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.indicator_indeterminate_pressed["border_width_value"], self.data.indicator_indeterminate_pressed["border_width_type"]))

        if self.data.indicator_indeterminate_pressed["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.indicator_indeterminate_pressed["border_style"]))

        if self.data.indicator_indeterminate_pressed["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.indicator_indeterminate_pressed["border_color"]))

        if self.data.indicator_indeterminate_pressed["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.indicator_indeterminate_pressed["border_top"]))

        if self.data.indicator_indeterminate_pressed["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.indicator_indeterminate_pressed["border_right"]))

        if self.data.indicator_indeterminate_pressed["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.indicator_indeterminate_pressed["border_bottom"]))

        if self.data.indicator_indeterminate_pressed["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.indicator_indeterminate_pressed["border_left"]))

        if self.data.indicator_indeterminate_pressed["border_radius"] != 0 and self.data.indicator_indeterminate_pressed["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.indicator_indeterminate_pressed["border_radius"]))

        if self.data.indicator_indeterminate_pressed["padding_top_value"] != 0 and self.data.indicator_indeterminate_pressed["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_indeterminate_pressed["padding_top_value"], self.data.indicator_indeterminate_pressed["padding_top_type"]))

        if self.data.indicator_indeterminate_pressed["padding_right_value"] != 0 and self.data.indicator_indeterminate_pressed["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.indicator_indeterminate_pressed["padding_right_value"], self.data.indicator_indeterminate_pressed["padding_right_type"]))

        if self.data.indicator_indeterminate_pressed["padding_bottom_value"] != 0 and self.data.indicator_indeterminate_pressed["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.indicator_indeterminate_pressed["padding_bottom_value"], self.data.indicator_indeterminate_pressed["padding_bottom_type"]))

        if self.data.indicator_indeterminate_pressed["padding_left_value"] != 0 and self.data.indicator_indeterminate_pressed["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.indicator_indeterminate_pressed["padding_left_value"], self.data.indicator_indeterminate_pressed["padding_left_type"]))


        if self.data.indicator_indeterminate_pressed["margin_top_value"] != 0 and self.data.indicator_indeterminate_pressed["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_indeterminate_pressed["margin_top_value"], self.data.indicator_indeterminate_pressed["margin_top_type"]))

        if self.data.indicator_indeterminate_pressed["margin_right_value"] != 0 and self.data.indicator_indeterminate_pressed["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.indicator_indeterminate_pressed["margin_right_value"], self.data.indicator_indeterminate_pressed["margin_right_type"]))

        if self.data.indicator_indeterminate_pressed["margin_bottom_value"] != 0 and self.data.indicator_indeterminate_pressed["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.indicator_indeterminate_pressed["margin_bottom_value"], self.data.indicator_indeterminate_pressed["margin_bottom_type"]))

        if self.data.indicator_indeterminate_pressed["margin_left_value"] != 0 and self.data.indicator_indeterminate_pressed["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.indicator_indeterminate_pressed["margin_left_value"], self.data.indicator_indeterminate_pressed["margin_left_type"]))

        f.write("\n}")
