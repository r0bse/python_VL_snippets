class SetToStringParser():
    def combine_set_to_string(self, toBeJoined: set) -> str:
        orderedList = list(toBeJoined)
        return "".join(sorted(orderedList))