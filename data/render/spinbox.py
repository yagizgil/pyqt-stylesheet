class SpinBox():

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




        f.write(self.text + "::up-button {")

        if self.data.up_button["color"] != "":
            f.write("\n   color: {};".format(self.data.up_button["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.up_button["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.up_button["outline"]))

        if self.data.up_button["width_value"] != 0 and self.data.up_button["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.up_button["width_value"], self.data.up_button["width_type"]))

        if self.data.up_button["height_value"] != 0 and self.data.up_button["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.up_button["height_value"], self.data.up_button["height_type"]))

        if self.data.up_button["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.up_button["font_family"]))

        if self.data.up_button["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.up_button["font_size"]))

        if self.data.up_button["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.up_button["font_weight"]))

        if self.data.up_button["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.up_button["font_style"]))

        if self.data.up_button["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.up_button["line_height"]))

        if self.data.up_button["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.up_button["text_align"]))

        if self.data.up_button["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.up_button["text_decoration"]))

        if self.data.up_button["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.up_button["text_transform"]))

        if self.data.up_button["background"] != "":
            f.write("\n   background: {};".format(self.data.up_button["background"]))

        if self.data.up_button["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.up_button["background_image"]))

        if self.data.up_button["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.up_button["background_color"]))

        if self.data.up_button["border"] != "":
            f.write("\n   border: {};".format(self.data.up_button["border"]))

        if self.data.up_button["border_width_value"] != 0 and self.data.up_button["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.up_button["border_width_value"], self.data.up_button["border_width_type"]))

        if self.data.up_button["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.up_button["border_style"]))

        if self.data.up_button["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.up_button["border_color"]))

        if self.data.up_button["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.up_button["border_top"]))

        if self.data.up_button["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.up_button["border_right"]))

        if self.data.up_button["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.up_button["border_bottom"]))

        if self.data.up_button["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.up_button["border_left"]))

        if self.data.up_button["border_radius"] != 0 and self.data.up_button["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.up_button["border_radius"]))

        if self.data.up_button["padding_top_value"] != 0 and self.data.up_button["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.up_button["padding_top_value"], self.data.up_button["padding_top_type"]))

        if self.data.up_button["padding_right_value"] != 0 and self.data.up_button["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.up_button["padding_right_value"], self.data.up_button["padding_right_type"]))

        if self.data.up_button["padding_bottom_value"] != 0 and self.data.up_button["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.up_button["padding_bottom_value"], self.data.up_button["padding_bottom_type"]))

        if self.data.up_button["padding_left_value"] != 0 and self.data.up_button["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.up_button["padding_left_value"], self.data.up_button["padding_left_type"]))


        if self.data.up_button["margin_top_value"] != 0 and self.data.up_button["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.up_button["margin_top_value"], self.data.up_button["margin_top_type"]))

        if self.data.up_button["margin_right_value"] != 0 and self.data.up_button["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.up_button["margin_right_value"], self.data.up_button["margin_right_type"]))

        if self.data.up_button["margin_bottom_value"] != 0 and self.data.up_button["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.up_button["margin_bottom_value"], self.data.up_button["margin_bottom_type"]))

        if self.data.up_button["margin_left_value"] != 0 and self.data.up_button["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.up_button["margin_left_value"], self.data.up_button["margin_left_type"]))

        f.write("\n}")



        f.write("\n")




        f.write(self.text + "::up-button:hover {")

        if self.data.up_button_hover["color"] != "":
            f.write("\n   color: {};".format(self.data.up_button_hover["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.up_button_hover["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.up_button_hover["outline"]))

        if self.data.up_button_hover["width_value"] != 0 and self.data.up_button_hover["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.up_button_hover["width_value"], self.data.up_button_hover["width_type"]))

        if self.data.up_button_hover["height_value"] != 0 and self.data.up_button_hover["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.up_button_hover["height_value"], self.data.up_button_hover["height_type"]))

        if self.data.up_button_hover["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.up_button_hover["font_family"]))

        if self.data.up_button_hover["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.up_button_hover["font_size"]))

        if self.data.up_button_hover["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.up_button_hover["font_weight"]))

        if self.data.up_button_hover["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.up_button_hover["font_style"]))

        if self.data.up_button_hover["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.up_button_hover["line_height"]))

        if self.data.up_button_hover["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.up_button_hover["text_align"]))

        if self.data.up_button_hover["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.up_button_hover["text_decoration"]))

        if self.data.up_button_hover["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.up_button_hover["text_transform"]))

        if self.data.up_button_hover["background"] != "":
            f.write("\n   background: {};".format(self.data.up_button_hover["background"]))

        if self.data.up_button_hover["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.up_button_hover["background_image"]))

        if self.data.up_button_hover["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.up_button_hover["background_color"]))

        if self.data.up_button_hover["border"] != "":
            f.write("\n   border: {};".format(self.data.up_button_hover["border"]))

        if self.data.up_button_hover["border_width_value"] != 0 and self.data.up_button_hover["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.up_button_hover["border_width_value"], self.data.up_button_hover["border_width_type"]))

        if self.data.up_button_hover["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.up_button_hover["border_style"]))

        if self.data.up_button_hover["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.up_button_hover["border_color"]))

        if self.data.up_button_hover["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.up_button_hover["border_top"]))

        if self.data.up_button_hover["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.up_button_hover["border_right"]))

        if self.data.up_button_hover["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.up_button_hover["border_bottom"]))

        if self.data.up_button_hover["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.up_button_hover["border_left"]))

        if self.data.up_button_hover["border_radius"] != 0 and self.data.up_button_hover["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.up_button_hover["border_radius"]))

        if self.data.up_button_hover["padding_top_value"] != 0 and self.data.up_button_hover["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.up_button_hover["padding_top_value"], self.data.up_button_hover["padding_top_type"]))

        if self.data.up_button_hover["padding_right_value"] != 0 and self.data.up_button_hover["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.up_button_hover["padding_right_value"], self.data.up_button_hover["padding_right_type"]))

        if self.data.up_button_hover["padding_bottom_value"] != 0 and self.data.up_button_hover["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.up_button_hover["padding_bottom_value"], self.data.up_button_hover["padding_bottom_type"]))

        if self.data.up_button_hover["padding_left_value"] != 0 and self.data.up_button_hover["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.up_button_hover["padding_left_value"], self.data.up_button_hover["padding_left_type"]))


        if self.data.up_button_hover["margin_top_value"] != 0 and self.data.up_button_hover["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.up_button_hover["margin_top_value"], self.data.up_button_hover["margin_top_type"]))

        if self.data.up_button_hover["margin_right_value"] != 0 and self.data.up_button_hover["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.up_button_hover["margin_right_value"], self.data.up_button_hover["margin_right_type"]))

        if self.data.up_button_hover["margin_bottom_value"] != 0 and self.data.up_button_hover["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.up_button_hover["margin_bottom_value"], self.data.up_button_hover["margin_bottom_type"]))

        if self.data.up_button_hover["margin_left_value"] != 0 and self.data.up_button_hover["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.up_button_hover["margin_left_value"], self.data.up_button_hover["margin_left_type"]))

        f.write("\n}")




        f.write("\n")




        f.write(self.text + "::up-button:pressed {")

        if self.data.up_button_pressed["color"] != "":
            f.write("\n   color: {};".format(self.data.up_button_pressed["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.up_button_pressed["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.up_button_pressed["outline"]))

        if self.data.up_button_pressed["width_value"] != 0 and self.data.up_button_pressed["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.up_button_pressed["width_value"], self.data.up_button_pressed["width_type"]))

        if self.data.up_button_pressed["height_value"] != 0 and self.data.up_button_pressed["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.up_button_pressed["height_value"], self.data.up_button_pressed["height_type"]))

        if self.data.up_button_pressed["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.up_button_pressed["font_family"]))

        if self.data.up_button_pressed["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.up_button_pressed["font_size"]))

        if self.data.up_button_pressed["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.up_button_pressed["font_weight"]))

        if self.data.up_button_pressed["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.up_button_pressed["font_style"]))

        if self.data.up_button_pressed["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.up_button_pressed["line_height"]))

        if self.data.up_button_pressed["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.up_button_pressed["text_align"]))

        if self.data.up_button_pressed["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.up_button_pressed["text_decoration"]))

        if self.data.up_button_pressed["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.up_button_pressed["text_transform"]))

        if self.data.up_button_pressed["background"] != "":
            f.write("\n   background: {};".format(self.data.up_button_pressed["background"]))

        if self.data.up_button_pressed["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.up_button_pressed["background_image"]))

        if self.data.up_button_pressed["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.up_button_pressed["background_color"]))

        if self.data.up_button_pressed["border"] != "":
            f.write("\n   border: {};".format(self.data.up_button_pressed["border"]))

        if self.data.up_button_pressed["border_width_value"] != 0 and self.data.up_button_pressed["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.up_button_pressed["border_width_value"], self.data.up_button_pressed["border_width_type"]))

        if self.data.up_button_pressed["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.up_button_pressed["border_style"]))

        if self.data.up_button_pressed["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.up_button_pressed["border_color"]))

        if self.data.up_button_pressed["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.up_button_pressed["border_top"]))

        if self.data.up_button_pressed["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.up_button_pressed["border_right"]))

        if self.data.up_button_pressed["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.up_button_pressed["border_bottom"]))

        if self.data.up_button_pressed["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.up_button_pressed["border_left"]))

        if self.data.up_button_pressed["border_radius"] != 0 and self.data.up_button_pressed["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.up_button_pressed["border_radius"]))

        if self.data.up_button_pressed["padding_top_value"] != 0 and self.data.up_button_pressed["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.up_button_pressed["padding_top_value"], self.data.up_button_pressed["padding_top_type"]))

        if self.data.up_button_pressed["padding_right_value"] != 0 and self.data.up_button_pressed["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.up_button_pressed["padding_right_value"], self.data.up_button_pressed["padding_right_type"]))

        if self.data.up_button_pressed["padding_bottom_value"] != 0 and self.data.up_button_pressed["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.up_button_pressed["padding_bottom_value"], self.data.up_button_pressed["padding_bottom_type"]))

        if self.data.up_button_pressed["padding_left_value"] != 0 and self.data.up_button_pressed["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.up_button_pressed["padding_left_value"], self.data.up_button_pressed["padding_left_type"]))


        if self.data.up_button_pressed["margin_top_value"] != 0 and self.data.up_button_pressed["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.up_button_pressed["margin_top_value"], self.data.up_button_pressed["margin_top_type"]))

        if self.data.up_button_pressed["margin_right_value"] != 0 and self.data.up_button_pressed["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.up_button_pressed["margin_right_value"], self.data.up_button_pressed["margin_right_type"]))

        if self.data.up_button_pressed["margin_bottom_value"] != 0 and self.data.up_button_pressed["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.up_button_pressed["margin_bottom_value"], self.data.up_button_pressed["margin_bottom_type"]))

        if self.data.up_button_pressed["margin_left_value"] != 0 and self.data.up_button_pressed["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.up_button_pressed["margin_left_value"], self.data.up_button_pressed["margin_left_type"]))

        f.write("\n}")





        f.write("\n")




        f.write(self.text + "::up-arrow {")

        if self.data.up_arrow["color"] != "":
            f.write("\n   color: {};".format(self.data.up_arrow["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.up_arrow["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.up_arrow["outline"]))

        if self.data.up_arrow["width_value"] != 0 and self.data.up_arrow["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.up_arrow["width_value"], self.data.up_arrow["width_type"]))

        if self.data.up_arrow["height_value"] != 0 and self.data.up_arrow["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.up_arrow["height_value"], self.data.up_arrow["height_type"]))

        if self.data.up_arrow["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.up_arrow["font_family"]))

        if self.data.up_arrow["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.up_arrow["font_size"]))

        if self.data.up_arrow["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.up_arrow["font_weight"]))

        if self.data.up_arrow["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.up_arrow["font_style"]))

        if self.data.up_arrow["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.up_arrow["line_height"]))

        if self.data.up_arrow["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.up_arrow["text_align"]))

        if self.data.up_arrow["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.up_arrow["text_decoration"]))

        if self.data.up_arrow["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.up_arrow["text_transform"]))

        if self.data.up_arrow["background"] != "":
            f.write("\n   background: {};".format(self.data.up_arrow["background"]))

        if self.data.up_arrow["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.up_arrow["background_image"]))

        if self.data.up_arrow["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.up_arrow["background_color"]))

        if self.data.up_arrow["border"] != "":
            f.write("\n   border: {};".format(self.data.up_arrow["border"]))

        if self.data.up_arrow["border_width_value"] != 0 and self.data.up_arrow["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.up_arrow["border_width_value"], self.data.up_arrow["border_width_type"]))

        if self.data.up_arrow["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.up_arrow["border_style"]))

        if self.data.up_arrow["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.up_arrow["border_color"]))

        if self.data.up_arrow["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.up_arrow["border_top"]))

        if self.data.up_arrow["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.up_arrow["border_right"]))

        if self.data.up_arrow["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.up_arrow["border_bottom"]))

        if self.data.up_arrow["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.up_arrow["border_left"]))

        if self.data.up_arrow["border_radius"] != 0 and self.data.up_arrow["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.up_arrow["border_radius"]))

        if self.data.up_arrow["padding_top_value"] != 0 and self.data.up_arrow["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.up_arrow["padding_top_value"], self.data.up_arrow["padding_top_type"]))

        if self.data.up_arrow["padding_right_value"] != 0 and self.data.up_arrow["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.up_arrow["padding_right_value"], self.data.up_arrow["padding_right_type"]))

        if self.data.up_arrow["padding_bottom_value"] != 0 and self.data.up_arrow["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.up_arrow["padding_bottom_value"], self.data.up_arrow["padding_bottom_type"]))

        if self.data.up_arrow["padding_left_value"] != 0 and self.data.up_arrow["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.up_arrow["padding_left_value"], self.data.up_arrow["padding_left_type"]))


        if self.data.up_arrow["margin_top_value"] != 0 and self.data.up_arrow["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.up_arrow["margin_top_value"], self.data.up_arrow["margin_top_type"]))

        if self.data.up_arrow["margin_right_value"] != 0 and self.data.up_arrow["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.up_arrow["margin_right_value"], self.data.up_arrow["margin_right_type"]))

        if self.data.up_arrow["margin_bottom_value"] != 0 and self.data.up_arrow["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.up_arrow["margin_bottom_value"], self.data.up_arrow["margin_bottom_type"]))

        if self.data.up_arrow["margin_left_value"] != 0 and self.data.up_arrow["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.up_arrow["margin_left_value"], self.data.up_arrow["margin_left_type"]))

        f.write("\n}")




        f.write("\n")




        f.write(self.text + "::up-arrow:disabled {")

        if self.data.up_arrow_disabled["color"] != "":
            f.write("\n   color: {};".format(self.data.up_arrow_disabled["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.up_arrow_disabled["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.up_arrow_disabled["outline"]))

        if self.data.up_arrow_disabled["width_value"] != 0 and self.data.up_arrow_disabled["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.up_arrow_disabled["width_value"], self.data.up_arrow_disabled["width_type"]))

        if self.data.up_arrow_disabled["height_value"] != 0 and self.data.up_arrow_disabled["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.up_arrow_disabled["height_value"], self.data.up_arrow_disabled["height_type"]))

        if self.data.up_arrow_disabled["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.up_arrow_disabled["font_family"]))

        if self.data.up_arrow_disabled["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.up_arrow_disabled["font_size"]))

        if self.data.up_arrow_disabled["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.up_arrow_disabled["font_weight"]))

        if self.data.up_arrow_disabled["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.up_arrow_disabled["font_style"]))

        if self.data.up_arrow_disabled["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.up_arrow_disabled["line_height"]))

        if self.data.up_arrow_disabled["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.up_arrow_disabled["text_align"]))

        if self.data.up_arrow_disabled["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.up_arrow_disabled["text_decoration"]))

        if self.data.up_arrow_disabled["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.up_arrow_disabled["text_transform"]))

        if self.data.up_arrow_disabled["background"] != "":
            f.write("\n   background: {};".format(self.data.up_arrow_disabled["background"]))

        if self.data.up_arrow_disabled["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.up_arrow_disabled["background_image"]))

        if self.data.up_arrow_disabled["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.up_arrow_disabled["background_color"]))

        if self.data.up_arrow_disabled["border"] != "":
            f.write("\n   border: {};".format(self.data.up_arrow_disabled["border"]))

        if self.data.up_arrow_disabled["border_width_value"] != 0 and self.data.up_arrow_disabled["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.up_arrow_disabled["border_width_value"], self.data.up_arrow_disabled["border_width_type"]))

        if self.data.up_arrow_disabled["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.up_arrow_disabled["border_style"]))

        if self.data.up_arrow_disabled["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.up_arrow_disabled["border_color"]))

        if self.data.up_arrow_disabled["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.up_arrow_disabled["border_top"]))

        if self.data.up_arrow_disabled["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.up_arrow_disabled["border_right"]))

        if self.data.up_arrow_disabled["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.up_arrow_disabled["border_bottom"]))

        if self.data.up_arrow_disabled["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.up_arrow_disabled["border_left"]))

        if self.data.up_arrow_disabled["border_radius"] != 0 and self.data.up_arrow_disabled["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.up_arrow_disabled["border_radius"]))

        if self.data.up_arrow_disabled["padding_top_value"] != 0 and self.data.up_arrow_disabled["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.up_arrow_disabled["padding_top_value"], self.data.up_arrow_disabled["padding_top_type"]))

        if self.data.up_arrow_disabled["padding_right_value"] != 0 and self.data.up_arrow_disabled["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.up_arrow_disabled["padding_right_value"], self.data.up_arrow_disabled["padding_right_type"]))

        if self.data.up_arrow_disabled["padding_bottom_value"] != 0 and self.data.up_arrow_disabled["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.up_arrow_disabled["padding_bottom_value"], self.data.up_arrow_disabled["padding_bottom_type"]))

        if self.data.up_arrow_disabled["padding_left_value"] != 0 and self.data.up_arrow_disabled["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.up_arrow_disabled["padding_left_value"], self.data.up_arrow_disabled["padding_left_type"]))


        if self.data.up_arrow_disabled["margin_top_value"] != 0 and self.data.up_arrow_disabled["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.up_arrow_disabled["margin_top_value"], self.data.up_arrow_disabled["margin_top_type"]))

        if self.data.up_arrow_disabled["margin_right_value"] != 0 and self.data.up_arrow_disabled["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.up_arrow_disabled["margin_right_value"], self.data.up_arrow_disabled["margin_right_type"]))

        if self.data.up_arrow_disabled["margin_bottom_value"] != 0 and self.data.up_arrow_disabled["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.up_arrow_disabled["margin_bottom_value"], self.data.up_arrow_disabled["margin_bottom_type"]))

        if self.data.up_arrow_disabled["margin_left_value"] != 0 and self.data.up_arrow_disabled["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.up_arrow_disabled["margin_left_value"], self.data.up_arrow_disabled["margin_left_type"]))

        f.write("\n}")





        f.write("\n")




        f.write(self.text + "::up-arrow:off {")

        if self.data.up_arrow_off["color"] != "":
            f.write("\n   color: {};".format(self.data.up_arrow_off["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.up_arrow_off["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.up_arrow_off["outline"]))

        if self.data.up_arrow_off["width_value"] != 0 and self.data.up_arrow_off["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.up_arrow_off["width_value"], self.data.up_arrow_off["width_type"]))

        if self.data.up_arrow_off["height_value"] != 0 and self.data.up_arrow_off["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.up_arrow_off["height_value"], self.data.up_arrow_off["height_type"]))

        if self.data.up_arrow_off["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.up_arrow_off["font_family"]))

        if self.data.up_arrow_off["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.up_arrow_off["font_size"]))

        if self.data.up_arrow_off["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.up_arrow_off["font_weight"]))

        if self.data.up_arrow_off["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.up_arrow_off["font_style"]))

        if self.data.up_arrow_off["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.up_arrow_off["line_height"]))

        if self.data.up_arrow_off["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.up_arrow_off["text_align"]))

        if self.data.up_arrow_off["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.up_arrow_off["text_decoration"]))

        if self.data.up_arrow_off["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.up_arrow_off["text_transform"]))

        if self.data.up_arrow_off["background"] != "":
            f.write("\n   background: {};".format(self.data.up_arrow_off["background"]))

        if self.data.up_arrow_off["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.up_arrow_off["background_image"]))

        if self.data.up_arrow_off["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.up_arrow_off["background_color"]))

        if self.data.up_arrow_off["border"] != "":
            f.write("\n   border: {};".format(self.data.up_arrow_off["border"]))

        if self.data.up_arrow_off["border_width_value"] != 0 and self.data.up_arrow_off["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.up_arrow_off["border_width_value"], self.data.up_arrow_off["border_width_type"]))

        if self.data.up_arrow_off["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.up_arrow_off["border_style"]))

        if self.data.up_arrow_off["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.up_arrow_off["border_color"]))

        if self.data.up_arrow_off["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.up_arrow_off["border_top"]))

        if self.data.up_arrow_off["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.up_arrow_off["border_right"]))

        if self.data.up_arrow_off["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.up_arrow_off["border_bottom"]))

        if self.data.up_arrow_off["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.up_arrow_off["border_left"]))

        if self.data.up_arrow_off["border_radius"] != 0 and self.data.up_arrow_off["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.up_arrow_off["border_radius"]))

        if self.data.up_arrow_off["padding_top_value"] != 0 and self.data.up_arrow_off["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.up_arrow_off["padding_top_value"], self.data.up_arrow_off["padding_top_type"]))

        if self.data.up_arrow_off["padding_right_value"] != 0 and self.data.up_arrow_off["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.up_arrow_off["padding_right_value"], self.data.up_arrow_off["padding_right_type"]))

        if self.data.up_arrow_off["padding_bottom_value"] != 0 and self.data.up_arrow_off["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.up_arrow_off["padding_bottom_value"], self.data.up_arrow_off["padding_bottom_type"]))

        if self.data.up_arrow_off["padding_left_value"] != 0 and self.data.up_arrow_off["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.up_arrow_off["padding_left_value"], self.data.up_arrow_off["padding_left_type"]))


        if self.data.up_arrow_off["margin_top_value"] != 0 and self.data.up_arrow_off["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.up_arrow_off["margin_top_value"], self.data.up_arrow_off["margin_top_type"]))

        if self.data.up_arrow_off["margin_right_value"] != 0 and self.data.up_arrow_off["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.up_arrow_off["margin_right_value"], self.data.up_arrow_off["margin_right_type"]))

        if self.data.up_arrow_off["margin_bottom_value"] != 0 and self.data.up_arrow_off["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.up_arrow_off["margin_bottom_value"], self.data.up_arrow_off["margin_bottom_type"]))

        if self.data.up_arrow_off["margin_left_value"] != 0 and self.data.up_arrow_off["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.up_arrow_off["margin_left_value"], self.data.up_arrow_off["margin_left_type"]))

        f.write("\n}")


        f.write("\n")




        f.write(self.text + "::down-button {")

        if self.data.down_button["color"] != "":
            f.write("\n   color: {};".format(self.data.down_button["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.down_button["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.down_button["outline"]))

        if self.data.down_button["width_value"] != 0 and self.data.down_button["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.down_button["width_value"], self.data.down_button["width_type"]))

        if self.data.down_button["height_value"] != 0 and self.data.down_button["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.down_button["height_value"], self.data.down_button["height_type"]))

        if self.data.down_button["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.down_button["font_family"]))

        if self.data.down_button["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.down_button["font_size"]))

        if self.data.down_button["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.down_button["font_weight"]))

        if self.data.down_button["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.down_button["font_style"]))

        if self.data.down_button["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.down_button["line_height"]))

        if self.data.down_button["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.down_button["text_align"]))

        if self.data.down_button["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.down_button["text_decoration"]))

        if self.data.down_button["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.down_button["text_transform"]))

        if self.data.down_button["background"] != "":
            f.write("\n   background: {};".format(self.data.down_button["background"]))

        if self.data.down_button["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.down_button["background_image"]))

        if self.data.down_button["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.down_button["background_color"]))

        if self.data.down_button["border"] != "":
            f.write("\n   border: {};".format(self.data.down_button["border"]))

        if self.data.down_button["border_width_value"] != 0 and self.data.down_button["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.down_button["border_width_value"], self.data.down_button["border_width_type"]))

        if self.data.down_button["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.down_button["border_style"]))

        if self.data.down_button["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.down_button["border_color"]))

        if self.data.down_button["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.down_button["border_top"]))

        if self.data.down_button["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.down_button["border_right"]))

        if self.data.down_button["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.down_button["border_bottom"]))

        if self.data.down_button["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.down_button["border_left"]))

        if self.data.down_button["border_radius"] != 0 and self.data.down_button["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.down_button["border_radius"]))

        if self.data.down_button["padding_top_value"] != 0 and self.data.down_button["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.down_button["padding_top_value"], self.data.down_button["padding_top_type"]))

        if self.data.down_button["padding_right_value"] != 0 and self.data.down_button["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.down_button["padding_right_value"], self.data.down_button["padding_right_type"]))

        if self.data.down_button["padding_bottom_value"] != 0 and self.data.down_button["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.down_button["padding_bottom_value"], self.data.down_button["padding_bottom_type"]))

        if self.data.down_button["padding_left_value"] != 0 and self.data.down_button["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.down_button["padding_left_value"], self.data.down_button["padding_left_type"]))


        if self.data.down_button["margin_top_value"] != 0 and self.data.down_button["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.down_button["margin_top_value"], self.data.down_button["margin_top_type"]))

        if self.data.down_button["margin_right_value"] != 0 and self.data.down_button["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.down_button["margin_right_value"], self.data.down_button["margin_right_type"]))

        if self.data.down_button["margin_bottom_value"] != 0 and self.data.down_button["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.down_button["margin_bottom_value"], self.data.down_button["margin_bottom_type"]))

        if self.data.down_button["margin_left_value"] != 0 and self.data.down_button["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.down_button["margin_left_value"], self.data.down_button["margin_left_type"]))

        f.write("\n}")



        f.write("\n")




        f.write(self.text + "::down-button:hover {")

        if self.data.down_button_hover["color"] != "":
            f.write("\n   color: {};".format(self.data.down_button_hover["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.down_button_hover["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.down_button_hover["outline"]))

        if self.data.down_button_hover["width_value"] != 0 and self.data.down_button_hover["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.down_button_hover["width_value"], self.data.down_button_hover["width_type"]))

        if self.data.down_button_hover["height_value"] != 0 and self.data.down_button_hover["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.down_button_hover["height_value"], self.data.down_button_hover["height_type"]))

        if self.data.down_button_hover["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.down_button_hover["font_family"]))

        if self.data.down_button_hover["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.down_button_hover["font_size"]))

        if self.data.down_button_hover["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.down_button_hover["font_weight"]))

        if self.data.down_button_hover["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.down_button_hover["font_style"]))

        if self.data.down_button_hover["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.down_button_hover["line_height"]))

        if self.data.down_button_hover["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.down_button_hover["text_align"]))

        if self.data.down_button_hover["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.down_button_hover["text_decoration"]))

        if self.data.down_button_hover["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.down_button_hover["text_transform"]))

        if self.data.down_button_hover["background"] != "":
            f.write("\n   background: {};".format(self.data.down_button_hover["background"]))

        if self.data.down_button_hover["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.down_button_hover["background_image"]))

        if self.data.down_button_hover["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.down_button_hover["background_color"]))

        if self.data.down_button_hover["border"] != "":
            f.write("\n   border: {};".format(self.data.down_button_hover["border"]))

        if self.data.down_button_hover["border_width_value"] != 0 and self.data.down_button_hover["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.down_button_hover["border_width_value"], self.data.down_button_hover["border_width_type"]))

        if self.data.down_button_hover["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.down_button_hover["border_style"]))

        if self.data.down_button_hover["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.down_button_hover["border_color"]))

        if self.data.down_button_hover["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.down_button_hover["border_top"]))

        if self.data.down_button_hover["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.down_button_hover["border_right"]))

        if self.data.down_button_hover["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.down_button_hover["border_bottom"]))

        if self.data.down_button_hover["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.down_button_hover["border_left"]))

        if self.data.down_button_hover["border_radius"] != 0 and self.data.down_button_hover["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.down_button_hover["border_radius"]))

        if self.data.down_button_hover["padding_top_value"] != 0 and self.data.down_button_hover["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.down_button_hover["padding_top_value"], self.data.down_button_hover["padding_top_type"]))

        if self.data.down_button_hover["padding_right_value"] != 0 and self.data.down_button_hover["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.down_button_hover["padding_right_value"], self.data.down_button_hover["padding_right_type"]))

        if self.data.down_button_hover["padding_bottom_value"] != 0 and self.data.down_button_hover["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.down_button_hover["padding_bottom_value"], self.data.down_button_hover["padding_bottom_type"]))

        if self.data.down_button_hover["padding_left_value"] != 0 and self.data.down_button_hover["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.down_button_hover["padding_left_value"], self.data.down_button_hover["padding_left_type"]))


        if self.data.down_button_hover["margin_top_value"] != 0 and self.data.down_button_hover["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.down_button_hover["margin_top_value"], self.data.down_button_hover["margin_top_type"]))

        if self.data.down_button_hover["margin_right_value"] != 0 and self.data.down_button_hover["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.down_button_hover["margin_right_value"], self.data.down_button_hover["margin_right_type"]))

        if self.data.down_button_hover["margin_bottom_value"] != 0 and self.data.down_button_hover["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.down_button_hover["margin_bottom_value"], self.data.down_button_hover["margin_bottom_type"]))

        if self.data.down_button_hover["margin_left_value"] != 0 and self.data.down_button_hover["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.down_button_hover["margin_left_value"], self.data.down_button_hover["margin_left_type"]))

        f.write("\n}")




        f.write("\n")




        f.write(self.text + "::down-button:pressed {")

        if self.data.down_button_pressed["color"] != "":
            f.write("\n   color: {};".format(self.data.down_button_pressed["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.down_button_pressed["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.down_button_pressed["outline"]))

        if self.data.down_button_pressed["width_value"] != 0 and self.data.down_button_pressed["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.down_button_pressed["width_value"], self.data.down_button_pressed["width_type"]))

        if self.data.down_button_pressed["height_value"] != 0 and self.data.down_button_pressed["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.down_button_pressed["height_value"], self.data.down_button_pressed["height_type"]))

        if self.data.down_button_pressed["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.down_button_pressed["font_family"]))

        if self.data.down_button_pressed["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.down_button_pressed["font_size"]))

        if self.data.down_button_pressed["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.down_button_pressed["font_weight"]))

        if self.data.down_button_pressed["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.down_button_pressed["font_style"]))

        if self.data.down_button_pressed["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.down_button_pressed["line_height"]))

        if self.data.down_button_pressed["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.down_button_pressed["text_align"]))

        if self.data.down_button_pressed["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.down_button_pressed["text_decoration"]))

        if self.data.down_button_pressed["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.down_button_pressed["text_transform"]))

        if self.data.down_button_pressed["background"] != "":
            f.write("\n   background: {};".format(self.data.down_button_pressed["background"]))

        if self.data.down_button_pressed["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.down_button_pressed["background_image"]))

        if self.data.down_button_pressed["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.down_button_pressed["background_color"]))

        if self.data.down_button_pressed["border"] != "":
            f.write("\n   border: {};".format(self.data.down_button_pressed["border"]))

        if self.data.down_button_pressed["border_width_value"] != 0 and self.data.down_button_pressed["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.down_button_pressed["border_width_value"], self.data.down_button_pressed["border_width_type"]))

        if self.data.down_button_pressed["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.down_button_pressed["border_style"]))

        if self.data.down_button_pressed["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.down_button_pressed["border_color"]))

        if self.data.down_button_pressed["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.down_button_pressed["border_top"]))

        if self.data.down_button_pressed["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.down_button_pressed["border_right"]))

        if self.data.down_button_pressed["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.down_button_pressed["border_bottom"]))

        if self.data.down_button_pressed["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.down_button_pressed["border_left"]))

        if self.data.down_button_pressed["border_radius"] != 0 and self.data.down_button_pressed["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.down_button_pressed["border_radius"]))

        if self.data.down_button_pressed["padding_top_value"] != 0 and self.data.down_button_pressed["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.down_button_pressed["padding_top_value"], self.data.down_button_pressed["padding_top_type"]))

        if self.data.down_button_pressed["padding_right_value"] != 0 and self.data.down_button_pressed["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.down_button_pressed["padding_right_value"], self.data.down_button_pressed["padding_right_type"]))

        if self.data.down_button_pressed["padding_bottom_value"] != 0 and self.data.down_button_pressed["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.down_button_pressed["padding_bottom_value"], self.data.down_button_pressed["padding_bottom_type"]))

        if self.data.down_button_pressed["padding_left_value"] != 0 and self.data.down_button_pressed["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.down_button_pressed["padding_left_value"], self.data.down_button_pressed["padding_left_type"]))


        if self.data.down_button_pressed["margin_top_value"] != 0 and self.data.down_button_pressed["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.down_button_pressed["margin_top_value"], self.data.down_button_pressed["margin_top_type"]))

        if self.data.down_button_pressed["margin_right_value"] != 0 and self.data.down_button_pressed["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.down_button_pressed["margin_right_value"], self.data.down_button_pressed["margin_right_type"]))

        if self.data.down_button_pressed["margin_bottom_value"] != 0 and self.data.down_button_pressed["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.down_button_pressed["margin_bottom_value"], self.data.down_button_pressed["margin_bottom_type"]))

        if self.data.down_button_pressed["margin_left_value"] != 0 and self.data.down_button_pressed["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.down_button_pressed["margin_left_value"], self.data.down_button_pressed["margin_left_type"]))

        f.write("\n}")





        f.write("\n")




        f.write(self.text + "::down-arrow {")

        if self.data.down_arrow["color"] != "":
            f.write("\n   color: {};".format(self.data.down_arrow["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.down_arrow["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.down_arrow["outline"]))

        if self.data.down_arrow["width_value"] != 0 and self.data.down_arrow["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.down_arrow["width_value"], self.data.down_arrow["width_type"]))

        if self.data.down_arrow["height_value"] != 0 and self.data.down_arrow["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.down_arrow["height_value"], self.data.down_arrow["height_type"]))

        if self.data.down_arrow["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.down_arrow["font_family"]))

        if self.data.down_arrow["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.down_arrow["font_size"]))

        if self.data.down_arrow["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.down_arrow["font_weight"]))

        if self.data.down_arrow["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.down_arrow["font_style"]))

        if self.data.down_arrow["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.down_arrow["line_height"]))

        if self.data.down_arrow["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.down_arrow["text_align"]))

        if self.data.down_arrow["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.down_arrow["text_decoration"]))

        if self.data.down_arrow["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.down_arrow["text_transform"]))

        if self.data.down_arrow["background"] != "":
            f.write("\n   background: {};".format(self.data.down_arrow["background"]))

        if self.data.down_arrow["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.down_arrow["background_image"]))

        if self.data.down_arrow["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.down_arrow["background_color"]))

        if self.data.down_arrow["border"] != "":
            f.write("\n   border: {};".format(self.data.down_arrow["border"]))

        if self.data.down_arrow["border_width_value"] != 0 and self.data.down_arrow["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.down_arrow["border_width_value"], self.data.down_arrow["border_width_type"]))

        if self.data.down_arrow["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.down_arrow["border_style"]))

        if self.data.down_arrow["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.down_arrow["border_color"]))

        if self.data.down_arrow["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.down_arrow["border_top"]))

        if self.data.down_arrow["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.down_arrow["border_right"]))

        if self.data.down_arrow["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.down_arrow["border_bottom"]))

        if self.data.down_arrow["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.down_arrow["border_left"]))

        if self.data.down_arrow["border_radius"] != 0 and self.data.down_arrow["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.down_arrow["border_radius"]))

        if self.data.down_arrow["padding_top_value"] != 0 and self.data.down_arrow["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.down_arrow["padding_top_value"], self.data.down_arrow["padding_top_type"]))

        if self.data.down_arrow["padding_right_value"] != 0 and self.data.down_arrow["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.down_arrow["padding_right_value"], self.data.down_arrow["padding_right_type"]))

        if self.data.down_arrow["padding_bottom_value"] != 0 and self.data.down_arrow["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.down_arrow["padding_bottom_value"], self.data.down_arrow["padding_bottom_type"]))

        if self.data.down_arrow["padding_left_value"] != 0 and self.data.down_arrow["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.down_arrow["padding_left_value"], self.data.down_arrow["padding_left_type"]))


        if self.data.down_arrow["margin_top_value"] != 0 and self.data.down_arrow["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.down_arrow["margin_top_value"], self.data.down_arrow["margin_top_type"]))

        if self.data.down_arrow["margin_right_value"] != 0 and self.data.down_arrow["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.down_arrow["margin_right_value"], self.data.down_arrow["margin_right_type"]))

        if self.data.down_arrow["margin_bottom_value"] != 0 and self.data.down_arrow["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.down_arrow["margin_bottom_value"], self.data.down_arrow["margin_bottom_type"]))

        if self.data.down_arrow["margin_left_value"] != 0 and self.data.down_arrow["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.down_arrow["margin_left_value"], self.data.down_arrow["margin_left_type"]))

        f.write("\n}")




        f.write("\n")




        f.write(self.text + "::down-arrow:disabled {")

        if self.data.down_arrow_disabled["color"] != "":
            f.write("\n   color: {};".format(self.data.down_arrow_disabled["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.down_arrow_disabled["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.down_arrow_disabled["outline"]))

        if self.data.down_arrow_disabled["width_value"] != 0 and self.data.down_arrow_disabled["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.down_arrow_disabled["width_value"], self.data.down_arrow_disabled["width_type"]))

        if self.data.down_arrow_disabled["height_value"] != 0 and self.data.down_arrow_disabled["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.down_arrow_disabled["height_value"], self.data.down_arrow_disabled["height_type"]))

        if self.data.down_arrow_disabled["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.down_arrow_disabled["font_family"]))

        if self.data.down_arrow_disabled["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.down_arrow_disabled["font_size"]))

        if self.data.down_arrow_disabled["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.down_arrow_disabled["font_weight"]))

        if self.data.down_arrow_disabled["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.down_arrow_disabled["font_style"]))

        if self.data.down_arrow_disabled["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.down_arrow_disabled["line_height"]))

        if self.data.down_arrow_disabled["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.down_arrow_disabled["text_align"]))

        if self.data.down_arrow_disabled["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.down_arrow_disabled["text_decoration"]))

        if self.data.down_arrow_disabled["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.down_arrow_disabled["text_transform"]))

        if self.data.down_arrow_disabled["background"] != "":
            f.write("\n   background: {};".format(self.data.down_arrow_disabled["background"]))

        if self.data.down_arrow_disabled["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.down_arrow_disabled["background_image"]))

        if self.data.down_arrow_disabled["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.down_arrow_disabled["background_color"]))

        if self.data.down_arrow_disabled["border"] != "":
            f.write("\n   border: {};".format(self.data.down_arrow_disabled["border"]))

        if self.data.down_arrow_disabled["border_width_value"] != 0 and self.data.down_arrow_disabled["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.down_arrow_disabled["border_width_value"], self.data.down_arrow_disabled["border_width_type"]))

        if self.data.down_arrow_disabled["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.down_arrow_disabled["border_style"]))

        if self.data.down_arrow_disabled["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.down_arrow_disabled["border_color"]))

        if self.data.down_arrow_disabled["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.down_arrow_disabled["border_top"]))

        if self.data.down_arrow_disabled["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.down_arrow_disabled["border_right"]))

        if self.data.down_arrow_disabled["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.down_arrow_disabled["border_bottom"]))

        if self.data.down_arrow_disabled["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.down_arrow_disabled["border_left"]))

        if self.data.down_arrow_disabled["border_radius"] != 0 and self.data.down_arrow_disabled["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.down_arrow_disabled["border_radius"]))

        if self.data.down_arrow_disabled["padding_top_value"] != 0 and self.data.down_arrow_disabled["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.down_arrow_disabled["padding_top_value"], self.data.down_arrow_disabled["padding_top_type"]))

        if self.data.down_arrow_disabled["padding_right_value"] != 0 and self.data.down_arrow_disabled["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.down_arrow_disabled["padding_right_value"], self.data.down_arrow_disabled["padding_right_type"]))

        if self.data.down_arrow_disabled["padding_bottom_value"] != 0 and self.data.down_arrow_disabled["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.down_arrow_disabled["padding_bottom_value"], self.data.down_arrow_disabled["padding_bottom_type"]))

        if self.data.down_arrow_disabled["padding_left_value"] != 0 and self.data.down_arrow_disabled["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.down_arrow_disabled["padding_left_value"], self.data.down_arrow_disabled["padding_left_type"]))


        if self.data.down_arrow_disabled["margin_top_value"] != 0 and self.data.down_arrow_disabled["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.down_arrow_disabled["margin_top_value"], self.data.down_arrow_disabled["margin_top_type"]))

        if self.data.down_arrow_disabled["margin_right_value"] != 0 and self.data.down_arrow_disabled["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.down_arrow_disabled["margin_right_value"], self.data.down_arrow_disabled["margin_right_type"]))

        if self.data.down_arrow_disabled["margin_bottom_value"] != 0 and self.data.down_arrow_disabled["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.down_arrow_disabled["margin_bottom_value"], self.data.down_arrow_disabled["margin_bottom_type"]))

        if self.data.down_arrow_disabled["margin_left_value"] != 0 and self.data.down_arrow_disabled["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.down_arrow_disabled["margin_left_value"], self.data.down_arrow_disabled["margin_left_type"]))

        f.write("\n}")





        f.write("\n")




        f.write(self.text + "::down-arrow:off {")

        if self.data.down_arrow_off["color"] != "":
            f.write("\n   color: {};".format(self.data.down_arrow_off["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.down_arrow_off["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.down_arrow_off["outline"]))

        if self.data.down_arrow_off["width_value"] != 0 and self.data.down_arrow_off["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.down_arrow_off["width_value"], self.data.down_arrow_off["width_type"]))

        if self.data.down_arrow_off["height_value"] != 0 and self.data.down_arrow_off["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.down_arrow_off["height_value"], self.data.down_arrow_off["height_type"]))

        if self.data.down_arrow_off["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.down_arrow_off["font_family"]))

        if self.data.down_arrow_off["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.down_arrow_off["font_size"]))

        if self.data.down_arrow_off["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.down_arrow_off["font_weight"]))

        if self.data.down_arrow_off["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.down_arrow_off["font_style"]))

        if self.data.down_arrow_off["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.down_arrow_off["line_height"]))

        if self.data.down_arrow_off["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.down_arrow_off["text_align"]))

        if self.data.down_arrow_off["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.down_arrow_off["text_decoration"]))

        if self.data.down_arrow_off["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.down_arrow_off["text_transform"]))

        if self.data.down_arrow_off["background"] != "":
            f.write("\n   background: {};".format(self.data.down_arrow_off["background"]))

        if self.data.down_arrow_off["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.down_arrow_off["background_image"]))

        if self.data.down_arrow_off["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.down_arrow_off["background_color"]))

        if self.data.down_arrow_off["border"] != "":
            f.write("\n   border: {};".format(self.data.down_arrow_off["border"]))

        if self.data.down_arrow_off["border_width_value"] != 0 and self.data.down_arrow_off["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.down_arrow_off["border_width_value"], self.data.down_arrow_off["border_width_type"]))

        if self.data.down_arrow_off["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.down_arrow_off["border_style"]))

        if self.data.down_arrow_off["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.down_arrow_off["border_color"]))

        if self.data.down_arrow_off["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.down_arrow_off["border_top"]))

        if self.data.down_arrow_off["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.down_arrow_off["border_right"]))

        if self.data.down_arrow_off["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.down_arrow_off["border_bottom"]))

        if self.data.down_arrow_off["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.down_arrow_off["border_left"]))

        if self.data.down_arrow_off["border_radius"] != 0 and self.data.down_arrow_off["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.down_arrow_off["border_radius"]))

        if self.data.down_arrow_off["padding_top_value"] != 0 and self.data.down_arrow_off["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.down_arrow_off["padding_top_value"], self.data.down_arrow_off["padding_top_type"]))

        if self.data.down_arrow_off["padding_right_value"] != 0 and self.data.down_arrow_off["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.down_arrow_off["padding_right_value"], self.data.down_arrow_off["padding_right_type"]))

        if self.data.down_arrow_off["padding_bottom_value"] != 0 and self.data.down_arrow_off["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.down_arrow_off["padding_bottom_value"], self.data.down_arrow_off["padding_bottom_type"]))

        if self.data.down_arrow_off["padding_left_value"] != 0 and self.data.down_arrow_off["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.down_arrow_off["padding_left_value"], self.data.down_arrow_off["padding_left_type"]))


        if self.data.down_arrow_off["margin_top_value"] != 0 and self.data.down_arrow_off["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.down_arrow_off["margin_top_value"], self.data.down_arrow_off["margin_top_type"]))

        if self.data.down_arrow_off["margin_right_value"] != 0 and self.data.down_arrow_off["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.down_arrow_off["margin_right_value"], self.data.down_arrow_off["margin_right_type"]))

        if self.data.down_arrow_off["margin_bottom_value"] != 0 and self.data.down_arrow_off["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.down_arrow_off["margin_bottom_value"], self.data.down_arrow_off["margin_bottom_type"]))

        if self.data.down_arrow_off["margin_left_value"] != 0 and self.data.down_arrow_off["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.down_arrow_off["margin_left_value"], self.data.down_arrow_off["margin_left_type"]))

        f.write("\n}")
