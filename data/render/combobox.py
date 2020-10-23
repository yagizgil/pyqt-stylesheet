class ComboBox():

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




        f.write(self.text + ":on {")

        if self.data.on["color"] != "":
            f.write("\n   color: {};".format(self.data.on["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.on["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.on["outline"]))

        if self.data.on["width_value"] != 0 and self.data.on["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.on["width_value"], self.data.on["width_type"]))

        if self.data.on["height_value"] != 0 and self.data.on["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.on["height_value"], self.data.on["height_type"]))

        if self.data.on["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.on["font_family"]))

        if self.data.on["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.on["font_size"]))

        if self.data.on["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.on["font_weight"]))

        if self.data.on["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.on["font_style"]))

        if self.data.on["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.on["line_height"]))

        if self.data.on["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.on["text_align"]))

        if self.data.on["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.on["text_decoration"]))

        if self.data.on["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.on["text_transform"]))

        if self.data.on["background"] != "":
            f.write("\n   background: {};".format(self.data.on["background"]))

        if self.data.on["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.on["background_image"]))

        if self.data.on["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.on["background_color"]))

        if self.data.on["border"] != "":
            f.write("\n   border: {};".format(self.data.on["border"]))

        if self.data.on["border_width_value"] != 0 and self.data.on["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.on["border_width_value"], self.data.on["border_width_type"]))

        if self.data.on["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.on["border_style"]))

        if self.data.on["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.on["border_color"]))

        if self.data.on["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.on["border_top"]))

        if self.data.on["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.on["border_right"]))

        if self.data.on["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.on["border_bottom"]))

        if self.data.on["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.on["border_left"]))

        if self.data.on["border_radius"] != 0 and self.data.on["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.on["border_radius"]))

        if self.data.on["padding_top_value"] != 0 and self.data.on["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.on["padding_top_value"], self.data.on["padding_top_type"]))

        if self.data.on["padding_right_value"] != 0 and self.data.on["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.on["padding_right_value"], self.data.on["padding_right_type"]))

        if self.data.on["padding_bottom_value"] != 0 and self.data.on["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.on["padding_bottom_value"], self.data.on["padding_bottom_type"]))

        if self.data.on["padding_left_value"] != 0 and self.data.on["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.on["padding_left_value"], self.data.on["padding_left_type"]))


        if self.data.on["margin_top_value"] != 0 and self.data.on["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.on["margin_top_value"], self.data.on["margin_top_type"]))

        if self.data.on["margin_right_value"] != 0 and self.data.on["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.on["margin_right_value"], self.data.on["margin_right_type"]))

        if self.data.on["margin_bottom_value"] != 0 and self.data.on["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.on["margin_bottom_value"], self.data.on["margin_bottom_type"]))

        if self.data.on["margin_left_value"] != 0 and self.data.on["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.on["margin_left_value"], self.data.on["margin_left_type"]))

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




        f.write(self.text + ":editable {")

        if self.data.editable["color"] != "":
            f.write("\n   color: {};".format(self.data.editable["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.editable["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.editable["outline"]))

        if self.data.editable["width_value"] != 0 and self.data.editable["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.editable["width_value"], self.data.editable["width_type"]))

        if self.data.editable["height_value"] != 0 and self.data.editable["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.editable["height_value"], self.data.editable["height_type"]))

        if self.data.editable["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.editable["font_family"]))

        if self.data.editable["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.editable["font_size"]))

        if self.data.editable["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.editable["font_weight"]))

        if self.data.editable["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.editable["font_style"]))

        if self.data.editable["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.editable["line_height"]))

        if self.data.editable["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.editable["text_align"]))

        if self.data.editable["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.editable["text_decoration"]))

        if self.data.editable["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.editable["text_transform"]))

        if self.data.editable["background"] != "":
            f.write("\n   background: {};".format(self.data.editable["background"]))

        if self.data.editable["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.editable["background_image"]))

        if self.data.editable["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.editable["background_color"]))

        if self.data.editable["border"] != "":
            f.write("\n   border: {};".format(self.data.editable["border"]))

        if self.data.editable["border_width_value"] != 0 and self.data.editable["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.editable["border_width_value"], self.data.editable["border_width_type"]))

        if self.data.editable["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.editable["border_style"]))

        if self.data.editable["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.editable["border_color"]))

        if self.data.editable["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.editable["border_top"]))

        if self.data.editable["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.editable["border_right"]))

        if self.data.editable["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.editable["border_bottom"]))

        if self.data.editable["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.editable["border_left"]))

        if self.data.editable["border_radius"] != 0 and self.data.editable["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.editable["border_radius"]))

        if self.data.editable["padding_top_value"] != 0 and self.data.editable["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.editable["padding_top_value"], self.data.editable["padding_top_type"]))

        if self.data.editable["padding_right_value"] != 0 and self.data.editable["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.editable["padding_right_value"], self.data.editable["padding_right_type"]))

        if self.data.editable["padding_bottom_value"] != 0 and self.data.editable["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.editable["padding_bottom_value"], self.data.editable["padding_bottom_type"]))

        if self.data.editable["padding_left_value"] != 0 and self.data.editable["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.editable["padding_left_value"], self.data.editable["padding_left_type"]))


        if self.data.editable["margin_top_value"] != 0 and self.data.editable["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.editable["margin_top_value"], self.data.editable["margin_top_type"]))

        if self.data.editable["margin_right_value"] != 0 and self.data.editable["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.editable["margin_right_value"], self.data.editable["margin_right_type"]))

        if self.data.editable["margin_bottom_value"] != 0 and self.data.editable["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.editable["margin_bottom_value"], self.data.editable["margin_bottom_type"]))

        if self.data.editable["margin_left_value"] != 0 and self.data.editable["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.editable["margin_left_value"], self.data.editable["margin_left_type"]))

        f.write("\n}")





        f.write("\n")




        f.write(self.text + ":!editable {")

        if self.data.u_editable["color"] != "":
            f.write("\n   color: {};".format(self.data.u_editable["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.u_editable["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.u_editable["outline"]))

        if self.data.u_editable["width_value"] != 0 and self.data.u_editable["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.u_editable["width_value"], self.data.u_editable["width_type"]))

        if self.data.u_editable["height_value"] != 0 and self.data.u_editable["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.u_editable["height_value"], self.data.u_editable["height_type"]))

        if self.data.u_editable["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.u_editable["font_family"]))

        if self.data.u_editable["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.u_editable["font_size"]))

        if self.data.u_editable["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.u_editable["font_weight"]))

        if self.data.u_editable["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.u_editable["font_style"]))

        if self.data.u_editable["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.u_editable["line_height"]))

        if self.data.u_editable["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.u_editable["text_align"]))

        if self.data.u_editable["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.u_editable["text_decoration"]))

        if self.data.u_editable["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.u_editable["text_transform"]))

        if self.data.u_editable["background"] != "":
            f.write("\n   background: {};".format(self.data.u_editable["background"]))

        if self.data.u_editable["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.u_editable["background_image"]))

        if self.data.u_editable["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.u_editable["background_color"]))

        if self.data.u_editable["border"] != "":
            f.write("\n   border: {};".format(self.data.u_editable["border"]))

        if self.data.u_editable["border_width_value"] != 0 and self.data.u_editable["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.u_editable["border_width_value"], self.data.u_editable["border_width_type"]))

        if self.data.u_editable["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.u_editable["border_style"]))

        if self.data.u_editable["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.u_editable["border_color"]))

        if self.data.u_editable["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.u_editable["border_top"]))

        if self.data.u_editable["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.u_editable["border_right"]))

        if self.data.u_editable["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.u_editable["border_bottom"]))

        if self.data.u_editable["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.u_editable["border_left"]))

        if self.data.u_editable["border_radius"] != 0 and self.data.u_editable["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.u_editable["border_radius"]))

        if self.data.u_editable["padding_top_value"] != 0 and self.data.u_editable["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.u_editable["padding_top_value"], self.data.u_editable["padding_top_type"]))

        if self.data.u_editable["padding_right_value"] != 0 and self.data.u_editable["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.u_editable["padding_right_value"], self.data.u_editable["padding_right_type"]))

        if self.data.u_editable["padding_bottom_value"] != 0 and self.data.u_editable["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.u_editable["padding_bottom_value"], self.data.u_editable["padding_bottom_type"]))

        if self.data.u_editable["padding_left_value"] != 0 and self.data.u_editable["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.u_editable["padding_left_value"], self.data.u_editable["padding_left_type"]))


        if self.data.u_editable["margin_top_value"] != 0 and self.data.u_editable["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.u_editable["margin_top_value"], self.data.u_editable["margin_top_type"]))

        if self.data.u_editable["margin_right_value"] != 0 and self.data.u_editable["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.u_editable["margin_right_value"], self.data.u_editable["margin_right_type"]))

        if self.data.u_editable["margin_bottom_value"] != 0 and self.data.u_editable["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.u_editable["margin_bottom_value"], self.data.u_editable["margin_bottom_type"]))

        if self.data.u_editable["margin_left_value"] != 0 and self.data.u_editable["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.u_editable["margin_left_value"], self.data.u_editable["margin_left_type"]))

        f.write("\n}")




        f.write("\n")




        f.write(self.text + ":!editable:on {")

        if self.data.u_editable_on["color"] != "":
            f.write("\n   color: {};".format(self.data.u_editable_on["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.u_editable_on["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.u_editable_on["outline"]))

        if self.data.u_editable_on["width_value"] != 0 and self.data.u_editable_on["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.u_editable_on["width_value"], self.data.u_editable_on["width_type"]))

        if self.data.u_editable_on["height_value"] != 0 and self.data.u_editable_on["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.u_editable_on["height_value"], self.data.u_editable_on["height_type"]))

        if self.data.u_editable_on["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.u_editable_on["font_family"]))

        if self.data.u_editable_on["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.u_editable_on["font_size"]))

        if self.data.u_editable_on["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.u_editable_on["font_weight"]))

        if self.data.u_editable_on["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.u_editable_on["font_style"]))

        if self.data.u_editable_on["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.u_editable_on["line_height"]))

        if self.data.u_editable_on["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.u_editable_on["text_align"]))

        if self.data.u_editable_on["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.u_editable_on["text_decoration"]))

        if self.data.u_editable_on["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.u_editable_on["text_transform"]))

        if self.data.u_editable_on["background"] != "":
            f.write("\n   background: {};".format(self.data.u_editable_on["background"]))

        if self.data.u_editable_on["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.u_editable_on["background_image"]))

        if self.data.u_editable_on["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.u_editable_on["background_color"]))

        if self.data.u_editable_on["border"] != "":
            f.write("\n   border: {};".format(self.data.u_editable_on["border"]))

        if self.data.u_editable_on["border_width_value"] != 0 and self.data.u_editable_on["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.u_editable_on["border_width_value"], self.data.u_editable_on["border_width_type"]))

        if self.data.u_editable_on["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.u_editable_on["border_style"]))

        if self.data.u_editable_on["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.u_editable_on["border_color"]))

        if self.data.u_editable_on["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.u_editable_on["border_top"]))

        if self.data.u_editable_on["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.u_editable_on["border_right"]))

        if self.data.u_editable_on["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.u_editable_on["border_bottom"]))

        if self.data.u_editable_on["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.u_editable_on["border_left"]))

        if self.data.u_editable_on["border_radius"] != 0 and self.data.u_editable_on["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.u_editable_on["border_radius"]))

        if self.data.u_editable_on["padding_top_value"] != 0 and self.data.u_editable_on["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.u_editable_on["padding_top_value"], self.data.u_editable_on["padding_top_type"]))

        if self.data.u_editable_on["padding_right_value"] != 0 and self.data.u_editable_on["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.u_editable_on["padding_right_value"], self.data.u_editable_on["padding_right_type"]))

        if self.data.u_editable_on["padding_bottom_value"] != 0 and self.data.u_editable_on["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.u_editable_on["padding_bottom_value"], self.data.u_editable_on["padding_bottom_type"]))

        if self.data.u_editable_on["padding_left_value"] != 0 and self.data.u_editable_on["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.u_editable_on["padding_left_value"], self.data.u_editable_on["padding_left_type"]))


        if self.data.u_editable_on["margin_top_value"] != 0 and self.data.u_editable_on["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.u_editable_on["margin_top_value"], self.data.u_editable_on["margin_top_type"]))

        if self.data.u_editable_on["margin_right_value"] != 0 and self.data.u_editable_on["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.u_editable_on["margin_right_value"], self.data.u_editable_on["margin_right_type"]))

        if self.data.u_editable_on["margin_bottom_value"] != 0 and self.data.u_editable_on["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.u_editable_on["margin_bottom_value"], self.data.u_editable_on["margin_bottom_type"]))

        if self.data.u_editable_on["margin_left_value"] != 0 and self.data.u_editable_on["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.u_editable_on["margin_left_value"], self.data.u_editable_on["margin_left_type"]))

        f.write("\n}")





        f.write("\n")




        f.write(self.text + "::drop-down {")

        if self.data.drop_down["color"] != "":
            f.write("\n   color: {};".format(self.data.drop_down["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.drop_down["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.drop_down["outline"]))

        if self.data.drop_down["width_value"] != 0 and self.data.drop_down["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.drop_down["width_value"], self.data.drop_down["width_type"]))

        if self.data.drop_down["height_value"] != 0 and self.data.drop_down["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.drop_down["height_value"], self.data.drop_down["height_type"]))

        if self.data.drop_down["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.drop_down["font_family"]))

        if self.data.drop_down["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.drop_down["font_size"]))

        if self.data.drop_down["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.drop_down["font_weight"]))

        if self.data.drop_down["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.drop_down["font_style"]))

        if self.data.drop_down["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.drop_down["line_height"]))

        if self.data.drop_down["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.drop_down["text_align"]))

        if self.data.drop_down["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.drop_down["text_decoration"]))

        if self.data.drop_down["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.drop_down["text_transform"]))

        if self.data.drop_down["background"] != "":
            f.write("\n   background: {};".format(self.data.drop_down["background"]))

        if self.data.drop_down["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.drop_down["background_image"]))

        if self.data.drop_down["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.drop_down["background_color"]))

        if self.data.drop_down["border"] != "":
            f.write("\n   border: {};".format(self.data.drop_down["border"]))

        if self.data.drop_down["border_width_value"] != 0 and self.data.drop_down["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.drop_down["border_width_value"], self.data.drop_down["border_width_type"]))

        if self.data.drop_down["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.drop_down["border_style"]))

        if self.data.drop_down["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.drop_down["border_color"]))

        if self.data.drop_down["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.drop_down["border_top"]))

        if self.data.drop_down["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.drop_down["border_right"]))

        if self.data.drop_down["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.drop_down["border_bottom"]))

        if self.data.drop_down["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.drop_down["border_left"]))

        if self.data.drop_down["border_radius"] != 0 and self.data.drop_down["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.drop_down["border_radius"]))

        if self.data.drop_down["padding_top_value"] != 0 and self.data.drop_down["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.drop_down["padding_top_value"], self.data.drop_down["padding_top_type"]))

        if self.data.drop_down["padding_right_value"] != 0 and self.data.drop_down["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.drop_down["padding_right_value"], self.data.drop_down["padding_right_type"]))

        if self.data.drop_down["padding_bottom_value"] != 0 and self.data.drop_down["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.drop_down["padding_bottom_value"], self.data.drop_down["padding_bottom_type"]))

        if self.data.drop_down["padding_left_value"] != 0 and self.data.drop_down["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.drop_down["padding_left_value"], self.data.drop_down["padding_left_type"]))


        if self.data.drop_down["margin_top_value"] != 0 and self.data.drop_down["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.drop_down["margin_top_value"], self.data.drop_down["margin_top_type"]))

        if self.data.drop_down["margin_right_value"] != 0 and self.data.drop_down["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.drop_down["margin_right_value"], self.data.drop_down["margin_right_type"]))

        if self.data.drop_down["margin_bottom_value"] != 0 and self.data.drop_down["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.drop_down["margin_bottom_value"], self.data.drop_down["margin_bottom_type"]))

        if self.data.drop_down["margin_left_value"] != 0 and self.data.drop_down["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.drop_down["margin_left_value"], self.data.drop_down["margin_left_type"]))

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




        f.write(self.text + "::down-arrow:on {")

        if self.data.down_arrow_on["color"] != "":
            f.write("\n   color: {};".format(self.data.down_arrow_on["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.down_arrow_on["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.down_arrow_on["outline"]))

        if self.data.down_arrow_on["width_value"] != 0 and self.data.down_arrow_on["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.down_arrow_on["width_value"], self.data.down_arrow_on["width_type"]))

        if self.data.down_arrow_on["height_value"] != 0 and self.data.down_arrow_on["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.down_arrow_on["height_value"], self.data.down_arrow_on["height_type"]))

        if self.data.down_arrow_on["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.down_arrow_on["font_family"]))

        if self.data.down_arrow_on["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.down_arrow_on["font_size"]))

        if self.data.down_arrow_on["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.down_arrow_on["font_weight"]))

        if self.data.down_arrow_on["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.down_arrow_on["font_style"]))

        if self.data.down_arrow_on["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.down_arrow_on["line_height"]))

        if self.data.down_arrow_on["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.down_arrow_on["text_align"]))

        if self.data.down_arrow_on["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.down_arrow_on["text_decoration"]))

        if self.data.down_arrow_on["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.down_arrow_on["text_transform"]))

        if self.data.down_arrow_on["background"] != "":
            f.write("\n   background: {};".format(self.data.down_arrow_on["background"]))

        if self.data.down_arrow_on["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.down_arrow_on["background_image"]))

        if self.data.down_arrow_on["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.down_arrow_on["background_color"]))

        if self.data.down_arrow_on["border"] != "":
            f.write("\n   border: {};".format(self.data.down_arrow_on["border"]))

        if self.data.down_arrow_on["border_width_value"] != 0 and self.data.down_arrow_on["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.down_arrow_on["border_width_value"], self.data.down_arrow_on["border_width_type"]))

        if self.data.down_arrow_on["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.down_arrow_on["border_style"]))

        if self.data.down_arrow_on["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.down_arrow_on["border_color"]))

        if self.data.down_arrow_on["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.down_arrow_on["border_top"]))

        if self.data.down_arrow_on["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.down_arrow_on["border_right"]))

        if self.data.down_arrow_on["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.down_arrow_on["border_bottom"]))

        if self.data.down_arrow_on["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.down_arrow_on["border_left"]))

        if self.data.down_arrow_on["border_radius"] != 0 and self.data.down_arrow_on["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.down_arrow_on["border_radius"]))

        if self.data.down_arrow_on["padding_top_value"] != 0 and self.data.down_arrow_on["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.down_arrow_on["padding_top_value"], self.data.down_arrow_on["padding_top_type"]))

        if self.data.down_arrow_on["padding_right_value"] != 0 and self.data.down_arrow_on["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.down_arrow_on["padding_right_value"], self.data.down_arrow_on["padding_right_type"]))

        if self.data.down_arrow_on["padding_bottom_value"] != 0 and self.data.down_arrow_on["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.down_arrow_on["padding_bottom_value"], self.data.down_arrow_on["padding_bottom_type"]))

        if self.data.down_arrow_on["padding_left_value"] != 0 and self.data.down_arrow_on["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.down_arrow_on["padding_left_value"], self.data.down_arrow_on["padding_left_type"]))


        if self.data.down_arrow_on["margin_top_value"] != 0 and self.data.down_arrow_on["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.down_arrow_on["margin_top_value"], self.data.down_arrow_on["margin_top_type"]))

        if self.data.down_arrow_on["margin_right_value"] != 0 and self.data.down_arrow_on["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.down_arrow_on["margin_right_value"], self.data.down_arrow_on["margin_right_type"]))

        if self.data.down_arrow_on["margin_bottom_value"] != 0 and self.data.down_arrow_on["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.down_arrow_on["margin_bottom_value"], self.data.down_arrow_on["margin_bottom_type"]))

        if self.data.down_arrow_on["margin_left_value"] != 0 and self.data.down_arrow_on["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.down_arrow_on["margin_left_value"], self.data.down_arrow_on["margin_left_type"]))

        f.write("\n}")





        f.write("\n")




        f.write(self.text + "::drop-down:editable {")

        if self.data.drop_down_editable["color"] != "":
            f.write("\n   color: {};".format(self.data.drop_down_editable["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.drop_down_editable["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.drop_down_editable["outline"]))

        if self.data.drop_down_editable["width_value"] != 0 and self.data.drop_down_editable["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.drop_down_editable["width_value"], self.data.drop_down_editable["width_type"]))

        if self.data.drop_down_editable["height_value"] != 0 and self.data.drop_down_editable["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.drop_down_editable["height_value"], self.data.drop_down_editable["height_type"]))

        if self.data.drop_down_editable["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.drop_down_editable["font_family"]))

        if self.data.drop_down_editable["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.drop_down_editable["font_size"]))

        if self.data.drop_down_editable["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.drop_down_editable["font_weight"]))

        if self.data.drop_down_editable["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.drop_down_editable["font_style"]))

        if self.data.drop_down_editable["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.drop_down_editable["line_height"]))

        if self.data.drop_down_editable["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.drop_down_editable["text_align"]))

        if self.data.drop_down_editable["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.drop_down_editable["text_decoration"]))

        if self.data.drop_down_editable["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.drop_down_editable["text_transform"]))

        if self.data.drop_down_editable["background"] != "":
            f.write("\n   background: {};".format(self.data.drop_down_editable["background"]))

        if self.data.drop_down_editable["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.drop_down_editable["background_image"]))

        if self.data.drop_down_editable["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.drop_down_editable["background_color"]))

        if self.data.drop_down_editable["border"] != "":
            f.write("\n   border: {};".format(self.data.drop_down_editable["border"]))

        if self.data.drop_down_editable["border_width_value"] != 0 and self.data.drop_down_editable["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.drop_down_editable["border_width_value"], self.data.drop_down_editable["border_width_type"]))

        if self.data.drop_down_editable["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.drop_down_editable["border_style"]))

        if self.data.drop_down_editable["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.drop_down_editable["border_color"]))

        if self.data.drop_down_editable["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.drop_down_editable["border_top"]))

        if self.data.drop_down_editable["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.drop_down_editable["border_right"]))

        if self.data.drop_down_editable["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.drop_down_editable["border_bottom"]))

        if self.data.drop_down_editable["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.drop_down_editable["border_left"]))

        if self.data.drop_down_editable["border_radius"] != 0 and self.data.drop_down_editable["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.drop_down_editable["border_radius"]))

        if self.data.drop_down_editable["padding_top_value"] != 0 and self.data.drop_down_editable["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.drop_down_editable["padding_top_value"], self.data.drop_down_editable["padding_top_type"]))

        if self.data.drop_down_editable["padding_right_value"] != 0 and self.data.drop_down_editable["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.drop_down_editable["padding_right_value"], self.data.drop_down_editable["padding_right_type"]))

        if self.data.drop_down_editable["padding_bottom_value"] != 0 and self.data.drop_down_editable["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.drop_down_editable["padding_bottom_value"], self.data.drop_down_editable["padding_bottom_type"]))

        if self.data.drop_down_editable["padding_left_value"] != 0 and self.data.drop_down_editable["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.drop_down_editable["padding_left_value"], self.data.drop_down_editable["padding_left_type"]))


        if self.data.drop_down_editable["margin_top_value"] != 0 and self.data.drop_down_editable["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.drop_down_editable["margin_top_value"], self.data.drop_down_editable["margin_top_type"]))

        if self.data.drop_down_editable["margin_right_value"] != 0 and self.data.drop_down_editable["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.drop_down_editable["margin_right_value"], self.data.drop_down_editable["margin_right_type"]))

        if self.data.drop_down_editable["margin_bottom_value"] != 0 and self.data.drop_down_editable["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.drop_down_editable["margin_bottom_value"], self.data.drop_down_editable["margin_bottom_type"]))

        if self.data.drop_down_editable["margin_left_value"] != 0 and self.data.drop_down_editable["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.drop_down_editable["margin_left_value"], self.data.drop_down_editable["margin_left_type"]))

        f.write("\n}")





        f.write("\n")




        f.write(self.text + "::drop-down:editable:on {")

        if self.data.drop_down_editable_on["color"] != "":
            f.write("\n   color: {};".format(self.data.drop_down_editable_on["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.drop_down_editable_on["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.drop_down_editable_on["outline"]))

        if self.data.drop_down_editable_on["width_value"] != 0 and self.data.drop_down_editable_on["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.drop_down_editable_on["width_value"], self.data.drop_down_editable_on["width_type"]))

        if self.data.drop_down_editable_on["height_value"] != 0 and self.data.drop_down_editable_on["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.drop_down_editable_on["height_value"], self.data.drop_down_editable_on["height_type"]))

        if self.data.drop_down_editable_on["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.drop_down_editable_on["font_family"]))

        if self.data.drop_down_editable_on["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.drop_down_editable_on["font_size"]))

        if self.data.drop_down_editable_on["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.drop_down_editable_on["font_weight"]))

        if self.data.drop_down_editable_on["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.drop_down_editable_on["font_style"]))

        if self.data.drop_down_editable_on["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.drop_down_editable_on["line_height"]))

        if self.data.drop_down_editable_on["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.drop_down_editable_on["text_align"]))

        if self.data.drop_down_editable_on["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.drop_down_editable_on["text_decoration"]))

        if self.data.drop_down_editable_on["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.drop_down_editable_on["text_transform"]))

        if self.data.drop_down_editable_on["background"] != "":
            f.write("\n   background: {};".format(self.data.drop_down_editable_on["background"]))

        if self.data.drop_down_editable_on["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.drop_down_editable_on["background_image"]))

        if self.data.drop_down_editable_on["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.drop_down_editable_on["background_color"]))

        if self.data.drop_down_editable_on["border"] != "":
            f.write("\n   border: {};".format(self.data.drop_down_editable_on["border"]))

        if self.data.drop_down_editable_on["border_width_value"] != 0 and self.data.drop_down_editable_on["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.drop_down_editable_on["border_width_value"], self.data.drop_down_editable_on["border_width_type"]))

        if self.data.drop_down_editable_on["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.drop_down_editable_on["border_style"]))

        if self.data.drop_down_editable_on["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.drop_down_editable_on["border_color"]))

        if self.data.drop_down_editable_on["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.drop_down_editable_on["border_top"]))

        if self.data.drop_down_editable_on["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.drop_down_editable_on["border_right"]))

        if self.data.drop_down_editable_on["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.drop_down_editable_on["border_bottom"]))

        if self.data.drop_down_editable_on["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.drop_down_editable_on["border_left"]))

        if self.data.drop_down_editable_on["border_radius"] != 0 and self.data.drop_down_editable_on["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.drop_down_editable_on["border_radius"]))

        if self.data.drop_down_editable_on["padding_top_value"] != 0 and self.data.drop_down_editable_on["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.drop_down_editable_on["padding_top_value"], self.data.drop_down_editable_on["padding_top_type"]))

        if self.data.drop_down_editable_on["padding_right_value"] != 0 and self.data.drop_down_editable_on["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.drop_down_editable_on["padding_right_value"], self.data.drop_down_editable_on["padding_right_type"]))

        if self.data.drop_down_editable_on["padding_bottom_value"] != 0 and self.data.drop_down_editable_on["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.drop_down_editable_on["padding_bottom_value"], self.data.drop_down_editable_on["padding_bottom_type"]))

        if self.data.drop_down_editable_on["padding_left_value"] != 0 and self.data.drop_down_editable_on["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.drop_down_editable_on["padding_left_value"], self.data.drop_down_editable_on["padding_left_type"]))


        if self.data.drop_down_editable_on["margin_top_value"] != 0 and self.data.drop_down_editable_on["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.drop_down_editable_on["margin_top_value"], self.data.drop_down_editable_on["margin_top_type"]))

        if self.data.drop_down_editable_on["margin_right_value"] != 0 and self.data.drop_down_editable_on["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.drop_down_editable_on["margin_right_value"], self.data.drop_down_editable_on["margin_right_type"]))

        if self.data.drop_down_editable_on["margin_bottom_value"] != 0 and self.data.drop_down_editable_on["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.drop_down_editable_on["margin_bottom_value"], self.data.drop_down_editable_on["margin_bottom_type"]))

        if self.data.drop_down_editable_on["margin_left_value"] != 0 and self.data.drop_down_editable_on["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.drop_down_editable_on["margin_left_value"], self.data.drop_down_editable_on["margin_left_type"]))

        f.write("\n}")
