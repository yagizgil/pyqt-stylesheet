class Slider():

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





        f.write(self.text + ":vertical {")

        if self.data.vertical["color"] != "":
            f.write("\n   color: {};".format(self.data.vertical["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.vertical["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.vertical["outline"]))

        if self.data.vertical["width_value"] != 0 and self.data.vertical["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.vertical["width_value"], self.data.vertical["width_type"]))

        if self.data.vertical["height_value"] != 0 and self.data.vertical["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.vertical["height_value"], self.data.vertical["height_type"]))

        if self.data.vertical["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.vertical["font_family"]))

        if self.data.vertical["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.vertical["font_size"]))

        if self.data.vertical["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.vertical["font_weight"]))

        if self.data.vertical["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.vertical["font_style"]))

        if self.data.vertical["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.vertical["line_height"]))

        if self.data.vertical["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.vertical["text_align"]))

        if self.data.vertical["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.vertical["text_decoration"]))

        if self.data.vertical["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.vertical["text_transform"]))

        if self.data.vertical["background"] != "":
            f.write("\n   background: {};".format(self.data.vertical["background"]))

        if self.data.vertical["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.vertical["background_image"]))

        if self.data.vertical["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.vertical["background_color"]))

        if self.data.vertical["border"] != "":
            f.write("\n   border: {};".format(self.data.vertical["border"]))

        if self.data.vertical["border_width_value"] != 0 and self.data.vertical["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.vertical["border_width_value"], self.data.vertical["border_width_type"]))

        if self.data.vertical["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.vertical["border_style"]))

        if self.data.vertical["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.vertical["border_color"]))

        if self.data.vertical["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.vertical["border_top"]))

        if self.data.vertical["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.vertical["border_right"]))

        if self.data.vertical["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.vertical["border_bottom"]))

        if self.data.vertical["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.vertical["border_left"]))

        if self.data.vertical["border_radius"] != 0 and self.data.vertical["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.vertical["border_radius"]))

        if self.data.vertical["padding_top_value"] != 0 and self.data.vertical["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.vertical["padding_top_value"], self.data.vertical["padding_top_type"]))

        if self.data.vertical["padding_right_value"] != 0 and self.data.vertical["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.vertical["padding_right_value"], self.data.vertical["padding_right_type"]))

        if self.data.vertical["padding_bottom_value"] != 0 and self.data.vertical["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.vertical["padding_bottom_value"], self.data.vertical["padding_bottom_type"]))

        if self.data.vertical["padding_left_value"] != 0 and self.data.vertical["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.vertical["padding_left_value"], self.data.vertical["padding_left_type"]))


        if self.data.vertical["margin_top_value"] != 0 and self.data.vertical["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.vertical["margin_top_value"], self.data.vertical["margin_top_type"]))

        if self.data.vertical["margin_right_value"] != 0 and self.data.vertical["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.vertical["margin_right_value"], self.data.vertical["margin_right_type"]))

        if self.data.vertical["margin_bottom_value"] != 0 and self.data.vertical["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.vertical["margin_bottom_value"], self.data.vertical["margin_bottom_type"]))

        if self.data.vertical["margin_left_value"] != 0 and self.data.vertical["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.vertical["margin_left_value"], self.data.vertical["margin_left_type"]))

        f.write("\n}")





        f.write("\n")





        f.write(self.text + "::groove:vertical {")

        if self.data.groove_vertical["color"] != "":
            f.write("\n   color: {};".format(self.data.groove_vertical["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.groove_vertical["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.groove_vertical["outline"]))

        if self.data.groove_vertical["width_value"] != 0 and self.data.groove_vertical["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.groove_vertical["width_value"], self.data.groove_vertical["width_type"]))

        if self.data.groove_vertical["height_value"] != 0 and self.data.groove_vertical["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.groove_vertical["height_value"], self.data.groove_vertical["height_type"]))

        if self.data.groove_vertical["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.groove_vertical["font_family"]))

        if self.data.groove_vertical["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.groove_vertical["font_size"]))

        if self.data.groove_vertical["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.groove_vertical["font_weight"]))

        if self.data.groove_vertical["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.groove_vertical["font_style"]))

        if self.data.groove_vertical["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.groove_vertical["line_height"]))

        if self.data.groove_vertical["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.groove_vertical["text_align"]))

        if self.data.groove_vertical["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.groove_vertical["text_decoration"]))

        if self.data.groove_vertical["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.groove_vertical["text_transform"]))

        if self.data.groove_vertical["background"] != "":
            f.write("\n   background: {};".format(self.data.groove_vertical["background"]))

        if self.data.groove_vertical["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.groove_vertical["background_image"]))

        if self.data.groove_vertical["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.groove_vertical["background_color"]))

        if self.data.groove_vertical["border"] != "":
            f.write("\n   border: {};".format(self.data.groove_vertical["border"]))

        if self.data.groove_vertical["border_width_value"] != 0 and self.data.groove_vertical["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.groove_vertical["border_width_value"], self.data.groove_vertical["border_width_type"]))

        if self.data.groove_vertical["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.groove_vertical["border_style"]))

        if self.data.groove_vertical["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.groove_vertical["border_color"]))

        if self.data.groove_vertical["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.groove_vertical["border_top"]))

        if self.data.groove_vertical["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.groove_vertical["border_right"]))

        if self.data.groove_vertical["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.groove_vertical["border_bottom"]))

        if self.data.groove_vertical["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.groove_vertical["border_left"]))

        if self.data.groove_vertical["border_radius"] != 0 and self.data.groove_vertical["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.groove_vertical["border_radius"]))

        if self.data.groove_vertical["padding_top_value"] != 0 and self.data.groove_vertical["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.groove_vertical["padding_top_value"], self.data.groove_vertical["padding_top_type"]))

        if self.data.groove_vertical["padding_right_value"] != 0 and self.data.groove_vertical["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.groove_vertical["padding_right_value"], self.data.groove_vertical["padding_right_type"]))

        if self.data.groove_vertical["padding_bottom_value"] != 0 and self.data.groove_vertical["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.groove_vertical["padding_bottom_value"], self.data.groove_vertical["padding_bottom_type"]))

        if self.data.groove_vertical["padding_left_value"] != 0 and self.data.groove_vertical["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.groove_vertical["padding_left_value"], self.data.groove_vertical["padding_left_type"]))


        if self.data.groove_vertical["margin_top_value"] != 0 and self.data.groove_vertical["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.groove_vertical["margin_top_value"], self.data.groove_vertical["margin_top_type"]))

        if self.data.groove_vertical["margin_right_value"] != 0 and self.data.groove_vertical["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.groove_vertical["margin_right_value"], self.data.groove_vertical["margin_right_type"]))

        if self.data.groove_vertical["margin_bottom_value"] != 0 and self.data.groove_vertical["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.groove_vertical["margin_bottom_value"], self.data.groove_vertical["margin_bottom_type"]))

        if self.data.groove_vertical["margin_left_value"] != 0 and self.data.groove_vertical["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.groove_vertical["margin_left_value"], self.data.groove_vertical["margin_left_type"]))

        f.write("\n}")




        f.write("\n")





        f.write(self.text + "::handle:vertical {")

        if self.data.handle_vertical["color"] != "":
            f.write("\n   color: {};".format(self.data.handle_vertical["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.handle_vertical["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.handle_vertical["outline"]))

        if self.data.handle_vertical["width_value"] != 0 and self.data.handle_vertical["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.handle_vertical["width_value"], self.data.handle_vertical["width_type"]))

        if self.data.handle_vertical["height_value"] != 0 and self.data.handle_vertical["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.handle_vertical["height_value"], self.data.handle_vertical["height_type"]))

        if self.data.handle_vertical["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.handle_vertical["font_family"]))

        if self.data.handle_vertical["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.handle_vertical["font_size"]))

        if self.data.handle_vertical["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.handle_vertical["font_weight"]))

        if self.data.handle_vertical["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.handle_vertical["font_style"]))

        if self.data.handle_vertical["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.handle_vertical["line_height"]))

        if self.data.handle_vertical["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.handle_vertical["text_align"]))

        if self.data.handle_vertical["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.handle_vertical["text_decoration"]))

        if self.data.handle_vertical["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.handle_vertical["text_transform"]))

        if self.data.handle_vertical["background"] != "":
            f.write("\n   background: {};".format(self.data.handle_vertical["background"]))

        if self.data.handle_vertical["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.handle_vertical["background_image"]))

        if self.data.handle_vertical["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.handle_vertical["background_color"]))

        if self.data.handle_vertical["border"] != "":
            f.write("\n   border: {};".format(self.data.handle_vertical["border"]))

        if self.data.handle_vertical["border_width_value"] != 0 and self.data.handle_vertical["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.handle_vertical["border_width_value"], self.data.handle_vertical["border_width_type"]))

        if self.data.handle_vertical["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.handle_vertical["border_style"]))

        if self.data.handle_vertical["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.handle_vertical["border_color"]))

        if self.data.handle_vertical["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.handle_vertical["border_top"]))

        if self.data.handle_vertical["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.handle_vertical["border_right"]))

        if self.data.handle_vertical["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.handle_vertical["border_bottom"]))

        if self.data.handle_vertical["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.handle_vertical["border_left"]))

        if self.data.handle_vertical["border_radius"] != 0 and self.data.handle_vertical["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.handle_vertical["border_radius"]))

        if self.data.handle_vertical["padding_top_value"] != 0 and self.data.handle_vertical["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.handle_vertical["padding_top_value"], self.data.handle_vertical["padding_top_type"]))

        if self.data.handle_vertical["padding_right_value"] != 0 and self.data.handle_vertical["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.handle_vertical["padding_right_value"], self.data.handle_vertical["padding_right_type"]))

        if self.data.handle_vertical["padding_bottom_value"] != 0 and self.data.handle_vertical["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.handle_vertical["padding_bottom_value"], self.data.handle_vertical["padding_bottom_type"]))

        if self.data.handle_vertical["padding_left_value"] != 0 and self.data.handle_vertical["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.handle_vertical["padding_left_value"], self.data.handle_vertical["padding_left_type"]))


        if self.data.handle_vertical["margin_top_value"] != 0 and self.data.handle_vertical["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.handle_vertical["margin_top_value"], self.data.handle_vertical["margin_top_type"]))

        if self.data.handle_vertical["margin_right_value"] != 0 and self.data.handle_vertical["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.handle_vertical["margin_right_value"], self.data.handle_vertical["margin_right_type"]))

        if self.data.handle_vertical["margin_bottom_value"] != 0 and self.data.handle_vertical["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.handle_vertical["margin_bottom_value"], self.data.handle_vertical["margin_bottom_type"]))

        if self.data.handle_vertical["margin_left_value"] != 0 and self.data.handle_vertical["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.handle_vertical["margin_left_value"], self.data.handle_vertical["margin_left_type"]))

        f.write("\n}")




        f.write("\n")





        f.write(self.text + "::handle:vertical:hover {")

        if self.data.handle_vertical_hover["color"] != "":
            f.write("\n   color: {};".format(self.data.handle_vertical_hover["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.handle_vertical_hover["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.handle_vertical_hover["outline"]))

        if self.data.handle_vertical_hover["width_value"] != 0 and self.data.handle_vertical_hover["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.handle_vertical_hover["width_value"], self.data.handle_vertical_hover["width_type"]))

        if self.data.handle_vertical_hover["height_value"] != 0 and self.data.handle_vertical_hover["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.handle_vertical_hover["height_value"], self.data.handle_vertical_hover["height_type"]))

        if self.data.handle_vertical_hover["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.handle_vertical_hover["font_family"]))

        if self.data.handle_vertical_hover["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.handle_vertical_hover["font_size"]))

        if self.data.handle_vertical_hover["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.handle_vertical_hover["font_weight"]))

        if self.data.handle_vertical_hover["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.handle_vertical_hover["font_style"]))

        if self.data.handle_vertical_hover["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.handle_vertical_hover["line_height"]))

        if self.data.handle_vertical_hover["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.handle_vertical_hover["text_align"]))

        if self.data.handle_vertical_hover["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.handle_vertical_hover["text_decoration"]))

        if self.data.handle_vertical_hover["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.handle_vertical_hover["text_transform"]))

        if self.data.handle_vertical_hover["background"] != "":
            f.write("\n   background: {};".format(self.data.handle_vertical_hover["background"]))

        if self.data.handle_vertical_hover["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.handle_vertical_hover["background_image"]))

        if self.data.handle_vertical_hover["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.handle_vertical_hover["background_color"]))

        if self.data.handle_vertical_hover["border"] != "":
            f.write("\n   border: {};".format(self.data.handle_vertical_hover["border"]))

        if self.data.handle_vertical_hover["border_width_value"] != 0 and self.data.handle_vertical_hover["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.handle_vertical_hover["border_width_value"], self.data.handle_vertical_hover["border_width_type"]))

        if self.data.handle_vertical_hover["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.handle_vertical_hover["border_style"]))

        if self.data.handle_vertical_hover["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.handle_vertical_hover["border_color"]))

        if self.data.handle_vertical_hover["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.handle_vertical_hover["border_top"]))

        if self.data.handle_vertical_hover["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.handle_vertical_hover["border_right"]))

        if self.data.handle_vertical_hover["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.handle_vertical_hover["border_bottom"]))

        if self.data.handle_vertical_hover["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.handle_vertical_hover["border_left"]))

        if self.data.handle_vertical_hover["border_radius"] != 0 and self.data.handle_vertical_hover["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.handle_vertical_hover["border_radius"]))

        if self.data.handle_vertical_hover["padding_top_value"] != 0 and self.data.handle_vertical_hover["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.handle_vertical_hover["padding_top_value"], self.data.handle_vertical_hover["padding_top_type"]))

        if self.data.handle_vertical_hover["padding_right_value"] != 0 and self.data.handle_vertical_hover["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.handle_vertical_hover["padding_right_value"], self.data.handle_vertical_hover["padding_right_type"]))

        if self.data.handle_vertical_hover["padding_bottom_value"] != 0 and self.data.handle_vertical_hover["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.handle_vertical_hover["padding_bottom_value"], self.data.handle_vertical_hover["padding_bottom_type"]))

        if self.data.handle_vertical_hover["padding_left_value"] != 0 and self.data.handle_vertical_hover["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.handle_vertical_hover["padding_left_value"], self.data.handle_vertical_hover["padding_left_type"]))


        if self.data.handle_vertical_hover["margin_top_value"] != 0 and self.data.handle_vertical_hover["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.handle_vertical_hover["margin_top_value"], self.data.handle_vertical_hover["margin_top_type"]))

        if self.data.handle_vertical_hover["margin_right_value"] != 0 and self.data.handle_vertical_hover["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.handle_vertical_hover["margin_right_value"], self.data.handle_vertical_hover["margin_right_type"]))

        if self.data.handle_vertical_hover["margin_bottom_value"] != 0 and self.data.handle_vertical_hover["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.handle_vertical_hover["margin_bottom_value"], self.data.handle_vertical_hover["margin_bottom_type"]))

        if self.data.handle_vertical_hover["margin_left_value"] != 0 and self.data.handle_vertical_hover["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.handle_vertical_hover["margin_left_value"], self.data.handle_vertical_hover["margin_left_type"]))

        f.write("\n}")



        f.write("\n")





        f.write(self.text + "::handle:vertical:disabled {")

        if self.data.handle_vertical_disabled["color"] != "":
            f.write("\n   color: {};".format(self.data.handle_vertical_disabled["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.handle_vertical_disabled["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.handle_vertical_disabled["outline"]))

        if self.data.handle_vertical_disabled["width_value"] != 0 and self.data.handle_vertical_disabled["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.handle_vertical_disabled["width_value"], self.data.handle_vertical_disabled["width_type"]))

        if self.data.handle_vertical_disabled["height_value"] != 0 and self.data.handle_vertical_disabled["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.handle_vertical_disabled["height_value"], self.data.handle_vertical_disabled["height_type"]))

        if self.data.handle_vertical_disabled["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.handle_vertical_disabled["font_family"]))

        if self.data.handle_vertical_disabled["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.handle_vertical_disabled["font_size"]))

        if self.data.handle_vertical_disabled["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.handle_vertical_disabled["font_weight"]))

        if self.data.handle_vertical_disabled["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.handle_vertical_disabled["font_style"]))

        if self.data.handle_vertical_disabled["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.handle_vertical_disabled["line_height"]))

        if self.data.handle_vertical_disabled["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.handle_vertical_disabled["text_align"]))

        if self.data.handle_vertical_disabled["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.handle_vertical_disabled["text_decoration"]))

        if self.data.handle_vertical_disabled["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.handle_vertical_disabled["text_transform"]))

        if self.data.handle_vertical_disabled["background"] != "":
            f.write("\n   background: {};".format(self.data.handle_vertical_disabled["background"]))

        if self.data.handle_vertical_disabled["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.handle_vertical_disabled["background_image"]))

        if self.data.handle_vertical_disabled["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.handle_vertical_disabled["background_color"]))

        if self.data.handle_vertical_disabled["border"] != "":
            f.write("\n   border: {};".format(self.data.handle_vertical_disabled["border"]))

        if self.data.handle_vertical_disabled["border_width_value"] != 0 and self.data.handle_vertical_disabled["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.handle_vertical_disabled["border_width_value"], self.data.handle_vertical_disabled["border_width_type"]))

        if self.data.handle_vertical_disabled["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.handle_vertical_disabled["border_style"]))

        if self.data.handle_vertical_disabled["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.handle_vertical_disabled["border_color"]))

        if self.data.handle_vertical_disabled["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.handle_vertical_disabled["border_top"]))

        if self.data.handle_vertical_disabled["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.handle_vertical_disabled["border_right"]))

        if self.data.handle_vertical_disabled["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.handle_vertical_disabled["border_bottom"]))

        if self.data.handle_vertical_disabled["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.handle_vertical_disabled["border_left"]))

        if self.data.handle_vertical_disabled["border_radius"] != 0 and self.data.handle_vertical_disabled["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.handle_vertical_disabled["border_radius"]))

        if self.data.handle_vertical_disabled["padding_top_value"] != 0 and self.data.handle_vertical_disabled["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.handle_vertical_disabled["padding_top_value"], self.data.handle_vertical_disabled["padding_top_type"]))

        if self.data.handle_vertical_disabled["padding_right_value"] != 0 and self.data.handle_vertical_disabled["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.handle_vertical_disabled["padding_right_value"], self.data.handle_vertical_disabled["padding_right_type"]))

        if self.data.handle_vertical_disabled["padding_bottom_value"] != 0 and self.data.handle_vertical_disabled["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.handle_vertical_disabled["padding_bottom_value"], self.data.handle_vertical_disabled["padding_bottom_type"]))

        if self.data.handle_vertical_disabled["padding_left_value"] != 0 and self.data.handle_vertical_disabled["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.handle_vertical_disabled["padding_left_value"], self.data.handle_vertical_disabled["padding_left_type"]))


        if self.data.handle_vertical_disabled["margin_top_value"] != 0 and self.data.handle_vertical_disabled["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.handle_vertical_disabled["margin_top_value"], self.data.handle_vertical_disabled["margin_top_type"]))

        if self.data.handle_vertical_disabled["margin_right_value"] != 0 and self.data.handle_vertical_disabled["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.handle_vertical_disabled["margin_right_value"], self.data.handle_vertical_disabled["margin_right_type"]))

        if self.data.handle_vertical_disabled["margin_bottom_value"] != 0 and self.data.handle_vertical_disabled["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.handle_vertical_disabled["margin_bottom_value"], self.data.handle_vertical_disabled["margin_bottom_type"]))

        if self.data.handle_vertical_disabled["margin_left_value"] != 0 and self.data.handle_vertical_disabled["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.handle_vertical_disabled["margin_left_value"], self.data.handle_vertical_disabled["margin_left_type"]))

        f.write("\n}")





        f.write("\n")





        f.write(self.text + "::add-page:vertical {")

        if self.data.add_page_vertical["color"] != "":
            f.write("\n   color: {};".format(self.data.add_page_vertical["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.add_page_vertical["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.add_page_vertical["outline"]))

        if self.data.add_page_vertical["width_value"] != 0 and self.data.add_page_vertical["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.add_page_vertical["width_value"], self.data.add_page_vertical["width_type"]))

        if self.data.add_page_vertical["height_value"] != 0 and self.data.add_page_vertical["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.add_page_vertical["height_value"], self.data.add_page_vertical["height_type"]))

        if self.data.add_page_vertical["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.add_page_vertical["font_family"]))

        if self.data.add_page_vertical["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.add_page_vertical["font_size"]))

        if self.data.add_page_vertical["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.add_page_vertical["font_weight"]))

        if self.data.add_page_vertical["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.add_page_vertical["font_style"]))

        if self.data.add_page_vertical["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.add_page_vertical["line_height"]))

        if self.data.add_page_vertical["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.add_page_vertical["text_align"]))

        if self.data.add_page_vertical["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.add_page_vertical["text_decoration"]))

        if self.data.add_page_vertical["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.add_page_vertical["text_transform"]))

        if self.data.add_page_vertical["background"] != "":
            f.write("\n   background: {};".format(self.data.add_page_vertical["background"]))

        if self.data.add_page_vertical["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.add_page_vertical["background_image"]))

        if self.data.add_page_vertical["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.add_page_vertical["background_color"]))

        if self.data.add_page_vertical["border"] != "":
            f.write("\n   border: {};".format(self.data.add_page_vertical["border"]))

        if self.data.add_page_vertical["border_width_value"] != 0 and self.data.add_page_vertical["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.add_page_vertical["border_width_value"], self.data.add_page_vertical["border_width_type"]))

        if self.data.add_page_vertical["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.add_page_vertical["border_style"]))

        if self.data.add_page_vertical["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.add_page_vertical["border_color"]))

        if self.data.add_page_vertical["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.add_page_vertical["border_top"]))

        if self.data.add_page_vertical["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.add_page_vertical["border_right"]))

        if self.data.add_page_vertical["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.add_page_vertical["border_bottom"]))

        if self.data.add_page_vertical["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.add_page_vertical["border_left"]))

        if self.data.add_page_vertical["border_radius"] != 0 and self.data.add_page_vertical["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.add_page_vertical["border_radius"]))

        if self.data.add_page_vertical["padding_top_value"] != 0 and self.data.add_page_vertical["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.add_page_vertical["padding_top_value"], self.data.add_page_vertical["padding_top_type"]))

        if self.data.add_page_vertical["padding_right_value"] != 0 and self.data.add_page_vertical["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.add_page_vertical["padding_right_value"], self.data.add_page_vertical["padding_right_type"]))

        if self.data.add_page_vertical["padding_bottom_value"] != 0 and self.data.add_page_vertical["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.add_page_vertical["padding_bottom_value"], self.data.add_page_vertical["padding_bottom_type"]))

        if self.data.add_page_vertical["padding_left_value"] != 0 and self.data.add_page_vertical["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.add_page_vertical["padding_left_value"], self.data.add_page_vertical["padding_left_type"]))


        if self.data.add_page_vertical["margin_top_value"] != 0 and self.data.add_page_vertical["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.add_page_vertical["margin_top_value"], self.data.add_page_vertical["margin_top_type"]))

        if self.data.add_page_vertical["margin_right_value"] != 0 and self.data.add_page_vertical["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.add_page_vertical["margin_right_value"], self.data.add_page_vertical["margin_right_type"]))

        if self.data.add_page_vertical["margin_bottom_value"] != 0 and self.data.add_page_vertical["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.add_page_vertical["margin_bottom_value"], self.data.add_page_vertical["margin_bottom_type"]))

        if self.data.add_page_vertical["margin_left_value"] != 0 and self.data.add_page_vertical["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.add_page_vertical["margin_left_value"], self.data.add_page_vertical["margin_left_type"]))

        f.write("\n}")




        f.write("\n")





        f.write(self.text + "::add-page:vertical:disabled {")

        if self.data.add_page_vertical_disabled["color"] != "":
            f.write("\n   color: {};".format(self.data.add_page_vertical_disabled["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.add_page_vertical_disabled["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.add_page_vertical_disabled["outline"]))

        if self.data.add_page_vertical_disabled["width_value"] != 0 and self.data.add_page_vertical_disabled["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.add_page_vertical_disabled["width_value"], self.data.add_page_vertical_disabled["width_type"]))

        if self.data.add_page_vertical_disabled["height_value"] != 0 and self.data.add_page_vertical_disabled["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.add_page_vertical_disabled["height_value"], self.data.add_page_vertical_disabled["height_type"]))

        if self.data.add_page_vertical_disabled["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.add_page_vertical_disabled["font_family"]))

        if self.data.add_page_vertical_disabled["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.add_page_vertical_disabled["font_size"]))

        if self.data.add_page_vertical_disabled["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.add_page_vertical_disabled["font_weight"]))

        if self.data.add_page_vertical_disabled["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.add_page_vertical_disabled["font_style"]))

        if self.data.add_page_vertical_disabled["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.add_page_vertical_disabled["line_height"]))

        if self.data.add_page_vertical_disabled["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.add_page_vertical_disabled["text_align"]))

        if self.data.add_page_vertical_disabled["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.add_page_vertical_disabled["text_decoration"]))

        if self.data.add_page_vertical_disabled["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.add_page_vertical_disabled["text_transform"]))

        if self.data.add_page_vertical_disabled["background"] != "":
            f.write("\n   background: {};".format(self.data.add_page_vertical_disabled["background"]))

        if self.data.add_page_vertical_disabled["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.add_page_vertical_disabled["background_image"]))

        if self.data.add_page_vertical_disabled["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.add_page_vertical_disabled["background_color"]))

        if self.data.add_page_vertical_disabled["border"] != "":
            f.write("\n   border: {};".format(self.data.add_page_vertical_disabled["border"]))

        if self.data.add_page_vertical_disabled["border_width_value"] != 0 and self.data.add_page_vertical_disabled["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.add_page_vertical_disabled["border_width_value"], self.data.add_page_vertical_disabled["border_width_type"]))

        if self.data.add_page_vertical_disabled["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.add_page_vertical_disabled["border_style"]))

        if self.data.add_page_vertical_disabled["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.add_page_vertical_disabled["border_color"]))

        if self.data.add_page_vertical_disabled["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.add_page_vertical_disabled["border_top"]))

        if self.data.add_page_vertical_disabled["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.add_page_vertical_disabled["border_right"]))

        if self.data.add_page_vertical_disabled["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.add_page_vertical_disabled["border_bottom"]))

        if self.data.add_page_vertical_disabled["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.add_page_vertical_disabled["border_left"]))

        if self.data.add_page_vertical_disabled["border_radius"] != 0 and self.data.add_page_vertical_disabled["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.add_page_vertical_disabled["border_radius"]))

        if self.data.add_page_vertical_disabled["padding_top_value"] != 0 and self.data.add_page_vertical_disabled["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.add_page_vertical_disabled["padding_top_value"], self.data.add_page_vertical_disabled["padding_top_type"]))

        if self.data.add_page_vertical_disabled["padding_right_value"] != 0 and self.data.add_page_vertical_disabled["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.add_page_vertical_disabled["padding_right_value"], self.data.add_page_vertical_disabled["padding_right_type"]))

        if self.data.add_page_vertical_disabled["padding_bottom_value"] != 0 and self.data.add_page_vertical_disabled["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.add_page_vertical_disabled["padding_bottom_value"], self.data.add_page_vertical_disabled["padding_bottom_type"]))

        if self.data.add_page_vertical_disabled["padding_left_value"] != 0 and self.data.add_page_vertical_disabled["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.add_page_vertical_disabled["padding_left_value"], self.data.add_page_vertical_disabled["padding_left_type"]))


        if self.data.add_page_vertical_disabled["margin_top_value"] != 0 and self.data.add_page_vertical_disabled["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.add_page_vertical_disabled["margin_top_value"], self.data.add_page_vertical_disabled["margin_top_type"]))

        if self.data.add_page_vertical_disabled["margin_right_value"] != 0 and self.data.add_page_vertical_disabled["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.add_page_vertical_disabled["margin_right_value"], self.data.add_page_vertical_disabled["margin_right_type"]))

        if self.data.add_page_vertical_disabled["margin_bottom_value"] != 0 and self.data.add_page_vertical_disabled["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.add_page_vertical_disabled["margin_bottom_value"], self.data.add_page_vertical_disabled["margin_bottom_type"]))

        if self.data.add_page_vertical_disabled["margin_left_value"] != 0 and self.data.add_page_vertical_disabled["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.add_page_vertical_disabled["margin_left_value"], self.data.add_page_vertical_disabled["margin_left_type"]))

        f.write("\n}")








        f.write("\n")





        f.write(self.text + "::sub-page:vertical {")

        if self.data.sub_page_vertical["color"] != "":
            f.write("\n   color: {};".format(self.data.sub_page_vertical["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.sub_page_vertical["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.sub_page_vertical["outline"]))

        if self.data.sub_page_vertical["width_value"] != 0 and self.data.sub_page_vertical["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.sub_page_vertical["width_value"], self.data.sub_page_vertical["width_type"]))

        if self.data.sub_page_vertical["height_value"] != 0 and self.data.sub_page_vertical["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.sub_page_vertical["height_value"], self.data.sub_page_vertical["height_type"]))

        if self.data.sub_page_vertical["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.sub_page_vertical["font_family"]))

        if self.data.sub_page_vertical["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.sub_page_vertical["font_size"]))

        if self.data.sub_page_vertical["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.sub_page_vertical["font_weight"]))

        if self.data.sub_page_vertical["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.sub_page_vertical["font_style"]))

        if self.data.sub_page_vertical["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.sub_page_vertical["line_height"]))

        if self.data.sub_page_vertical["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.sub_page_vertical["text_align"]))

        if self.data.sub_page_vertical["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.sub_page_vertical["text_decoration"]))

        if self.data.sub_page_vertical["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.sub_page_vertical["text_transform"]))

        if self.data.sub_page_vertical["background"] != "":
            f.write("\n   background: {};".format(self.data.sub_page_vertical["background"]))

        if self.data.sub_page_vertical["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.sub_page_vertical["background_image"]))

        if self.data.sub_page_vertical["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.sub_page_vertical["background_color"]))

        if self.data.sub_page_vertical["border"] != "":
            f.write("\n   border: {};".format(self.data.sub_page_vertical["border"]))

        if self.data.sub_page_vertical["border_width_value"] != 0 and self.data.sub_page_vertical["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.sub_page_vertical["border_width_value"], self.data.sub_page_vertical["border_width_type"]))

        if self.data.sub_page_vertical["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.sub_page_vertical["border_style"]))

        if self.data.sub_page_vertical["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.sub_page_vertical["border_color"]))

        if self.data.sub_page_vertical["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.sub_page_vertical["border_top"]))

        if self.data.sub_page_vertical["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.sub_page_vertical["border_right"]))

        if self.data.sub_page_vertical["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.sub_page_vertical["border_bottom"]))

        if self.data.sub_page_vertical["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.sub_page_vertical["border_left"]))

        if self.data.sub_page_vertical["border_radius"] != 0 and self.data.sub_page_vertical["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.sub_page_vertical["border_radius"]))

        if self.data.sub_page_vertical["padding_top_value"] != 0 and self.data.sub_page_vertical["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.sub_page_vertical["padding_top_value"], self.data.sub_page_vertical["padding_top_type"]))

        if self.data.sub_page_vertical["padding_right_value"] != 0 and self.data.sub_page_vertical["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.sub_page_vertical["padding_right_value"], self.data.sub_page_vertical["padding_right_type"]))

        if self.data.sub_page_vertical["padding_bottom_value"] != 0 and self.data.sub_page_vertical["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.sub_page_vertical["padding_bottom_value"], self.data.sub_page_vertical["padding_bottom_type"]))

        if self.data.sub_page_vertical["padding_left_value"] != 0 and self.data.sub_page_vertical["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.sub_page_vertical["padding_left_value"], self.data.sub_page_vertical["padding_left_type"]))


        if self.data.sub_page_vertical["margin_top_value"] != 0 and self.data.sub_page_vertical["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.sub_page_vertical["margin_top_value"], self.data.sub_page_vertical["margin_top_type"]))

        if self.data.sub_page_vertical["margin_right_value"] != 0 and self.data.sub_page_vertical["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.sub_page_vertical["margin_right_value"], self.data.sub_page_vertical["margin_right_type"]))

        if self.data.sub_page_vertical["margin_bottom_value"] != 0 and self.data.sub_page_vertical["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.sub_page_vertical["margin_bottom_value"], self.data.sub_page_vertical["margin_bottom_type"]))

        if self.data.sub_page_vertical["margin_left_value"] != 0 and self.data.sub_page_vertical["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.sub_page_vertical["margin_left_value"], self.data.sub_page_vertical["margin_left_type"]))

        f.write("\n}")







        f.write("\n")





        f.write(self.text + "::sub-page:vertical:disabled {")

        if self.data.sub_page_vertical_disabled["color"] != "":
            f.write("\n   color: {};".format(self.data.sub_page_vertical_disabled["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.sub_page_vertical_disabled["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.sub_page_vertical_disabled["outline"]))

        if self.data.sub_page_vertical_disabled["width_value"] != 0 and self.data.sub_page_vertical_disabled["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.sub_page_vertical_disabled["width_value"], self.data.sub_page_vertical_disabled["width_type"]))

        if self.data.sub_page_vertical_disabled["height_value"] != 0 and self.data.sub_page_vertical_disabled["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.sub_page_vertical_disabled["height_value"], self.data.sub_page_vertical_disabled["height_type"]))

        if self.data.sub_page_vertical_disabled["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.sub_page_vertical_disabled["font_family"]))

        if self.data.sub_page_vertical_disabled["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.sub_page_vertical_disabled["font_size"]))

        if self.data.sub_page_vertical_disabled["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.sub_page_vertical_disabled["font_weight"]))

        if self.data.sub_page_vertical_disabled["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.sub_page_vertical_disabled["font_style"]))

        if self.data.sub_page_vertical_disabled["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.sub_page_vertical_disabled["line_height"]))

        if self.data.sub_page_vertical_disabled["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.sub_page_vertical_disabled["text_align"]))

        if self.data.sub_page_vertical_disabled["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.sub_page_vertical_disabled["text_decoration"]))

        if self.data.sub_page_vertical_disabled["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.sub_page_vertical_disabled["text_transform"]))

        if self.data.sub_page_vertical_disabled["background"] != "":
            f.write("\n   background: {};".format(self.data.sub_page_vertical_disabled["background"]))

        if self.data.sub_page_vertical_disabled["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.sub_page_vertical_disabled["background_image"]))

        if self.data.sub_page_vertical_disabled["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.sub_page_vertical_disabled["background_color"]))

        if self.data.sub_page_vertical_disabled["border"] != "":
            f.write("\n   border: {};".format(self.data.sub_page_vertical_disabled["border"]))

        if self.data.sub_page_vertical_disabled["border_width_value"] != 0 and self.data.sub_page_vertical_disabled["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.sub_page_vertical_disabled["border_width_value"], self.data.sub_page_vertical_disabled["border_width_type"]))

        if self.data.sub_page_vertical_disabled["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.sub_page_vertical_disabled["border_style"]))

        if self.data.sub_page_vertical_disabled["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.sub_page_vertical_disabled["border_color"]))

        if self.data.sub_page_vertical_disabled["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.sub_page_vertical_disabled["border_top"]))

        if self.data.sub_page_vertical_disabled["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.sub_page_vertical_disabled["border_right"]))

        if self.data.sub_page_vertical_disabled["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.sub_page_vertical_disabled["border_bottom"]))

        if self.data.sub_page_vertical_disabled["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.sub_page_vertical_disabled["border_left"]))

        if self.data.sub_page_vertical_disabled["border_radius"] != 0 and self.data.sub_page_vertical_disabled["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.sub_page_vertical_disabled["border_radius"]))

        if self.data.sub_page_vertical_disabled["padding_top_value"] != 0 and self.data.sub_page_vertical_disabled["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.sub_page_vertical_disabled["padding_top_value"], self.data.sub_page_vertical_disabled["padding_top_type"]))

        if self.data.sub_page_vertical_disabled["padding_right_value"] != 0 and self.data.sub_page_vertical_disabled["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.sub_page_vertical_disabled["padding_right_value"], self.data.sub_page_vertical_disabled["padding_right_type"]))

        if self.data.sub_page_vertical_disabled["padding_bottom_value"] != 0 and self.data.sub_page_vertical_disabled["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.sub_page_vertical_disabled["padding_bottom_value"], self.data.sub_page_vertical_disabled["padding_bottom_type"]))

        if self.data.sub_page_vertical_disabled["padding_left_value"] != 0 and self.data.sub_page_vertical_disabled["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.sub_page_vertical_disabled["padding_left_value"], self.data.sub_page_vertical_disabled["padding_left_type"]))


        if self.data.sub_page_vertical_disabled["margin_top_value"] != 0 and self.data.sub_page_vertical_disabled["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.sub_page_vertical_disabled["margin_top_value"], self.data.sub_page_vertical_disabled["margin_top_type"]))

        if self.data.sub_page_vertical_disabled["margin_right_value"] != 0 and self.data.sub_page_vertical_disabled["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.sub_page_vertical_disabled["margin_right_value"], self.data.sub_page_vertical_disabled["margin_right_type"]))

        if self.data.sub_page_vertical_disabled["margin_bottom_value"] != 0 and self.data.sub_page_vertical_disabled["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.sub_page_vertical_disabled["margin_bottom_value"], self.data.sub_page_vertical_disabled["margin_bottom_type"]))

        if self.data.sub_page_vertical_disabled["margin_left_value"] != 0 and self.data.sub_page_vertical_disabled["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.sub_page_vertical_disabled["margin_left_value"], self.data.sub_page_vertical_disabled["margin_left_type"]))

        f.write("\n}")




        f.write(self.text + ":horizontal {")

        if self.data.horizontal["color"] != "":
            f.write("\n   color: {};".format(self.data.horizontal["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.horizontal["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.horizontal["outline"]))

        if self.data.horizontal["width_value"] != 0 and self.data.horizontal["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.horizontal["width_value"], self.data.horizontal["width_type"]))

        if self.data.horizontal["height_value"] != 0 and self.data.horizontal["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.horizontal["height_value"], self.data.horizontal["height_type"]))

        if self.data.horizontal["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.horizontal["font_family"]))

        if self.data.horizontal["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.horizontal["font_size"]))

        if self.data.horizontal["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.horizontal["font_weight"]))

        if self.data.horizontal["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.horizontal["font_style"]))

        if self.data.horizontal["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.horizontal["line_height"]))

        if self.data.horizontal["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.horizontal["text_align"]))

        if self.data.horizontal["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.horizontal["text_decoration"]))

        if self.data.horizontal["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.horizontal["text_transform"]))

        if self.data.horizontal["background"] != "":
            f.write("\n   background: {};".format(self.data.horizontal["background"]))

        if self.data.horizontal["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.horizontal["background_image"]))

        if self.data.horizontal["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.horizontal["background_color"]))

        if self.data.horizontal["border"] != "":
            f.write("\n   border: {};".format(self.data.horizontal["border"]))

        if self.data.horizontal["border_width_value"] != 0 and self.data.horizontal["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.horizontal["border_width_value"], self.data.horizontal["border_width_type"]))

        if self.data.horizontal["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.horizontal["border_style"]))

        if self.data.horizontal["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.horizontal["border_color"]))

        if self.data.horizontal["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.horizontal["border_top"]))

        if self.data.horizontal["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.horizontal["border_right"]))

        if self.data.horizontal["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.horizontal["border_bottom"]))

        if self.data.horizontal["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.horizontal["border_left"]))

        if self.data.horizontal["border_radius"] != 0 and self.data.horizontal["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.horizontal["border_radius"]))

        if self.data.horizontal["padding_top_value"] != 0 and self.data.horizontal["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.horizontal["padding_top_value"], self.data.horizontal["padding_top_type"]))

        if self.data.horizontal["padding_right_value"] != 0 and self.data.horizontal["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.horizontal["padding_right_value"], self.data.horizontal["padding_right_type"]))

        if self.data.horizontal["padding_bottom_value"] != 0 and self.data.horizontal["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.horizontal["padding_bottom_value"], self.data.horizontal["padding_bottom_type"]))

        if self.data.horizontal["padding_left_value"] != 0 and self.data.horizontal["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.horizontal["padding_left_value"], self.data.horizontal["padding_left_type"]))


        if self.data.horizontal["margin_top_value"] != 0 and self.data.horizontal["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.horizontal["margin_top_value"], self.data.horizontal["margin_top_type"]))

        if self.data.horizontal["margin_right_value"] != 0 and self.data.horizontal["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.horizontal["margin_right_value"], self.data.horizontal["margin_right_type"]))

        if self.data.horizontal["margin_bottom_value"] != 0 and self.data.horizontal["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.horizontal["margin_bottom_value"], self.data.horizontal["margin_bottom_type"]))

        if self.data.horizontal["margin_left_value"] != 0 and self.data.horizontal["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.horizontal["margin_left_value"], self.data.horizontal["margin_left_type"]))

        f.write("\n}")





        f.write("\n")





        f.write(self.text + "::groove:horizontal {")

        if self.data.groove_horizontal["color"] != "":
            f.write("\n   color: {};".format(self.data.groove_horizontal["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.groove_horizontal["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.groove_horizontal["outline"]))

        if self.data.groove_horizontal["width_value"] != 0 and self.data.groove_horizontal["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.groove_horizontal["width_value"], self.data.groove_horizontal["width_type"]))

        if self.data.groove_horizontal["height_value"] != 0 and self.data.groove_horizontal["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.groove_horizontal["height_value"], self.data.groove_horizontal["height_type"]))

        if self.data.groove_horizontal["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.groove_horizontal["font_family"]))

        if self.data.groove_horizontal["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.groove_horizontal["font_size"]))

        if self.data.groove_horizontal["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.groove_horizontal["font_weight"]))

        if self.data.groove_horizontal["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.groove_horizontal["font_style"]))

        if self.data.groove_horizontal["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.groove_horizontal["line_height"]))

        if self.data.groove_horizontal["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.groove_horizontal["text_align"]))

        if self.data.groove_horizontal["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.groove_horizontal["text_decoration"]))

        if self.data.groove_horizontal["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.groove_horizontal["text_transform"]))

        if self.data.groove_horizontal["background"] != "":
            f.write("\n   background: {};".format(self.data.groove_horizontal["background"]))

        if self.data.groove_horizontal["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.groove_horizontal["background_image"]))

        if self.data.groove_horizontal["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.groove_horizontal["background_color"]))

        if self.data.groove_horizontal["border"] != "":
            f.write("\n   border: {};".format(self.data.groove_horizontal["border"]))

        if self.data.groove_horizontal["border_width_value"] != 0 and self.data.groove_horizontal["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.groove_horizontal["border_width_value"], self.data.groove_horizontal["border_width_type"]))

        if self.data.groove_horizontal["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.groove_horizontal["border_style"]))

        if self.data.groove_horizontal["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.groove_horizontal["border_color"]))

        if self.data.groove_horizontal["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.groove_horizontal["border_top"]))

        if self.data.groove_horizontal["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.groove_horizontal["border_right"]))

        if self.data.groove_horizontal["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.groove_horizontal["border_bottom"]))

        if self.data.groove_horizontal["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.groove_horizontal["border_left"]))

        if self.data.groove_horizontal["border_radius"] != 0 and self.data.groove_horizontal["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.groove_horizontal["border_radius"]))

        if self.data.groove_horizontal["padding_top_value"] != 0 and self.data.groove_horizontal["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.groove_horizontal["padding_top_value"], self.data.groove_horizontal["padding_top_type"]))

        if self.data.groove_horizontal["padding_right_value"] != 0 and self.data.groove_horizontal["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.groove_horizontal["padding_right_value"], self.data.groove_horizontal["padding_right_type"]))

        if self.data.groove_horizontal["padding_bottom_value"] != 0 and self.data.groove_horizontal["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.groove_horizontal["padding_bottom_value"], self.data.groove_horizontal["padding_bottom_type"]))

        if self.data.groove_horizontal["padding_left_value"] != 0 and self.data.groove_horizontal["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.groove_horizontal["padding_left_value"], self.data.groove_horizontal["padding_left_type"]))


        if self.data.groove_horizontal["margin_top_value"] != 0 and self.data.groove_horizontal["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.groove_horizontal["margin_top_value"], self.data.groove_horizontal["margin_top_type"]))

        if self.data.groove_horizontal["margin_right_value"] != 0 and self.data.groove_horizontal["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.groove_horizontal["margin_right_value"], self.data.groove_horizontal["margin_right_type"]))

        if self.data.groove_horizontal["margin_bottom_value"] != 0 and self.data.groove_horizontal["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.groove_horizontal["margin_bottom_value"], self.data.groove_horizontal["margin_bottom_type"]))

        if self.data.groove_horizontal["margin_left_value"] != 0 and self.data.groove_horizontal["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.groove_horizontal["margin_left_value"], self.data.groove_horizontal["margin_left_type"]))

        f.write("\n}")




        f.write("\n")





        f.write(self.text + "::handle:horizontal {")

        if self.data.handle_horizontal["color"] != "":
            f.write("\n   color: {};".format(self.data.handle_horizontal["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.handle_horizontal["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.handle_horizontal["outline"]))

        if self.data.handle_horizontal["width_value"] != 0 and self.data.handle_horizontal["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.handle_horizontal["width_value"], self.data.handle_horizontal["width_type"]))

        if self.data.handle_horizontal["height_value"] != 0 and self.data.handle_horizontal["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.handle_horizontal["height_value"], self.data.handle_horizontal["height_type"]))

        if self.data.handle_horizontal["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.handle_horizontal["font_family"]))

        if self.data.handle_horizontal["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.handle_horizontal["font_size"]))

        if self.data.handle_horizontal["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.handle_horizontal["font_weight"]))

        if self.data.handle_horizontal["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.handle_horizontal["font_style"]))

        if self.data.handle_horizontal["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.handle_horizontal["line_height"]))

        if self.data.handle_horizontal["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.handle_horizontal["text_align"]))

        if self.data.handle_horizontal["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.handle_horizontal["text_decoration"]))

        if self.data.handle_horizontal["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.handle_horizontal["text_transform"]))

        if self.data.handle_horizontal["background"] != "":
            f.write("\n   background: {};".format(self.data.handle_horizontal["background"]))

        if self.data.handle_horizontal["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.handle_horizontal["background_image"]))

        if self.data.handle_horizontal["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.handle_horizontal["background_color"]))

        if self.data.handle_horizontal["border"] != "":
            f.write("\n   border: {};".format(self.data.handle_horizontal["border"]))

        if self.data.handle_horizontal["border_width_value"] != 0 and self.data.handle_horizontal["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.handle_horizontal["border_width_value"], self.data.handle_horizontal["border_width_type"]))

        if self.data.handle_horizontal["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.handle_horizontal["border_style"]))

        if self.data.handle_horizontal["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.handle_horizontal["border_color"]))

        if self.data.handle_horizontal["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.handle_horizontal["border_top"]))

        if self.data.handle_horizontal["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.handle_horizontal["border_right"]))

        if self.data.handle_horizontal["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.handle_horizontal["border_bottom"]))

        if self.data.handle_horizontal["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.handle_horizontal["border_left"]))

        if self.data.handle_horizontal["border_radius"] != 0 and self.data.handle_horizontal["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.handle_horizontal["border_radius"]))

        if self.data.handle_horizontal["padding_top_value"] != 0 and self.data.handle_horizontal["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.handle_horizontal["padding_top_value"], self.data.handle_horizontal["padding_top_type"]))

        if self.data.handle_horizontal["padding_right_value"] != 0 and self.data.handle_horizontal["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.handle_horizontal["padding_right_value"], self.data.handle_horizontal["padding_right_type"]))

        if self.data.handle_horizontal["padding_bottom_value"] != 0 and self.data.handle_horizontal["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.handle_horizontal["padding_bottom_value"], self.data.handle_horizontal["padding_bottom_type"]))

        if self.data.handle_horizontal["padding_left_value"] != 0 and self.data.handle_horizontal["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.handle_horizontal["padding_left_value"], self.data.handle_horizontal["padding_left_type"]))


        if self.data.handle_horizontal["margin_top_value"] != 0 and self.data.handle_horizontal["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.handle_horizontal["margin_top_value"], self.data.handle_horizontal["margin_top_type"]))

        if self.data.handle_horizontal["margin_right_value"] != 0 and self.data.handle_horizontal["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.handle_horizontal["margin_right_value"], self.data.handle_horizontal["margin_right_type"]))

        if self.data.handle_horizontal["margin_bottom_value"] != 0 and self.data.handle_horizontal["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.handle_horizontal["margin_bottom_value"], self.data.handle_horizontal["margin_bottom_type"]))

        if self.data.handle_horizontal["margin_left_value"] != 0 and self.data.handle_horizontal["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.handle_horizontal["margin_left_value"], self.data.handle_horizontal["margin_left_type"]))

        f.write("\n}")




        f.write("\n")





        f.write(self.text + "::handle:horizontal:hover {")

        if self.data.handle_horizontal_hover["color"] != "":
            f.write("\n   color: {};".format(self.data.handle_horizontal_hover["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.handle_horizontal_hover["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.handle_horizontal_hover["outline"]))

        if self.data.handle_horizontal_hover["width_value"] != 0 and self.data.handle_horizontal_hover["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.handle_horizontal_hover["width_value"], self.data.handle_horizontal_hover["width_type"]))

        if self.data.handle_horizontal_hover["height_value"] != 0 and self.data.handle_horizontal_hover["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.handle_horizontal_hover["height_value"], self.data.handle_horizontal_hover["height_type"]))

        if self.data.handle_horizontal_hover["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.handle_horizontal_hover["font_family"]))

        if self.data.handle_horizontal_hover["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.handle_horizontal_hover["font_size"]))

        if self.data.handle_horizontal_hover["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.handle_horizontal_hover["font_weight"]))

        if self.data.handle_horizontal_hover["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.handle_horizontal_hover["font_style"]))

        if self.data.handle_horizontal_hover["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.handle_horizontal_hover["line_height"]))

        if self.data.handle_horizontal_hover["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.handle_horizontal_hover["text_align"]))

        if self.data.handle_horizontal_hover["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.handle_horizontal_hover["text_decoration"]))

        if self.data.handle_horizontal_hover["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.handle_horizontal_hover["text_transform"]))

        if self.data.handle_horizontal_hover["background"] != "":
            f.write("\n   background: {};".format(self.data.handle_horizontal_hover["background"]))

        if self.data.handle_horizontal_hover["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.handle_horizontal_hover["background_image"]))

        if self.data.handle_horizontal_hover["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.handle_horizontal_hover["background_color"]))

        if self.data.handle_horizontal_hover["border"] != "":
            f.write("\n   border: {};".format(self.data.handle_horizontal_hover["border"]))

        if self.data.handle_horizontal_hover["border_width_value"] != 0 and self.data.handle_horizontal_hover["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.handle_horizontal_hover["border_width_value"], self.data.handle_horizontal_hover["border_width_type"]))

        if self.data.handle_horizontal_hover["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.handle_horizontal_hover["border_style"]))

        if self.data.handle_horizontal_hover["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.handle_horizontal_hover["border_color"]))

        if self.data.handle_horizontal_hover["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.handle_horizontal_hover["border_top"]))

        if self.data.handle_horizontal_hover["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.handle_horizontal_hover["border_right"]))

        if self.data.handle_horizontal_hover["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.handle_horizontal_hover["border_bottom"]))

        if self.data.handle_horizontal_hover["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.handle_horizontal_hover["border_left"]))

        if self.data.handle_horizontal_hover["border_radius"] != 0 and self.data.handle_horizontal_hover["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.handle_horizontal_hover["border_radius"]))

        if self.data.handle_horizontal_hover["padding_top_value"] != 0 and self.data.handle_horizontal_hover["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.handle_horizontal_hover["padding_top_value"], self.data.handle_horizontal_hover["padding_top_type"]))

        if self.data.handle_horizontal_hover["padding_right_value"] != 0 and self.data.handle_horizontal_hover["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.handle_horizontal_hover["padding_right_value"], self.data.handle_horizontal_hover["padding_right_type"]))

        if self.data.handle_horizontal_hover["padding_bottom_value"] != 0 and self.data.handle_horizontal_hover["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.handle_horizontal_hover["padding_bottom_value"], self.data.handle_horizontal_hover["padding_bottom_type"]))

        if self.data.handle_horizontal_hover["padding_left_value"] != 0 and self.data.handle_horizontal_hover["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.handle_horizontal_hover["padding_left_value"], self.data.handle_horizontal_hover["padding_left_type"]))


        if self.data.handle_horizontal_hover["margin_top_value"] != 0 and self.data.handle_horizontal_hover["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.handle_horizontal_hover["margin_top_value"], self.data.handle_horizontal_hover["margin_top_type"]))

        if self.data.handle_horizontal_hover["margin_right_value"] != 0 and self.data.handle_horizontal_hover["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.handle_horizontal_hover["margin_right_value"], self.data.handle_horizontal_hover["margin_right_type"]))

        if self.data.handle_horizontal_hover["margin_bottom_value"] != 0 and self.data.handle_horizontal_hover["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.handle_horizontal_hover["margin_bottom_value"], self.data.handle_horizontal_hover["margin_bottom_type"]))

        if self.data.handle_horizontal_hover["margin_left_value"] != 0 and self.data.handle_horizontal_hover["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.handle_horizontal_hover["margin_left_value"], self.data.handle_horizontal_hover["margin_left_type"]))

        f.write("\n}")



        f.write("\n")





        f.write(self.text + "::handle:horizontal:disabled {")

        if self.data.handle_horizontal_disabled["color"] != "":
            f.write("\n   color: {};".format(self.data.handle_horizontal_disabled["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.handle_horizontal_disabled["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.handle_horizontal_disabled["outline"]))

        if self.data.handle_horizontal_disabled["width_value"] != 0 and self.data.handle_horizontal_disabled["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.handle_horizontal_disabled["width_value"], self.data.handle_horizontal_disabled["width_type"]))

        if self.data.handle_horizontal_disabled["height_value"] != 0 and self.data.handle_horizontal_disabled["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.handle_horizontal_disabled["height_value"], self.data.handle_horizontal_disabled["height_type"]))

        if self.data.handle_horizontal_disabled["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.handle_horizontal_disabled["font_family"]))

        if self.data.handle_horizontal_disabled["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.handle_horizontal_disabled["font_size"]))

        if self.data.handle_horizontal_disabled["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.handle_horizontal_disabled["font_weight"]))

        if self.data.handle_horizontal_disabled["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.handle_horizontal_disabled["font_style"]))

        if self.data.handle_horizontal_disabled["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.handle_horizontal_disabled["line_height"]))

        if self.data.handle_horizontal_disabled["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.handle_horizontal_disabled["text_align"]))

        if self.data.handle_horizontal_disabled["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.handle_horizontal_disabled["text_decoration"]))

        if self.data.handle_horizontal_disabled["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.handle_horizontal_disabled["text_transform"]))

        if self.data.handle_horizontal_disabled["background"] != "":
            f.write("\n   background: {};".format(self.data.handle_horizontal_disabled["background"]))

        if self.data.handle_horizontal_disabled["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.handle_horizontal_disabled["background_image"]))

        if self.data.handle_horizontal_disabled["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.handle_horizontal_disabled["background_color"]))

        if self.data.handle_horizontal_disabled["border"] != "":
            f.write("\n   border: {};".format(self.data.handle_horizontal_disabled["border"]))

        if self.data.handle_horizontal_disabled["border_width_value"] != 0 and self.data.handle_horizontal_disabled["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.handle_horizontal_disabled["border_width_value"], self.data.handle_horizontal_disabled["border_width_type"]))

        if self.data.handle_horizontal_disabled["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.handle_horizontal_disabled["border_style"]))

        if self.data.handle_horizontal_disabled["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.handle_horizontal_disabled["border_color"]))

        if self.data.handle_horizontal_disabled["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.handle_horizontal_disabled["border_top"]))

        if self.data.handle_horizontal_disabled["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.handle_horizontal_disabled["border_right"]))

        if self.data.handle_horizontal_disabled["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.handle_horizontal_disabled["border_bottom"]))

        if self.data.handle_horizontal_disabled["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.handle_horizontal_disabled["border_left"]))

        if self.data.handle_horizontal_disabled["border_radius"] != 0 and self.data.handle_horizontal_disabled["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.handle_horizontal_disabled["border_radius"]))

        if self.data.handle_horizontal_disabled["padding_top_value"] != 0 and self.data.handle_horizontal_disabled["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.handle_horizontal_disabled["padding_top_value"], self.data.handle_horizontal_disabled["padding_top_type"]))

        if self.data.handle_horizontal_disabled["padding_right_value"] != 0 and self.data.handle_horizontal_disabled["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.handle_horizontal_disabled["padding_right_value"], self.data.handle_horizontal_disabled["padding_right_type"]))

        if self.data.handle_horizontal_disabled["padding_bottom_value"] != 0 and self.data.handle_horizontal_disabled["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.handle_horizontal_disabled["padding_bottom_value"], self.data.handle_horizontal_disabled["padding_bottom_type"]))

        if self.data.handle_horizontal_disabled["padding_left_value"] != 0 and self.data.handle_horizontal_disabled["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.handle_horizontal_disabled["padding_left_value"], self.data.handle_horizontal_disabled["padding_left_type"]))


        if self.data.handle_horizontal_disabled["margin_top_value"] != 0 and self.data.handle_horizontal_disabled["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.handle_horizontal_disabled["margin_top_value"], self.data.handle_horizontal_disabled["margin_top_type"]))

        if self.data.handle_horizontal_disabled["margin_right_value"] != 0 and self.data.handle_horizontal_disabled["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.handle_horizontal_disabled["margin_right_value"], self.data.handle_horizontal_disabled["margin_right_type"]))

        if self.data.handle_horizontal_disabled["margin_bottom_value"] != 0 and self.data.handle_horizontal_disabled["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.handle_horizontal_disabled["margin_bottom_value"], self.data.handle_horizontal_disabled["margin_bottom_type"]))

        if self.data.handle_horizontal_disabled["margin_left_value"] != 0 and self.data.handle_horizontal_disabled["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.handle_horizontal_disabled["margin_left_value"], self.data.handle_horizontal_disabled["margin_left_type"]))

        f.write("\n}")





        f.write("\n")





        f.write(self.text + "::add-page:horizontal {")

        if self.data.add_page_horizontal["color"] != "":
            f.write("\n   color: {};".format(self.data.add_page_horizontal["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.add_page_horizontal["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.add_page_horizontal["outline"]))

        if self.data.add_page_horizontal["width_value"] != 0 and self.data.add_page_horizontal["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.add_page_horizontal["width_value"], self.data.add_page_horizontal["width_type"]))

        if self.data.add_page_horizontal["height_value"] != 0 and self.data.add_page_horizontal["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.add_page_horizontal["height_value"], self.data.add_page_horizontal["height_type"]))

        if self.data.add_page_horizontal["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.add_page_horizontal["font_family"]))

        if self.data.add_page_horizontal["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.add_page_horizontal["font_size"]))

        if self.data.add_page_horizontal["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.add_page_horizontal["font_weight"]))

        if self.data.add_page_horizontal["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.add_page_horizontal["font_style"]))

        if self.data.add_page_horizontal["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.add_page_horizontal["line_height"]))

        if self.data.add_page_horizontal["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.add_page_horizontal["text_align"]))

        if self.data.add_page_horizontal["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.add_page_horizontal["text_decoration"]))

        if self.data.add_page_horizontal["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.add_page_horizontal["text_transform"]))

        if self.data.add_page_horizontal["background"] != "":
            f.write("\n   background: {};".format(self.data.add_page_horizontal["background"]))

        if self.data.add_page_horizontal["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.add_page_horizontal["background_image"]))

        if self.data.add_page_horizontal["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.add_page_horizontal["background_color"]))

        if self.data.add_page_horizontal["border"] != "":
            f.write("\n   border: {};".format(self.data.add_page_horizontal["border"]))

        if self.data.add_page_horizontal["border_width_value"] != 0 and self.data.add_page_horizontal["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.add_page_horizontal["border_width_value"], self.data.add_page_horizontal["border_width_type"]))

        if self.data.add_page_horizontal["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.add_page_horizontal["border_style"]))

        if self.data.add_page_horizontal["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.add_page_horizontal["border_color"]))

        if self.data.add_page_horizontal["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.add_page_horizontal["border_top"]))

        if self.data.add_page_horizontal["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.add_page_horizontal["border_right"]))

        if self.data.add_page_horizontal["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.add_page_horizontal["border_bottom"]))

        if self.data.add_page_horizontal["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.add_page_horizontal["border_left"]))

        if self.data.add_page_horizontal["border_radius"] != 0 and self.data.add_page_horizontal["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.add_page_horizontal["border_radius"]))

        if self.data.add_page_horizontal["padding_top_value"] != 0 and self.data.add_page_horizontal["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.add_page_horizontal["padding_top_value"], self.data.add_page_horizontal["padding_top_type"]))

        if self.data.add_page_horizontal["padding_right_value"] != 0 and self.data.add_page_horizontal["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.add_page_horizontal["padding_right_value"], self.data.add_page_horizontal["padding_right_type"]))

        if self.data.add_page_horizontal["padding_bottom_value"] != 0 and self.data.add_page_horizontal["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.add_page_horizontal["padding_bottom_value"], self.data.add_page_horizontal["padding_bottom_type"]))

        if self.data.add_page_horizontal["padding_left_value"] != 0 and self.data.add_page_horizontal["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.add_page_horizontal["padding_left_value"], self.data.add_page_horizontal["padding_left_type"]))


        if self.data.add_page_horizontal["margin_top_value"] != 0 and self.data.add_page_horizontal["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.add_page_horizontal["margin_top_value"], self.data.add_page_horizontal["margin_top_type"]))

        if self.data.add_page_horizontal["margin_right_value"] != 0 and self.data.add_page_horizontal["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.add_page_horizontal["margin_right_value"], self.data.add_page_horizontal["margin_right_type"]))

        if self.data.add_page_horizontal["margin_bottom_value"] != 0 and self.data.add_page_horizontal["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.add_page_horizontal["margin_bottom_value"], self.data.add_page_horizontal["margin_bottom_type"]))

        if self.data.add_page_horizontal["margin_left_value"] != 0 and self.data.add_page_horizontal["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.add_page_horizontal["margin_left_value"], self.data.add_page_horizontal["margin_left_type"]))

        f.write("\n}")




        f.write("\n")





        f.write(self.text + "::add-page:horizontal:disabled {")

        if self.data.add_page_horizontal_disabled["color"] != "":
            f.write("\n   color: {};".format(self.data.add_page_horizontal_disabled["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.add_page_horizontal_disabled["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.add_page_horizontal_disabled["outline"]))

        if self.data.add_page_horizontal_disabled["width_value"] != 0 and self.data.add_page_horizontal_disabled["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.add_page_horizontal_disabled["width_value"], self.data.add_page_horizontal_disabled["width_type"]))

        if self.data.add_page_horizontal_disabled["height_value"] != 0 and self.data.add_page_horizontal_disabled["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.add_page_horizontal_disabled["height_value"], self.data.add_page_horizontal_disabled["height_type"]))

        if self.data.add_page_horizontal_disabled["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.add_page_horizontal_disabled["font_family"]))

        if self.data.add_page_horizontal_disabled["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.add_page_horizontal_disabled["font_size"]))

        if self.data.add_page_horizontal_disabled["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.add_page_horizontal_disabled["font_weight"]))

        if self.data.add_page_horizontal_disabled["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.add_page_horizontal_disabled["font_style"]))

        if self.data.add_page_horizontal_disabled["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.add_page_horizontal_disabled["line_height"]))

        if self.data.add_page_horizontal_disabled["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.add_page_horizontal_disabled["text_align"]))

        if self.data.add_page_horizontal_disabled["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.add_page_horizontal_disabled["text_decoration"]))

        if self.data.add_page_horizontal_disabled["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.add_page_horizontal_disabled["text_transform"]))

        if self.data.add_page_horizontal_disabled["background"] != "":
            f.write("\n   background: {};".format(self.data.add_page_horizontal_disabled["background"]))

        if self.data.add_page_horizontal_disabled["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.add_page_horizontal_disabled["background_image"]))

        if self.data.add_page_horizontal_disabled["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.add_page_horizontal_disabled["background_color"]))

        if self.data.add_page_horizontal_disabled["border"] != "":
            f.write("\n   border: {};".format(self.data.add_page_horizontal_disabled["border"]))

        if self.data.add_page_horizontal_disabled["border_width_value"] != 0 and self.data.add_page_horizontal_disabled["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.add_page_horizontal_disabled["border_width_value"], self.data.add_page_horizontal_disabled["border_width_type"]))

        if self.data.add_page_horizontal_disabled["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.add_page_horizontal_disabled["border_style"]))

        if self.data.add_page_horizontal_disabled["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.add_page_horizontal_disabled["border_color"]))

        if self.data.add_page_horizontal_disabled["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.add_page_horizontal_disabled["border_top"]))

        if self.data.add_page_horizontal_disabled["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.add_page_horizontal_disabled["border_right"]))

        if self.data.add_page_horizontal_disabled["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.add_page_horizontal_disabled["border_bottom"]))

        if self.data.add_page_horizontal_disabled["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.add_page_horizontal_disabled["border_left"]))

        if self.data.add_page_horizontal_disabled["border_radius"] != 0 and self.data.add_page_horizontal_disabled["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.add_page_horizontal_disabled["border_radius"]))

        if self.data.add_page_horizontal_disabled["padding_top_value"] != 0 and self.data.add_page_horizontal_disabled["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.add_page_horizontal_disabled["padding_top_value"], self.data.add_page_horizontal_disabled["padding_top_type"]))

        if self.data.add_page_horizontal_disabled["padding_right_value"] != 0 and self.data.add_page_horizontal_disabled["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.add_page_horizontal_disabled["padding_right_value"], self.data.add_page_horizontal_disabled["padding_right_type"]))

        if self.data.add_page_horizontal_disabled["padding_bottom_value"] != 0 and self.data.add_page_horizontal_disabled["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.add_page_horizontal_disabled["padding_bottom_value"], self.data.add_page_horizontal_disabled["padding_bottom_type"]))

        if self.data.add_page_horizontal_disabled["padding_left_value"] != 0 and self.data.add_page_horizontal_disabled["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.add_page_horizontal_disabled["padding_left_value"], self.data.add_page_horizontal_disabled["padding_left_type"]))


        if self.data.add_page_horizontal_disabled["margin_top_value"] != 0 and self.data.add_page_horizontal_disabled["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.add_page_horizontal_disabled["margin_top_value"], self.data.add_page_horizontal_disabled["margin_top_type"]))

        if self.data.add_page_horizontal_disabled["margin_right_value"] != 0 and self.data.add_page_horizontal_disabled["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.add_page_horizontal_disabled["margin_right_value"], self.data.add_page_horizontal_disabled["margin_right_type"]))

        if self.data.add_page_horizontal_disabled["margin_bottom_value"] != 0 and self.data.add_page_horizontal_disabled["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.add_page_horizontal_disabled["margin_bottom_value"], self.data.add_page_horizontal_disabled["margin_bottom_type"]))

        if self.data.add_page_horizontal_disabled["margin_left_value"] != 0 and self.data.add_page_horizontal_disabled["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.add_page_horizontal_disabled["margin_left_value"], self.data.add_page_horizontal_disabled["margin_left_type"]))

        f.write("\n}")








        f.write("\n")





        f.write(self.text + "::sub-page:horizontal {")

        if self.data.sub_page_horizontal["color"] != "":
            f.write("\n   color: {};".format(self.data.sub_page_horizontal["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.sub_page_horizontal["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.sub_page_horizontal["outline"]))

        if self.data.sub_page_horizontal["width_value"] != 0 and self.data.sub_page_horizontal["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.sub_page_horizontal["width_value"], self.data.sub_page_horizontal["width_type"]))

        if self.data.sub_page_horizontal["height_value"] != 0 and self.data.sub_page_horizontal["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.sub_page_horizontal["height_value"], self.data.sub_page_horizontal["height_type"]))

        if self.data.sub_page_horizontal["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.sub_page_horizontal["font_family"]))

        if self.data.sub_page_horizontal["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.sub_page_horizontal["font_size"]))

        if self.data.sub_page_horizontal["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.sub_page_horizontal["font_weight"]))

        if self.data.sub_page_horizontal["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.sub_page_horizontal["font_style"]))

        if self.data.sub_page_horizontal["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.sub_page_horizontal["line_height"]))

        if self.data.sub_page_horizontal["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.sub_page_horizontal["text_align"]))

        if self.data.sub_page_horizontal["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.sub_page_horizontal["text_decoration"]))

        if self.data.sub_page_horizontal["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.sub_page_horizontal["text_transform"]))

        if self.data.sub_page_horizontal["background"] != "":
            f.write("\n   background: {};".format(self.data.sub_page_horizontal["background"]))

        if self.data.sub_page_horizontal["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.sub_page_horizontal["background_image"]))

        if self.data.sub_page_horizontal["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.sub_page_horizontal["background_color"]))

        if self.data.sub_page_horizontal["border"] != "":
            f.write("\n   border: {};".format(self.data.sub_page_horizontal["border"]))

        if self.data.sub_page_horizontal["border_width_value"] != 0 and self.data.sub_page_horizontal["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.sub_page_horizontal["border_width_value"], self.data.sub_page_horizontal["border_width_type"]))

        if self.data.sub_page_horizontal["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.sub_page_horizontal["border_style"]))

        if self.data.sub_page_horizontal["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.sub_page_horizontal["border_color"]))

        if self.data.sub_page_horizontal["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.sub_page_horizontal["border_top"]))

        if self.data.sub_page_horizontal["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.sub_page_horizontal["border_right"]))

        if self.data.sub_page_horizontal["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.sub_page_horizontal["border_bottom"]))

        if self.data.sub_page_horizontal["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.sub_page_horizontal["border_left"]))

        if self.data.sub_page_horizontal["border_radius"] != 0 and self.data.sub_page_horizontal["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.sub_page_horizontal["border_radius"]))

        if self.data.sub_page_horizontal["padding_top_value"] != 0 and self.data.sub_page_horizontal["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.sub_page_horizontal["padding_top_value"], self.data.sub_page_horizontal["padding_top_type"]))

        if self.data.sub_page_horizontal["padding_right_value"] != 0 and self.data.sub_page_horizontal["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.sub_page_horizontal["padding_right_value"], self.data.sub_page_horizontal["padding_right_type"]))

        if self.data.sub_page_horizontal["padding_bottom_value"] != 0 and self.data.sub_page_horizontal["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.sub_page_horizontal["padding_bottom_value"], self.data.sub_page_horizontal["padding_bottom_type"]))

        if self.data.sub_page_horizontal["padding_left_value"] != 0 and self.data.sub_page_horizontal["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.sub_page_horizontal["padding_left_value"], self.data.sub_page_horizontal["padding_left_type"]))


        if self.data.sub_page_horizontal["margin_top_value"] != 0 and self.data.sub_page_horizontal["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.sub_page_horizontal["margin_top_value"], self.data.sub_page_horizontal["margin_top_type"]))

        if self.data.sub_page_horizontal["margin_right_value"] != 0 and self.data.sub_page_horizontal["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.sub_page_horizontal["margin_right_value"], self.data.sub_page_horizontal["margin_right_type"]))

        if self.data.sub_page_horizontal["margin_bottom_value"] != 0 and self.data.sub_page_horizontal["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.sub_page_horizontal["margin_bottom_value"], self.data.sub_page_horizontal["margin_bottom_type"]))

        if self.data.sub_page_horizontal["margin_left_value"] != 0 and self.data.sub_page_horizontal["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.sub_page_horizontal["margin_left_value"], self.data.sub_page_horizontal["margin_left_type"]))

        f.write("\n}")







        f.write("\n")





        f.write(self.text + "::sub-page:horizontal:disabled {")

        if self.data.sub_page_horizontal_disabled["color"] != "":
            f.write("\n   color: {};".format(self.data.sub_page_horizontal_disabled["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.sub_page_horizontal_disabled["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.sub_page_horizontal_disabled["outline"]))

        if self.data.sub_page_horizontal_disabled["width_value"] != 0 and self.data.sub_page_horizontal_disabled["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.sub_page_horizontal_disabled["width_value"], self.data.sub_page_horizontal_disabled["width_type"]))

        if self.data.sub_page_horizontal_disabled["height_value"] != 0 and self.data.sub_page_horizontal_disabled["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.sub_page_horizontal_disabled["height_value"], self.data.sub_page_horizontal_disabled["height_type"]))

        if self.data.sub_page_horizontal_disabled["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.sub_page_horizontal_disabled["font_family"]))

        if self.data.sub_page_horizontal_disabled["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.sub_page_horizontal_disabled["font_size"]))

        if self.data.sub_page_horizontal_disabled["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.sub_page_horizontal_disabled["font_weight"]))

        if self.data.sub_page_horizontal_disabled["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.sub_page_horizontal_disabled["font_style"]))

        if self.data.sub_page_horizontal_disabled["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.sub_page_horizontal_disabled["line_height"]))

        if self.data.sub_page_horizontal_disabled["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.sub_page_horizontal_disabled["text_align"]))

        if self.data.sub_page_horizontal_disabled["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.sub_page_horizontal_disabled["text_decoration"]))

        if self.data.sub_page_horizontal_disabled["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.sub_page_horizontal_disabled["text_transform"]))

        if self.data.sub_page_horizontal_disabled["background"] != "":
            f.write("\n   background: {};".format(self.data.sub_page_horizontal_disabled["background"]))

        if self.data.sub_page_horizontal_disabled["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.sub_page_horizontal_disabled["background_image"]))

        if self.data.sub_page_horizontal_disabled["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.sub_page_horizontal_disabled["background_color"]))

        if self.data.sub_page_horizontal_disabled["border"] != "":
            f.write("\n   border: {};".format(self.data.sub_page_horizontal_disabled["border"]))

        if self.data.sub_page_horizontal_disabled["border_width_value"] != 0 and self.data.sub_page_horizontal_disabled["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.sub_page_horizontal_disabled["border_width_value"], self.data.sub_page_horizontal_disabled["border_width_type"]))

        if self.data.sub_page_horizontal_disabled["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.sub_page_horizontal_disabled["border_style"]))

        if self.data.sub_page_horizontal_disabled["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.sub_page_horizontal_disabled["border_color"]))

        if self.data.sub_page_horizontal_disabled["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.sub_page_horizontal_disabled["border_top"]))

        if self.data.sub_page_horizontal_disabled["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.sub_page_horizontal_disabled["border_right"]))

        if self.data.sub_page_horizontal_disabled["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.sub_page_horizontal_disabled["border_bottom"]))

        if self.data.sub_page_horizontal_disabled["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.sub_page_horizontal_disabled["border_left"]))

        if self.data.sub_page_horizontal_disabled["border_radius"] != 0 and self.data.sub_page_horizontal_disabled["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.sub_page_horizontal_disabled["border_radius"]))

        if self.data.sub_page_horizontal_disabled["padding_top_value"] != 0 and self.data.sub_page_horizontal_disabled["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.sub_page_horizontal_disabled["padding_top_value"], self.data.sub_page_horizontal_disabled["padding_top_type"]))

        if self.data.sub_page_horizontal_disabled["padding_right_value"] != 0 and self.data.sub_page_horizontal_disabled["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.sub_page_horizontal_disabled["padding_right_value"], self.data.sub_page_horizontal_disabled["padding_right_type"]))

        if self.data.sub_page_horizontal_disabled["padding_bottom_value"] != 0 and self.data.sub_page_horizontal_disabled["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.sub_page_horizontal_disabled["padding_bottom_value"], self.data.sub_page_horizontal_disabled["padding_bottom_type"]))

        if self.data.sub_page_horizontal_disabled["padding_left_value"] != 0 and self.data.sub_page_horizontal_disabled["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.sub_page_horizontal_disabled["padding_left_value"], self.data.sub_page_horizontal_disabled["padding_left_type"]))


        if self.data.sub_page_horizontal_disabled["margin_top_value"] != 0 and self.data.sub_page_horizontal_disabled["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.sub_page_horizontal_disabled["margin_top_value"], self.data.sub_page_horizontal_disabled["margin_top_type"]))

        if self.data.sub_page_horizontal_disabled["margin_right_value"] != 0 and self.data.sub_page_horizontal_disabled["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.sub_page_horizontal_disabled["margin_right_value"], self.data.sub_page_horizontal_disabled["margin_right_type"]))

        if self.data.sub_page_horizontal_disabled["margin_bottom_value"] != 0 and self.data.sub_page_horizontal_disabled["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.sub_page_horizontal_disabled["margin_bottom_value"], self.data.sub_page_horizontal_disabled["margin_bottom_type"]))

        if self.data.sub_page_horizontal_disabled["margin_left_value"] != 0 and self.data.sub_page_horizontal_disabled["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.sub_page_horizontal_disabled["margin_left_value"], self.data.sub_page_horizontal_disabled["margin_left_type"]))

        f.write("\n}")
