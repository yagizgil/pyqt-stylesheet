class GroupBox():

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




        f.write(self.text + "::title {")

        if self.data.title["color"] != "":
            f.write("\n   color: {};".format(self.data.title["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.title["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.title["outline"]))

        if self.data.title["width_value"] != 0 and self.data.title["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.title["width_value"], self.data.title["width_type"]))

        if self.data.title["height_value"] != 0 and self.data.title["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.title["height_value"], self.data.title["height_type"]))

        if self.data.title["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.title["font_family"]))

        if self.data.title["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.title["font_size"]))

        if self.data.title["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.title["font_weight"]))

        if self.data.title["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.title["font_style"]))

        if self.data.title["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.title["line_height"]))

        if self.data.title["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.title["text_align"]))

        if self.data.title["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.title["text_decoration"]))

        if self.data.title["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.title["text_transform"]))

        if self.data.title["background"] != "":
            f.write("\n   background: {};".format(self.data.title["background"]))

        if self.data.title["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.title["background_image"]))

        if self.data.title["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.title["background_color"]))

        if self.data.title["border"] != "":
            f.write("\n   border: {};".format(self.data.title["border"]))

        if self.data.title["border_width_value"] != 0 and self.data.title["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.title["border_width_value"], self.data.title["border_width_type"]))

        if self.data.title["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.title["border_style"]))

        if self.data.title["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.title["border_color"]))

        if self.data.title["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.title["border_top"]))

        if self.data.title["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.title["border_right"]))

        if self.data.title["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.title["border_bottom"]))

        if self.data.title["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.title["border_left"]))

        if self.data.title["border_radius"] != 0 and self.data.title["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.title["border_radius"]))

        if self.data.title["padding_top_value"] != 0 and self.data.title["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.title["padding_top_value"], self.data.title["padding_top_type"]))

        if self.data.title["padding_right_value"] != 0 and self.data.title["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.title["padding_right_value"], self.data.title["padding_right_type"]))

        if self.data.title["padding_bottom_value"] != 0 and self.data.title["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.title["padding_bottom_value"], self.data.title["padding_bottom_type"]))

        if self.data.title["padding_left_value"] != 0 and self.data.title["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.title["padding_left_value"], self.data.title["padding_left_type"]))


        if self.data.title["margin_top_value"] != 0 and self.data.title["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.title["margin_top_value"], self.data.title["margin_top_type"]))

        if self.data.title["margin_right_value"] != 0 and self.data.title["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.title["margin_right_value"], self.data.title["margin_right_type"]))

        if self.data.title["margin_bottom_value"] != 0 and self.data.title["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.title["margin_bottom_value"], self.data.title["margin_bottom_type"]))

        if self.data.title["margin_left_value"] != 0 and self.data.title["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.title["margin_left_value"], self.data.title["margin_left_type"]))


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
