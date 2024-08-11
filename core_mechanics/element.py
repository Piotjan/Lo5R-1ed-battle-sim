"""
Module with classes and functions to simulate elements mechanics.
"""
from utilities import RingsNames
from utilities import CharacterAttributes


class Ring:
    """
    Class which represents element Ring from Character description.

    Fields:
        self.name (RingsNames): Name of the ring.
        attributes (dict): Dictionary with values of 2 internal attributes.
    """
    def __init__(self, name: RingsNames, internal_attributes: dict) -> None:
        self.name = name
        self.internal_attributes = internal_attributes

    def get_ring_value(self) -> int:
        """Funtion returns value of the ring.

        The value of the ring is calculated based on internal attributes
        and is equal to the smaller one.
        In case of Void Ring, the values is equal to the amount of void points.

        Returns:
            int: Value of the ring.
        """
        attributes_values = self.internal_attributes.values()
        return min(attributes_values)

    def get_attribute(self, attribute_name: CharacterAttributes) -> int:
        """Function returns value of attribute.

        This function returns value of specific attribute of the ring.
        If the object represents Void, attribute name has to be also provided (VOID_POINTS).

        Args:
            attribute_name (CharacterAttribute): Attribute which value should be returned.

        Returns:
            int: Value of the attribute

        Raises:
            KeyError: In case of wrongly declared attribute.
        """

        if attribute_name in self.internal_attributes.keys():
            return self.internal_attributes[attribute_name]
        raise KeyError(f'Ring {self.name} does not contain attribute {attribute_name.name}.')
