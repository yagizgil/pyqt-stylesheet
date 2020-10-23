class DockWidget():

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




        f.write(self.text + "::close-button {")

        if self.data.close_button["color"] != "":
            f.write("\n   color: {};".format(self.data.close_button["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.close_button["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.close_button["outline"]))

        if self.data.close_button["width_value"] != 0 and self.data.close_button["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.close_button["width_value"], self.data.close_button["width_type"]))

        if self.data.close_button["height_value"] != 0 and self.data.close_button["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.close_button["height_value"], self.data.close_button["height_type"]))

        if self.data.close_button["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.close_button["font_family"]))

        if self.data.close_button["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.close_button["font_size"]))

        if self.data.close_button["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.close_button["font_weight"]))

        if self.data.close_button["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.close_button["font_style"]))

        if self.data.close_button["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.close_button["line_height"]))

        if self.data.close_button["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.close_button["text_align"]))

        if self.data.close_button["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.close_button["text_decoration"]))

        if self.data.close_button["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.close_button["text_transform"]))

        if self.data.close_button["background"] != "":
            f.write("\n   background: {};".format(self.data.close_button["background"]))

        if self.data.close_button["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.close_button["background_image"]))

        if self.data.close_button["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.close_button["background_color"]))

        if self.data.close_button["border"] != "":
            f.write("\n   border: {};".format(self.data.close_button["border"]))

        if self.data.close_button["border_width_value"] != 0 and self.data.close_button["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.close_button["border_width_value"], self.data.close_button["border_width_type"]))

        if self.data.close_button["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.close_button["border_style"]))

        if self.data.close_button["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.close_button["border_color"]))

        if self.data.close_button["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.close_button["border_top"]))

        if self.data.close_button["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.close_button["border_right"]))

        if self.data.close_button["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.close_button["border_bottom"]))

        if self.data.close_button["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.close_button["border_left"]))

        if self.data.close_button["border_radius"] != 0 and self.data.close_button["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.close_button["border_radius"]))

        if self.data.close_button["padding_top_value"] != 0 and self.data.close_button["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.close_button["padding_top_value"], self.data.close_button["padding_top_type"]))

        if self.data.close_button["padding_right_value"] != 0 and self.data.close_button["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.close_button["padding_right_value"], self.data.close_button["padding_right_type"]))

        if self.data.close_button["padding_bottom_value"] != 0 and self.data.close_button["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.close_button["padding_bottom_value"], self.data.close_button["padding_bottom_type"]))

        if self.data.close_button["padding_left_value"] != 0 and self.data.close_button["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.close_button["padding_left_value"], self.data.close_button["padding_left_type"]))


        if self.data.close_button["margin_top_value"] != 0 and self.data.close_button["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.close_button["margin_top_value"], self.data.close_button["margin_top_type"]))

        if self.data.close_button["margin_right_value"] != 0 and self.data.close_button["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.close_button["margin_right_value"], self.data.close_button["margin_right_type"]))

        if self.data.close_button["margin_bottom_value"] != 0 and self.data.close_button["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.close_button["margin_bottom_value"], self.data.close_button["margin_bottom_type"]))

        if self.data.close_button["margin_left_value"] != 0 and self.data.close_button["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.close_button["margin_left_value"], self.data.close_button["margin_left_type"]))


        f.write("\n}")




        f.write("\n")




        f.write(self.text + "::close-button:hover {")

        if self.data.close_button_hover["color"] != "":
            f.write("\n   color: {};".format(self.data.close_button_hover["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.close_button_hover["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.close_button_hover["outline"]))

        if self.data.close_button_hover["width_value"] != 0 and self.data.close_button_hover["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.close_button_hover["width_value"], self.data.close_button_hover["width_type"]))

        if self.data.close_button_hover["height_value"] != 0 and self.data.close_button_hover["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.close_button_hover["height_value"], self.data.close_button_hover["height_type"]))

        if self.data.close_button_hover["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.close_button_hover["font_family"]))

        if self.data.close_button_hover["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.close_button_hover["font_size"]))

        if self.data.close_button_hover["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.close_button_hover["font_weight"]))

        if self.data.close_button_hover["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.close_button_hover["font_style"]))

        if self.data.close_button_hover["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.close_button_hover["line_height"]))

        if self.data.close_button_hover["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.close_button_hover["text_align"]))

        if self.data.close_button_hover["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.close_button_hover["text_decoration"]))

        if self.data.close_button_hover["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.close_button_hover["text_transform"]))

        if self.data.close_button_hover["background"] != "":
            f.write("\n   background: {};".format(self.data.close_button_hover["background"]))

        if self.data.close_button_hover["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.close_button_hover["background_image"]))

        if self.data.close_button_hover["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.close_button_hover["background_color"]))

        if self.data.close_button_hover["border"] != "":
            f.write("\n   border: {};".format(self.data.close_button_hover["border"]))

        if self.data.close_button_hover["border_width_value"] != 0 and self.data.close_button_hover["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.close_button_hover["border_width_value"], self.data.close_button_hover["border_width_type"]))

        if self.data.close_button_hover["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.close_button_hover["border_style"]))

        if self.data.close_button_hover["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.close_button_hover["border_color"]))

        if self.data.close_button_hover["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.close_button_hover["border_top"]))

        if self.data.close_button_hover["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.close_button_hover["border_right"]))

        if self.data.close_button_hover["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.close_button_hover["border_bottom"]))

        if self.data.close_button_hover["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.close_button_hover["border_left"]))

        if self.data.close_button_hover["border_radius"] != 0 and self.data.close_button_hover["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.close_button_hover["border_radius"]))

        if self.data.close_button_hover["padding_top_value"] != 0 and self.data.close_button_hover["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.close_button_hover["padding_top_value"], self.data.close_button_hover["padding_top_type"]))

        if self.data.close_button_hover["padding_right_value"] != 0 and self.data.close_button_hover["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.close_button_hover["padding_right_value"], self.data.close_button_hover["padding_right_type"]))

        if self.data.close_button_hover["padding_bottom_value"] != 0 and self.data.close_button_hover["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.close_button_hover["padding_bottom_value"], self.data.close_button_hover["padding_bottom_type"]))

        if self.data.close_button_hover["padding_left_value"] != 0 and self.data.close_button_hover["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.close_button_hover["padding_left_value"], self.data.close_button_hover["padding_left_type"]))


        if self.data.close_button_hover["margin_top_value"] != 0 and self.data.close_button_hover["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.close_button_hover["margin_top_value"], self.data.close_button_hover["margin_top_type"]))

        if self.data.close_button_hover["margin_right_value"] != 0 and self.data.close_button_hover["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.close_button_hover["margin_right_value"], self.data.close_button_hover["margin_right_type"]))

        if self.data.close_button_hover["margin_bottom_value"] != 0 and self.data.close_button_hover["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.close_button_hover["margin_bottom_value"], self.data.close_button_hover["margin_bottom_type"]))

        if self.data.close_button_hover["margin_left_value"] != 0 and self.data.close_button_hover["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.close_button_hover["margin_left_value"], self.data.close_button_hover["margin_left_type"]))


        f.write("\n}")





        f.write("\n")




        f.write(self.text + "::close-button:pressed {")

        if self.data.close_button_pressed["color"] != "":
            f.write("\n   color: {};".format(self.data.close_button_pressed["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.close_button_pressed["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.close_button_pressed["outline"]))

        if self.data.close_button_pressed["width_value"] != 0 and self.data.close_button_pressed["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.close_button_pressed["width_value"], self.data.close_button_pressed["width_type"]))

        if self.data.close_button_pressed["height_value"] != 0 and self.data.close_button_pressed["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.close_button_pressed["height_value"], self.data.close_button_pressed["height_type"]))

        if self.data.close_button_pressed["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.close_button_pressed["font_family"]))

        if self.data.close_button_pressed["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.close_button_pressed["font_size"]))

        if self.data.close_button_pressed["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.close_button_pressed["font_weight"]))

        if self.data.close_button_pressed["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.close_button_pressed["font_style"]))

        if self.data.close_button_pressed["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.close_button_pressed["line_height"]))

        if self.data.close_button_pressed["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.close_button_pressed["text_align"]))

        if self.data.close_button_pressed["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.close_button_pressed["text_decoration"]))

        if self.data.close_button_pressed["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.close_button_pressed["text_transform"]))

        if self.data.close_button_pressed["background"] != "":
            f.write("\n   background: {};".format(self.data.close_button_pressed["background"]))

        if self.data.close_button_pressed["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.close_button_pressed["background_image"]))

        if self.data.close_button_pressed["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.close_button_pressed["background_color"]))

        if self.data.close_button_pressed["border"] != "":
            f.write("\n   border: {};".format(self.data.close_button_pressed["border"]))

        if self.data.close_button_pressed["border_width_value"] != 0 and self.data.close_button_pressed["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.close_button_pressed["border_width_value"], self.data.close_button_pressed["border_width_type"]))

        if self.data.close_button_pressed["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.close_button_pressed["border_style"]))

        if self.data.close_button_pressed["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.close_button_pressed["border_color"]))

        if self.data.close_button_pressed["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.close_button_pressed["border_top"]))

        if self.data.close_button_pressed["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.close_button_pressed["border_right"]))

        if self.data.close_button_pressed["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.close_button_pressed["border_bottom"]))

        if self.data.close_button_pressed["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.close_button_pressed["border_left"]))

        if self.data.close_button_pressed["border_radius"] != 0 and self.data.close_button_pressed["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.close_button_pressed["border_radius"]))

        if self.data.close_button_pressed["padding_top_value"] != 0 and self.data.close_button_pressed["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.close_button_pressed["padding_top_value"], self.data.close_button_pressed["padding_top_type"]))

        if self.data.close_button_pressed["padding_right_value"] != 0 and self.data.close_button_pressed["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.close_button_pressed["padding_right_value"], self.data.close_button_pressed["padding_right_type"]))

        if self.data.close_button_pressed["padding_bottom_value"] != 0 and self.data.close_button_pressed["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.close_button_pressed["padding_bottom_value"], self.data.close_button_pressed["padding_bottom_type"]))

        if self.data.close_button_pressed["padding_left_value"] != 0 and self.data.close_button_pressed["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.close_button_pressed["padding_left_value"], self.data.close_button_pressed["padding_left_type"]))


        if self.data.close_button_pressed["margin_top_value"] != 0 and self.data.close_button_pressed["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.close_button_pressed["margin_top_value"], self.data.close_button_pressed["margin_top_type"]))

        if self.data.close_button_pressed["margin_right_value"] != 0 and self.data.close_button_pressed["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.close_button_pressed["margin_right_value"], self.data.close_button_pressed["margin_right_type"]))

        if self.data.close_button_pressed["margin_bottom_value"] != 0 and self.data.close_button_pressed["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.close_button_pressed["margin_bottom_value"], self.data.close_button_pressed["margin_bottom_type"]))

        if self.data.close_button_pressed["margin_left_value"] != 0 and self.data.close_button_pressed["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.close_button_pressed["margin_left_value"], self.data.close_button_pressed["margin_left_type"]))


        f.write("\n}")






        f.write("\n")




        f.write(self.text + "::float-button {")

        if self.data.float_button["color"] != "":
            f.write("\n   color: {};".format(self.data.float_button["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.float_button["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.float_button["outline"]))

        if self.data.float_button["width_value"] != 0 and self.data.float_button["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.float_button["width_value"], self.data.float_button["width_type"]))

        if self.data.float_button["height_value"] != 0 and self.data.float_button["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.float_button["height_value"], self.data.float_button["height_type"]))

        if self.data.float_button["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.float_button["font_family"]))

        if self.data.float_button["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.float_button["font_size"]))

        if self.data.float_button["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.float_button["font_weight"]))

        if self.data.float_button["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.float_button["font_style"]))

        if self.data.float_button["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.float_button["line_height"]))

        if self.data.float_button["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.float_button["text_align"]))

        if self.data.float_button["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.float_button["text_decoration"]))

        if self.data.float_button["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.float_button["text_transform"]))

        if self.data.float_button["background"] != "":
            f.write("\n   background: {};".format(self.data.float_button["background"]))

        if self.data.float_button["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.float_button["background_image"]))

        if self.data.float_button["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.float_button["background_color"]))

        if self.data.float_button["border"] != "":
            f.write("\n   border: {};".format(self.data.float_button["border"]))

        if self.data.float_button["border_width_value"] != 0 and self.data.float_button["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.float_button["border_width_value"], self.data.float_button["border_width_type"]))

        if self.data.float_button["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.float_button["border_style"]))

        if self.data.float_button["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.float_button["border_color"]))

        if self.data.float_button["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.float_button["border_top"]))

        if self.data.float_button["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.float_button["border_right"]))

        if self.data.float_button["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.float_button["border_bottom"]))

        if self.data.float_button["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.float_button["border_left"]))

        if self.data.float_button["border_radius"] != 0 and self.data.float_button["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.float_button["border_radius"]))

        if self.data.float_button["padding_top_value"] != 0 and self.data.float_button["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.float_button["padding_top_value"], self.data.float_button["padding_top_type"]))

        if self.data.float_button["padding_right_value"] != 0 and self.data.float_button["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.float_button["padding_right_value"], self.data.float_button["padding_right_type"]))

        if self.data.float_button["padding_bottom_value"] != 0 and self.data.float_button["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.float_button["padding_bottom_value"], self.data.float_button["padding_bottom_type"]))

        if self.data.float_button["padding_left_value"] != 0 and self.data.float_button["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.float_button["padding_left_value"], self.data.float_button["padding_left_type"]))


        if self.data.float_button["margin_top_value"] != 0 and self.data.float_button["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.float_button["margin_top_value"], self.data.float_button["margin_top_type"]))

        if self.data.float_button["margin_right_value"] != 0 and self.data.float_button["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.float_button["margin_right_value"], self.data.float_button["margin_right_type"]))

        if self.data.float_button["margin_bottom_value"] != 0 and self.data.float_button["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.float_button["margin_bottom_value"], self.data.float_button["margin_bottom_type"]))

        if self.data.float_button["margin_left_value"] != 0 and self.data.float_button["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.float_button["margin_left_value"], self.data.float_button["margin_left_type"]))


        f.write("\n}")




        f.write("\n")




        f.write(self.text + "::float-button:hover {")

        if self.data.float_button_hover["color"] != "":
            f.write("\n   color: {};".format(self.data.float_button_hover["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.float_button_hover["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.float_button_hover["outline"]))

        if self.data.float_button_hover["width_value"] != 0 and self.data.float_button_hover["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.float_button_hover["width_value"], self.data.float_button_hover["width_type"]))

        if self.data.float_button_hover["height_value"] != 0 and self.data.float_button_hover["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.float_button_hover["height_value"], self.data.float_button_hover["height_type"]))

        if self.data.float_button_hover["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.float_button_hover["font_family"]))

        if self.data.float_button_hover["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.float_button_hover["font_size"]))

        if self.data.float_button_hover["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.float_button_hover["font_weight"]))

        if self.data.float_button_hover["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.float_button_hover["font_style"]))

        if self.data.float_button_hover["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.float_button_hover["line_height"]))

        if self.data.float_button_hover["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.float_button_hover["text_align"]))

        if self.data.float_button_hover["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.float_button_hover["text_decoration"]))

        if self.data.float_button_hover["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.float_button_hover["text_transform"]))

        if self.data.float_button_hover["background"] != "":
            f.write("\n   background: {};".format(self.data.float_button_hover["background"]))

        if self.data.float_button_hover["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.float_button_hover["background_image"]))

        if self.data.float_button_hover["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.float_button_hover["background_color"]))

        if self.data.float_button_hover["border"] != "":
            f.write("\n   border: {};".format(self.data.float_button_hover["border"]))

        if self.data.float_button_hover["border_width_value"] != 0 and self.data.float_button_hover["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.float_button_hover["border_width_value"], self.data.float_button_hover["border_width_type"]))

        if self.data.float_button_hover["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.float_button_hover["border_style"]))

        if self.data.float_button_hover["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.float_button_hover["border_color"]))

        if self.data.float_button_hover["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.float_button_hover["border_top"]))

        if self.data.float_button_hover["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.float_button_hover["border_right"]))

        if self.data.float_button_hover["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.float_button_hover["border_bottom"]))

        if self.data.float_button_hover["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.float_button_hover["border_left"]))

        if self.data.float_button_hover["border_radius"] != 0 and self.data.float_button_hover["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.float_button_hover["border_radius"]))

        if self.data.float_button_hover["padding_top_value"] != 0 and self.data.float_button_hover["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.float_button_hover["padding_top_value"], self.data.float_button_hover["padding_top_type"]))

        if self.data.float_button_hover["padding_right_value"] != 0 and self.data.float_button_hover["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.float_button_hover["padding_right_value"], self.data.float_button_hover["padding_right_type"]))

        if self.data.float_button_hover["padding_bottom_value"] != 0 and self.data.float_button_hover["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.float_button_hover["padding_bottom_value"], self.data.float_button_hover["padding_bottom_type"]))

        if self.data.float_button_hover["padding_left_value"] != 0 and self.data.float_button_hover["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.float_button_hover["padding_left_value"], self.data.float_button_hover["padding_left_type"]))


        if self.data.float_button_hover["margin_top_value"] != 0 and self.data.float_button_hover["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.float_button_hover["margin_top_value"], self.data.float_button_hover["margin_top_type"]))

        if self.data.float_button_hover["margin_right_value"] != 0 and self.data.float_button_hover["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.float_button_hover["margin_right_value"], self.data.float_button_hover["margin_right_type"]))

        if self.data.float_button_hover["margin_bottom_value"] != 0 and self.data.float_button_hover["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.float_button_hover["margin_bottom_value"], self.data.float_button_hover["margin_bottom_type"]))

        if self.data.float_button_hover["margin_left_value"] != 0 and self.data.float_button_hover["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.float_button_hover["margin_left_value"], self.data.float_button_hover["margin_left_type"]))


        f.write("\n}")





        f.write("\n")




        f.write(self.text + "::float-button:pressed {")

        if self.data.float_button_pressed["color"] != "":
            f.write("\n   color: {};".format(self.data.float_button_pressed["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.float_button_pressed["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.float_button_pressed["outline"]))

        if self.data.float_button_pressed["width_value"] != 0 and self.data.float_button_pressed["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.float_button_pressed["width_value"], self.data.float_button_pressed["width_type"]))

        if self.data.float_button_pressed["height_value"] != 0 and self.data.float_button_pressed["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.float_button_pressed["height_value"], self.data.float_button_pressed["height_type"]))

        if self.data.float_button_pressed["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.float_button_pressed["font_family"]))

        if self.data.float_button_pressed["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.float_button_pressed["font_size"]))

        if self.data.float_button_pressed["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.float_button_pressed["font_weight"]))

        if self.data.float_button_pressed["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.float_button_pressed["font_style"]))

        if self.data.float_button_pressed["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.float_button_pressed["line_height"]))

        if self.data.float_button_pressed["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.float_button_pressed["text_align"]))

        if self.data.float_button_pressed["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.float_button_pressed["text_decoration"]))

        if self.data.float_button_pressed["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.float_button_pressed["text_transform"]))

        if self.data.float_button_pressed["background"] != "":
            f.write("\n   background: {};".format(self.data.float_button_pressed["background"]))

        if self.data.float_button_pressed["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.float_button_pressed["background_image"]))

        if self.data.float_button_pressed["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.float_button_pressed["background_color"]))

        if self.data.float_button_pressed["border"] != "":
            f.write("\n   border: {};".format(self.data.float_button_pressed["border"]))

        if self.data.float_button_pressed["border_width_value"] != 0 and self.data.float_button_pressed["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.float_button_pressed["border_width_value"], self.data.float_button_pressed["border_width_type"]))

        if self.data.float_button_pressed["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.float_button_pressed["border_style"]))

        if self.data.float_button_pressed["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.float_button_pressed["border_color"]))

        if self.data.float_button_pressed["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.float_button_pressed["border_top"]))

        if self.data.float_button_pressed["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.float_button_pressed["border_right"]))

        if self.data.float_button_pressed["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.float_button_pressed["border_bottom"]))

        if self.data.float_button_pressed["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.float_button_pressed["border_left"]))

        if self.data.float_button_pressed["border_radius"] != 0 and self.data.float_button_pressed["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.float_button_pressed["border_radius"]))

        if self.data.float_button_pressed["padding_top_value"] != 0 and self.data.float_button_pressed["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.float_button_pressed["padding_top_value"], self.data.float_button_pressed["padding_top_type"]))

        if self.data.float_button_pressed["padding_right_value"] != 0 and self.data.float_button_pressed["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.float_button_pressed["padding_right_value"], self.data.float_button_pressed["padding_right_type"]))

        if self.data.float_button_pressed["padding_bottom_value"] != 0 and self.data.float_button_pressed["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.float_button_pressed["padding_bottom_value"], self.data.float_button_pressed["padding_bottom_type"]))

        if self.data.float_button_pressed["padding_left_value"] != 0 and self.data.float_button_pressed["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.float_button_pressed["padding_left_value"], self.data.float_button_pressed["padding_left_type"]))


        if self.data.float_button_pressed["margin_top_value"] != 0 and self.data.float_button_pressed["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.float_button_pressed["margin_top_value"], self.data.float_button_pressed["margin_top_type"]))

        if self.data.float_button_pressed["margin_right_value"] != 0 and self.data.float_button_pressed["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.float_button_pressed["margin_right_value"], self.data.float_button_pressed["margin_right_type"]))

        if self.data.float_button_pressed["margin_bottom_value"] != 0 and self.data.float_button_pressed["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.float_button_pressed["margin_bottom_value"], self.data.float_button_pressed["margin_bottom_type"]))

        if self.data.float_button_pressed["margin_left_value"] != 0 and self.data.float_button_pressed["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.float_button_pressed["margin_left_value"], self.data.float_button_pressed["margin_left_type"]))


        f.write("\n}")
