def oxford_comma(items):
    def oxford_comma(items):
        if len(items) == 1:
            return items [0]
        elif len (items)==2:
            return f"{items[0]} and {items[1]}"
        elif len(items) >= 3:
            formatted_items = ", ".join(items[:-1])
            return f"{formatted_items}, and {items[-1]}"
