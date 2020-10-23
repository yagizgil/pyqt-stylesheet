class ListWidget():

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




        f.write(self.text + "::item {")

        if self.data.item["color"] != "":
            f.write("\n   color: {};".format(self.data.item["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.item["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.item["outline"]))

        if self.data.item["width_value"] != 0 and self.data.item["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.item["width_value"], self.data.item["width_type"]))

        if self.data.item["height_value"] != 0 and self.data.item["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.item["height_value"], self.data.item["height_type"]))

        if self.data.item["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.item["font_family"]))

        if self.data.item["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.item["font_size"]))

        if self.data.item["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.item["font_weight"]))

        if self.data.item["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.item["font_style"]))

        if self.data.item["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.item["line_height"]))

        if self.data.item["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.item["text_align"]))

        if self.data.item["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.item["text_decoration"]))

        if self.data.item["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.item["text_transform"]))

        if self.data.item["background"] != "":
            f.write("\n   background: {};".format(self.data.item["background"]))

        if self.data.item["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.item["background_image"]))

        if self.data.item["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.item["background_color"]))

        if self.data.item["border"] != "":
            f.write("\n   border: {};".format(self.data.item["border"]))

        if self.data.item["border_width_value"] != 0 and self.data.item["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.item["border_width_value"], self.data.item["border_width_type"]))

        if self.data.item["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.item["border_style"]))

        if self.data.item["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.item["border_color"]))

        if self.data.item["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.item["border_top"]))

        if self.data.item["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.item["border_right"]))

        if self.data.item["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.item["border_bottom"]))

        if self.data.item["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.item["border_left"]))

        if self.data.item["border_radius"] != 0 and self.data.item["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.item["border_radius"]))

        if self.data.item["padding_top_value"] != 0 and self.data.item["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.item["padding_top_value"], self.data.item["padding_top_type"]))

        if self.data.item["padding_right_value"] != 0 and self.data.item["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.item["padding_right_value"], self.data.item["padding_right_type"]))

        if self.data.item["padding_bottom_value"] != 0 and self.data.item["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.item["padding_bottom_value"], self.data.item["padding_bottom_type"]))

        if self.data.item["padding_left_value"] != 0 and self.data.item["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.item["padding_left_value"], self.data.item["padding_left_type"]))


        if self.data.item["margin_top_value"] != 0 and self.data.item["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.item["margin_top_value"], self.data.item["margin_top_type"]))

        if self.data.item["margin_right_value"] != 0 and self.data.item["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.item["margin_right_value"], self.data.item["margin_right_type"]))

        if self.data.item["margin_bottom_value"] != 0 and self.data.item["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.item["margin_bottom_value"], self.data.item["margin_bottom_type"]))

        if self.data.item["margin_left_value"] != 0 and self.data.item["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.item["margin_left_value"], self.data.item["margin_left_type"]))


        f.write("\n}")





        f.write("\n")




        f.write(self.text + "::item:hover {")

        if self.data.item_hover["color"] != "":
            f.write("\n   color: {};".format(self.data.item_hover["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.item_hover["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.item_hover["outline"]))

        if self.data.item_hover["width_value"] != 0 and self.data.item_hover["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.item_hover["width_value"], self.data.item_hover["width_type"]))

        if self.data.item_hover["height_value"] != 0 and self.data.item_hover["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.item_hover["height_value"], self.data.item_hover["height_type"]))

        if self.data.item_hover["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.item_hover["font_family"]))

        if self.data.item_hover["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.item_hover["font_size"]))

        if self.data.item_hover["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.item_hover["font_weight"]))

        if self.data.item_hover["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.item_hover["font_style"]))

        if self.data.item_hover["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.item_hover["line_height"]))

        if self.data.item_hover["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.item_hover["text_align"]))

        if self.data.item_hover["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.item_hover["text_decoration"]))

        if self.data.item_hover["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.item_hover["text_transform"]))

        if self.data.item_hover["background"] != "":
            f.write("\n   background: {};".format(self.data.item_hover["background"]))

        if self.data.item_hover["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.item_hover["background_image"]))

        if self.data.item_hover["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.item_hover["background_color"]))

        if self.data.item_hover["border"] != "":
            f.write("\n   border: {};".format(self.data.item_hover["border"]))

        if self.data.item_hover["border_width_value"] != 0 and self.data.item_hover["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.item_hover["border_width_value"], self.data.item_hover["border_width_type"]))

        if self.data.item_hover["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.item_hover["border_style"]))

        if self.data.item_hover["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.item_hover["border_color"]))

        if self.data.item_hover["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.item_hover["border_top"]))

        if self.data.item_hover["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.item_hover["border_right"]))

        if self.data.item_hover["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.item_hover["border_bottom"]))

        if self.data.item_hover["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.item_hover["border_left"]))

        if self.data.item_hover["border_radius"] != 0 and self.data.item_hover["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.item_hover["border_radius"]))

        if self.data.item_hover["padding_top_value"] != 0 and self.data.item_hover["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.item_hover["padding_top_value"], self.data.item_hover["padding_top_type"]))

        if self.data.item_hover["padding_right_value"] != 0 and self.data.item_hover["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.item_hover["padding_right_value"], self.data.item_hover["padding_right_type"]))

        if self.data.item_hover["padding_bottom_value"] != 0 and self.data.item_hover["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.item_hover["padding_bottom_value"], self.data.item_hover["padding_bottom_type"]))

        if self.data.item_hover["padding_left_value"] != 0 and self.data.item_hover["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.item_hover["padding_left_value"], self.data.item_hover["padding_left_type"]))


        if self.data.item_hover["margin_top_value"] != 0 and self.data.item_hover["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.item_hover["margin_top_value"], self.data.item_hover["margin_top_type"]))

        if self.data.item_hover["margin_right_value"] != 0 and self.data.item_hover["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.item_hover["margin_right_value"], self.data.item_hover["margin_right_type"]))

        if self.data.item_hover["margin_bottom_value"] != 0 and self.data.item_hover["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.item_hover["margin_bottom_value"], self.data.item_hover["margin_bottom_type"]))

        if self.data.item_hover["margin_left_value"] != 0 and self.data.item_hover["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.item_hover["margin_left_value"], self.data.item_hover["margin_left_type"]))


        f.write("\n}")





        f.write("\n")




        f.write(self.text + "::item:alternate {")

        if self.data.item_alternate["color"] != "":
            f.write("\n   color: {};".format(self.data.item_alternate["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.item_alternate["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.item_alternate["outline"]))

        if self.data.item_alternate["width_value"] != 0 and self.data.item_alternate["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.item_alternate["width_value"], self.data.item_alternate["width_type"]))

        if self.data.item_alternate["height_value"] != 0 and self.data.item_alternate["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.item_alternate["height_value"], self.data.item_alternate["height_type"]))

        if self.data.item_alternate["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.item_alternate["font_family"]))

        if self.data.item_alternate["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.item_alternate["font_size"]))

        if self.data.item_alternate["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.item_alternate["font_weight"]))

        if self.data.item_alternate["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.item_alternate["font_style"]))

        if self.data.item_alternate["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.item_alternate["line_height"]))

        if self.data.item_alternate["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.item_alternate["text_align"]))

        if self.data.item_alternate["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.item_alternate["text_decoration"]))

        if self.data.item_alternate["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.item_alternate["text_transform"]))

        if self.data.item_alternate["background"] != "":
            f.write("\n   background: {};".format(self.data.item_alternate["background"]))

        if self.data.item_alternate["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.item_alternate["background_image"]))

        if self.data.item_alternate["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.item_alternate["background_color"]))

        if self.data.item_alternate["border"] != "":
            f.write("\n   border: {};".format(self.data.item_alternate["border"]))

        if self.data.item_alternate["border_width_value"] != 0 and self.data.item_alternate["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.item_alternate["border_width_value"], self.data.item_alternate["border_width_type"]))

        if self.data.item_alternate["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.item_alternate["border_style"]))

        if self.data.item_alternate["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.item_alternate["border_color"]))

        if self.data.item_alternate["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.item_alternate["border_top"]))

        if self.data.item_alternate["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.item_alternate["border_right"]))

        if self.data.item_alternate["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.item_alternate["border_bottom"]))

        if self.data.item_alternate["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.item_alternate["border_left"]))

        if self.data.item_alternate["border_radius"] != 0 and self.data.item_alternate["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.item_alternate["border_radius"]))

        if self.data.item_alternate["padding_top_value"] != 0 and self.data.item_alternate["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.item_alternate["padding_top_value"], self.data.item_alternate["padding_top_type"]))

        if self.data.item_alternate["padding_right_value"] != 0 and self.data.item_alternate["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.item_alternate["padding_right_value"], self.data.item_alternate["padding_right_type"]))

        if self.data.item_alternate["padding_bottom_value"] != 0 and self.data.item_alternate["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.item_alternate["padding_bottom_value"], self.data.item_alternate["padding_bottom_type"]))

        if self.data.item_alternate["padding_left_value"] != 0 and self.data.item_alternate["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.item_alternate["padding_left_value"], self.data.item_alternate["padding_left_type"]))


        if self.data.item_alternate["margin_top_value"] != 0 and self.data.item_alternate["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.item_alternate["margin_top_value"], self.data.item_alternate["margin_top_type"]))

        if self.data.item_alternate["margin_right_value"] != 0 and self.data.item_alternate["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.item_alternate["margin_right_value"], self.data.item_alternate["margin_right_type"]))

        if self.data.item_alternate["margin_bottom_value"] != 0 and self.data.item_alternate["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.item_alternate["margin_bottom_value"], self.data.item_alternate["margin_bottom_type"]))

        if self.data.item_alternate["margin_left_value"] != 0 and self.data.item_alternate["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.item_alternate["margin_left_value"], self.data.item_alternate["margin_left_type"]))


        f.write("\n}")




        f.write("\n")




        f.write(self.text + "::item:selected {")

        if self.data.item_selected["color"] != "":
            f.write("\n   color: {};".format(self.data.item_selected["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.item_selected["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.item_selected["outline"]))

        if self.data.item_selected["width_value"] != 0 and self.data.item_selected["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.item_selected["width_value"], self.data.item_selected["width_type"]))

        if self.data.item_selected["height_value"] != 0 and self.data.item_selected["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.item_selected["height_value"], self.data.item_selected["height_type"]))

        if self.data.item_selected["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.item_selected["font_family"]))

        if self.data.item_selected["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.item_selected["font_size"]))

        if self.data.item_selected["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.item_selected["font_weight"]))

        if self.data.item_selected["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.item_selected["font_style"]))

        if self.data.item_selected["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.item_selected["line_height"]))

        if self.data.item_selected["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.item_selected["text_align"]))

        if self.data.item_selected["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.item_selected["text_decoration"]))

        if self.data.item_selected["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.item_selected["text_transform"]))

        if self.data.item_selected["background"] != "":
            f.write("\n   background: {};".format(self.data.item_selected["background"]))

        if self.data.item_selected["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.item_selected["background_image"]))

        if self.data.item_selected["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.item_selected["background_color"]))

        if self.data.item_selected["border"] != "":
            f.write("\n   border: {};".format(self.data.item_selected["border"]))

        if self.data.item_selected["border_width_value"] != 0 and self.data.item_selected["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.item_selected["border_width_value"], self.data.item_selected["border_width_type"]))

        if self.data.item_selected["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.item_selected["border_style"]))

        if self.data.item_selected["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.item_selected["border_color"]))

        if self.data.item_selected["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.item_selected["border_top"]))

        if self.data.item_selected["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.item_selected["border_right"]))

        if self.data.item_selected["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.item_selected["border_bottom"]))

        if self.data.item_selected["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.item_selected["border_left"]))

        if self.data.item_selected["border_radius"] != 0 and self.data.item_selected["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.item_selected["border_radius"]))

        if self.data.item_selected["padding_top_value"] != 0 and self.data.item_selected["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.item_selected["padding_top_value"], self.data.item_selected["padding_top_type"]))

        if self.data.item_selected["padding_right_value"] != 0 and self.data.item_selected["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.item_selected["padding_right_value"], self.data.item_selected["padding_right_type"]))

        if self.data.item_selected["padding_bottom_value"] != 0 and self.data.item_selected["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.item_selected["padding_bottom_value"], self.data.item_selected["padding_bottom_type"]))

        if self.data.item_selected["padding_left_value"] != 0 and self.data.item_selected["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.item_selected["padding_left_value"], self.data.item_selected["padding_left_type"]))


        if self.data.item_selected["margin_top_value"] != 0 and self.data.item_selected["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.item_selected["margin_top_value"], self.data.item_selected["margin_top_type"]))

        if self.data.item_selected["margin_right_value"] != 0 and self.data.item_selected["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.item_selected["margin_right_value"], self.data.item_selected["margin_right_type"]))

        if self.data.item_selected["margin_bottom_value"] != 0 and self.data.item_selected["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.item_selected["margin_bottom_value"], self.data.item_selected["margin_bottom_type"]))

        if self.data.item_selected["margin_left_value"] != 0 and self.data.item_selected["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.item_selected["margin_left_value"], self.data.item_selected["margin_left_type"]))


        f.write("\n}")




        f.write("\n")




        f.write(self.text + "::item:selected:active {")

        if self.data.item_selected_active["color"] != "":
            f.write("\n   color: {};".format(self.data.item_selected_active["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.item_selected_active["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.item_selected_active["outline"]))

        if self.data.item_selected_active["width_value"] != 0 and self.data.item_selected_active["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.item_selected_active["width_value"], self.data.item_selected_active["width_type"]))

        if self.data.item_selected_active["height_value"] != 0 and self.data.item_selected_active["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.item_selected_active["height_value"], self.data.item_selected_active["height_type"]))

        if self.data.item_selected_active["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.item_selected_active["font_family"]))

        if self.data.item_selected_active["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.item_selected_active["font_size"]))

        if self.data.item_selected_active["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.item_selected_active["font_weight"]))

        if self.data.item_selected_active["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.item_selected_active["font_style"]))

        if self.data.item_selected_active["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.item_selected_active["line_height"]))

        if self.data.item_selected_active["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.item_selected_active["text_align"]))

        if self.data.item_selected_active["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.item_selected_active["text_decoration"]))

        if self.data.item_selected_active["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.item_selected_active["text_transform"]))

        if self.data.item_selected_active["background"] != "":
            f.write("\n   background: {};".format(self.data.item_selected_active["background"]))

        if self.data.item_selected_active["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.item_selected_active["background_image"]))

        if self.data.item_selected_active["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.item_selected_active["background_color"]))

        if self.data.item_selected_active["border"] != "":
            f.write("\n   border: {};".format(self.data.item_selected_active["border"]))

        if self.data.item_selected_active["border_width_value"] != 0 and self.data.item_selected_active["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.item_selected_active["border_width_value"], self.data.item_selected_active["border_width_type"]))

        if self.data.item_selected_active["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.item_selected_active["border_style"]))

        if self.data.item_selected_active["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.item_selected_active["border_color"]))

        if self.data.item_selected_active["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.item_selected_active["border_top"]))

        if self.data.item_selected_active["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.item_selected_active["border_right"]))

        if self.data.item_selected_active["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.item_selected_active["border_bottom"]))

        if self.data.item_selected_active["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.item_selected_active["border_left"]))

        if self.data.item_selected_active["border_radius"] != 0 and self.data.item_selected_active["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.item_selected_active["border_radius"]))

        if self.data.item_selected_active["padding_top_value"] != 0 and self.data.item_selected_active["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.item_selected_active["padding_top_value"], self.data.item_selected_active["padding_top_type"]))

        if self.data.item_selected_active["padding_right_value"] != 0 and self.data.item_selected_active["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.item_selected_active["padding_right_value"], self.data.item_selected_active["padding_right_type"]))

        if self.data.item_selected_active["padding_bottom_value"] != 0 and self.data.item_selected_active["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.item_selected_active["padding_bottom_value"], self.data.item_selected_active["padding_bottom_type"]))

        if self.data.item_selected_active["padding_left_value"] != 0 and self.data.item_selected_active["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.item_selected_active["padding_left_value"], self.data.item_selected_active["padding_left_type"]))


        if self.data.item_selected_active["margin_top_value"] != 0 and self.data.item_selected_active["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.item_selected_active["margin_top_value"], self.data.item_selected_active["margin_top_type"]))

        if self.data.item_selected_active["margin_right_value"] != 0 and self.data.item_selected_active["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.item_selected_active["margin_right_value"], self.data.item_selected_active["margin_right_type"]))

        if self.data.item_selected_active["margin_bottom_value"] != 0 and self.data.item_selected_active["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.item_selected_active["margin_bottom_value"], self.data.item_selected_active["margin_bottom_type"]))

        if self.data.item_selected_active["margin_left_value"] != 0 and self.data.item_selected_active["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.item_selected_active["margin_left_value"], self.data.item_selected_active["margin_left_type"]))


        f.write("\n}")




        f.write("\n")




        f.write(self.text + "::item:selected:!active {")

        if self.data.item_selected_u_active["color"] != "":
            f.write("\n   color: {};".format(self.data.item_selected_u_active["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.item_selected_u_active["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.item_selected_u_active["outline"]))

        if self.data.item_selected_u_active["width_value"] != 0 and self.data.item_selected_u_active["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.item_selected_u_active["width_value"], self.data.item_selected_u_active["width_type"]))

        if self.data.item_selected_u_active["height_value"] != 0 and self.data.item_selected_u_active["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.item_selected_u_active["height_value"], self.data.item_selected_u_active["height_type"]))

        if self.data.item_selected_u_active["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.item_selected_u_active["font_family"]))

        if self.data.item_selected_u_active["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.item_selected_u_active["font_size"]))

        if self.data.item_selected_u_active["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.item_selected_u_active["font_weight"]))

        if self.data.item_selected_u_active["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.item_selected_u_active["font_style"]))

        if self.data.item_selected_u_active["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.item_selected_u_active["line_height"]))

        if self.data.item_selected_u_active["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.item_selected_u_active["text_align"]))

        if self.data.item_selected_u_active["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.item_selected_u_active["text_decoration"]))

        if self.data.item_selected_u_active["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.item_selected_u_active["text_transform"]))

        if self.data.item_selected_u_active["background"] != "":
            f.write("\n   background: {};".format(self.data.item_selected_u_active["background"]))

        if self.data.item_selected_u_active["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.item_selected_u_active["background_image"]))

        if self.data.item_selected_u_active["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.item_selected_u_active["background_color"]))

        if self.data.item_selected_u_active["border"] != "":
            f.write("\n   border: {};".format(self.data.item_selected_u_active["border"]))

        if self.data.item_selected_u_active["border_width_value"] != 0 and self.data.item_selected_u_active["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.item_selected_u_active["border_width_value"], self.data.item_selected_u_active["border_width_type"]))

        if self.data.item_selected_u_active["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.item_selected_u_active["border_style"]))

        if self.data.item_selected_u_active["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.item_selected_u_active["border_color"]))

        if self.data.item_selected_u_active["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.item_selected_u_active["border_top"]))

        if self.data.item_selected_u_active["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.item_selected_u_active["border_right"]))

        if self.data.item_selected_u_active["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.item_selected_u_active["border_bottom"]))

        if self.data.item_selected_u_active["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.item_selected_u_active["border_left"]))

        if self.data.item_selected_u_active["border_radius"] != 0 and self.data.item_selected_u_active["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.item_selected_u_active["border_radius"]))

        if self.data.item_selected_u_active["padding_top_value"] != 0 and self.data.item_selected_u_active["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.item_selected_u_active["padding_top_value"], self.data.item_selected_u_active["padding_top_type"]))

        if self.data.item_selected_u_active["padding_right_value"] != 0 and self.data.item_selected_u_active["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.item_selected_u_active["padding_right_value"], self.data.item_selected_u_active["padding_right_type"]))

        if self.data.item_selected_u_active["padding_bottom_value"] != 0 and self.data.item_selected_u_active["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.item_selected_u_active["padding_bottom_value"], self.data.item_selected_u_active["padding_bottom_type"]))

        if self.data.item_selected_u_active["padding_left_value"] != 0 and self.data.item_selected_u_active["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.item_selected_u_active["padding_left_value"], self.data.item_selected_u_active["padding_left_type"]))


        if self.data.item_selected_u_active["margin_top_value"] != 0 and self.data.item_selected_u_active["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.item_selected_u_active["margin_top_value"], self.data.item_selected_u_active["margin_top_type"]))

        if self.data.item_selected_u_active["margin_right_value"] != 0 and self.data.item_selected_u_active["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.item_selected_u_active["margin_right_value"], self.data.item_selected_u_active["margin_right_type"]))

        if self.data.item_selected_u_active["margin_bottom_value"] != 0 and self.data.item_selected_u_active["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.item_selected_u_active["margin_bottom_value"], self.data.item_selected_u_active["margin_bottom_type"]))

        if self.data.item_selected_u_active["margin_left_value"] != 0 and self.data.item_selected_u_active["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.item_selected_u_active["margin_left_value"], self.data.item_selected_u_active["margin_left_type"]))


        f.write("\n}")
